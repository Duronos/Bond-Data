# Breaks: auction yield, Intermediate bucket, penalty 2

Breaks are scored against [events_v2.csv](../../../events_v2.csv), one break per event, within ±3 months; shortest segment 6 months. 59 breaks in 22 countries; 355 country-event pairs checked.

| | Model | Random baseline |
|---|:-:|:-:|
| Precision | **66%** (39 of 59 breaks) | 45% |
| Recall | **11%** (39 of 355 events) | 8% |
| F1 | **0.19** | 0.13 |

Confusion counts: **39 TP**, **20 FP**, **316 FN** (no true negatives: see below). p-value vs random: ≤ 0.001.

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

Accuracy isn't reported: it needs true negatives (months with neither a break nor an event), and almost every month is one. A model that never finds a break would score 92% accuracy on these 4,439 months.

## Recall by event

| Date | Event | Countries checked | TP | FN | Recall |
|---|---|:-:|:-:|:-:|:-:|
| 2007-04-25 | NBP starts raising rates | 1 | 0 | 1 | 0% |
| 2007-06-25 | MNB starts cutting rates + BNP Paribas freezes funds; global credit crunch begins (9 Aug 2007) | 1 | 0 | 1 | 0% |
| 2007-08-09 | BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) | 13 | 0 | 13 | 0% |
| 2007-12-04 | BoC starts cutting rates | 1 | 0 | 1 | 0% |
| 2007-12-06 | BoE starts cutting rates | 1 | 0 | 1 | 0% |
| 2008-02-25 | Hungary abolishes forint band (free float) + MNB starts raising rates (31 Mar 2008) | 1 | 0 | 1 | 0% |
| 2008-03-16 | Bear Stearns rescue; Fed lends to dealers | 1 | 0 | 1 | 0% |
| 2008-08-07 | CNB starts cutting rates + Lehman Brothers collapses (global financial crisis) (15 Sep 2008) | 1 | 0 | 1 | 0% |
| 2008-09-15 | Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) | 13 | 5 | 8 | 38% |
| 2009-03-05 | BoE cuts to 0.5% and starts QE | 1 | 0 | 1 | 0% |
| 2009-03-18 | Fed to buy Treasuries (QE1 expanded) | 1 | 0 | 1 | 0% |
| 2009-10-28 | Norges Bank starts raising rates | 1 | 0 | 1 | 0% |
| 2010-04-23 | Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) | 9 | 0 | 9 | 0% |
| 2010-06-01 | BoC starts raising rates | 1 | 0 | 1 | 0% |
| 2010-10-05 | BoJ comprehensive easing (asset purchases, zero rates) | 1 | 0 | 1 | 0% |
| 2010-11-03 | Fed announces QE2 | 1 | 0 | 1 | 0% |
| 2010-11-29 | MNB starts raising rates | 1 | 0 | 1 | 0% |
| 2011-01-19 | NBP starts raising rates | 1 | 0 | 1 | 0% |
| 2011-04-07 | ECB starts raising rates | 8 | 0 | 8 | 0% |
| 2011-07-08 | Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) | 8 | 0 | 8 | 0% |
| 2011-08-05 | S&P downgrades US after debt-ceiling crisis + Fed Operation Twist (21 Sep 2011) | 1 | 0 | 1 | 0% |
| 2011-10-06 | BoE restarts QE | 1 | 0 | 1 | 0% |
| 2011-10-31 | Greek PM calls bailout referendum; euro crisis peaks + ECB starts cutting rates (Draghi) (3 Nov 2011) + Italian 10-year yield above 7%; Berlusconi resigns (12 Nov) (9 Nov 2011) + ECB announces 3-year LTROs (8 Dec 2011) | 8 | 3 | 5 | 38% |
| 2011-11-17 | Hungary seeks IMF/EU aid; Moody's cuts to junk (24 Nov); MNB hikes (29 Nov) | 1 | 0 | 1 | 0% |
| 2011-12-14 | Norges Bank starts cutting rates | 1 | 0 | 1 | 0% |
| 2012-04-23 | Dutch government collapses over budget cuts | 1 | 0 | 1 | 0% |
| 2012-06-27 | CNB resumes cutting rates (first cut since May 2010) | 1 | 0 | 1 | 0% |
| 2012-07-05 | Danmarks Nationalbank introduces negative rates | 1 | 0 | 1 | 0% |
| 2012-07-26 | ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) | 8 | 1 | 7 | 12% |
| 2012-08-28 | MNB starts cutting rates | 1 | 1 | 0 | 100% |
| 2012-09-13 | Fed announces QE3 | 1 | 0 | 1 | 0% |
| 2012-11-07 | NBP starts cutting rates | 1 | 1 | 0 | 100% |
| 2013-02-25 | Italian election gives hung parliament + US taper tantrum (Fed signals slower bond buying) (22 May 2013) | 1 | 0 | 1 | 0% |
| 2013-04-04 | BoJ launches QQE + US taper tantrum (Fed signals slower bond buying) (22 May 2013) | 1 | 0 | 1 | 0% |
| 2013-05-02 | ECB resumes cutting rates (first cut since Jul 2012) + US taper tantrum (22 May 2013) | 6 | 0 | 6 | 0% |
| 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | 10 | 1 | 9 | 10% |
| 2013-11-07 | CNB sets koruna floor (27 per euro) | 1 | 0 | 1 | 0% |
| 2013-12-18 | Fed starts tapering QE3 | 1 | 0 | 1 | 0% |
| 2014-06-04 | EU backs Lithuania joining the euro in 2015 (Council decision 23 Jul) | 1 | 1 | 0 | 100% |
| 2014-06-05 | ECB introduces negative interest rates | 7 | 1 | 6 | 14% |
| 2014-10-08 | NBP resumes cutting rates | 1 | 0 | 1 | 0% |
| 2014-11-27 | OPEC declines to cut output; oil price collapse + Norges Bank resumes cutting rates (11 Dec 2014) + BoC surprise rate cut (21 Jan 2015) | 2 | 1 | 1 | 50% |
| 2015-01-22 | ECB announces QE (public sector purchases) + Heta (Hypo Alpe Adria bad bank) debt moratorium (1 Mar 2015) | 8 | 2 | 6 | 25% |
| 2015-12-16 | Fed first rate hike since 2006 | 1 | 0 | 1 | 0% |
| 2016-01-29 | BoJ introduces negative interest rates | 1 | 0 | 1 | 0% |
| 2016-05-20 | Fitch returns Hungary to investment grade | 1 | 0 | 1 | 0% |
| 2016-06-23 | Brexit referendum + BoE cuts rate and restarts QE (4 Aug 2016) | 1 | 0 | 1 | 0% |
| 2016-09-21 | BoJ introduces yield-curve control + Trump elected US president; global bond sell-off (8 Nov 2016) | 1 | 0 | 1 | 0% |
| 2016-11-08 | Trump elected US president; global bond sell-off | 19 | 1 | 18 | 5% |
| 2017-04-06 | CNB ends koruna floor | 1 | 0 | 1 | 0% |
| 2017-04-23 | French election first round (Macron v Le Pen); OAT spread narrows sharply | 1 | 0 | 1 | 0% |
| 2017-07-12 | BoC starts raising rates | 1 | 0 | 1 | 0% |
| 2017-08-03 | CNB starts raising rates | 1 | 0 | 1 | 0% |
| 2017-11-02 | BoE first hike in a decade | 1 | 0 | 1 | 0% |
| 2018-05-27 | Italian government crisis (Savona veto); worst bond day since 1992 + ECB announces end of net asset purchases (14 Jun 2018) | 1 | 0 | 1 | 0% |
| 2018-06-14 | ECB announces end of net asset purchases | 8 | 0 | 8 | 0% |
| 2018-08-02 | BoE raises rates after a 9-month pause | 1 | 0 | 1 | 0% |
| 2018-09-20 | Norges Bank starts raising rates | 1 | 0 | 1 | 0% |
| 2018-09-27 | Italy sets 2.4% deficit target, clash with EU | 1 | 0 | 1 | 0% |
| 2018-11-30 | BoK resumes raising rates (first hike in 12 months) | 1 | 0 | 1 | 0% |
| 2019-07-18 | BoK starts cutting rates | 1 | 0 | 1 | 0% |
| 2019-07-31 | Fed starts cutting rates; ends QT | 1 | 0 | 1 | 0% |
| 2019-08-08 | Salvini pulls support for Italian government + ECB cuts deposit rate to -0.5% and restarts QE (12 Sep 2019) | 1 | 0 | 1 | 0% |
| 2019-09-12 | ECB cuts deposit rate to -0.5% and restarts QE | 8 | 0 | 8 | 0% |
| 2020-02-24 | COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) | 19 | 0 | 19 | 0% |
| 2020-06-23 | MNB cuts base rate (first cut since 2016) | 1 | 0 | 1 | 0% |
| 2021-02-02 | Conte government falls; Draghi asked to form government | 1 | 0 | 1 | 0% |
| 2021-06-22 | MNB starts raising rates | 1 | 0 | 1 | 0% |
| 2021-06-23 | CNB starts raising rates | 1 | 0 | 1 | 0% |
| 2021-08-26 | BoK starts raising rates | 1 | 0 | 1 | 0% |
| 2021-09-23 | Norges Bank starts raising rates | 1 | 0 | 1 | 0% |
| 2021-10-06 | NBP starts raising rates | 1 | 0 | 1 | 0% |
| 2021-10-27 | BoC ends QE | 1 | 0 | 1 | 0% |
| 2021-11-03 | Fed starts tapering QE | 1 | 0 | 1 | 0% |
| 2021-12-16 | BoE starts raising rates + Russia invades Ukraine (24 Feb 2022) | 1 | 0 | 1 | 0% |
| 2022-02-24 | Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) | 19 | 6 | 13 | 32% |
| 2022-06-09 | ECB announces end of QE and first hike + Draghi government collapses (resigns 21 Jul) (14 Jul 2022) + ECB first hike since 2011; TPI anti-fragmentation tool (21 Jul 2022) | 9 | 9 | 0 | 100% |
| 2022-06-16 | SNB first hike since 2007 (exits negative rates Sep) | 1 | 0 | 1 | 0% |
| 2022-07-21 | Nationalbank starts raising rates (exits negative rates 8 Sep) | 1 | 1 | 0 | 100% |
| 2022-09-23 | UK mini-budget gilt crisis (BoE gilt buying 28 Sep) | 1 | 1 | 0 | 100% |
| 2022-10-14 | Forint slump; MNB emergency 18% deposit tender | 1 | 0 | 1 | 0% |
| 2022-12-20 | BoJ widens YCC band (surprise) + Silicon Valley Bank fails; banking stress (10 Mar 2023) | 1 | 0 | 1 | 0% |
| 2023-03-10 | Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) | 19 | 0 | 19 | 0% |
| 2023-09-06 | NBP starts cutting rates (surprise 75bp) + Polish election: pro-EU opposition wins (15 Oct 2023) | 1 | 0 | 1 | 0% |
| 2023-12-21 | CNB starts cutting rates | 1 | 0 | 1 | 0% |
| 2024-03-19 | BoJ ends negative rates and yield-curve control | 1 | 1 | 0 | 100% |
| 2024-03-21 | SNB starts cutting rates | 1 | 0 | 1 | 0% |
| 2024-06-05 | BoC starts cutting rates | 1 | 0 | 1 | 0% |
| 2024-06-06 | ECB starts cutting rates + Macron calls snap election (9 Jun 2024) | 10 | 0 | 10 | 0% |
| 2024-06-06 | Nationalbank starts cutting rates | 1 | 0 | 1 | 0% |
| 2024-08-01 | BoE starts cutting rates | 1 | 0 | 1 | 0% |
| 2024-09-18 | Fed starts cutting rates + Trump re-elected; Treasury yields jump (5 Nov 2024) | 1 | 0 | 1 | 0% |
| 2024-10-11 | BoK starts cutting rates + Martial law declared in South Korea (3 Dec 2024) | 1 | 0 | 1 | 0% |
| 2024-12-02 | Barnier forces budget; government toppled (4 Dec) | 1 | 0 | 1 | 0% |
| 2025-03-04 | Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) | 11 | 0 | 11 | 0% |
| 2025-04-02 | US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) | 11 | 0 | 11 | 0% |
| 2025-08-25 | Bayrou calls confidence vote; government falls (8 Sep); Lecornu resigns (6 Oct) | 1 | 0 | 1 | 0% |
| 2025-09-07 | Ishiba resigns + Takaichi wins LDP leadership; JGB and yen sell-off (4 Oct 2025) | 1 | 0 | 1 | 0% |
| 2025-09-17 | Fed resumes cutting after 9-month pause + Fed announces end of QT (1 Dec) (29 Oct 2025) | 1 | 0 | 1 | 0% |
| 2026-01-13 | Takaichi snap-election plan; super-long JGB rout (election 8 Feb) + US and Israel attack Iran; Strait of Hormuz closed, oil surges (28 Feb 2026) | 1 | 1 | 0 | 100% |
| 2026-02-24 | MNB starts cutting rates + US and Israel attack Iran; Strait of Hormuz closed, oil surges (28 Feb 2026) + Orban loses election; forint and bonds rally (12 Apr 2026) | 1 | 0 | 1 | 0% |
| 2026-02-28 | US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) | 20 | 2 | 18 | 10% |
| 2026-06-11 | ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) | 11 | 0 | 11 | 0% |
| 2026-06-11 | Nationalbank starts raising rates + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) | 1 | 0 | 1 | 0% |
| 2026-06-18 | CNB starts raising rates + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) | 1 | 0 | 1 | 0% |
| 2026-07-08 | US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) | 9 | 0 | 9 | 0% |
| 2026-10-01 | French 2027 budget; OAT-Bund spread widest since 2012 | 1 | 0 | 1 | 0% |

