"""
Compare the LLM's own break list (results/llm_analysis/breaks.csv,
made by reading the data without ruptures) with the breaks ruptures found,
and score both against events.csv with the same rules as breaks.py.

Run from the project root, after breaks.py:
    python model_testing/compare_llm.py

Only LLM breaks that ruptures could have found count in the comparison:
inside a stretch it analysed, and not within 6 months of the stretch's
start or end. The others are listed with ruptures_could_see = False.

Writes results/llm_analysis/comparison.json (the numbers) and
comparison.csv (every LLM and ruptures break for the main setting, side by
side).
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import breaks  # noqa: E402  (load_stretches, COUNTRIES, in_scope)

RESULTS = HERE / "results"
LLM = RESULTS / "llm_analysis"
MAIN = "auction_yield_intermediate_pen2"
SETTINGS = ["auction_yield_intermediate_pen0.5", "auction_yield_intermediate_pen1", MAIN]
TOLERANCE = pd.Timedelta(days=31 * 6)  # as in breaks.py
CAUSE_MONTHS = 3  # LLM cause within this many months of our matched event = same cause


def load_breaks(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path).fillna("")
    df["break_month"] = pd.to_datetime(df["break_month"].astype(str).str[:7])
    return df


def pair(a: pd.DataFrame, b: pd.DataFrame) -> list[tuple[int, int]]:
    """One-to-one matches within TOLERANCE, per country, closest pairs first."""
    candidates = []
    for country in set(a["country"]) & set(b["country"]):
        for i, x in a[a["country"] == country]["break_month"].items():
            for j, y in b[b["country"] == country]["break_month"].items():
                if abs(x - y) <= TOLERANCE:
                    candidates.append((abs(x - y), i, j))
    used_a, used_b, pairs = set(), set(), []
    for _, i, j in sorted(candidates):
        if i not in used_a and j not in used_b:
            used_a.add(i); used_b.add(j); pairs.append((i, j))
    return pairs


def event_scores(found: pd.DataFrame, events: pd.DataFrame, stretches: dict) -> dict:
    """
    Same three numbers as breaks.py: near an event, events found, and the
    chance rate, each event checked within one stretch of a country's data
    and its chance rate taken over that same stretch.
    """
    near, checked, chance = [], [], []
    for country, parts in stretches.items():
        dates = list(found.loc[found["country"] == country, "break_month"])
        relevant = events[[breaks.in_scope(e, country) for e in events["countries"]]]
        for d in dates:
            near.append(bool(((relevant["date"] - d).abs() <= TOLERANCE).any()))
        for s in parts:
            first, last = s.index[0] + pd.DateOffset(months=6), s.index[-1] - pd.DateOffset(months=6)
            months = s.index[(s.index >= first) & (s.index <= last)]
            own = [d for d in dates if s.index[0] <= d <= s.index[-1]]
            rate = float(np.mean([any(abs(m - d) <= TOLERANCE for d in own) for m in months])) if len(months) else 0.0
            for ev in relevant["date"]:
                if first <= ev <= last:
                    checked.append(any(abs(d - ev) <= TOLERANCE for d in own))
                    chance.append(rate)
    return {"breaks": len(found), "near_event": float(np.mean(near)),
            "events_found": float(np.mean(checked)), "chance": float(np.mean(chance))}


def visible(country: str, month: pd.Timestamp, stretches: dict, min_months: int = 6) -> bool:
    """
    Could ruptures have put a break here? Only inside a stretch it analysed,
    and not within min_months of the stretch's start or end (no segment may
    be shorter than that).
    """
    return any(s.index[0] + pd.DateOffset(months=min_months) <= month
               <= s.index[-1] - pd.DateOffset(months=min_months - 1)
               for s in stretches.get(country, []))


def main():
    all_llm = load_breaks(LLM / "breaks.csv")
    events = pd.read_csv(HERE / "events.csv", parse_dates=["date"])
    codes = {name: code for code, name in breaks.COUNTRIES.items()}
    # Every country with 2-10 year yields, including any where the LLM found
    # no break; the same stretches breaks.py analyses.
    stretches = {c: parts for c in sorted(codes)
                 if (parts := breaks.load_stretches(codes[c], "auction_yield", "Intermediate", 18))}
    # Compare only LLM breaks that ruptures could have found; list the rest.
    seen = all_llm.apply(lambda r: visible(r["country"], r["break_month"], stretches), axis=1)
    llm, unseen = all_llm[seen], all_llm[~seen]

    rows = []
    for setting in SETTINGS:
        rup = load_breaks(RESULTS / setting / "breaks.csv")
        rup = rup[rup["country"].isin(stretches)]
        pairs = pair(llm, rup)
        matched_llm = {i for i, _ in pairs}
        by_conf = {c: float(np.mean([i in matched_llm for i in llm.index[llm["confidence"] == c]]))
                   for c in ["high", "medium", "low"]}
        rows.append({"setting": setting, "ruptures_breaks": len(rup), "llm_breaks": len(llm),
                     "pairs": len(pairs), "ruptures_found_by_llm": len(pairs) / len(rup),
                     "llm_found_by_ruptures": len(pairs) / len(llm), **{f"llm_{k}_found": v for k, v in by_conf.items()}})
    overlap = pd.DataFrame(rows)

    # Main setting in detail.
    rup = load_breaks(RESULTS / MAIN / "breaks.csv")
    rup = rup[rup["country"].isin(stretches)]
    pairs = pair(llm, rup)
    llm_scores = event_scores(llm, events, stretches)
    llm_high = event_scores(llm[llm["confidence"] == "high"], events, stretches)
    rup_scores = event_scores(rup, events, stretches)

    side = []
    for i, j in pairs:
        r, l = rup.loc[j], llm.loc[i]
        same_cause = ""
        if r["nearest_event"] and l["cause_month"]:
            gap = abs(pd.Timestamp(l["cause_month"]) - pd.Timestamp(r["event_date"]))
            same_cause = gap <= pd.Timedelta(days=31 * CAUSE_MONTHS)
        side.append({"country": l["country"], "ruptures_break": r["break_month"].date(),
                     "llm_break": l["break_month"].date(), "ruptures_event": r["nearest_event"],
                     "llm_cause": l["cause"], "llm_cause_month": l["cause_month"],
                     "llm_confidence": l["confidence"], "same_cause": same_cause,
                     "ruptures_could_see": True})
    for j in sorted(set(rup.index) - {j for _, j in pairs}):
        r = rup.loc[j]
        side.append({"country": r["country"], "ruptures_break": r["break_month"].date(),
                     "llm_break": "", "ruptures_event": r["nearest_event"], "llm_cause": "",
                     "llm_cause_month": "", "llm_confidence": "", "same_cause": "",
                     "ruptures_could_see": True})
    for i in sorted(set(llm.index) - {i for i, _ in pairs}) + list(unseen.index):
        l = all_llm.loc[i]
        side.append({"country": l["country"], "ruptures_break": "", "llm_break": l["break_month"].date(),
                     "ruptures_event": "", "llm_cause": l["cause"], "llm_cause_month": l["cause_month"],
                     "llm_confidence": l["confidence"], "same_cause": "",
                     "ruptures_could_see": i not in unseen.index})
    side = pd.DataFrame(side).sort_values(["country", "llm_break", "ruptures_break"], key=lambda s: s.astype(str))
    side.to_csv(LLM / "comparison.csv", index=False)

    both = side[(side["llm_break"] != "") & (side["ruptures_break"] != "")]
    with_event = both[both["ruptures_event"] != ""]
    summary = {
        "llm_breaks_total": len(all_llm),
        "llm_breaks_ruptures_could_not_see": len(unseen),
        "llm": llm_scores, "llm_high_confidence": llm_high, "ruptures": rup_scores,
        "pairs": len(both), "same_cause": int((with_event["same_cause"] == True).sum()),  # noqa: E712
        "pairs_with_event": len(with_event),
        "overlap": overlap.to_dict(orient="records"),
    }
    (LLM / "comparison.json").write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    sys.exit(main())
