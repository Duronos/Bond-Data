# Breaks: bid to cover, Intermediate bucket, penalty 2

Breaks are scored against [events.csv](../../events.csv), one break per event, within ±6 months; shortest segment 6 months. 11 breaks in 7 countries; 116 country-event pairs checked.

| | Model | Random baseline |
|---|:-:|:-:|
| Precision | **27%** (3 of 11 breaks) | 28% |
| Recall | **3%** (3 of 116 events) | 3% |
| F1 | **0.05** | 0.05 |

Confusion counts: **3 TP**, **8 FP**, **113 FN** (no true negatives: see below). p-value vs random: 0.672.

| Term | Meaning here |
|---|---|
| True positive (TP) | a break matched to a known event within the window (±6 months for events.csv, ±3 for events_v2.csv) |
| False positive (FP) | a break with no event left to match (a lead, or noise) |
| False negative (FN) | a known event with no break matched to it (missed) |
| Precision | TP / (TP + FP): share of breaks that match an event |
| Recall | TP / (TP + FN): share of events that were detected |
| F1 | 2 × precision × recall / (precision + recall) |
| Random baseline | the same number of breaks per stretch at random dates, scored the same way (1,000 draws, average) |
| p-value | share of random draws with an F1 at least as high as the real one |

Accuracy isn't reported: it needs true negatives (months with neither a break nor an event), and almost every month is one. A model that never finds a break would score 97% accuracy on these 3,973 months.

## Recall by event

| Date | Event | Countries checked | TP | FN | Recall |
|---|---|:-:|:-:|:-:|:-:|
| 2008-09-15 | Global financial crisis (Lehman Brothers collapses) | 12 | 0 | 12 | 0% |
| 2010-05-02 | Euro debt crisis begins (first Greek bailout) | 7 | 0 | 7 | 0% |
| 2011-11-09 | Euro crisis peak (Italian 10-year above 7%) | 6 | 0 | 6 | 0% |
| 2012-07-26 | ECB "whatever it takes" (Draghi) | 6 | 1 | 5 | 17% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 16 | 0 | 16 | 0% |
| 2014-06-05 | ECB introduces negative interest rates | 5 | 0 | 5 | 0% |
| 2015-03-09 | ECB starts quantitative easing | 6 | 0 | 6 | 0% |
| 2016-01-29 | Bank of Japan introduces negative interest rates | 1 | 0 | 1 | 0% |
| 2016-06-23 | Brexit referendum | 1 | 1 | 0 | 100% |
| 2020-03-11 | COVID-19 declared a pandemic | 18 | 1 | 17 | 6% |
| 2022-02-24 | Russia invades Ukraine | 18 | 0 | 18 | 0% |
| 2022-03-16 | Fed starts raising rates (global hiking cycle) | 18 | 0 | 18 | 0% |
| 2022-09-23 | UK mini-budget (gilt crisis) | 1 | 0 | 1 | 0% |
| 2024-03-19 | Bank of Japan ends negative rates and yield-curve control | 1 | 0 | 1 | 0% |

## Scores by country

| Country | TP | FP | FN | Precision | Recall | F1 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| United States | 0 | 2 | 5 | 0% | 0% | 0.00 |
| Canada | 0 | 0 | 5 | 0% | 0% | 0.00 |
| United Kingdom | 1 | 2 | 6 | 33% | 14% | 0.20 |
| Germany | 0 | 0 | 10 | 0% | 0% | 0.00 |
| Japan | 1 | 1 | 6 | 50% | 14% | 0.22 |
| Belgium | 1 | 0 | 6 | 100% | 14% | 0.25 |
| Czech Republic | 0 | 0 | 5 | 0% | 0% | 0.00 |
| Denmark | 0 | 0 | 4 | 0% | 0% | 0.00 |
| Finland | 0 | 1 | 6 | 0% | 0% | 0.00 |
| France | 0 | 0 | 10 | 0% | 0% | 0.00 |
| Hungary | 0 | 0 | 5 | 0% | 0% | 0.00 |
| Ireland | 0 | 0 | 2 | 0% | 0% | 0.00 |
| Italy | 0 | 1 | 10 | 0% | 0% | 0.00 |
| Lithuania | 0 | 0 | 5 | 0% | 0% | 0.00 |
| Norway | 0 | 0 | 5 | 0% | 0% | 0.00 |
| Poland | 0 | 1 | 5 | 0% | 0% | 0.00 |
| Slovakia | 0 | 0 | 9 | 0% | 0% | 0.00 |
| South Korea | 0 | 0 | 3 | 0% | 0% | 0.00 |
| Spain | 0 | 0 | 0 | 0% | 0% | 0.00 |
| Switzerland | 0 | 0 | 4 | 0% | 0% | 0.00 |
| European Union | 0 | 0 | 2 | 0% | 0% | 0.00 |

## False positives (breaks with no event left to match)

Leads worth looking into: something changed, but it isn't in events.csv (or its event was already matched to another break).

- United States: 2009-06-01
- United States: 2015-09-01
- United Kingdom: 2011-03-01
- United Kingdom: 2024-01-01
- Japan: 2012-01-01
- Finland: 2018-11-01
- Italy: 2024-10-01
- Poland: 2021-07-01

## False negatives (events with no break)

