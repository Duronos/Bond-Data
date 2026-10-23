# Breaks: auction yield, Intermediate bucket, penalty 0.5

Settings: shortest segment 6 months; a break within ±6 months of an event counts as a match.

| | |
|---|---|
| Breaks found | 93, in 22 countries |
| Breaks near a known event | 56% |
| Events found (country by country) | 61% |
| Chance rate (a random date) | 28% |

## Each event

| Date | Event | Countries checked | Found | Hit rate |
|---|---|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 14 | 9 | 64% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 7 | 1 | 14% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 7 | 5 | 71% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 7 | 5 | 71% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 15 | 2 | 13% |
| 2014-06-05 | ECB introduces negative interest rates | 7 | 6 | 86% |
| 2015-03-09 | ECB starts quantitative easing | 7 | 3 | 43% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 1 | 100% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 17 | 3 | 18% |
| 2022-02-24 | Russia invades Ukraine | 18 | 17 | 94% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 19 | 19 | 100% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 1 | 100% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 1 | 100% |

## Breaks with no listed event

Leads worth looking into: something changed, but it isn't in events.csv.

- United States: 2008-01-01
- United States: 2011-05-01
- United States: 2017-03-01
- Canada: 2008-02-01
- Canada: 2011-06-01
- Canada: 2015-03-01
- Canada: 2017-09-01
- Canada: 2024-10-01
- United Kingdom: 2011-06-01
- Germany: 2009-09-01
- Japan: 2011-05-01
- Japan: 2025-02-01
- Japan: 2025-12-01
- Austria: 2009-08-01
- Czech Republic: 2010-03-01
- Czech Republic: 2012-09-01
- Czech Republic: 2014-05-01
- Czech Republic: 2017-09-01
- Denmark: 2022-11-01
- France: 2023-02-01
- Hungary: 2008-01-01
- Hungary: 2009-09-01
- Hungary: 2014-09-01
- Hungary: 2023-11-01
- Italy: 2009-04-01
- Italy: 2011-05-01
- Italy: 2018-06-01
- Italy: 2019-04-01
- Norway: 2010-03-01
- Norway: 2011-11-01
- Norway: 2014-10-01
- Norway: 2023-07-01
- Poland: 2012-09-01
- Poland: 2014-05-01
- Poland: 2021-06-01
- Poland: 2023-07-01
- South Korea: 2019-04-01
- South Korea: 2024-09-01
- South Korea: 2025-12-01
- Spain: 2026-04-01
- Switzerland: 2024-09-01

## Files

- [breaks.csv](breaks.csv): every break and its nearest event
- [sanity_check.csv](sanity_check.csv): the event table above
- [charts/](charts/): one chart per country (red dashed = break found, grey dotted = known event)
