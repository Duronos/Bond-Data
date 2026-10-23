# Breaks: bid to cover, Intermediate bucket, penalty 2

Settings: shortest segment 6 months; a break within ±6 months of an event counts as a match.

| | |
|---|---|
| Breaks found | 8, in 5 countries |
| Breaks near a known event | 12% |
| Events found (country by country) | 1% |
| Chance rate (a random date) | 2% |

## Each event

| Date | Event | Countries checked | Found | Hit rate |
|---|---|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 12 | 0 | 0% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 6 | 0 | 0% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 6 | 0 | 0% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 6 | 0 | 0% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 14 | 0 | 0% |
| 2014-06-05 | ECB introduces negative interest rates | 6 | 0 | 0% |
| 2015-03-09 | ECB starts quantitative easing | 6 | 0 | 0% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 0 | 0% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 15 | 0 | 0% |
| 2022-02-24 | Russia invades Ukraine | 16 | 0 | 0% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 17 | 0 | 0% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 0 | 0% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 0 | 0% |

## Breaks with no listed event

Leads worth looking into: something changed, but it isn't in events.csv.

- United States: 2009-09-01
- United States: 2015-07-01
- United Kingdom: 2011-06-01
- United Kingdom: 2023-12-01
- Japan: 2010-02-01
- Italy: 2024-09-01
- Poland: 2021-06-01

## Files

- [breaks.csv](breaks.csv): every break and its nearest event
- [sanity_check.csv](sanity_check.csv): the event table above
- [charts/](charts/): one chart per country (red dashed = break found, grey dotted = known event)
