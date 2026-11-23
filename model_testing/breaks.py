"""
Find break dates (regime changes) in the auction data with
ruptures, then score them against known historical events (events.csv):
precision, recall and F1 against a random baseline (see scoring.py).

Standalone: it only reads the monthly CSVs in results/auctions/ (a copy of
the latest run) and writes to model_testing/results/. Nothing in the main
project imports or depends on this folder.

How it works: ruptures splits each country's monthly series into segments
and adds a break wherever the fit improves by more than a penalty. A higher
--penalty gives fewer, bigger breaks.

Run from the project root:
    python model_testing/breaks.py                                  # auction yields, 2-10Y
    python model_testing/breaks.py --measure bid_to_cover
    python model_testing/breaks.py --bucket Long --penalty 1

Outputs (results/<measure>_<bucket>_pen<penalty>/):
    README.md           the results, readable on GitHub
    breaks.csv          every break: true positive (matched to an event) or false positive
    event_outcomes.csv  every country-event pair checked: true positive or false negative
    event_recall.csv    recall for each event across countries
    country_scores.csv  TP/FP/FN, precision, recall and F1 per country
    summary.json        headline numbers (used for results/README.md)
    charts/<country>.png
results/README.md and settings_comparison.png compare every setting run so far.
"""

import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # draw to files, no window
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import pandas as pd
import ruptures as rpt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scoring  # noqa: E402  (matching, precision/recall, random baseline)

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results" / "auctions"

# Folder code -> display name, as in the main project's results/ folders.
COUNTRIES = {
    "us": "United States", "canada": "Canada", "uk": "United Kingdom",
    "germany": "Germany", "japan": "Japan", "austria": "Austria", "belgium": "Belgium",
    "czechia": "Czech Republic", "denmark": "Denmark", "finland": "Finland",
    "france": "France", "greece": "Greece", "hungary": "Hungary", "ireland": "Ireland",
    "italy": "Italy", "lithuania": "Lithuania", "netherlands": "Netherlands",
    "norway": "Norway", "poland": "Poland", "slovakia": "Slovakia", "slovenia": "Slovenia",
    "korea": "South Korea", "spain": "Spain", "switzerland": "Switzerland",
    "eu": "European Union",
}
# "euro" in events.csv: euro-area members in the data, plus the EU itself.
EURO = {
    "Austria", "Belgium", "Finland", "France", "Germany", "Greece", "Ireland", "Italy",
    "Lithuania", "Netherlands", "Slovakia", "Slovenia", "Spain", "European Union",
}

# Yields mostly shift in level ("l2" = change in the average). Bid-to-cover
# also changes in how jumpy it is, which "rbf" picks up.
MODELS = {"auction_yield": "l2", "bid_to_cover": "rbf"}

GAP_MONTHS = 6  # longest run of months without an auction that gets filled in


def load_stretches(code: str, measure: str, bucket: str, min_length: int) -> list[pd.Series]:
    """
    One country's monthly median (not the 3-month average) as a list of
    unbroken stretches, each at least `min_length` months long.

    ruptures needs evenly spaced data, so a gap of up to GAP_MONTHS months
    with no auction is filled with a straight line between the months on
    either side. A longer gap is left empty, which splits the series: each
    stretch is analysed on its own, so no part of the history is dropped
    and nothing is invented across a long gap.
    """
    path = RESULTS / code / f"{code}_auction_20y_monthly.csv"
    if not path.exists():
        return []
    df = pd.read_csv(path, parse_dates=["month"])
    df = df[df["bucket"].str.startswith(bucket)]
    series = df.set_index("month")[measure].dropna()
    if series.empty:
        return []
    series = series.asfreq("MS")
    # Length of the gap each empty month belongs to.
    gap = series.isna().groupby(series.notna().cumsum()).transform("sum")
    filled = series.interpolate(limit_area="inside").where(series.notna() | (gap <= GAP_MONTHS))
    stretch_id = filled.isna().cumsum()[filled.notna()]
    stretches = [s for _, s in filled.dropna().groupby(stretch_id)]
    return [s for s in stretches if len(s) >= min_length]


