# Breaks: auction yield, Long bucket, penalty 2

Settings: shortest segment 6 months; a break within ±6 months of an event counts as a match.

| | |
|---|---|
| Breaks found | 64, in 22 countries |
| Breaks near a known event | 48% |
| Events found (country by country) | 41% |
| Chance rate (a random date) | 20% |

The chance rate is worked out for each event check over the same span of that country's data, so the two rates compare like for like.

## Each event

| Date | Event | Countries checked | Found | Hit rate |
|---|---|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 9 | 0 | 0% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 6 | 2 | 33% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 7 | 3 | 43% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 7 | 2 | 29% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 15 | 0 | 0% |
| 2014-06-05 | ECB introduces negative interest rates | 7 | 7 | 100% |
| 2015-03-09 | ECB starts quantitative easing | 7 | 3 | 43% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 1 | 100% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 15 | 1 | 7% |
| 2022-02-24 | Russia invades Ukraine | 17 | 12 | 71% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 17 | 13 | 76% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 1 | 100% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 0 | 0% |

## Breaks with no listed event

Leads worth looking into: something changed, but it isn't in events.csv.

- United States: 2011-09-01
- United States: 2019-08-01
- Canada: 2011-08-01
- Canada: 2014-12-01
- United Kingdom: 2011-12-01
- Germany: 2022-11-01
- Japan: 2025-03-01
- Austria: 2022-11-01
- Belgium: 2026-02-01
- Czech Republic: 2007-09-01
- Czech Republic: 2010-06-01
- Czech Republic: 2014-05-01
- Denmark: 2011-09-01
- Denmark: 2014-08-01
- Denmark: 2016-08-01
- Finland: 2019-04-01
- France: 2022-11-01
- Hungary: 2014-05-01
- Ireland: 2015-12-01
- Ireland: 2017-03-01
- Ireland: 2018-01-01
- Italy: 2019-06-01
- Lithuania: 2021-04-01
- Netherlands: 2019-06-01
- Norway: 2025-02-01
- Poland: 2012-11-01
- Poland: 2016-12-01
- Poland: 2019-06-01
- Poland: 2023-11-01
- South Korea: 2026-05-01
- Switzerland: 2011-09-01
- Switzerland: 2015-01-01
- European Union: 2023-02-01

## Data analysed

Gaps of up to 6 months without an auction are filled with a straight line; a longer gap splits the series, and each stretch of at least 18 months is analysed on its own. A break can't be placed within 6 months of a stretch's start or end.

| Country | Months analysed |
|---|---|
| United States | 2007-02 to 2026-10 |
| Canada | 2007-01 to 2026-10 |
| United Kingdom | 2006-12 to 2026-07 |
| Germany | 2007-01 to 2026-10 |
| Japan | 2006-11 to 2026-09 |
| Austria | 2008-04 to 2026-10 |
| Belgium | 2009-01 to 2019-11, 2023-03 to 2026-10 |
| Czech Republic | 2006-11 to 2008-06, 2009-03 to 2012-03, 2013-02 to 2026-09 |
| Denmark | 2010-06 to 2015-01, 2015-10 to 2018-05, 2019-01 to 2026-10 |
| Finland | 2012-10 to 2014-10, 2018-06 to 2019-11, 2020-09 to 2026-10 |
| France | 2007-01 to 2026-10 |
| Hungary | 2006-11 to 2026-10 |
| Ireland | 2015-02 to 2019-07, 2020-05 to 2024-05 |
| Italy | 2006-12 to 2026-10 |
| Lithuania | 2019-08 to 2022-01 |
| Netherlands | 2007-01 to 2008-06, 2009-02 to 2017-07, 2018-03 to 2020-06, 2021-02 to 2026-09 |
| Norway | 2023-01 to 2026-10 |
| Poland | 2007-01 to 2013-10, 2014-06 to 2020-07, 2023-01 to 2026-07 |
| Slovakia | 2011-02 to 2026-10 |
| South Korea | 2018-01 to 2026-10 |
| Spain | 2025-01 to 2026-10 |
| Switzerland | 2010-11 to 2026-09 |
| European Union | 2022-04 to 2026-10 |

## Files

- [breaks.csv](breaks.csv): every break and its nearest event
- [sanity_check.csv](sanity_check.csv): the event table above
- [charts/](charts/): one chart per country (red dashed = break found, grey dotted = known event)
