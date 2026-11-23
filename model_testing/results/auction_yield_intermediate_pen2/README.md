# Breaks: auction yield, Intermediate bucket, penalty 2

Breaks are scored against [events.csv](../../events.csv), one break per event, within ±6 months; shortest segment 6 months. 59 breaks in 22 countries; 140 country-event pairs checked.

| | Model | Random baseline |
|---|:-:|:-:|
| Precision | **66%** (39 of 59 breaks) | 32% |
| Recall | **28%** (39 of 140 events) | 13% |
| F1 | **0.39** | 0.19 |

Confusion counts: **39 TP**, **20 FP**, **101 FN** (no true negatives: see below). p-value vs random: ≤ 0.001.

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

Accuracy isn't reported: it needs true negatives (months with neither a break nor an event), and almost every month is one. A model that never finds a break would score 97% accuracy on these 4,439 months.

## Recall by event

| Date | Event | Countries checked | TP | FN | Recall |
|---|---|:-:|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 14 | 5 | 9 | 36% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 10 | 0 | 10 | 0% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 9 | 3 | 6 | 33% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 9 | 3 | 6 | 33% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 18 | 3 | 15 | 17% |
| 2014-06-05 | ECB introduces negative interest rates | 8 | 3 | 5 | 38% |
| 2015-03-09 | ECB starts quantitative easing | 8 | 2 | 6 | 25% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 0 | 1 | 0% |
| 2016-06-23 | Brexit referendum | 1 | 0 | 1 | 0% |
| 2020-03-11 | COVID-19 declared a pandemic | 20 | 0 | 20 | 0% |
| 2022-02-24 | Russia invades Ukraine | 20 | 4 | 16 | 20% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 20 | 14 | 6 | 70% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 1 | 0 | 100% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 1 | 0 | 100% |

## Scores by country

| Country | TP | FP | FN | Precision | Recall | F1 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| United States | 2 | 0 | 3 | 100% | 40% | 0.57 |
| Canada | 2 | 1 | 3 | 67% | 40% | 0.50 |
| United Kingdom | 2 | 1 | 5 | 67% | 29% | 0.40 |
| Germany | 2 | 1 | 8 | 67% | 20% | 0.31 |
| Japan | 1 | 3 | 6 | 25% | 14% | 0.18 |
| Austria | 2 | 1 | 8 | 67% | 20% | 0.31 |
| Belgium | 2 | 1 | 5 | 67% | 29% | 0.40 |
| Czech Republic | 1 | 2 | 4 | 33% | 20% | 0.25 |
| Denmark | 1 | 1 | 3 | 50% | 25% | 0.33 |
| Finland | 2 | 2 | 4 | 50% | 33% | 0.40 |
| France | 3 | 0 | 7 | 100% | 30% | 0.46 |
| Hungary | 1 | 2 | 4 | 33% | 20% | 0.25 |
| Ireland | 0 | 0 | 2 | 0% | 0% | 0.00 |
| Italy | 2 | 0 | 8 | 100% | 20% | 0.33 |
| Lithuania | 3 | 0 | 6 | 100% | 33% | 0.50 |
| Netherlands | 3 | 0 | 7 | 100% | 30% | 0.46 |
| Norway | 1 | 2 | 4 | 33% | 20% | 0.25 |
| Poland | 2 | 0 | 3 | 100% | 40% | 0.57 |
| Slovakia | 3 | 0 | 6 | 100% | 33% | 0.50 |
| South Korea | 1 | 0 | 2 | 100% | 33% | 0.50 |
| Spain | 0 | 1 | 0 | 0% | 0% | 0.00 |
| Switzerland | 2 | 2 | 2 | 50% | 50% | 0.50 |
| European Union | 1 | 0 | 1 | 100% | 50% | 0.67 |

## False positives (breaks with no event left to match)

Leads worth looking into: something changed, but it isn't in events.csv (or its event was already matched to another break).

- Canada: 2011-08-01
- United Kingdom: 2015-12-01
- Germany: 2009-10-01
- Japan: 2009-09-01
- Japan: 2014-12-01
- Japan: 2025-12-01
- Austria: 2009-10-01
- Belgium: 2026-03-01
- Czech Republic: 2010-04-01
- Czech Republic: 2012-11-01
- Denmark: 2011-08-01
- Finland: 2017-11-01
- Finland: 2018-11-01
- Hungary: 2012-10-01
- Hungary: 2014-06-01
- Norway: 2010-03-01
- Norway: 2014-11-01
- Spain: 2026-03-01
- Switzerland: 2016-10-01
- Switzerland: 2024-08-01

## False negatives (events with no break)

