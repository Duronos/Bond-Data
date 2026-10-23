# Breaks: auction yield, Long bucket, penalty 2

Settings: shortest segment 6 months; a break within ±6 months of an event counts as a match.

| | |
|---|---|
| Breaks found | 45, in 22 countries |
| Breaks near a known event | 60% |
| Events found (country by country) | 41% |
| Chance rate (a random date) | 18% |

## Each event

| Date | Event | Countries checked | Found | Hit rate |
|---|---|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 9 | 0 | 0% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 6 | 2 | 33% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 6 | 3 | 50% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 6 | 1 | 17% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 13 | 0 | 0% |
| 2014-06-05 | ECB introduces negative interest rates | 6 | 6 | 100% |
| 2015-03-09 | ECB starts quantitative easing | 6 | 3 | 50% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 1 | 100% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 15 | 0 | 0% |
| 2022-02-24 | Russia invades Ukraine | 15 | 10 | 67% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 15 | 13 | 87% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 1 | 100% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 0 | 0% |

## Breaks with no listed event

Leads worth looking into: something changed, but it isn't in events.csv.

- United States: 2011-06-01
- United States: 2019-05-01
- Canada: 2011-08-01
- Canada: 2014-12-01
- United Kingdom: 2011-11-01
- Japan: 2025-02-01
- Austria: 2022-11-01
- Czech Republic: 2014-05-01
- France: 2022-11-01
- Hungary: 2014-04-01
- Ireland: 2019-04-01
- Italy: 2019-06-01
- Norway: 2025-02-01
- Poland: 2012-06-01
- South Korea: 2026-05-01
- Switzerland: 2011-09-01
- Switzerland: 2015-01-01
- European Union: 2023-02-01

## Files

- [breaks.csv](breaks.csv): every break and its nearest event
- [sanity_check.csv](sanity_check.csv): the event table above
- [charts/](charts/): one chart per country (red dashed = break found, grey dotted = known event)
