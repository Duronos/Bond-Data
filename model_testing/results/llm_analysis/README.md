# LLM analysis vs ruptures

An LLM (Claude Opus 5.5, in a Claude Code session) read every country's
monthly 2-10 year auction yields and marked break dates and their causes
**before** ruptures was rerun on the same data. See [METHOD.md](METHOD.md)
for the rules and the file hash that shows the list wasn't edited afterwards.
Data: run of 19 November 2026.

- [breaks.csv](breaks.csv): the LLM's 148 breaks, each with a cause and a confidence
- [comparison.csv](comparison.csv): LLM and ruptures breaks side by side (main setting)
- [comparison.json](comparison.json): the numbers below
- Rebuild the numbers: `python model_testing/compare_llm.py`

## Headline

Compared with ruptures' main setting (penalty 2, 50 breaks); a match is within ±6 months.

| | Ruptures | LLM, all breaks | LLM, high confidence only |
|---|:-:|:-:|:-:|
| Breaks | 50 | 148 | 57 |
| Near a known event | 66% | 46% | 72% |
| Events found (country by country) | 43% | 62% | 43% |
| Chance rate (a random date) | 17% | 38% | 15% |

- **They mostly agree on where the big breaks are.** 43 of ruptures' 50
  breaks (86%) are also in the LLM's list. Ruptures finds 44% of the LLM's
  high-confidence breaks at penalty 2, and 77% at penalty 0.5.
- **The LLM's confident breaks are as good as ruptures', no better.** Its 57
  high-confidence breaks line up with known events at almost exactly the same
  rate (43% found vs 15% by chance; ruptures 43% vs 17%). Its medium and low
  confidence breaks barely beat chance against `events.csv`, partly because
  most of their causes are country-specific (a single central bank's move),
  which `events.csv` doesn't list.
- **On causes they agree 82% of the time.** Of the 33 paired breaks where
  ruptures matched an event, the LLM's cause is dated within 3 months of that
  event in 27.

## Where they differ, and what it shows

**Ruptures misses some well-known episodes.** High-confidence LLM breaks with
no ruptures break nearby include the US taper tantrum (2013), COVID in the
US, UK, Canada, Norway, Poland and South Korea (2020), Italy's euro crisis
(2011), "whatever it takes" (2012) and the 2018 budget clash, and Canada's
2015 oil shock. At penalty 2 only the biggest moves relative to each
country's 20-year range survive: the US fall from ~1.5% to ~0.3% in 2020 is
small next to its 0-5% range. Lower penalties catch more of them.

**The ±6 month event matching sometimes credits the wrong event.** Ruptures
dates the Czech, Hungarian and Polish breaks to Nov-Dec 2021 and the
matching labels them "Russia invades Ukraine" (Feb 2022). They came *before*
the invasion; the LLM's explanation, central-bank hiking cycles that started
in mid-to-late 2021, fits the dates. Similarly Germany Sep 2022 is labelled
"Fed starts raising rates" where the ECB's own 75bp hike that month is the
closer cause. Events country by country would fix this (see below).

**The LLM explains 10 breaks that ruptures left unmatched,** mostly
country-specific: Hungary's and Poland's easing cycles (Aug and Nov 2012),
the Czech cut to 0.05% (Nov 2012), Hungary's record-low rates (May 2014),
Norway's oil shock (Oct-Nov 2014), the 2009 crisis in Austria and Japan, and
Canada's 2011 flight to safety.

**Ruptures-only breaks (7):** Germany 2009-10, Japan 2014-05, Norway 2010-03,
Poland 2019-01, Switzerland 2024-09, plus two the LLM excluded on purpose:
Spain 2026-04 (the series only starts in 2025) and **Finland 2026-06, which
comes from a data error** (below).

## Problems found in the data

- **Finland:** the 17 Nov 2026 4-year auction is reported at a yield of
  **3,389%** (almost certainly 3.389%), making November's median 1,696%. It
  produces a false ruptures break and distorts Finland's charts. Needs a fix
  in the loader.
- **Belgium:** no 2-10 year auctions 2020-2022, so the 2022 rise happens in a
  gap and can't be dated.
- **Finland, Ireland, Switzerland:** too few auctions per year to date breaks
  with any confidence.
- **Sep-Oct 2026:** yields jumped in most countries at once (US 5.1%, UK 5.0%,
  France 4.1%). This is after the LLM's knowledge cutoff (June 2026), so it
  names no cause.

## Caveats

- The LLM is not fully independent: it wrote `events.csv` and saw the
  previous ruptures results earlier in the same conversation. Its causes come
  from its own knowledge and were not checked against sources.
- Judging breaks by eye is subjective and can't be rerun to give the same
  answer; ruptures can.
- Agreement on a cause is by timing (within 3 months), not by reading both
  explanations.

## Suggested next steps

- Fix the Finland yield (e.g. reject auction yields above 25%).
- Add country-specific events to `events.csv` (each country's main central
  bank moves), so matching stops crediting regional breaks to global events.
- Report results at penalty 1 alongside penalty 2: it keeps more of the
  breaks both methods agree on.