def find_breaks(series: pd.Series, model: str, penalty: float, min_months: int) -> list:
    """Break dates: the first month of each new segment."""
    # Standardise so one penalty works across countries and measures; the
    # penalty is then log(n) x (variance = 1) x the --penalty factor.
    values = ((series - series.mean()) / series.std()).to_numpy().reshape(-1, 1)
    # jump=1: consider every month as a break date (the default, 5, only
    # tries every 5th month, which shifts dates by up to 2 months).
    bkps = rpt.Pelt(model=model, min_size=min_months, jump=1).fit(values).predict(
        pen=penalty * np.log(len(values))
    )
    return [series.index[i] for i in bkps[:-1]]  # the last one is just the series end


def in_scope(scope: str, country: str) -> bool:
    return scope == "all" or (scope == "euro" and country in EURO) or scope == country


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--measure", choices=list(MODELS), default="auction_yield")
    parser.add_argument("--bucket", choices=["Short", "Intermediate", "Long"], default="Intermediate")
    parser.add_argument("--penalty", type=float, default=2.0, help="higher = fewer breaks")
    parser.add_argument("--min-months", type=int, default=6, help="shortest segment allowed")
    args = parser.parse_args()

    events = pd.read_csv(HERE / "events.csv", parse_dates=["date"])
    out = HERE / "results" / f"{args.measure}_{args.bucket.lower()}_pen{args.penalty:g}"
    (out / "charts").mkdir(parents=True, exist_ok=True)

    stretches, found, relevant, codes = {}, {}, {}, {}
    for code, country in COUNTRIES.items():
        parts = load_stretches(code, args.measure, args.bucket, 3 * args.min_months)
        if not parts:
            continue
        stretches[country], codes[country] = parts, code
        found[country] = [b for s in parts for b in find_breaks(s, MODELS[args.measure], args.penalty, args.min_months)]
        relevant[country] = events[[in_scope(s, country) for s in events["countries"]]]

    stats, break_rows, event_rows = scoring.evaluate(found, stretches, relevant, args.min_months)
    breaks_df, events_df = pd.DataFrame(break_rows), pd.DataFrame(event_rows)
    breaks_df.to_csv(out / "breaks.csv", index=False)
    events_df.to_csv(out / "event_outcomes.csv", index=False)

    per_event = (
        events_df.assign(tp=events_df["outcome"] == "TP", fn=events_df["outcome"] == "FN")
        .groupby(["date", "event"], sort=True)
        .agg(countries_checked=("outcome", "size"), tp=("tp", "sum"), fn=("fn", "sum"))
        .reset_index()
    )
    per_event["recall"] = (per_event["tp"] / per_event["countries_checked"]).round(2)
    per_event.to_csv(out / "event_recall.csv", index=False)

    per_country = []
    for country in stretches:
        b = breaks_df[breaks_df["country"] == country] if len(breaks_df) else breaks_df
        e = events_df[events_df["country"] == country] if len(events_df) else events_df
        tp, fp, fn = int((b["outcome"] == "TP").sum()), int((b["outcome"] == "FP").sum()), int((e["outcome"] == "FN").sum())
        precision, recall, f1 = scoring.prf(tp, fp, fn)
        per_country.append({"country": country, "tp": tp, "fp": fp, "fn": fn,
                            "precision": precision, "recall": recall, "f1": f1})
        chart(stretches[country], b, e, country, args, out / "charts" / f"{codes[country]}.png")
    per_country = pd.DataFrame(per_country)
    per_country.round(3).to_csv(out / "country_scores.csv", index=False)

    stats = {
        "folder": out.name, "measure": args.measure, "bucket": args.bucket,
        "penalty": args.penalty, "min_months": args.min_months,
        "tolerance": scoring.TOLERANCE_MONTHS, "simulations": scoring.SIMULATIONS,
        "countries": int(breaks_df["country"].nunique()) if len(breaks_df) else 0,
        "months_analysed": sum(len(s) for parts in stretches.values() for s in parts),
        **stats,
    }
    (out / "summary.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    report = run_report(stats, per_event, per_country, breaks_df, events_df, list(stretches.items()))
    (out / "README.md").write_text(report, encoding="utf-8")
    write_index(out.parent)
    print(report)
    print(f"Saved to {out.relative_to(HERE.parent)}")


def describe(stats: dict) -> str:
    return (f"{stats['measure'].replace('_', ' ')}, {stats['bucket']} bucket, "
            f"penalty {stats['penalty']:g}")


TERMS = [
    "| Term | Meaning here |",
    "|---|---|",
    "| True positive (TP) | a break matched to a known event within ±6 months |",
    "| False positive (FP) | a break with no event left to match (a lead, or noise) |",
    "| False negative (FN) | a known event with no break matched to it (missed) |",
    "| Precision | TP / (TP + FP): share of breaks that match an event |",
    "| Recall | TP / (TP + FN): share of events that were detected |",
    "| F1 | 2 × precision × recall / (precision + recall) |",
    "| Random baseline | the same number of breaks per stretch at random dates, "
    f"scored the same way ({scoring.SIMULATIONS:,} draws, average) |",
    "| p-value | share of random draws with an F1 at least as high as the real one |",
]


def metrics_table(stats: dict) -> list[str]:
    return [
        "| | Model | Random baseline |",
        "|---|:-:|:-:|",
        f"| Precision | **{stats['precision']:.0%}** ({stats['tp']} of {stats['breaks']} breaks) "
        f"| {stats['baseline_precision']:.0%} |",
        f"| Recall | **{stats['recall']:.0%}** ({stats['tp']} of {stats['events_checked']} events) "
        f"| {stats['baseline_recall']:.0%} |",
        f"| F1 | **{stats['f1']:.2f}** | {stats['baseline_f1']:.2f} |",
        "",
        f"Confusion counts: **{stats['tp']} TP**, **{stats['fp']} FP**, **{stats['fn']} FN** "
        f"(no true negatives: see below). p-value vs random: {scoring.p_text(stats['p_value'])}.",
    ]


def run_report(stats, per_event, per_country, breaks_df, events_df, analysed) -> str:
    """One run's results as a markdown page (also printed to the console)."""
    fp = breaks_df[breaks_df["outcome"] == "FP"] if len(breaks_df) else breaks_df
    fn = events_df[events_df["outcome"] == "FN"] if len(events_df) else events_df
    spans = lambda parts: ", ".join(f"{s.index[0]:%Y-%m} to {s.index[-1]:%Y-%m}" for s in parts)
    lines = [
        f"# Breaks: {describe(stats)}",
        "",
        f"Breaks are scored against [events.csv](../../events.csv), one break per event, "
        f"within ±{stats['tolerance']} months; shortest segment {stats['min_months']} months. "
        f"{stats['breaks']} breaks in {stats['countries']} countries; "
        f"{stats['events_checked']} country-event pairs checked.",
        "",
        *metrics_table(stats),
        "",
        *TERMS,
        "",
        "Accuracy isn't reported: it needs true negatives (months with neither a "
        "break nor an event), and almost every month is one. A model that never "
        f"finds a break would score {1 - stats['events_checked'] / stats['months_analysed']:.0%} "
        f"accuracy on these {stats['months_analysed']:,} months.",
        "",
        "## Recall by event",
        "",
        "| Date | Event | Countries checked | TP | FN | Recall |",
        "|---|---|:-:|:-:|:-:|:-:|",
        *[f"| {r.date} | {r.event} | {r.countries_checked} | {r.tp} | {r.fn} | {r.recall:.0%} |"
          for r in per_event.itertuples()],
        "",
        "## Scores by country",
        "",
        "| Country | TP | FP | FN | Precision | Recall | F1 |",
        "|---|:-:|:-:|:-:|:-:|:-:|:-:|",
        *[f"| {r.country} | {r.tp} | {r.fp} | {r.fn} | {r.precision:.0%} | {r.recall:.0%} | {r.f1:.2f} |"
          for r in per_country.itertuples()],
        "",
        "## False positives (breaks with no event left to match)",
        "",
        "Leads worth looking into: something changed, but it isn't in events.csv "
        "(or its event was already matched to another break).",
        "",
        *([f"- {r.country}: {r.break_month}" + (f" ({r.note})" if r.note else "")
           for r in fp.itertuples()] or ["- none"]),
        "",
        "## False negatives (events with no break)",
        "",
        *([f"- {r.country}: {r.event} ({r.date})" for r in fn.itertuples()] or ["- none"]),
        "",
        "## Data analysed",
        "",
        f"Gaps of up to {GAP_MONTHS} months without an auction are filled with a straight "
        "line; a longer gap splits the series, and each stretch of at least "
        f"{3 * stats['min_months']} months is analysed on its own. A break can't be placed "
        f"within {stats['min_months']} months of a stretch's start or end. Events are "
        "checked when they fall inside a stretch.",
        "",
        "| Country | Months analysed |",
        "|---|---|",
        *[f"| {country} | {spans(parts)} |" for country, parts in analysed],
        "",
        "## Files",
        "",
        "- [breaks.csv](breaks.csv): every break, TP or FP, with its matched event",
        "- [event_outcomes.csv](event_outcomes.csv): every country-event pair checked, TP or FN",
        "- [event_recall.csv](event_recall.csv): the recall-by-event table above",
        "- [country_scores.csv](country_scores.csv): the by-country table above",
        "- [charts/](charts/): one chart per country (green = TP, red dashed = FP, "
        "orange = FN, grey = event matched)",
        "",
    ]
    return "\n".join(lines)


def write_index(results: Path):
    """results/README.md and settings_comparison.png: every setting run so far."""
    runs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(results.glob("*/summary.json"))]
    runs = [r for r in runs if "precision" in r]  # skip any folder from an older version
    lines = [
        "# Break detection results",
        "",
        "One folder per setting tested by `breaks.py`; open a folder's README for "
        "recall by event, scores by country, the false positives and negatives, "
        "and the charts. Breaks are scored against `events.csv`, one break per "
        "event within ±6 months.",
        "",
        "| Run | TP | FP | FN | Precision | Recall | F1 | Random F1 | p-value |",
        "|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|",
        *[f"| [{describe(r)}]({r['folder']}/) | {r['tp']} | {r['fp']} | {r['fn']} "
          f"| {r['precision']:.0%} | {r['recall']:.0%} | {r['f1']:.2f} "
          f"| {r['baseline_f1']:.2f} | {scoring.p_text(r['p_value'])} |" for r in runs],
        "",
        "![Precision vs recall for each setting](settings_comparison.png)",
        "",
        *TERMS,
        "",
    ]
    (results / "README.md").write_text("\n".join(lines), encoding="utf-8")
    settings_chart(runs, results / "settings_comparison.png")


