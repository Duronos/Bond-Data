"""
Compare the LLM's own break list (results/llm_analysis/breaks.csv,
made by reading the data without ruptures) with the breaks ruptures found.

Run from the project root, after breaks.py:
    python model_testing/compare_llm.py

Two comparisons, both with the one-to-one ±6 month matching of scoring.py:

1. Against events.csv: precision, recall and F1 for ruptures (main
   setting), all LLM breaks and the LLM's high-confidence breaks, each
   against its own random baseline.
2. Agreement, with the LLM's list as the reference: TP = a ruptures break
   the LLM also marked, FP = ruptures only, FN = LLM only.

Only LLM breaks that ruptures could have found count: inside a stretch it
analysed, and not within 6 months of the stretch's start or end. The others
are listed with ruptures_could_see = False.

Writes results/llm_analysis/comparison.json (the numbers), comparison.csv
(every break side by side, main setting) and llm_vs_ruptures.png.
"""

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import breaks  # noqa: E402  (load_stretches, COUNTRIES, in_scope)
import scoring  # noqa: E402

RESULTS = HERE / "results"
LLM = RESULTS / "llm_analysis"
MAIN = "auction_yield_intermediate_pen2"
SETTINGS = ["auction_yield_intermediate_pen0.5", "auction_yield_intermediate_pen1", MAIN]
CAUSE_MONTHS = 3  # LLM cause within this many months of the matched event = same cause


def load_breaks(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path).fillna("")
    df["break_month"] = pd.to_datetime(df["break_month"].astype(str).str[:7])
    return df.reset_index(drop=True)


def pair(a: pd.DataFrame, b: pd.DataFrame) -> list[tuple[int, int]]:
    """One-to-one matches (index in a, index in b) within ±6 months, per country."""
    pairs = []
    for country in set(a["country"]) & set(b["country"]):
        x, y = a[a["country"] == country], b[b["country"] == country]
        pairs += [(x.index[i], y.index[j]) for i, j in scoring.match(list(x["break_month"]), list(y["break_month"]))]
    return pairs


def visible(country: str, month: pd.Timestamp, stretches: dict, min_months: int = 6) -> bool:
    """
    Could ruptures have put a break here? Only inside a stretch it analysed,
    and not within min_months of the stretch's start or end (no segment may
    be shorter than that).
    """
    return any(s.index[0] + pd.DateOffset(months=min_months) <= month
               <= s.index[-1] - pd.DateOffset(months=min_months - 1)
               for s in stretches.get(country, []))


def by_country(df: pd.DataFrame) -> dict:
    return {c: list(g["break_month"]) for c, g in df.groupby("country")}


def agreement(llm: pd.DataFrame, rup: pd.DataFrame) -> dict:
    """Ruptures scored against the LLM's list as the reference."""
    pairs = pair(llm, rup)
    tp = len(pairs)
    fp, fn = len(rup) - tp, len(llm) - tp
    precision, recall, f1 = scoring.prf(tp, fp, fn)
    matched = {i for i, _ in pairs}
    by_conf = {}
    for c in ["high", "medium", "low"]:
        idx = llm.index[llm["confidence"] == c]
        by_conf[f"recall_llm_{c}"] = sum(i in matched for i in idx) / len(idx) if len(idx) else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "precision": precision, "recall": recall, "f1": f1, **by_conf}


def main():
    all_llm = load_breaks(LLM / "breaks.csv")
    events = pd.read_csv(HERE / "events.csv", parse_dates=["date"])
    codes = {name: code for code, name in breaks.COUNTRIES.items()}
    # Every country with 2-10 year yields, including any where the LLM found
    # no break; the same stretches breaks.py analyses.
    stretches = {c: parts for c in sorted(codes)
                 if (parts := breaks.load_stretches(codes[c], "auction_yield", "Intermediate", 18))}
    relevant = {c: events[[breaks.in_scope(s, c) for s in events["countries"]]] for c in stretches}
    seen = all_llm.apply(lambda r: visible(r["country"], r["break_month"], stretches), axis=1)
    llm, unseen = all_llm[seen], all_llm[~seen]

    # 1. Each method against events.csv.
    rup = load_breaks(RESULTS / MAIN / "breaks.csv")
    rup = rup[rup["country"].isin(stretches)]
    scores, outcomes = {}, {}
    for name, found in [("ruptures", rup), ("llm", llm), ("llm_high_confidence", llm[llm["confidence"] == "high"])]:
        stats, rows, _ = scoring.evaluate(by_country(found), stretches, relevant)
        scores[name] = stats
        outcomes[name] = {(r["country"], pd.Timestamp(r["break_month"])): r for r in rows}

    # 2. Agreement at each penalty, the LLM's list as reference.
    overlap = []
    for setting in SETTINGS:
        r = load_breaks(RESULTS / setting / "breaks.csv")
        overlap.append({"setting": setting, **agreement(llm, r[r["country"].isin(stretches)])})

    # Side by side, main setting.
    pairs = pair(llm, rup)
    side = []

    def row(country, r=None, l=None, could_see=True):
        ro = outcomes["ruptures"].get((country, r["break_month"])) if r is not None else None
        lo = outcomes["llm"].get((country, l["break_month"])) if l is not None and could_see else None
        same = ""
        if ro and ro["outcome"] == "TP" and l is not None and l["cause_month"]:
            same = abs(pd.Timestamp(l["cause_month"]) - pd.Timestamp(ro["event_date"])) <= pd.Timedelta(days=31 * CAUSE_MONTHS)
        return {
            "country": country,
            "agreement": "both" if r is not None and l is not None else ("ruptures only (FP)" if r is not None else "LLM only (FN)"),
            "ruptures_break": r["break_month"].date() if r is not None else "",
            "ruptures_vs_events": ro["outcome"] if ro else "",
            "ruptures_event": ro["event"] if ro else "",
            "llm_break": l["break_month"].date() if l is not None else "",
            "llm_vs_events": lo["outcome"] if lo else "",
            "llm_event": lo["event"] if lo else "",
            "llm_cause": l["cause"] if l is not None else "",
            "llm_cause_month": l["cause_month"] if l is not None else "",
            "llm_confidence": l["confidence"] if l is not None else "",
            "same_cause": same,
            "ruptures_could_see": could_see,
        }

    for i, j in pairs:
        side.append(row(llm.loc[i, "country"], r=rup.loc[j], l=llm.loc[i]))
    for j in sorted(set(rup.index) - {j for _, j in pairs}):
        side.append(row(rup.loc[j, "country"], r=rup.loc[j]))
    for i in sorted(set(llm.index) - {i for i, _ in pairs}):
        side.append(row(llm.loc[i, "country"], l=llm.loc[i]))
    for i in unseen.index:
        side.append(row(all_llm.loc[i, "country"], l=all_llm.loc[i], could_see=False) | {"agreement": "not comparable"})
    side = pd.DataFrame(side).sort_values(["country", "llm_break", "ruptures_break"], key=lambda s: s.astype(str))
    side.to_csv(LLM / "comparison.csv", index=False)

    both = side[side["agreement"] == "both"]
    with_event = both[both["ruptures_vs_events"] == "TP"]
    summary = {
        "llm_breaks_total": len(all_llm),
        "llm_breaks_ruptures_could_not_see": len(unseen),
        "vs_events": scores,
        "agreement_main": next(o for o in overlap if o["setting"] == MAIN),
        "cause_agreement": {"pairs_with_event": len(with_event),
                            "same_cause": int((with_event["same_cause"] == True).sum())},  # noqa: E712
        "agreement_by_setting": overlap,
    }
    (LLM / "comparison.json").write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    chart(scores, overlap, LLM / "llm_vs_ruptures.png")
    print(json.dumps(summary, indent=2, default=str))


