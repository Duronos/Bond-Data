# LLM analysis: method (written before looking at the data)

An independent check on `breaks.py`, done by an LLM (Claude Opus 5.5, in a
Claude Code session) instead of a statistical model. Written down before the
analysis so the method can't drift to fit the results.

## Isolation

- Data: the fresh run copied into `results/`, the same monthly CSVs
  `breaks.py` reads (`results/auctions/<code>/<code>_auction_20y_monthly.csv`).
- Same series as the main `breaks.py` setting: monthly median **auction
  yield**, **Intermediate (2-10 year)** bucket.
- Done **before** `breaks.py` is rerun on the new data, without running or
  reading any ruptures output. The SHA-256 of `breaks.csv` here is recorded
  before ruptures runs, so it can be checked that it wasn't edited afterwards.
- Caveat: the LLM saw the *previous* ruptures results (from the 22 Oct 2026
  data) earlier in the same conversation, so it is not perfectly blind.

## What the LLM does, per country

1. Read the monthly numbers (not the charts).
2. Mark each **break**: the first month of a lasting move to a new level
   (roughly 6+ months), not one-off spikes. Same idea as ruptures' level-shift
   model, judged by eye from the numbers.
3. For each break, name the most likely cause from its own knowledge, the
   month the cause started, and a confidence (high / medium / low). "No clear
   cause" is allowed.
4. Also note anything notable in the data that isn't a break (spikes, gaps,
   data problems).

## Comparison (after ruptures has run)

- LLM breaks vs ruptures breaks: matched if within ±6 months (same tolerance
  as `breaks.py`).
- Both against `events.csv`, with the same ±6 month rule.
- Where they disagree, look at why (missed shift, spike, data issue).

## Record

- Data: run `2026-11-19_055415_20y` (copied into `results/`).
- `breaks.csv` finished 2026-11-19 06:06, before `breaks.py` was rerun:
  148 breaks in 22 countries (Greece and Slovenia have no 2-10 year yields).
- SHA-256 of `breaks.csv` at that point:
  `9222e958b43d5cf70be1b298db4717ace9ef26a3170ee847e4642fb75789b583`
  (LF line endings, as stored in git; check with
  `git show HEAD:model_testing/results/llm_analysis/breaks.csv | sha256sum`).