def settings_chart(runs: list, path: Path):
    """Precision vs recall per setting, each next to its random baseline."""
    fig, ax = plt.subplots(figsize=(9, 6.5))
    scoring.style(ax)
    # Faint curves of equal F1 as a reading aid.
    r = np.linspace(0.01, 1, 200)
    for f in (0.2, 0.4, 0.6):
        p = f * r / (2 * r - f)
        keep = (p > 0) & (p <= 1)
        ax.plot(r[keep], p[keep], color=scoring.GRID, lw=1, zorder=1)
        ax.text(r[keep][-1], p[keep][-1], f" F1 = {f}", color=scoring.MUTED, fontsize=8, va="center")
    for colour, run in zip(scoring.SERIES, runs):
        ax.plot([run["baseline_recall"], run["recall"]], [run["baseline_precision"], run["precision"]],
                color=colour, lw=1, ls=":", zorder=2)
        ax.scatter(run["baseline_recall"], run["baseline_precision"], s=60, facecolor="white",
                   edgecolor=colour, lw=1.6, zorder=3)
        ax.scatter(run["recall"], run["precision"], s=80, color=colour, edgecolor="white", lw=1.5,
                   zorder=4, label=f"{describe(run)}: {scoring.counts(run)}, F1 {run['f1']:.2f}")
        ax.annotate(f"pen {run['penalty']:g}" + ("" if run["measure"] == "auction_yield" and
                                                  run["bucket"] == "Intermediate" else
                                                  f", {run['bucket'] if run['measure'] == 'auction_yield' else 'bid-to-cover'}"),
                    (run["recall"], run["precision"]), xytext=(7, 4), textcoords="offset points",
                    fontsize=8.5, color=scoring.INK_2)
    ax.scatter([], [], s=60, facecolor="white", edgecolor=scoring.MUTED, lw=1.6,
               label="Hollow = random baseline for that setting (same number of breaks)")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1))
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1))
    ax.set_xlabel("Recall = TP / (TP + FN)   (share of events detected)", color=scoring.INK_2)
    ax.set_ylabel("Precision = TP / (TP + FP)   (share of breaks that match an event)", color=scoring.INK_2)
    ax.set_title("Break detection: precision vs recall by setting", loc="left", color=scoring.INK, fontsize=12)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), frameon=False, fontsize=8.5,
              labelcolor=scoring.INK_2)
    fig.tight_layout()
    fig.savefig(path, dpi=120, facecolor="white")
    plt.close(fig)