- United States: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- United States: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United States: COVID-19 declared a pandemic (2020-03-11)
- United States: Russia invades Ukraine (2022-02-24)
- United States: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Canada: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Canada: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Canada: COVID-19 declared a pandemic (2020-03-11)
- Canada: Russia invades Ukraine (2022-02-24)
- Canada: Fed starts raising rates (global hiking cycle) (2022-03-16)
- United Kingdom: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- United Kingdom: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United Kingdom: COVID-19 declared a pandemic (2020-03-11)
- United Kingdom: Russia invades Ukraine (2022-02-24)
- United Kingdom: Fed starts raising rates (global hiking cycle) (2022-03-16)
- United Kingdom: UK mini-budget (gilt crisis) (2022-09-23)
- Germany: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Germany: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Germany: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Germany: ECB "whatever it takes" (Draghi) (2012-07-26)
- Germany: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Germany: ECB introduces negative interest rates (2014-06-05)
- Germany: ECB starts quantitative easing (2015-03-09)
- Germany: COVID-19 declared a pandemic (2020-03-11)
- Germany: Russia invades Ukraine (2022-02-24)
- Germany: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Japan: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Japan: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Japan: Bank of Japan introduces negative interest rates (2016-01-29)
- Japan: Russia invades Ukraine (2022-02-24)
- Japan: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Japan: Bank of Japan ends negative rates and yield-curve control (2024-03-19)
- Belgium: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Belgium: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Belgium: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Belgium: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Belgium: ECB introduces negative interest rates (2014-06-05)
- Belgium: ECB starts quantitative easing (2015-03-09)
- Czech Republic: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Czech Republic: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Czech Republic: COVID-19 declared a pandemic (2020-03-11)
- Czech Republic: Russia invades Ukraine (2022-02-24)
- Czech Republic: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Denmark: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Denmark: COVID-19 declared a pandemic (2020-03-11)
- Denmark: Russia invades Ukraine (2022-02-24)
- Denmark: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Finland: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Finland: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Finland: ECB "whatever it takes" (Draghi) (2012-07-26)
- Finland: COVID-19 declared a pandemic (2020-03-11)
- Finland: Russia invades Ukraine (2022-02-24)
- Finland: Fed starts raising rates (global hiking cycle) (2022-03-16)
- France: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- France: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- France: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- France: ECB "whatever it takes" (Draghi) (2012-07-26)
- France: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- France: ECB introduces negative interest rates (2014-06-05)
- France: ECB starts quantitative easing (2015-03-09)
- France: COVID-19 declared a pandemic (2020-03-11)
- France: Russia invades Ukraine (2022-02-24)
- France: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Hungary: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Hungary: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Hungary: COVID-19 declared a pandemic (2020-03-11)
- Hungary: Russia invades Ukraine (2022-02-24)
- Hungary: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Ireland: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Ireland: COVID-19 declared a pandemic (2020-03-11)
- Italy: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Italy: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Italy: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Italy: ECB "whatever it takes" (Draghi) (2012-07-26)
- Italy: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Italy: ECB introduces negative interest rates (2014-06-05)
- Italy: ECB starts quantitative easing (2015-03-09)
- Italy: COVID-19 declared a pandemic (2020-03-11)
- Italy: Russia invades Ukraine (2022-02-24)
- Italy: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Lithuania: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Lithuania: ECB starts quantitative easing (2015-03-09)
- Lithuania: COVID-19 declared a pandemic (2020-03-11)
- Lithuania: Russia invades Ukraine (2022-02-24)
- Lithuania: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Norway: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Norway: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Norway: COVID-19 declared a pandemic (2020-03-11)
- Norway: Russia invades Ukraine (2022-02-24)
- Norway: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Poland: Global financial crisis (Lehman Brothers collapses) (2008-09-15)
- Poland: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Poland: COVID-19 declared a pandemic (2020-03-11)
- Poland: Russia invades Ukraine (2022-02-24)
- Poland: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Slovakia: Euro debt crisis begins (first Greek bailout) (2010-05-02)
- Slovakia: Euro crisis peak (Italian 10-year above 7%) (2011-11-09)
- Slovakia: ECB "whatever it takes" (Draghi) (2012-07-26)
- Slovakia: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Slovakia: ECB introduces negative interest rates (2014-06-05)
- Slovakia: ECB starts quantitative easing (2015-03-09)
- Slovakia: COVID-19 declared a pandemic (2020-03-11)
- Slovakia: Russia invades Ukraine (2022-02-24)
- Slovakia: Fed starts raising rates (global hiking cycle) (2022-03-16)
- South Korea: COVID-19 declared a pandemic (2020-03-11)
- South Korea: Russia invades Ukraine (2022-02-24)
- South Korea: Fed starts raising rates (global hiking cycle) (2022-03-16)
- Switzerland: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Switzerland: COVID-19 declared a pandemic (2020-03-11)
- Switzerland: Russia invades Ukraine (2022-02-24)
- Switzerland: Fed starts raising rates (global hiking cycle) (2022-03-16)
- European Union: Russia invades Ukraine (2022-02-24)
- European Union: Fed starts raising rates (global hiking cycle) (2022-03-16)

## Data analysed

Gaps of up to 6 months without an auction are filled with a straight line; a longer gap splits the series, and each stretch of at least 18 months is analysed on its own. A break can't be placed within 6 months of a stretch's start or end. Events are checked when they fall inside a stretch.

| Country | Months analysed |
|---|---|
| United States | 2006-11 to 2026-09 |
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
| Spain | 2025-01 to 2026-09 |
| Switzerland | 2012-03 to 2014-10, 2016-04 to 2018-01, 2019-09 to 2026-10 |
| European Union | 2021-09 to 2026-10 |

## Files

- [breaks.csv](breaks.csv): every break, TP or FP, with its matched event
- [event_outcomes.csv](event_outcomes.csv): every country-event pair checked, TP or FN
- [event_recall.csv](event_recall.csv): the recall-by-event table above
- [country_scores.csv](country_scores.csv): the by-country table above
- [charts/](charts/): one chart per country (green = TP, red dashed = FP, orange = FN, grey = event matched)
