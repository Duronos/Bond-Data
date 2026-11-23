# LLM analysis vs ruptures

An LLM (Claude Opus 5.5, in a Claude Code session) read every country's
monthly 2-10 year auction yields and marked break dates and their causes
**before** ruptures was rerun on the same data. See [METHOD.md](METHOD.md)
for the rules and the file hash that shows the list wasn't edited afterwards.

The LLM's list was made on the run of 19 November 2026. The comparison below
uses the run of 22 November 2026, after a code review fixed several data
problems (Italian dates, Slovak yields for 2009-2016 that were missing
before, a Finnish typo and others; see the main README) and made ruptures
consider every month as a break date. The LLM's list wasn't redone, so it
has no Slovak breaks before 2017.

- [breaks.csv](breaks.csv): the LLM's 148 breaks, each with a cause and a confidence
- [comparison.csv](comparison.csv): LLM and ruptures breaks side by side (main setting)
- [comparison.json](comparison.json): the numbers below
- [llm_vs_ruptures.png](llm_vs_ruptures.png): the chart below
- Rebuild the numbers: `python model_testing/compare_llm.py`

## How it's scored

Same rules as `breaks.py` ([scoring.py](../../scoring.py)): one-to-one
matching within ±6 months; TP = break matched, FP = break left unmatched,
FN = item in the reference left unmatched; precision = TP / (TP + FP),
recall = TP / (TP + FN), F1 their harmonic mean; each method against a
random baseline with the same number of breaks per stretch (1,000 draws).
Accuracy isn't used: almost every month is a true negative, so it would be
about 97% for any model.

Only the LLM's breaks that ruptures could have found count: inside a
stretch of data ruptures analyses, and not within 6 months of the
stretch's start or end (ruptures can't put a break there). That leaves 133
of the 148; of the other 15, 7 are in the last few months of data and the
rest near the edges of a stretch (Ireland, which auctions rarely, has 3).

![Ruptures and the LLM scored against events and against each other](llm_vs_ruptures.png)

## Headline

**Against known events** (`events.csv`, 140 country-event pairs):

| | TP | FP | FN | Precision | Recall | F1 | Random F1 | p-value |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Ruptures, penalty 2 (59 breaks) | 39 | 20 | 101 | 66% | 28% | 0.39 | 0.19 | ≤ 0.001 |
| LLM, all (133) | 63 | 70 | 77 | 47% | 45% | 0.46 | 0.29 | ≤ 0.001 |
| LLM, high confidence (56) | 40 | 16 | 100 | 71% | 29% | 0.41 | 0.17 | ≤ 0.001 |
| LLM, medium confidence (58) | 21 | 37 | 119 | 36% | 15% | 0.21 | 0.19 | 0.29 |
| LLM, low confidence (19) | 2 | 17 | 138 | 11% | 1% | 0.03 | 0.08 | 1.00 |

**Agreement, the LLM's list as reference** (TP = in both, FP = ruptures
only, FN = LLM only):

| Ruptures setting | TP | FP | FN | Precision | Recall | F1 | Recall of LLM high / medium / low |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Penalty 0.5 | 90 | 32 | 43 | 74% | 68% | 0.71 | 89% / 57% / 37% |
| Penalty 1 | 73 | 19 | 60 | 79% | 55% | 0.65 | 68% / 48% / 37% |
| Penalty 2 | 49 | 10 | 84 | 83% | 37% | 0.51 | 48% / 31% / 21% |

- **They agree on the big breaks.** At penalty 2, 83% of ruptures' breaks
  are in the LLM's list (precision); ruptures finds 37% of the LLM's
  breaks (recall), and 48% of its high-confidence ones. At penalty 0.5 F1
  rises to 0.71.
