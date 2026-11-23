# Breaks: auction yield, Long bucket, penalty 2

Breaks are scored against [events.csv](../../events.csv), one break per event, within ±6 months; shortest segment 6 months. 68 breaks in 22 countries; 118 country-event pairs checked.

| | Model | Random baseline |
|---|:-:|:-:|
| Precision | **50%** (34 of 68 breaks) | 28% |
| Recall | **29%** (34 of 118 events) | 16% |
| F1 | **0.37** | 0.20 |

Confusion counts: **34 TP**, **34 FP**, **84 FN** (no true negatives: see below). p-value vs random: ≤ 0.001.

| Term | Meaning here |
|---|---|
| True positive (TP) | a break matched to a known event within ±6 months |
| False positive (FP) | a break with no event left to match (a lead, or noise) |
| False negative (FN) | a known event with no break matched to it (missed) |
| Precision | TP / (TP + FP): share of breaks that match an event |
| Recall | TP / (TP + FN): share of events that were detected |
| F1 | 2 × precision × recall / (precision + recall) |
| Random baseline | the same number of breaks per stretch at random dates, scored the same way (1,000 draws, average) |
| p-value | share of random draws with an F1 at least as high as the real one |

Accuracy isn't reported: it needs true negatives (months with neither a break nor an event), and almost every month is one. A model that never finds a break would score 97% accuracy on these 3,977 months.

## Recall by event

| Date | Event | Countries checked | TP | FN | Recall |
|---|---|:-:|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 10 | 0 | 10 | 0% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 6 | 2 | 4 | 33% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 7 | 2 | 5 | 29% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 7 | 2 | 5 | 29% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 17 | 0 | 17 | 0% |
| 2014-06-05 | ECB introduces negative interest rates | 8 | 5 | 3 | 62% |
| 2015-03-09 | ECB starts quantitative easing | 8 | 3 | 5 | 38% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 1 | 0 | 100% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 0 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 17 | 1 | 16 | 6% |
| 2022-02-24 | Russia invades Ukraine | 17 | 3 | 14 | 18% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 17 | 13 | 4 | 76% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 1 | 0 | 100% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 0 | 1 | 0% |

## Scores by country

| Country | TP | FP | FN | Precision | Recall | F1 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| United States | 1 | 3 | 4 | 25% | 20% | 0.22 |
| Canada | 1 | 2 | 4 | 33% | 20% | 0.25 |
| United Kingdom | 2 | 1 | 5 | 67% | 29% | 0.40 |
| Germany | 3 | 0 | 7 | 100% | 30% | 0.46 |
| Japan | 2 | 1 | 5 | 67% | 29% | 0.40 |
| Austria | 3 | 0 | 7 | 100% | 30% | 0.46 |
| Belgium | 2 | 1 | 4 | 67% | 33% | 0.44 |
| Czech Republic | 1 | 3 | 3 | 25% | 25% | 0.25 |
| Denmark | 1 | 4 | 3 | 20% | 25% | 0.22 |
| Finland | 2 | 1 | 2 | 67% | 50% | 0.57 |
| France | 3 | 0 | 7 | 100% | 30% | 0.46 |
| Hungary | 1 | 1 | 4 | 50% | 20% | 0.29 |
| Ireland | 1 | 3 | 2 | 25% | 33% | 0.29 |
| Italy | 2 | 1 | 8 | 67% | 20% | 0.31 |
| Lithuania | 1 | 1 | 0 | 50% | 100% | 0.67 |
| Netherlands | 3 | 1 | 6 | 75% | 33% | 0.46 |
| Norway | 0 | 1 | 0 | 0% | 0% | 0.00 |
| Poland | 0 | 4 | 3 | 0% | 0% | 0.00 |
| Slovakia | 3 | 0 | 5 | 100% | 38% | 0.55 |
| South Korea | 1 | 1 | 2 | 50% | 33% | 0.40 |
| Spain | 0 | 0 | 0 | 0% | 0% | 0.00 |
| Switzerland | 1 | 3 | 3 | 25% | 25% | 0.25 |
| European Union | 0 | 2 | 0 | 0% | 0% | 0.00 |

## False positives (breaks with no event left to match)

Leads worth looking into: something changed, but it isn't in events.csv (or its event was already matched to another break).

- United States: 2011-08-01
- United States: 2019-08-01
- United States: 2023-08-01
- Canada: 2011-07-01
- Canada: 2014-12-01
- United Kingdom: 2011-10-01
- Japan: 2025-05-01
- Belgium: 2026-03-01
- Czech Republic: 2007-05-01
- Czech Republic: 2010-04-01
- Czech Republic: 2014-05-01
- Denmark: 2011-08-01
- Denmark: 2014-08-01
- Denmark: 2016-05-01
- Denmark: 2017-12-01
- Finland: 2019-05-01
- Hungary: 2014-05-01
- Ireland: 2015-12-01
- Ireland: 2017-01-01
- Ireland: 2018-02-01
- Italy: 2019-07-01
- Lithuania: 2021-08-01
- Netherlands: 2019-06-01
- Norway: 2025-03-01
- Poland: 2012-09-01
- Poland: 2016-11-01
- Poland: 2019-05-01
- Poland: 2023-07-01
- South Korea: 2026-05-01
- Switzerland: 2011-08-01
- Switzerland: 2014-11-01
- Switzerland: 2023-12-01
- European Union: 2022-10-01
- European Union: 2025-03-01

