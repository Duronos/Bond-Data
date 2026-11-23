# Rules for the events list (events_v2.csv)

The events list is the answer key that break detection (ruptures, and the
LLM's own list) is scored against. These rules are fixed **before** any
research, so the list can't be bent towards the breaks the models found.

## 1. Stay blind to the results

The researcher and the reviewer must not open:

- anything in `model_testing/results/` (breaks, comparisons, charts, READMEs)
- the auction data in `results/` or `runs/`, or any yield chart of it

Events come from history and sources, not from looking at the yields:
picking dates where the data jumps is the detectors' job, not the answer
key's.

## 2. Period and countries

- Period: 1 November 2006 to 31 October 2026 (the 20-year window).
- Countries: United States, Canada, United Kingdom, Germany, Japan, Austria,
  Belgium, Czech Republic, Denmark, Finland, France, Greece, Hungary,
  Ireland, Italy, Lithuania, Netherlands, Norway, Poland, Slovakia,
  Slovenia, South Korea, Spain, Switzerland, European Union (EU bonds).

## 3. What counts as an event

An event must have a clear start date and be something that plausibly
moves a country's 2-10 year government bond yields for months, not days.

| Type | Counts | Doesn't count |
|---|---|---|
| **Monetary** | First move of a new hiking or cutting cycle; start or end of QE, yield-curve control or negative rates; a currency floor or peg set or dropped; a surprise change of central bank framework | Each further move in a cycle already under way; routine meetings with no change |
| **Fiscal / sovereign** | Bailouts, debt restructuring, a budget crisis that markets react to, joining the euro, a rating cut to or from junk | Ordinary budgets; small rating changes |
| **Political** | A government falling, a snap election or referendum, where a source says bond markets reacted | Scheduled elections with no market reaction reported |
| **Geopolitical** | Start of a war or invasion, a major escalation, sweeping sanctions, an energy-supply cut caused by conflict | Ongoing wars after their start (unless a major escalation); threats or rhetoric |
| **Financial / global shock** | Bank failures or rescues that spread (e.g. a systemic bank collapse), a pandemic, a sharp commodity shock | Single-day market drops that reverse |

## 4. The date

- The day the news first reached markets (announcement, invasion, failure),
  not when a policy took effect.
- For a cycle: the date of the first decision.
- Within the period in section 2; nothing outside it.

## 5. Which countries an event covers (`countries` column)

- `all`: only if a source shows a reaction in bond markets broadly (not
  just one region). Global events go here: the financial crisis, a
  pandemic, the start of a major war.
- `euro`: euro-area events (ECB decisions, euro crisis). Applies to a
  country only from the date it joined: Slovenia 1 Jan 2007, Slovakia
  1 Jan 2009, Lithuania 1 Jan 2015. The EU's own bonds count as euro.
- One or more named countries, separated by `;` (e.g.
  `Czech Republic;Hungary;Poland`), for anything narrower. A country's own
  central bank decisions cover that country only.

## 6. Events close together

If two events would apply to the same country within **3 months** of each
other, they are one event for that country: dated at the earlier one, with
both named in the `event` text (e.g. "Russia invades Ukraine + Fed starts
raising rates"). A break can only be matched to one event, so without this
rule a single real shift would count as one TP and one FN.

## 7. Evidence

Every event needs a source with a URL: a central bank or government
statement, an official body (IMF, BIS, ECB, OECD), or a major news outlet
(Reuters, FT, Bloomberg, AP). Wikipedia can help find events but isn't the
source. Political and geopolitical events, and any `all` scope, need a
source that mentions the bond-market reaction.

## 8. File format

`events_v2.csv`, one row per event:

```
date,event,countries,type,source
2022-02-24,Russia invades Ukraine,all,geopolitical,https://...
```

`type` is one of: monetary, fiscal, political, geopolitical, financial.
The old `events.csv` (14 events) is kept as it is, so scores on the old and
new lists can be compared.

## 9. Review

A second, separate agent checks every row, also blind (section 1):

- the date matches the source (within 3 days)
- the type and scope follow sections 3 and 5
- section 6 was applied
- marks each row **keep**, **fix** (with the correction) or **drop** (with
  the reason), and lists big events it thinks are missing, marked as
  added by the reviewer

Rows the researcher and reviewer disagree on go to the owner to decide.

## 10. Note on list size

More events make it easier for any break to land near one. The random
baseline and p-value in `scoring.py` account for this (random breaks get
the same chance), so a longer list doesn't flatter the models; but events
should still be picked by these rules, not added to fill gaps.