## Scores by country

| Country | TP | FP | FN | Precision | Recall | F1 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| United States | 1 | 1 | 20 | 50% | 5% | 0.09 |
| Canada | 2 | 1 | 14 | 67% | 12% | 0.21 |
| United Kingdom | 2 | 1 | 16 | 67% | 11% | 0.19 |
| Germany | 2 | 1 | 19 | 67% | 10% | 0.17 |
| Japan | 2 | 2 | 12 | 50% | 14% | 0.22 |
| Austria | 2 | 1 | 19 | 67% | 10% | 0.17 |
| Belgium | 2 | 1 | 15 | 67% | 12% | 0.20 |
| Czech Republic | 0 | 3 | 16 | 0% | 0% | 0.00 |
| Denmark | 1 | 1 | 10 | 50% | 9% | 0.15 |
| Finland | 2 | 2 | 12 | 50% | 14% | 0.22 |
| France | 3 | 0 | 22 | 100% | 12% | 0.21 |
| Hungary | 2 | 1 | 16 | 67% | 11% | 0.19 |
| Ireland | 0 | 0 | 5 | 0% | 0% | 0.00 |
| Italy | 1 | 1 | 22 | 50% | 4% | 0.08 |
| Lithuania | 2 | 1 | 12 | 67% | 14% | 0.24 |
| Netherlands | 3 | 0 | 19 | 100% | 14% | 0.24 |
| Norway | 2 | 1 | 13 | 67% | 13% | 0.22 |
| Poland | 2 | 0 | 14 | 100% | 12% | 0.22 |
| Slovakia | 2 | 1 | 16 | 67% | 11% | 0.19 |
| South Korea | 1 | 0 | 9 | 100% | 10% | 0.18 |
| Spain | 1 | 0 | 2 | 100% | 33% | 0.50 |
| Switzerland | 3 | 1 | 7 | 75% | 30% | 0.43 |
| European Union | 1 | 0 | 6 | 100% | 14% | 0.25 |