## False negatives (events with no break)

- United States: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- United States: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United States: COVID-19 declared a pandemic (2020-03-11)
- United States: Russia invades Ukraine (2022-02-24)
- Canada: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Canada: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Canada: COVID-19 declared a pandemic (2020-03-11)
- Canada: Russia invades Ukraine (2022-02-24)
- United Kingdom: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- United Kingdom: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United Kingdom: COVID-19 declared a pandemic (2020-03-11)
- United Kingdom: Russia invades Ukraine (2022-02-24)
- United Kingdom: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Germany: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Germany: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Germany: ECB "whatever it takes" (Draghi) (2012-07-26)
- Germany: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Germany: ECB introduces negative interest rates (2014-06-05)
- Germany: COVID-19 declared a pandemic (2020-03-11)
- Germany: Russia invades Ukraine (2022-02-24)
- Japan: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Japan: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Japan: COVID-19 declared a pandemic (2020-03-11)
- Japan: Russia invades Ukraine (2022-02-24)
- Japan: Bank of Japan ends negative rates and yield-curve control (2024-03-19)
- Austria: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Austria: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Austria: ECB "whatever it takes" (Draghi) (2012-07-26)
- Austria: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Austria: ECB starts quantitative easing (2015-03-09)
- Austria: COVID-19 declared a pandemic (2020-03-11)
- Austria: Russia invades Ukraine (2022-02-24)
- Belgium: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Belgium: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Belgium: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Belgium: ECB introduces negative interest rates (2014-06-05)
- Czech Republic: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Czech Republic: COVID-19 declared a pandemic (2020-03-11)
- Czech Republic: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Denmark: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Denmark: COVID-19 declared a pandemic (2020-03-11)
- Denmark: Russia invades Ukraine (2022-02-24)
- Finland: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Finland: Russia invades Ukraine (2022-02-24)
- France: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- France: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- France: ECB "whatever it takes" (Draghi) (2012-07-26)
- France: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- France: ECB starts quantitative easing (2015-03-09)
- France: COVID-19 declared a pandemic (2020-03-11)
- France: Russia invades Ukraine (2022-02-24)
- Hungary: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Hungary: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Hungary: COVID-19 declared a pandemic (2020-03-11)
- Hungary: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Ireland: ECB starts quantitative easing (2015-03-09)
- Ireland: Russia invades Ukraine (2022-02-24)
- Italy: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Italy: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Italy: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Italy: ECB "whatever it takes" (Draghi) (2012-07-26)
- Italy: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Italy: ECB starts quantitative easing (2015-03-09)
- Italy: COVID-19 declared a pandemic (2020-03-11)
- Italy: Russia invades Ukraine (2022-02-24)
- Netherlands: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Netherlands: ECB "whatever it takes" (Draghi) (2012-07-26)
- Netherlands: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Netherlands: ECB introduces negative interest rates (2014-06-05)
- Netherlands: COVID-19 declared a pandemic (2020-03-11)
- Netherlands: Russia invades Ukraine (2022-02-24)
- Poland: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Poland: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Poland: COVID-19 declared a pandemic (2020-03-11)
- Slovakia: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Slovakia: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Slovakia: ECB starts quantitative easing (2015-03-09)
- Slovakia: COVID-19 declared a pandemic (2020-03-11)
- Slovakia: Russia invades Ukraine (2022-02-24)
- South Korea: COVID-19 declared a pandemic (2020-03-11)
- South Korea: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Switzerland: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Switzerland: COVID-19 declared a pandemic (2020-03-11)
- Switzerland: Russia invades Ukraine (2022-02-24)

## Data analysed

Gaps of up to 6 months without an auction are filled with a straight line; a longer gap splits the series, and each stretch of at least 18 months is analysed on its own. A break can't be placed within 6 months of a stretch's start or end. Events are checked when they fall inside a stretch.

| Country | Months analysed |
|---|---|
| United States | 2007-02 to 2026-09 |
| Canada | 2007-01 to 2026-10 |
| United Kingdom | 2006-12 to 2026-07 |
| Germany | 2007-01 to 2026-10 |
| Japan | 2006-12 to 2026-09 |
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
| Spain | 2025-01 to 2026-09 |
| Switzerland | 2010-11 to 2026-09 |
| European Union | 2022-04 to 2026-10 |

## Files

- [breaks.csv](breaks.csv): every break, TP or FP, with its matched event
- [event_outcomes.csv](event_outcomes.csv): every country-event pair checked, TP or FN
- [event_recall.csv](event_recall.csv): the recall-by-event table above
- [country_scores.csv](country_scores.csv): the by-country table above
- [charts/](charts/): one chart per country (green = TP, red dashed = FP, orange = FN, grey = event matched)
