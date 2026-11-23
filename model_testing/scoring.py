"""
Scoring for break detection, shared by breaks.py and compare_llm.py.

A detected break is scored against the known events (events.csv) that fall
inside the same stretch of a country's data:

    True positive (TP)   a break matched to an event within the window
                         (±6 months for events.csv, ±3 for events_v2.csv)
    False positive (FP)  a break with no event left to match
    False negative (FN)  an event with no break matched to it

Matching is one-to-one: each break counts for at most one event and each
event for at most one break (the most matches possible, then the closest).
Then

    precision = TP / (TP + FP)   share of breaks that are real events
    recall    = TP / (TP + FN)   share of events that were detected
    F1        = 2PR / (P + R)    one number balancing the two

Accuracy isn't used: it needs true negatives (months with neither a break
nor an event), and almost every month is one: a model that never finds a
break would score about 97% on the 2-10 year yields.

Random baseline: the same number of breaks per stretch, placed at random
months a break could fall on (respecting the shortest-segment rule),
scored the same way, SIMULATIONS times. The p-value is the share of those
random draws whose F1 is at least the real F1.
"""

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment

TOLERANCE_MONTHS = 6
TOLERANCE = pd.Timedelta(days=31 * TOLERANCE_MONTHS)
SIMULATIONS = 1000

# Chart colours (dataviz reference palette): status colours for outcomes.
TP_COLOUR, FP_COLOUR, FN_COLOUR = "#0ca30c", "#d03b3b", "#ec835a"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
INK, INK_2, MUTED, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"


def match(breaks: list, events: list, tolerance: pd.Timedelta = TOLERANCE) -> list[tuple[int, int]]:
    """
    One-to-one pairs (break index, event index) within `tolerance`: the most
    pairs possible, and among those the smallest total distance.
    """
    if not len(breaks) or not len(events):
        return []
    b = pd.DatetimeIndex(breaks).values[:, None]
    e = pd.DatetimeIndex(events).values[None, :]
    gap = np.abs(b - e) / np.timedelta64(1, "D")
    ok = gap <= tolerance.days
    # An impossible pair costs more than all possible ones together, so the
    # solver first maximises the number of pairs, then minimises distance.
    rows, cols = linear_sum_assignment(np.where(ok, gap, 1e9))
    return [(int(i), int(j)) for i, j in zip(rows, cols) if ok[i, j]]


def prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return precision, recall, f1


def random_breaks(months: pd.DatetimeIndex, k: int, min_months: int, rng) -> list:
    """
    k random break months in a stretch, where ruptures could put them: at
    least min_months from either end and from each other (uniform over all
    such layouts; spacing is dropped if k breaks can't fit).
    """
    lo, hi = min_months, len(months) - min_months  # allowed positions, inclusive
    slots = hi - lo + 1
    if k <= 0 or slots <= 0:
        return []
    k = min(k, slots)
    free = slots - (k - 1) * (min_months - 1)
    if free >= k:
        picks = np.sort(rng.choice(free, size=k, replace=False)) + np.arange(k) * (min_months - 1) + lo
    else:
        picks = np.sort(rng.choice(slots, size=k, replace=False)) + lo
    return list(months[picks])


def evaluate(found: dict, stretches: dict, relevant: dict, min_months: int = 6, seed: int = 0,
             tolerance: pd.Timedelta = TOLERANCE):
    """
    Score detected breaks against events, stretch by stretch.

    found:     {country: [break months]}
    stretches: {country: [monthly Series]} (the data analysed)
    relevant:  {country: events DataFrame with date, event} (events in scope)
    tolerance: how far a break may be from its event

    Returns (stats, break_rows, event_rows): the totals, one row per break
    (TP/FP and its event) and one row per event checked (TP/FN).
    """
    units, break_rows, event_rows = [], [], []
    for country, parts in stretches.items():
        dates = sorted(found.get(country, []))
        events = relevant[country]
        for s in parts:
            start, end = s.index[0], s.index[-1]
            own = [d for d in dates if start <= d <= end]
            pool = events[(events["date"] >= start) & (events["date"] <= end)].reset_index(drop=True)
            pairs = dict(match(own, list(pool["date"]), tolerance))
            hit = set(pairs.values())
            units.append((s.index, len(own), list(pool["date"])))
            for i, d in enumerate(own):
                if i in pairs:
                    ev = pool.loc[pairs[i]]
                    break_rows.append({
                        "country": country, "break_month": d.date(), "outcome": "TP",
                        "event": ev["event"], "event_date": ev["date"].date(),
                        "months_off": round((d - ev["date"]).days / 30.4, 1), "note": "",
                    })
                else:
                    close = pool[(pool["date"] - d).abs() <= tolerance]
                    break_rows.append({
                        "country": country, "break_month": d.date(), "outcome": "FP",
                        "event": "", "event_date": "", "months_off": "",
                        "note": (f"near {close.iloc[0]['event']}, already matched to another break"
                                 if not close.empty else ""),
                    })
            for j, ev in pool.iterrows():
                event_rows.append({"country": country, "date": ev["date"].date(), "event": ev["event"],
                                   "outcome": "TP" if j in hit else "FN"})

    tp = sum(r["outcome"] == "TP" for r in break_rows)
    fp = len(break_rows) - tp
    fn = sum(r["outcome"] == "FN" for r in event_rows)
    precision, recall, f1 = prf(tp, fp, fn)

    rng = np.random.default_rng(seed)
    draws = []
    for _ in range(SIMULATIONS):
        t = f = n = 0
        for months, k, evs in units:
            b = random_breaks(months, k, min_months, rng)
            m = len(match(b, evs, tolerance))
            t, f, n = t + m, f + len(b) - m, n + len(evs) - m
        draws.append(prf(t, f, n))
    draws = np.array(draws)

    stats = {
        "breaks": tp + fp, "events_checked": tp + fn, "tp": tp, "fp": fp, "fn": fn,
        "precision": precision, "recall": recall, "f1": f1,
        "baseline_precision": float(draws[:, 0].mean()),
        "baseline_recall": float(draws[:, 1].mean()),
        "baseline_f1": float(draws[:, 2].mean()),
        "p_value": float((1 + (draws[:, 2] >= f1).sum()) / (1 + SIMULATIONS)),
    }
    return stats, break_rows, event_rows


def p_text(p: float) -> str:
    """The smallest p-value SIMULATIONS draws can show is 1 / (SIMULATIONS + 1)."""
    floor = 1 / (SIMULATIONS + 1)
    return f"≤ {floor:.3f}" if p <= floor + 1e-12 else f"{p:.3f}"


def counts(stats: dict) -> str:
    return f"TP {stats['tp']} · FP {stats['fp']} · FN {stats['fn']}"


def style(ax):
    """Recessive grid and axes for the analysis charts."""
    ax.grid(color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#c3c2b7")
    ax.tick_params(colors=INK_2, labelsize=9)