- **The LLM's high-confidence breaks are about as good as ruptures', not
  better.** Precision 71% vs 66% at about the same recall (29% vs 28%);
  both beat their random baselines by about 2 to 1 (p ≤ 0.001). Its medium
  confidence breaks are no better than random (p = 0.29) and its low
  confidence ones worse, partly because most of their causes are
  country-specific (a single central bank's move), which `events.csv`
  doesn't list.
- **On causes they agree 78% of the time.** Of the 37 TP pairs where
  ruptures' break is matched to an event, the LLM's cause is dated within
  3 months of that event in 29.

## Where they differ, and what it shows

**Ruptures misses some well-known episodes.** High-confidence LLM breaks that
ruptures could have found but didn't (FNs against the LLM's list) include the US taper tantrum (2013),
COVID in the US, UK, Canada, Norway, Poland and South Korea (2020), Italy's
euro crisis (2011), "whatever it takes" (2012) and the 2018 budget clash,
and Canada's 2015 oil shock. At penalty 2 only the biggest moves relative to
each country's 20-year range survive: the US fall from ~1.5% to ~0.3% in 2020
is small next to its 0-5% range. Lower penalties catch more of them.

**The ±6 month event matching sometimes credits the wrong event.** Ruptures
dates the Czech break to Nov 2021 and the matching labels it "Russia invades
Ukraine" (Feb 2022). It came *before* the invasion; the LLM's explanation,
the CNB's hiking cycle from mid-2021, fits the date. Hungary (Jan 2022) is
a closer call; Poland's break falls in Feb 2022, the invasion month itself.
Similarly Germany Sep 2022 is labelled "Fed starts raising rates" where the
ECB's own 75bp hike that month is the closer cause. Events country by
country would fix this (see below).

**Ruptures only (the 10 FPs against the LLM's list):** Germany 2009-10, Japan 2009-09, Norway
2010-03, Finland 2017-11 and 2018-11, Switzerland 2016-10, Belgium 2026-03,
plus three the LLM couldn't or didn't judge: Spain 2026-03 (the series only
starts in 2025, so the LLM skipped it) and Slovakia 2012-02 and 2014-03 (no
Slovak yields before 2017 when the LLM made its list).

## Problems found in the data

All found while preparing this analysis or in the code reviews that
followed, and fixed in the runs of 21-22 November 2026:

- **Break dates on a 5-month grid:** ruptures by default only tries every
  5th month as a break date (`jump=5`), which moved dates by up to 2 months
  (e.g. Poland Dec 2021 instead of Feb 2022). It now tries every month.

- **Finland:** the 17 Nov 2026 4-year auction is published at a yield of
  3,389% (almost certainly 3.389%). It gave ruptures a false break; such
  values are now left out as typos.
- **Gaps:** filling months without auctions used to reach across long gaps
  and invent values (e.g. Belgium Dec 2019-May 2020), and only each
  country's longest unbroken stretch was analysed. Now only gaps of up to 6
  months are filled, and every stretch of 18+ months is analysed.

Still true:

- **Belgium:** no 2-10 year auctions in 2020-2022, so the 2022 rise happens
  in a gap and can't be dated.
- **Finland, Ireland, Switzerland:** few auctions per year, so breaks there
  are dated less precisely.
- **Sep-Oct 2026:** yields jumped in most countries at once. This is after
  the LLM's knowledge cutoff (June 2026), so it names no cause.

## Caveats

- The LLM is not fully independent: it wrote `events.csv` and saw an
  earlier set of ruptures results in the same conversation. Its causes come
  from its own knowledge and were not checked against sources.
- Judging breaks by eye is subjective and can't be rerun to give the same
  answer; ruptures can.
- Agreement on a cause is by timing (within 3 months), not by reading both
  explanations.

## Suggested next steps

- Add country-specific events to `events.csv` (each country's main central
  bank moves), so matching stops crediting regional breaks to global events.
- Report results at penalty 0.5 or 1 alongside penalty 2: they have a
  higher F1, against events and against the LLM's list.
- Events only weeks apart (the Ukraine invasion and the Fed's first hike,
  2022) can't both be matched in one country, which caps recall; merging
  such clusters into one event would score them fairly.
- Redo the LLM's list on the current data (Slovakia 2009-2016 in particular).