- United States: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United States: COVID-19 declared a pandemic (2020-03-11)
- United States: Russia invades Ukraine (2022-02-24)
- Canada: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Canada: COVID-19 declared a pandemic (2020-03-11)
- Canada: Russia invades Ukraine (2022-02-24)
- United Kingdom: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United Kingdom: Brexit referendum (2016-06-23)
- United Kingdom: COVID-19 declared a pandemic (2020-03-11)
- United Kingdom: Russia invades Ukraine (2022-02-24)
- United Kingdom: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Germany: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Germany: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Germany: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Germany: ECB "whatever it takes" (Draghi) (2012-07-26)
- Germany: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Germany: ECB introduces negative interest rates (2014-06-05)
- Germany: COVID-19 declared a pandemic (2020-03-11)
- Germany: Russia invades Ukraine (2022-02-24)
- Japan: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Japan: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Japan: Bank of Japan introduces negative interest rates (2016-01-29)
- Japan: COVID-19 declared a pandemic (2020-03-11)
- Japan: Russia invades Ukraine (2022-02-24)
- Japan: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Austria: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Austria: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Austria: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Austria: ECB "whatever it takes" (Draghi) (2012-07-26)
- Austria: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Austria: ECB starts quantitative easing (2015-03-09)
- Austria: COVID-19 declared a pandemic (2020-03-11)
- Austria: Russia invades Ukraine (2022-02-24)
- Belgium: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Belgium: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Belgium: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Belgium: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Belgium: ECB introduces negative interest rates (2014-06-05)
- Czech Republic: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Czech Republic: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Czech Republic: COVID-19 declared a pandemic (2020-03-11)
- Czech Republic: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Denmark: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Denmark: COVID-19 declared a pandemic (2020-03-11)
- Denmark: Russia invades Ukraine (2022-02-24)
- Finland: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Finland: ECB "whatever it takes" (Draghi) (2012-07-26)
- Finland: COVID-19 declared a pandemic (2020-03-11)
- Finland: Russia invades Ukraine (2022-02-24)
- France: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- France: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- France: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- France: ECB introduces negative interest rates (2014-06-05)
- France: ECB starts quantitative easing (2015-03-09)
- France: COVID-19 declared a pandemic (2020-03-11)
- France: Russia invades Ukraine (2022-02-24)
- Hungary: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Hungary: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Hungary: COVID-19 declared a pandemic (2020-03-11)
- Hungary: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Ireland: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Ireland: COVID-19 declared a pandemic (2020-03-11)
- Italy: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Italy: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Italy: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Italy: ECB "whatever it takes" (Draghi) (2012-07-26)
- Italy: ECB introduces negative interest rates (2014-06-05)
- Italy: ECB starts quantitative easing (2015-03-09)
- Italy: COVID-19 declared a pandemic (2020-03-11)
- Italy: Russia invades Ukraine (2022-02-24)
- Lithuania: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Lithuania: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Lithuania: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Lithuania: ECB starts quantitative easing (2015-03-09)
- Lithuania: COVID-19 declared a pandemic (2020-03-11)
- Lithuania: Russia invades Ukraine (2022-02-24)
- Netherlands: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Netherlands: ECB "whatever it takes" (Draghi) (2012-07-26)
- Netherlands: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Netherlands: ECB introduces negative interest rates (2014-06-05)
- Netherlands: ECB starts quantitative easing (2015-03-09)
- Netherlands: COVID-19 declared a pandemic (2020-03-11)
- Netherlands: Russia invades Ukraine (2022-02-24)
- Norway: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Norway: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Norway: COVID-19 declared a pandemic (2020-03-11)
- Norway: Russia invades Ukraine (2022-02-24)
- Poland: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Poland: COVID-19 declared a pandemic (2020-03-11)
- Poland: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Slovakia: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Slovakia: ECB "whatever it takes" (Draghi) (2012-07-26)
- Slovakia: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Slovakia: ECB starts quantitative easing (2015-03-09)
- Slovakia: COVID-19 declared a pandemic (2020-03-11)
- Slovakia: Russia invades Ukraine (2022-02-24)
- South Korea: COVID-19 declared a pandemic (2020-03-11)
- South Korea: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Switzerland: COVID-19 declared a pandemic (2020-03-11)
- Switzerland: Russia invades Ukraine (2022-02-24)
- European Union: Russia invades Ukraine (2022-02-24)

## Data analysed

Gaps of up to 6 months without an auction are filled with a straight line; a longer gap splits the series, and each stretch of at least 18 months is analysed on its own. A break can't be placed within 6 months of a stretch's start or end. Events are checked when they fall inside a stretch.

| Country | Months analysed |
|---|---|
| United States | 2006-11 to 2026-09 |
| Canada | 2007-05 to 2026-10 |
| United Kingdom | 2006-11 to 2026-10 |
| Germany | 2006-11 to 2026-10 |
| Japan | 2006-11 to 2026-09 |
| Austria | 2007-02 to 2026-10 |
| Belgium | 2006-11 to 2019-11, 2024-06 to 2026-10 |
| Czech Republic | 2006-11 to 2026-10 |
| Denmark | 2009-04 to 2014-09, 2015-10 to 2026-10 |
| Finland | 2010-04 to 2012-10, 2015-11 to 2019-04, 2020-03 to 2026-10 |
| France | 2007-01 to 2026-10 |
| Hungary | 2006-11 to 2026-10 |
| Ireland | 2009-03 to 2010-09, 2016-05 to 2018-11, 2019-07 to 2021-11 |
| Italy | 2006-12 to 2026-10 |
| Lithuania | 2009-10 to 2026-10 |
| Netherlands | 2007-03 to 2019-01, 2019-09 to 2026-10 |
| Norway | 2006-11 to 2026-10 |
| Poland | 2006-12 to 2026-10 |
| Slovakia | 2009-11 to 2017-11, 2018-10 to 2026-10 |
| South Korea | 2018-01 to 2026-10 |
| Spain | 2025-01 to 2026-09 |
| Switzerland | 2012-03 to 2014-10, 2016-04 to 2018-01, 2019-09 to 2026-10 |
| European Union | 2021-09 to 2026-10 |

## Files

- [breaks.csv](breaks.csv): every break, TP or FP, with its matched event
- [event_outcomes.csv](event_outcomes.csv): every country-event pair checked, TP or FN
- [event_recall.csv](event_recall.csv): the recall-by-event table above
- [country_scores.csv](country_scores.csv): the by-country table above
- [charts/](charts/): one chart per country (green = TP, red dashed = FP, orange = FN, grey = event matched)
