"""
Experimental: find break dates (regime changes) in the auction data with
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


def load_series(code: str, measure: str, bucket: str) -> pd.Series | None:
    """One country's monthly median (not the 3-month average), gaps filled."""
    path = RESULTS / code / f"{code}_auction_20y_monthly.csv"
    if not path.exists():
        return None
    df = pd.read_csv(path, parse_dates=["month"])
    df = df[df["bucket"].str.startswith(bucket)]
    series = df.set_index("month")[measure].dropna()
    if series.empty:
        return None
    # Months without an auction: fill gaps of up to 6 months by straight
    # lines so ruptures sees evenly spaced data; longer gaps stay empty and
    # the series is cut to its longest unbroken stretch.
    series = series.asfreq("MS").interpolate(limit=6, limit_area="inside")
    runs = series.notna().astype(int).groupby(series.isna().cumsum()).cumsum()
    end = runs.idxmax()
    return series.loc[end - pd.DateOffset(months=int(runs.max()) - 1):end]


def find_breaks(series: pd.Series, model: str, penalty: float, min_months: int) -> list:
    """Break dates: the first month of each new segment."""
    # Standardise so one penalty works across countries and measures; the
    # penalty is then log(n) x (variance = 1) x the --penalty factor.
    values = ((series - series.mean()) / series.std()).to_numpy().reshape(-1, 1)
    bkps = rpt.Pelt(model=model, min_size=min_months).fit(values).predict(
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

    rows, coverage, checked = [], [], []
    for code, country in COUNTRIES.items():
        series = load_series(code, args.measure, args.bucket)
        if series is None or len(series) < 3 * args.min_months:
            continue
        breaks = find_breaks(series, MODELS[args.measure], args.penalty, args.min_months)
        relevant = events[[in_scope(s, country) for s in events["countries"]]]

        for date in breaks:
            gap = (relevant["date"] - date).abs()
            near = relevant[gap <= pd.Timedelta(days=31 * args.tolerance)]
            nearest = near.loc[gap[near.index].idxmin()] if not near.empty else None
            rows.append({
                "country": country, "break_month": date.date(),
                "nearest_event": nearest["event"] if nearest is not None else "",
                "event_date": nearest["date"].date() if nearest is not None else "",
                "months_off": round((date - nearest["date"]).days / 30.4, 1) if nearest is not None else "",
            })

        # Which events this country's data covers, and whether a break fell nearby.
        for _, ev in relevant.iterrows():
            if series.index[0] + tolerance <= ev["date"] <= series.index[-1] - tolerance:
                hit = any(abs(b - ev["date"]) <= pd.Timedelta(days=31 * args.tolerance) for b in breaks)
                checked.append({"event": ev["event"], "date": ev["date"].date(),
                                "country": country, "found": hit})

        # Chance rate: share of this country's months that lie within the
        # tolerance of some break. A randomly dated "event" would be matched
        # this often, so the real hit rate has to beat it to mean anything.
        months = series.index
        near_break = np.zeros(len(months), dtype=bool)
        for b in breaks:
            near_break |= np.abs((months - b).days) <= 31 * args.tolerance
        coverage.append(near_break.mean())

        chart(series, breaks, relevant, country, args, out / "charts" / f"{code}.png")

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
        "chance": float(np.mean(coverage)),
    }
    (out / "summary.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    report = run_report(stats, summary, breaks_df)
    (out / "README.md").write_text(report, encoding="utf-8")
    write_index(out.parent)
    print(report)
    print(f"Saved to {out.relative_to(HERE.parent)}")


def describe(stats: dict) -> str:
    return (f"{stats['measure'].replace('_', ' ')}, {stats['bucket']} bucket, "
            f"penalty {stats['penalty']:g}")


def run_report(stats: dict, summary: pd.DataFrame, breaks_df: pd.DataFrame) -> str:
    """One run's results as a markdown page (also printed to the console)."""
    unmatched = breaks_df[breaks_df["nearest_event"].fillna("") == ""]
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


def chart(series, breaks, events, country, args, path):
    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(series.index, series.values, color="#2a78d6", lw=1.4, label=args.measure)
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
