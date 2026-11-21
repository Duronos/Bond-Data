# Breaks: bid to cover, Intermediate bucket, penalty 2

Settings: shortest segment 6 months; a break within ±6 months of an event counts as a match.

| | |
|---|---|
| Breaks found | 9, in 5 countries |
| Breaks near a known event | 22% |
| Events found (country by country) | 2% |
| Chance rate (a random date) | 3% |

The chance rate is worked out for each event check over the same span of that country's data, so the two rates compare like for like.

## Each event

| Date | Event | Countries checked | Found | Hit rate |
|---|---|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 12 | 0 | 0% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 6 | 0 | 0% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 7 | 0 | 0% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 6 | 0 | 0% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 16 | 0 | 0% |
| 2014-06-05 | ECB introduces negative interest rates | 6 | 0 | 0% |
| 2015-03-09 | ECB starts quantitative easing | 6 | 0 | 0% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 0 | 0% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 17 | 1 | 6% |
| 2022-02-24 | Russia invades Ukraine | 17 | 0 | 0% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 18 | 0 | 0% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 0 | 0% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 0 | 0% |

## Breaks with no listed event

Leads worth looking into: something changed, but it isn't in events.csv.

- United States: 2009-10-01
- United States: 2015-03-01
- United Kingdom: 2011-06-01
- United Kingdom: 2023-12-01
- Japan: 2011-11-01
- Italy: 2024-11-01
- Poland: 2021-07-01

## Data analysed

Gaps of up to 6 months without an auction are filled with a straight line; a longer gap splits the series, and each stretch of at least 18 months is analysed on its own. A break can't be placed within 6 months of a stretch's start or end.

| Country | Months analysed |
|---|---|
| United States | 2006-11 to 2026-10 |
| Canada | 2007-05 to 2026-10 |
| United Kingdom | 2006-11 to 2026-10 |
| Germany | 2006-11 to 2026-10 |
| Japan | 2006-11 to 2026-09 |
| Belgium | 2006-11 to 2019-11, 2024-06 to 2026-10 |
| Czech Republic | 2006-11 to 2026-10 |
| Denmark | 2009-04 to 2014-09, 2015-10 to 2026-10 |
| Finland | 2010-04 to 2012-10, 2015-11 to 2019-04, 2020-03 to 2026-10 |
| France | 2007-01 to 2026-10 |
| Hungary | 2006-11 to 2026-10 |
| Ireland | 2009-03 to 2010-09, 2016-05 to 2018-11, 2019-07 to 2021-11 |
| Italy | 2006-12 to 2026-10 |
| Lithuania | 2009-10 to 2026-10 |
| Norway | 2006-11 to 2026-10 |
| Poland | 2006-12 to 2026-10 |
| Slovakia | 2009-11 to 2017-11, 2018-10 to 2026-10 |
| South Korea | 2018-01 to 2026-10 |
| Spain | 2025-01 to 2026-10 |
| Switzerland | 2012-03 to 2014-10, 2016-04 to 2018-01, 2019-09 to 2026-10 |
| European Union | 2021-09 to 2026-10 |

## Files

- [breaks.csv](breaks.csv): every break and its nearest event
- [sanity_check.csv](sanity_check.csv): the event table above
- [charts/](charts/): one chart per country (red dashed = break found, grey dotted = known event)
