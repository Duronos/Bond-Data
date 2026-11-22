"""
Find break dates (regime changes) in the auction data with
ruptures, then check them against known historical events (events.csv).

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
    README.md         the results, readable on GitHub
    breaks.csv        every break, with the nearest relevant event (if any)
    sanity_check.csv  each event: in how many countries a break was found nearby
    summary.json      headline numbers (used for results/README.md)
    charts/<country>.png
results/README.md compares every setting run so far.
"""

import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # draw to files, no window
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ruptures as rpt

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
    parser.add_argument("--tolerance", type=int, default=6,
                        help="months either side of an event that count as a match")
    args = parser.parse_args()

    events = pd.read_csv(HERE / "events.csv", parse_dates=["date"])
    tolerance = pd.DateOffset(months=args.tolerance)
    out = HERE / "results" / f"{args.measure}_{args.bucket.lower()}_pen{args.penalty:g}"
    (out / "charts").mkdir(parents=True, exist_ok=True)

    rows, checked, analysed = [], [], []
    near = lambda a, b: abs(a - b) <= pd.Timedelta(days=31 * args.tolerance)
    for code, country in COUNTRIES.items():
        stretches = load_stretches(code, args.measure, args.bucket, 3 * args.min_months)
        if not stretches:
            continue
        breaks = [b for s in stretches for b in find_breaks(s, MODELS[args.measure], args.penalty, args.min_months)]
        relevant = events[[in_scope(s, country) for s in events["countries"]]]
        analysed.append((country, [(s.index[0], s.index[-1]) for s in stretches]))

        for date in breaks:
            gap = (relevant["date"] - date).abs()
            close = relevant[gap <= pd.Timedelta(days=31 * args.tolerance)]
            nearest = close.loc[gap[close.index].idxmin()] if not close.empty else None
            rows.append({
                "country": country, "break_month": date.date(),
                "nearest_event": nearest["event"] if nearest is not None else "",
                "event_date": nearest["date"].date() if nearest is not None else "",
                "months_off": round((date - nearest["date"]).days / 30.4, 1) if nearest is not None else "",
            })

        # Which events each stretch covers (with room either side), whether
        # a break fell nearby, and the chance rate for that check: the share
        # of the stretch's months, over the same span, that lie near some
        # break. A randomly dated event would be matched that often, so the
        # real hit rate has to beat it to mean anything.
        for s in stretches:
            first, last = s.index[0] + tolerance, s.index[-1] - tolerance
            months = s.index[(s.index >= first) & (s.index <= last)]
            own = [b for b in breaks if s.index[0] <= b <= s.index[-1]]
            chance = float(np.mean([any(near(m, b) for b in own) for m in months])) if len(months) else 0.0
            for _, ev in relevant.iterrows():
                if first <= ev["date"] <= last:
                    checked.append({"event": ev["event"], "date": ev["date"].date(), "country": country,
                                    "found": any(near(ev["date"], b) for b in own), "chance": chance})

        chart(stretches, breaks, relevant, country, args, out / "charts" / f"{code}.png")

    breaks_df = pd.DataFrame(rows)
    breaks_df.to_csv(out / "breaks.csv", index=False)
    checked = pd.DataFrame(checked)
    summary = (
        checked.groupby(["date", "event"], sort=True)
        .agg(countries_checked=("found", "size"), countries_found=("found", "sum"))
        .reset_index()
    )
    summary["hit_rate"] = (summary["countries_found"] / summary["countries_checked"]).round(2)
    summary.to_csv(out / "sanity_check.csv", index=False)

    stats = {
        "folder": out.name,
        "measure": args.measure,
        "bucket": args.bucket,
        "penalty": args.penalty,
        "min_months": args.min_months,
        "tolerance": args.tolerance,
        "breaks": len(breaks_df),
        "countries": int(breaks_df["country"].nunique()),
        "breaks_near_event": float((breaks_df["nearest_event"].fillna("") != "").mean()),
        "events_found": float(checked["found"].mean()),
        "chance": float(checked["chance"].mean()),
    }
    (out / "summary.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    report = run_report(stats, summary, breaks_df, analysed)
    (out / "README.md").write_text(report, encoding="utf-8")
    write_index(out.parent)
    print(report)
    print(f"Saved to {out.relative_to(HERE.parent)}")


def describe(stats: dict) -> str:
    return (f"{stats['measure'].replace('_', ' ')}, {stats['bucket']} bucket, "
            f"penalty {stats['penalty']:g}")


def run_report(stats: dict, summary: pd.DataFrame, breaks_df: pd.DataFrame, analysed: list) -> str:
    """One run's results as a markdown page (also printed to the console)."""
    unmatched = breaks_df[breaks_df["nearest_event"].fillna("") == ""]
    spans = lambda stretches: ", ".join(f"{a:%Y-%m} to {b:%Y-%m}" for a, b in stretches)
    lines = [
        f"# Breaks: {describe(stats)}",
        "",
        f"Settings: shortest segment {stats['min_months']} months; a break within "
        f"±{stats['tolerance']} months of an event counts as a match.",
        "",
        "| | |", "|---|---|",
        f"| Breaks found | {stats['breaks']}, in {stats['countries']} countries |",
        f"| Breaks near a known event | {stats['breaks_near_event']:.0%} |",
        f"| Events found (country by country) | {stats['events_found']:.0%} |",
        f"| Chance rate (a random date) | {stats['chance']:.0%} |",
        "",
        "The chance rate is worked out for each event check over the same span of "
        "that country's data, so the two rates compare like for like.",
        "",
        "## Each event",
        "",
        "| Date | Event | Countries checked | Found | Hit rate |",
        "|---|---|:-:|:-:|:-:|",
        *[f"| {r.date} | {r.event} | {r.countries_checked} | {r.countries_found} | {r.hit_rate:.0%} |"
          for r in summary.itertuples()],
        "",
        "## Breaks with no listed event",
        "",
        "Leads worth looking into: something changed, but it isn't in events.csv.",
        "",
        *([f"- {r.country}: {r.break_month}" for r in unmatched.itertuples()] or ["- none"]),
        "",
        "## Data analysed",
        "",
        f"Gaps of up to {GAP_MONTHS} months without an auction are filled with a straight "
        "line; a longer gap splits the series, and each stretch of at least "
        f"{3 * stats['min_months']} months is analysed on its own. A break can't be placed "
        f"within {stats['min_months']} months of a stretch's start or end.",
        "",
        "| Country | Months analysed |",
        "|---|---|",
        *[f"| {country} | {spans(stretches)} |" for country, stretches in analysed],
        "",
        "## Files",
        "",
        "- [breaks.csv](breaks.csv): every break and its nearest event",
        "- [sanity_check.csv](sanity_check.csv): the event table above",
        "- [charts/](charts/): one chart per country (red dashed = break found, "
        "grey dotted = known event)",
        "",
    ]
    return "\n".join(lines)


def write_index(results: Path):
    """results/README.md: one row per run folder, rebuilt after every run."""
    runs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(results.glob("*/summary.json"))]
    lines = [
        "# Break detection results",
        "",
        "One folder per setting tested by `breaks.py`; open a folder's README for "
        "the event-by-event table, the unmatched breaks and the charts. An events "
        "rate well above the chance rate means the breaks line up with real events.",
        "",
        "| Run | Breaks | Near an event | Events found | Chance rate |",
        "|---|:-:|:-:|:-:|:-:|",
        *[f"| [{describe(r)}]({r['folder']}/) | {r['breaks']} | {r['breaks_near_event']:.0%} "
          f"| {r['events_found']:.0%} | {r['chance']:.0%} |" for r in runs],
        "",
    ]
    (results / "README.md").write_text("\n".join(lines), encoding="utf-8")


def chart(stretches, breaks, events, country, args, path):
    fig, ax = plt.subplots(figsize=(12, 4.5))
    for i, s in enumerate(stretches):  # a gap between stretches = no data there
        ax.plot(s.index, s.values, color="#2a78d6", lw=1.4, label=args.measure if i == 0 else None)
    for i, ev in enumerate(events.itertuples()):
        ax.axvline(ev.date, color="#999999", ls=":", lw=1, label="Known event" if i == 0 else None)
    for i, b in enumerate(breaks):
        ax.axvline(b, color="#e34948", ls="--", lw=1.2, label="Break found" if i == 0 else None)
    ax.set_title(f"{country}: {args.measure.replace('_', ' ')} ({args.bucket}), "
                 f"breaks found by ruptures (penalty {args.penalty})", loc="left")
    ax.legend(loc="upper right", frameon=False)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    sys.exit(main())
