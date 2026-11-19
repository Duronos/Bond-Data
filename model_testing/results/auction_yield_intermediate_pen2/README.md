# Breaks: auction yield, Intermediate bucket, penalty 2

Settings: shortest segment 6 months; a break within ±6 months of an event counts as a match.

| | |
|---|---|
| Breaks found | 50, in 22 countries |
| Breaks near a known event | 66% |
| Events found (country by country) | 43% |
| Chance rate (a random date) | 17% |

## Each event

| Date | Event | Countries checked | Found | Hit rate |
|---|---|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 14 | 5 | 36% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 7 | 0 | 0% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 7 | 2 | 29% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 7 | 4 | 57% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 15 | 0 | 0% |
| 2014-06-05 | ECB introduces negative interest rates | 7 | 5 | 71% |
| 2015-03-09 | ECB starts quantitative easing | 7 | 3 | 43% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 0 | 0% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 17 | 0 | 0% |
| 2022-02-24 | Russia invades Ukraine | 18 | 14 | 78% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 19 | 17 | 89% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 1 | 100% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 1 | 100% |

## Breaks with no listed event

Leads worth looking into: something changed, but it isn't in events.csv.

- Canada: 2011-07-01
- Germany: 2009-10-01
- Japan: 2009-05-01
- Japan: 2014-05-01
- Japan: 2026-01-01
- Austria: 2009-08-01
- Czech Republic: 2010-03-01
- Czech Republic: 2012-09-01
- Finland: 2026-06-01
- Hungary: 2012-09-01
- Hungary: 2014-05-01
- Norway: 2010-03-01
- Norway: 2014-10-01
- Poland: 2012-10-01
- Poland: 2019-01-01
- Spain: 2026-04-01
- Switzerland: 2024-09-01

## Files

- [breaks.csv](breaks.csv): every break and its nearest event
- [sanity_check.csv](sanity_check.csv): the event table above
- [charts/](charts/): one chart per country (red dashed = break found, grey dotted = known event)