def chart(scores: dict, overlap: list, path: Path):
    fig, (left, right) = plt.subplots(1, 2, figsize=(14, 6.2), gridspec_kw={"width_ratios": [1.25, 1]})
    metrics = [("precision", "Precision"), ("recall", "Recall"), ("f1", "F1")]

    # Left: each method against events.csv, with its random baseline.
    scoring.style(left)
    names = [("ruptures", "Ruptures (penalty 2)"), ("llm", "LLM, all"),
             ("llm_high_confidence", "LLM, high confidence")]
    width = 0.26
    for k, (key, label) in enumerate(names):
        s = scores[key]
        xs = [m + (k - 1) * width for m in range(len(metrics))]
        values = [s[m] for m, _ in metrics]
        left.bar(xs, values, width=width - 0.03, color=scoring.SERIES[k], zorder=2,
                 label=f"{label}: {scoring.counts(s)}")
        for x, v, (m, _) in zip(xs, values, metrics):
            left.text(x, v + 0.015, f"{v:.0%}" if m != "f1" else f"{v:.2f}", ha="center",
                      fontsize=8, color=scoring.INK_2)
            base = s[f"baseline_{m}"]
            left.plot([x - width / 2.4, x + width / 2.4], [base, base], color=scoring.INK, lw=2, zorder=3)
    left.plot([], [], color=scoring.INK, lw=2, label="Random baseline (same number of breaks)")
    left.set_xticks(range(len(metrics)), [m for _, m in metrics])
    left.set_ylim(0, 1)
    left.set_ylabel("Score (0 to 1)", color=scoring.INK_2)
    left.set_title("Against known events (events.csv)", loc="left", color=scoring.INK, fontsize=11)
    left.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=8.5,
                labelcolor=scoring.INK_2)

    # Right: agreement, the LLM's list as reference.
    scoring.style(right)
    xs = range(len(overlap))
    for k, (m, label) in enumerate(metrics):
        values = [o[m] for o in overlap]
        right.bar([x + (k - 1) * width for x in xs], values, width=width - 0.03,
                  color=["#eda100", "#e87ba4", "#6250d6"][k], zorder=2, label=label)
        for x, v in zip(xs, values):
            right.text(x + (k - 1) * width, v + 0.015, f"{v:.0%}" if m != "f1" else f"{v:.2f}",
                       ha="center", fontsize=8, color=scoring.INK_2)
    right.set_xticks(list(xs), [f"penalty {o['setting'].split('pen')[-1]}\n{scoring.counts(o)}" for o in overlap],
                     fontsize=8.5)
    right.set_ylim(0, 1)
    right.set_ylabel("Score (0 to 1)", color=scoring.INK_2)
    right.set_title("Ruptures vs the LLM's list (reference)", loc="left", color=scoring.INK, fontsize=11)
    right.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False, fontsize=8.5,
                 labelcolor=scoring.INK_2)
    right.text(0, -0.36, "TP = break in both lists · FP = ruptures only · FN = LLM only\n"
               "Precision = share of ruptures' breaks the LLM also marked; recall = share of the LLM's breaks ruptures found",
               transform=right.transAxes, fontsize=8, color=scoring.INK_2, va="top")
    fig.suptitle("Break detection: ruptures and the LLM, scored one break per event within ±6 months",
                 x=0.01, ha="left", color=scoring.INK, fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    sys.exit(main())