## False positives (breaks with no event left to match)

Leads worth looking into: something changed, but it isn't in events_v2.csv (or its event was already matched to another break).

- United States: 2022-06-01
- Canada: 2011-08-01
- United Kingdom: 2015-12-01
- Germany: 2009-10-01
- Japan: 2009-09-01
- Japan: 2014-12-01
- Austria: 2009-10-01
- Belgium: 2012-04-01
- Czech Republic: 2010-04-01
- Czech Republic: 2012-11-01
- Czech Republic: 2021-11-01
- Denmark: 2011-08-01
- Finland: 2017-11-01
- Finland: 2018-11-01
- Hungary: 2014-06-01
- Italy: 2013-11-01
- Lithuania: 2012-09-01
- Norway: 2010-03-01
- Slovakia: 2014-03-01
- Switzerland: 2024-08-01

## False negatives (events with no break)

- United States: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- United States: Bear Stearns rescue; Fed lends to dealers (2008-03-16)
- United States: Fed to buy Treasuries (QE1 expanded) (2009-03-18)
- United States: Fed announces QE2 (2010-11-03)
- United States: S&P downgrades US after debt-ceiling crisis + Fed Operation Twist (21 Sep 2011) (2011-08-05)
- United States: Fed announces QE3 (2012-09-13)
- United States: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United States: Fed starts tapering QE3 (2013-12-18)
- United States: Fed first rate hike since 2006 (2015-12-16)
- United States: Trump elected US president; global bond sell-off (2016-11-08)
- United States: Fed starts cutting rates; ends QT (2019-07-31)
- United States: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- United States: Fed starts tapering QE (2021-11-03)
- United States: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- United States: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- United States: Fed starts cutting rates + Trump re-elected; Treasury yields jump (5 Nov 2024) (2024-09-18)
- United States: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- United States: Fed resumes cutting after 9-month pause + Fed announces end of QT (1 Dec) (29 Oct 2025) (2025-09-17)
- United States: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- United States: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- Canada: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Canada: BoC starts cutting rates (2007-12-04)
- Canada: BoC starts raising rates (2010-06-01)
- Canada: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Canada: OPEC declines to cut output; oil price collapse + Norges Bank resumes cutting rates (11 Dec 2014) + BoC surprise rate cut (21 Jan 2015) (2014-11-27)
- Canada: Trump elected US president; global bond sell-off (2016-11-08)
- Canada: BoC starts raising rates (2017-07-12)
- Canada: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Canada: BoC ends QE (2021-10-27)
- Canada: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Canada: BoC starts cutting rates (2024-06-05)
- Canada: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Canada: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Canada: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- United Kingdom: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- United Kingdom: BoE starts cutting rates (2007-12-06)
- United Kingdom: BoE cuts to 0.5% and starts QE (2009-03-05)
- United Kingdom: BoE restarts QE (2011-10-06)
- United Kingdom: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- United Kingdom: Brexit referendum + BoE cuts rate and restarts QE (4 Aug 2016) (2016-06-23)
- United Kingdom: Trump elected US president; global bond sell-off (2016-11-08)
- United Kingdom: BoE first hike in a decade (2017-11-02)
- United Kingdom: BoE raises rates after a 9-month pause (2018-08-02)
- United Kingdom: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- United Kingdom: BoE starts raising rates + Russia invades Ukraine (24 Feb 2022) (2021-12-16)
- United Kingdom: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- United Kingdom: BoE starts cutting rates (2024-08-01)
- United Kingdom: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- United Kingdom: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- United Kingdom: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- Germany: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Germany: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Germany: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Germany: ECB starts raising rates (2011-04-07)
- Germany: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- Germany: Greek PM calls bailout referendum; euro crisis peaks + ECB starts cutting rates (Draghi) (3 Nov 2011) + Italian 10-year yield above 7%; Berlusconi resigns (12 Nov) (9 Nov 2011) + ECB announces 3-year LTROs (8 Dec 2011) (2011-10-31)
- Germany: ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) (2012-07-26)
- Germany: ECB resumes cutting rates (first cut since Jul 2012) + US taper tantrum (22 May 2013) (2013-05-02)
- Germany: ECB introduces negative interest rates (2014-06-05)
- Germany: Trump elected US president; global bond sell-off (2016-11-08)
- Germany: ECB announces end of net asset purchases (2018-06-14)
- Germany: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- Germany: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Germany: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Germany: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Germany: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Germany: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Germany: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Germany: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Japan: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Japan: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Japan: BoJ comprehensive easing (asset purchases, zero rates) (2010-10-05)
- Japan: BoJ launches QQE + US taper tantrum (Fed signals slower bond buying) (22 May 2013) (2013-04-04)
- Japan: BoJ introduces negative interest rates (2016-01-29)
- Japan: BoJ introduces yield-curve control + Trump elected US president; global bond sell-off (8 Nov 2016) (2016-09-21)
- Japan: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Japan: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Japan: BoJ widens YCC band (surprise) + Silicon Valley Bank fails; banking stress (10 Mar 2023) (2022-12-20)
- Japan: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Japan: Ishiba resigns + Takaichi wins LDP leadership; JGB and yen sell-off (4 Oct 2025) (2025-09-07)
- Japan: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- Austria: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Austria: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Austria: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Austria: ECB starts raising rates (2011-04-07)
- Austria: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- Austria: Greek PM calls bailout referendum; euro crisis peaks + ECB starts cutting rates (Draghi) (3 Nov 2011) + Italian 10-year yield above 7%; Berlusconi resigns (12 Nov) (9 Nov 2011) + ECB announces 3-year LTROs (8 Dec 2011) (2011-10-31)
- Austria: ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) (2012-07-26)
- Austria: ECB resumes cutting rates (first cut since Jul 2012) + US taper tantrum (22 May 2013) (2013-05-02)
- Austria: ECB announces QE (public sector purchases) + Heta (Hypo Alpe Adria bad bank) debt moratorium (1 Mar 2015) (2015-01-22)
- Austria: Trump elected US president; global bond sell-off (2016-11-08)
- Austria: ECB announces end of net asset purchases (2018-06-14)
- Austria: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- Austria: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Austria: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Austria: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Austria: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Austria: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Austria: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Austria: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Belgium: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Belgium: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Belgium: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Belgium: ECB starts raising rates (2011-04-07)
- Belgium: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- Belgium: Greek PM calls bailout referendum; euro crisis peaks + ECB starts cutting rates (Draghi) (3 Nov 2011) + Italian 10-year yield above 7%; Berlusconi resigns (12 Nov) (9 Nov 2011) + ECB announces 3-year LTROs (8 Dec 2011) (2011-10-31)
- Belgium: ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) (2012-07-26)
- Belgium: ECB resumes cutting rates (first cut since Jul 2012) + US taper tantrum (22 May 2013) (2013-05-02)
- Belgium: ECB introduces negative interest rates (2014-06-05)
- Belgium: Trump elected US president; global bond sell-off (2016-11-08)
- Belgium: ECB announces end of net asset purchases (2018-06-14)
- Belgium: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- Belgium: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Belgium: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Belgium: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Czech Republic: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Czech Republic: CNB starts cutting rates + Lehman Brothers collapses (global financial crisis) (15 Sep 2008) (2008-08-07)
- Czech Republic: CNB resumes cutting rates (first cut since May 2010) (2012-06-27)
- Czech Republic: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Czech Republic: CNB sets koruna floor (27 per euro) (2013-11-07)
- Czech Republic: Trump elected US president; global bond sell-off (2016-11-08)
- Czech Republic: CNB ends koruna floor (2017-04-06)
- Czech Republic: CNB starts raising rates (2017-08-03)
- Czech Republic: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Czech Republic: CNB starts raising rates (2021-06-23)
- Czech Republic: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Czech Republic: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Czech Republic: CNB starts cutting rates (2023-12-21)
- Czech Republic: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Czech Republic: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Czech Republic: CNB starts raising rates + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-18)
- Denmark: Danmarks Nationalbank introduces negative rates (2012-07-05)
- Denmark: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Denmark: Trump elected US president; global bond sell-off (2016-11-08)
- Denmark: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Denmark: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Denmark: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Denmark: Nationalbank starts cutting rates (2024-06-06)
- Denmark: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Denmark: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Denmark: Nationalbank starts raising rates + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Finland: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Finland: ECB starts raising rates (2011-04-07)
- Finland: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- Finland: ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) (2012-07-26)
- Finland: Trump elected US president; global bond sell-off (2016-11-08)
- Finland: ECB announces end of net asset purchases (2018-06-14)
- Finland: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Finland: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Finland: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Finland: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Finland: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Finland: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- France: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- France: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- France: ECB starts raising rates (2011-04-07)
- France: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- France: Greek PM calls bailout referendum; euro crisis peaks + ECB starts cutting rates (Draghi) (3 Nov 2011) + Italian 10-year yield above 7%; Berlusconi resigns (12 Nov) (9 Nov 2011) + ECB announces 3-year LTROs (8 Dec 2011) (2011-10-31)
- France: ECB resumes cutting rates (first cut since Jul 2012) + US taper tantrum (22 May 2013) (2013-05-02)
- France: ECB introduces negative interest rates (2014-06-05)
- France: ECB announces QE (public sector purchases) + Heta (Hypo Alpe Adria bad bank) debt moratorium (1 Mar 2015) (2015-01-22)
- France: Trump elected US president; global bond sell-off (2016-11-08)
- France: French election first round (Macron v Le Pen); OAT spread narrows sharply (2017-04-23)
- France: ECB announces end of net asset purchases (2018-06-14)
- France: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- France: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- France: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- France: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- France: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- France: Barnier forces budget; government toppled (4 Dec) (2024-12-02)
- France: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- France: Bayrou calls confidence vote; government falls (8 Sep); Lecornu resigns (6 Oct) (2025-08-25)
- France: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- France: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- France: French 2027 budget; OAT-Bund spread widest since 2012 (2026-10-01)
- Hungary: MNB starts cutting rates + BNP Paribas freezes funds; global credit crunch begins (9 Aug 2007) (2007-06-25)
- Hungary: Hungary abolishes forint band (free float) + MNB starts raising rates (31 Mar 2008) (2008-02-25)
- Hungary: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Hungary: MNB starts raising rates (2010-11-29)
- Hungary: Hungary seeks IMF/EU aid; Moody's cuts to junk (24 Nov); MNB hikes (29 Nov) (2011-11-17)
- Hungary: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Hungary: Fitch returns Hungary to investment grade (2016-05-20)
- Hungary: Trump elected US president; global bond sell-off (2016-11-08)
- Hungary: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Hungary: MNB cuts base rate (first cut since 2016) (2020-06-23)
- Hungary: MNB starts raising rates (2021-06-22)
- Hungary: Forint slump; MNB emergency 18% deposit tender (2022-10-14)
- Hungary: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Hungary: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Hungary: MNB starts cutting rates + US and Israel attack Iran; Strait of Hormuz closed, oil surges (28 Feb 2026) + Orban loses election; forint and bonds rally (12 Apr 2026) (2026-02-24)
- Hungary: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- Ireland: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Ireland: Trump elected US president; global bond sell-off (2016-11-08)
- Ireland: ECB announces end of net asset purchases (2018-06-14)
- Ireland: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- Ireland: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Italy: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Italy: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Italy: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Italy: ECB starts raising rates (2011-04-07)
- Italy: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- Italy: Greek PM calls bailout referendum; euro crisis peaks + ECB starts cutting rates (Draghi) (3 Nov 2011) + Italian 10-year yield above 7%; Berlusconi resigns (12 Nov) (9 Nov 2011) + ECB announces 3-year LTROs (8 Dec 2011) (2011-10-31)
- Italy: ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) (2012-07-26)
- Italy: Italian election gives hung parliament + US taper tantrum (Fed signals slower bond buying) (22 May 2013) (2013-02-25)
- Italy: ECB introduces negative interest rates (2014-06-05)
- Italy: ECB announces QE (public sector purchases) + Heta (Hypo Alpe Adria bad bank) debt moratorium (1 Mar 2015) (2015-01-22)
- Italy: Trump elected US president; global bond sell-off (2016-11-08)
- Italy: Italian government crisis (Savona veto); worst bond day since 1992 + ECB announces end of net asset purchases (14 Jun 2018) (2018-05-27)
- Italy: Italy sets 2.4% deficit target, clash with EU (2018-09-27)
- Italy: Salvini pulls support for Italian government + ECB cuts deposit rate to -0.5% and restarts QE (12 Sep 2019) (2019-08-08)
- Italy: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Italy: Conte government falls; Draghi asked to form government (2021-02-02)
- Italy: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Italy: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Italy: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Italy: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Italy: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Italy: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Lithuania: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Lithuania: ECB announces QE (public sector purchases) + Heta (Hypo Alpe Adria bad bank) debt moratorium (1 Mar 2015) (2015-01-22)
- Lithuania: Trump elected US president; global bond sell-off (2016-11-08)
- Lithuania: ECB announces end of net asset purchases (2018-06-14)
- Lithuania: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- Lithuania: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Lithuania: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Lithuania: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Lithuania: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Lithuania: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Lithuania: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Lithuania: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Netherlands: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Netherlands: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Netherlands: ECB starts raising rates (2011-04-07)
- Netherlands: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- Netherlands: Dutch government collapses over budget cuts (2012-04-23)
- Netherlands: ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) (2012-07-26)
- Netherlands: ECB resumes cutting rates (first cut since Jul 2012) + US taper tantrum (22 May 2013) (2013-05-02)
- Netherlands: ECB introduces negative interest rates (2014-06-05)
- Netherlands: ECB announces QE (public sector purchases) + Heta (Hypo Alpe Adria bad bank) debt moratorium (1 Mar 2015) (2015-01-22)
- Netherlands: Trump elected US president; global bond sell-off (2016-11-08)
- Netherlands: ECB announces end of net asset purchases (2018-06-14)
- Netherlands: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- Netherlands: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Netherlands: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Netherlands: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Netherlands: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Netherlands: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Netherlands: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Netherlands: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Norway: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Norway: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Norway: Norges Bank starts raising rates (2009-10-28)
- Norway: Norges Bank starts cutting rates (2011-12-14)
- Norway: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Norway: Trump elected US president; global bond sell-off (2016-11-08)
- Norway: Norges Bank starts raising rates (2018-09-20)
- Norway: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Norway: Norges Bank starts raising rates (2021-09-23)
- Norway: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Norway: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Norway: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Norway: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- Poland: NBP starts raising rates (2007-04-25)
- Poland: BNP Paribas freezes funds; global credit crunch begins + Northern Rock bank run; BoE emergency support (14 Sep 2007) + Fed starts cutting rates (18 Sep 2007) (2007-08-09)
- Poland: Lehman Brothers collapses (global financial crisis) + Irish blanket bank guarantee (30 Sep 2008) + SNB starts cutting rates (coordinated cut) (8 Oct 2008) + ECB starts cutting rates (coordinated cut) (8 Oct 2008) + BoK starts cutting rates (9 Oct 2008) + Norges Bank starts cutting rates (15 Oct 2008) + MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) (22 Oct 2008) + BoJ cuts rates (31 Oct 2008) + Fed announces QE1 (agency debt and MBS) (25 Nov 2008) + NBP starts cutting rates (26 Nov 2008) (2008-09-15)
- Poland: NBP starts raising rates (2011-01-19)
- Poland: US taper tantrum (Fed signals slower bond buying) (2013-05-22)
- Poland: NBP resumes cutting rates (2014-10-08)
- Poland: Trump elected US president; global bond sell-off (2016-11-08)
- Poland: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Poland: NBP starts raising rates (2021-10-06)
- Poland: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Poland: NBP starts cutting rates (surprise 75bp) + Polish election: pro-EU opposition wins (15 Oct 2023) (2023-09-06)
- Poland: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Poland: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Poland: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- Slovakia: Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) + ECB starts buying government bonds (SMP); EFSF agreed (10 May 2010) (2010-04-23)
- Slovakia: ECB starts raising rates (2011-04-07)
- Slovakia: Euro crisis spreads to Italy and Spain + Second Greek bailout with private-sector losses (21 Jul 2011) + ECB extends bond buying to Italy and Spain (7 Aug 2011) (2011-07-08)
- Slovakia: ECB 'whatever it takes' (Draghi) + ECB announces OMT (6 Sep 2012) (2012-07-26)
- Slovakia: ECB resumes cutting rates (first cut since Jul 2012) + US taper tantrum (22 May 2013) (2013-05-02)
- Slovakia: ECB introduces negative interest rates (2014-06-05)
- Slovakia: ECB announces QE (public sector purchases) + Heta (Hypo Alpe Adria bad bank) debt moratorium (1 Mar 2015) (2015-01-22)
- Slovakia: Trump elected US president; global bond sell-off (2016-11-08)
- Slovakia: ECB cuts deposit rate to -0.5% and restarts QE (2019-09-12)
- Slovakia: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Slovakia: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- Slovakia: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Slovakia: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- Slovakia: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Slovakia: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Slovakia: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- South Korea: BoK resumes raising rates (first hike in 12 months) (2018-11-30)
- South Korea: BoK starts cutting rates (2019-07-18)
- South Korea: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- South Korea: BoK starts raising rates (2021-08-26)
- South Korea: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- South Korea: BoK starts cutting rates + Martial law declared in South Korea (3 Dec 2024) (2024-10-11)
- South Korea: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- South Korea: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- South Korea: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- Spain: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- Spain: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)
- Switzerland: COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide + ECB launches PEPP (18 Mar 2020) + BoC starts QE (27 Mar 2020) + MNB starts government bond purchases (QE) (7 Apr 2020) + Franco-German proposal for joint EU recovery fund (NGEU) (18 May 2020) (2020-02-24)
- Switzerland: SNB first hike since 2007 (exits negative rates Sep) (2022-06-16)
- Switzerland: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- Switzerland: SNB starts cutting rates (2024-03-21)
- Switzerland: US 'Liberation Day' tariffs; global market turmoil + NBP resumes cutting rates (7 May 2025) + Norges Bank starts cutting rates (19 Jun 2025) (2025-04-02)
- Switzerland: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- Switzerland: US-Iran ceasefire collapses; new attacks in Strait of Hormuz + BoK starts raising rates (16 Jul 2026) + Fed starts raising rates (16 Sep 2026) (2026-07-08)
- European Union: Russia invades Ukraine + BoC starts raising rates (2 Mar 2022) + Fed starts raising rates (16 Mar 2022) + Fed announces QT from June (4 May 2022) (2022-02-24)
- European Union: Silicon Valley Bank fails; banking stress + Credit Suisse rescued by UBS takeover (19 Mar 2023) + MNB starts easing (cuts top of rate corridor) (25 Apr 2023) (2023-03-10)
- European Union: ECB starts cutting rates + Macron calls snap election (9 Jun 2024) (2024-06-06)
- European Union: Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 + US 'Liberation Day' tariffs; global market turmoil (2 Apr 2025) (2025-03-04)
- European Union: US and Israel attack Iran; Strait of Hormuz closed, oil surges + Norges Bank starts raising rates (7 May 2026) + Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) (12 May 2026) (2026-02-28)
- European Union: ECB starts raising rates (energy-driven inflation) + US-Iran ceasefire collapses; new attacks in Strait of Hormuz (8 Jul 2026) (2026-06-11)

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