def chart(stretches, breaks_df, events_df, country, args, path):
    """One country's series with each break and event marked by its outcome."""
    fig, ax = plt.subplots(figsize=(12, 4.8))
    scoring.style(ax)
    for i, s in enumerate(stretches):  # a gap between stretches = no data there
        ax.plot(s.index, s.values, color=scoring.SERIES[0], lw=1.6,
                label=args.measure.replace("_", " ") if i == 0 else None)
    seen = set()

    def mark(x, colour, ls, lw, label):
        ax.axvline(pd.Timestamp(x), color=colour, ls=ls, lw=lw, label=None if label in seen else label)
        seen.add(label)

    for r in events_df.itertuples():
        if r.outcome == "TP":
            mark(r.date, scoring.MUTED, ":", 1, "Event, detected")
        else:
            mark(r.date, scoring.FN_COLOUR, ":", 2.2, "False negative: event missed")
    for r in breaks_df.itertuples():
        if r.outcome == "TP":
            mark(r.break_month, scoring.TP_COLOUR, "-", 1.6, "True positive: break matched to an event")
        else:
            mark(r.break_month, scoring.FP_COLOUR, "--", 1.6, "False positive: break, no event")
    tp = int((breaks_df["outcome"] == "TP").sum()) if len(breaks_df) else 0
    fp = len(breaks_df) - tp
    fn = int((events_df["outcome"] == "FN").sum()) if len(events_df) else 0
    precision, recall, f1 = scoring.prf(tp, fp, fn)
    ax.set_title(f"{country}: {args.measure.replace('_', ' ')} ({args.bucket}), "
                 f"breaks found by ruptures (penalty {args.penalty:g})", loc="left",
                 color=scoring.INK, fontsize=11, pad=22)
    ax.text(0, 1.015, f"TP {tp} · FP {fp} · FN {fn}    precision {precision:.0%} · "
            f"recall {recall:.0%} · F1 {f1:.2f}    (match = within ±{scoring.TOLERANCE_MONTHS} months)",
            transform=ax.transAxes, fontsize=9, color=scoring.INK_2, va="bottom")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False, fontsize=8.5,
              labelcolor=scoring.INK_2)
    fig.tight_layout()
    fig.savefig(path, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    sys.exit(main())
