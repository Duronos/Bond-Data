# events_v2 research notes (draft)

Draft answer key for break scoring, built under `event_rules.md`. I did not
open `model_testing/results/`, `results/`, `runs/`, `cache/`, `docs/images/`,
README.md or any chart. Events were picked from central bank rate histories,
official statements and news coverage, not from yield data.

## How the file was built

1. **Raw list.** 180 events, each with its own scope (`all`, `euro`, one
   country or a list). The full list is in the appendix at the end.
2. **3-month merge (rule 6), country by country.** The earliest event starts
   a group. Any event within 3 calendar months of that first date joins the
   group and is named in the text with its own date, e.g.
   `Russia invades Ukraine + Fed starts raising rates (16 Mar 2022)`.
   A group is never extended from a later member (no chaining).
3. **Rows.** One row per group leader. A country whose own earlier event
   absorbed a global event is left out of that global row's scope. So most
   "global" rows list countries explicitly (e.g. Lehman covers 24 countries,
   with the Czech Republic left out because its 7 Aug 2008 CNB cut absorbs
   Lehman). Scopes are written as `all` or `euro` only when they match
   exactly. A merged row takes the leader's `type`.
4. Result: **128 rows** in `events_v2_draft.csv` (UTF-8, no BOM).

### Conventions used

- **Date** = the decision or announcement day, or the day the event happened.
  For weekend or overnight news this is the calendar date, not the next
  trading day (all within 1-2 days). Where a rate history only gives
  effective dates (CNB, NBP, ECB), I used the decision date (the day before
  for CNB and NBP; the Thursday before for the ECB).
- **First move of a cycle** = the first move in the opposite direction to the
  last one, or the first move after a pause of at least about 9 months
  (labelled "resumes"). Single moves that were reversed soon after are left
  out (listed below).
- **Political events**: only with a source that reports a bond-market
  reaction. A scheduled election counts only if a source reports a strong
  reaction (France 2017, Trump 2016 and 2024, Poland 2023, Hungary 2026).
- **QT start and QE taper** decisions count as "end of QE" (Fed 2013, 2017,
  2021, 2025; ECB 2018, 2022; BoC 2021; BoJ 2024).

### Sources

Central bank decisions are cited to official pages: Fed press releases, ECB
press releases, BoE Bank Rate history, the BoC history and press releases,
BoJ statements, SNB, Norges Bank and CNB rate histories, NBP rate archive
(XML), MNB decrees and press releases, and Danmarks Nationalbank releases.
The BoK base-rate page loads its table dynamically, so the BoK dates
(checked against news reports) are hard to see on that page. Political,
geopolitical and `all` rows cite Bloomberg, AP (via PBS and Arab News),
Reuters (via syndication: Business Standard, Kitco, NST, Free Malaysia
Today), the BIS Quarterly Review, and a few others (Fox Business/Dow Jones,
Semafor, CNBC, CBC, ANSA, Korea Times, Euronext news). Bloomberg, IMF, FMA and
Bank of Lithuania pages block scripted checks (HTTP 403), and ECB pages time
out for scripts. ECB links were checked one by one with a browser fetch. All
other links returned HTTP 200.

## Rejected candidates, by country (one line each)

### Global / multi-country
- 2007-02-27 Shanghai sell-off: a single-day drop.
- 2008-10-08 coordinated rate cut: recorded only as first cuts for the ECB and SNB; for the Fed, BoE and BoC it continued a cycle.
- 2010-05-06 US flash crash: single day, reversed.
- 2011-03-11 Japan earthquake: a natural disaster, not a listed type; the JGB effect was modest.
- 2015-08-11 China devaluation and the 24 Aug crash: short-lived.
- 2016-06-23 Brexit as `all`: kept as UK only. BIS (Sep 2016) says the market impact "soon subsided".
- 2018-2019 US-China trade war (e.g. 2019-08-05): a gradual escalation, no single dated shock.
- 2020-03-09 oil price war: inside the COVID window.
- 2022-09-02 Nord Stream shut indefinitely (an energy cut caused by the conflict): found no source on a bond-market reaction; it is part of the invasion's aftermath.
- 2023-10-07 Hamas attack on Israel: no lasting bond move reported.
- 2024-08-05 yen carry-trade crash: single day, mostly reversed.
- 2025-06-13 Israel-Iran strikes (June 2025): short-lived.
- 2026-04-08 US-Iran ceasefire: a ceasefire is not an event type.

### United States
- 2008-09-07 Fannie Mae and Freddie Mac conservatorship: same crisis wave, 8 days before Lehman; not listed separately.
- 2008-12-16 rate cut to zero: a further move in the cutting cycle (QE1 of 25 Nov is listed).
- 2010-08-10 reinvestment decision and 2010-08-27 Jackson Hole signal: signals only; the QE2 decision is used.
- 2013-10 shutdown and debt ceiling: short-lived bill-market stress.
- 2019-01 "patience" pivot: a pause, not a new cycle.
- 2019-09-17 repo spike and Oct 2019 bill purchases: "not QE", and inside the Jul 2019 window anyway.
- 2020-08-27 average inflation targeting: an anticipated framework change, not a surprise.
- 2023-08-01 Fitch and 2025-05-16 Moody's downgrades: small rating changes (rule 3).
- 2026 Fed chair change (Warsh): personnel, not a framework change.

### Canada
- 2007-07-10 hike: a single hike, reversed in Dec 2007.
- 2009-04-21 conditional commitment: forward guidance, not a regime change.
- 2022-04-13 QT start: inside the invasion window (not listed separately).
- 2025-02-01 US tariffs on Canada: paused within days.
- 2025-09-17 cut: followed a 6-month pause, below the 9-month threshold.

### United Kingdom
- 2008-02-17 Northern Rock nationalised: inside the Dec 2007 window.
- 2010-05-06 hung parliament: no clear gilt reaction found.
- 2012 QE extension and Funding for Lending: further moves.
- 2013-08-07 BoE forward guidance: inside the taper-tantrum window.
- 2019 Brexit deadlines: no single break.
- 2022-02-03 passive QT and 2022-09-22 active-sales decision: the first is inside the Dec 2021 window; the second was announced in advance (Aug 2022).
- 2022-10-20 Truss resigns: the aftermath of the mini-budget, inside its window.
- 2024-10-30 budget and the Jan 2025 gilt sell-off: modest, or no single dated event.
- 2026-02-09 first pressure on Starmer: used the May 2026 peak instead.
- 2026-11-05 BoE first hike of the new cycle: after the window ends.

### Euro area / ECB
- 2008-07-03 ECB hike: a single hike, reversed in Oct 2008.
- 2009-05-07 covered bond purchases and 12-month LTROs: not government bonds; a further easing step.
- 2010-10-18 Deauville agreement: a statement of intent, its effect blends into the Irish crisis.
- 2011-12-21 first 3-year LTRO allotment: the announcement (8 Dec) is used.
- 2013-07-04 ECB forward guidance: inside the taper window.
- 2014-09-04 ABS and covered-bond purchases: inside the Jun 2014 window, a further step.
- 2015-04/05 Bund tantrum: a market move, not an event.
- 2015-12-03, 2016-03-10, 2016-12-08, 2017-10-26 ECB recalibrations: further moves within QE.
- 2021-07-08 new strategy (symmetric 2%): anticipated, not a surprise.
- 2021-12-16 PEPP end announced: replaced by more APP, so not the end of QE (that is 9 Jun 2022).
- 2013-03-16/25 Cyprus bail-in: Cyprus is not in the list and contagion was limited (noted under Slovenia).

### Germany
- 2024-11-06 coalition collapse: small Bund reaction.
- 2025-02-23 election: scheduled; the market effect came with the 4 Mar 2025 fiscal package, which is listed.

### France
- 2012-01-13 S&P removes AAA: a small rating change.
- 2025-09-12 Fitch cut to A+: a small rating change, inside the Aug 2025 window.
- 2025-10-06 Lecornu resigns: named inside the 25 Aug 2025 row text (same episode, inside the window).

### Italy
- 2016-12-04 Renzi referendum: a small reaction, inside the Trump window.
- 2018-03-04 election: scheduled; spread +10 bp only.
- 2022-09-25 Meloni election: expected, muted reaction.

### Spain
- 2012-05-09 Bankia nationalisation: treated as the same episode as the 9 Jun 2012 bank-bailout request (named in that row).
- 2011-11-20, 2015, 2016, 2019 and 2023 elections; 2018-06-01 Rajoy no-confidence: mild or no reported bond reaction.

### Greece
- 2009-12-08 Fitch cut to BBB+: not junk, and inside the Oct 2009 window.
- 2012-05-06 and 2012-06-17 elections: no separate source sought. May is inside the Feb 2012 window; June sits next to "whatever it takes".
- 2012-11-27 debt relief and buyback (Dec 2012): **candidate not included.** It is arguably a debt restructuring; the reviewer may want to add it.
- 2014-04-10 return to bond markets: a milestone, not an event.
- 2018-08-20 end of bailout: expected.

### Ireland
- 2011-07-12 Moody's cut to junk: one agency only; inside the euro July 2011 window.
- 2013-02-07 promissory-note deal (IBRC liquidated): **candidate not included.** It restructured bank-related debt; the reviewer may want to add it.
- 2013-12-15 bailout exit: expected.

### Belgium
- 2008-09-28 Fortis and 2008-09-30 Dexia rescues: part of the Lehman wave.
- 2011-10-10 second Dexia rescue: inside the euro July 2011 window, not listed separately.
- 2010-11 541-day government crisis: no single date.

### Netherlands
- 2008-10-03 Fortis/ABN AMRO nationalisation and 2008-10-19 ING aid: Lehman wave.

### Austria
- 2009 worries about exposure to Eastern Europe and 2009-12-14 Hypo Alpe Adria nationalisation: no clear dated bond reaction found.

### Finland
- 2011-08 collateral deal with Greece: minor. Finland has no events of its own; it gets only `all` and `euro` rows.

### Slovakia
- 2011-10-11 parliament rejects EFSF expansion and the government falls: no source found on a bond-market reaction (rule 7).
- 2008-05-28 central-parity revaluation and 2008-07-08 conversion rate: part of the 7 May 2008 euro-entry row.
- 2012-03-10 snap election: no reported reaction.

### Slovenia
- 2007-01-01 joins the euro: decided in 2006, before the window.
- 2013-02-27 Jansa government falls: no separate bond source. It would have led the 2013 group; the Moody's junk cut (30 Apr) is used instead.

### Lithuania
- 2008-2009 crisis (austerity, pressure on the litas peg): no dated event with a sourced bond reaction, and the peg held. Before 2015 Lithuania gets only `all` rows and the euro-entry row.

### European Union (EU bonds)
- 2020-10-20 first SURE bond, 2021-06-15 first NGEU bond, 2022-2023 switch to regular auctions: issuance milestones, not events under rule 3. The EU's own fiscal event (the recovery fund, 18 May 2020) is in the COVID row.

### Czech Republic
- 2012-11-01 rates cut to "technical zero": a further cut in the cycle.
- 2020-02-06 hike: a single hike, reversed in Mar 2020.
- 2021-10 and 2025-10 elections: no bond reaction found.

### Hungary
- 2006-09 Oszod speech: before the window.
- 2010-06-04 officials compare Hungary to Greece: rhetoric.
- 2012-01 dispute with the EU over the central bank law: inside the Nov 2011 window.
- 2014 self-financing programme: gradual.
- 2016-09-16 S&P and 2016-11-04 Moody's upgrades: Fitch (20 May 2016) was the first return to investment grade and is used.
- 2022-09-18 Commission proposes suspending EU funds: the forint crisis is dated by the MNB emergency step (14 Oct). It would have led the group if included.
- 2026-06/07/08 further cuts: continuing the cycle.

### Poland
- 2012-05-09 hike: a single hike, reversed in Nov 2012.
- 2015-10-25 PiS wins: scheduled, no strong reaction found.
- 2016-01-15 S&P cut to BBB+: a small rating change, although the reaction was large (**uncertain rejection**).
- 2025-06-01 presidential election: modest reaction.
- 2026-03-04 cut: continuing the cycle.

### Switzerland
- 2010 SNB stops FX interventions: a gradual change.
- 2025-06-19 rate back to 0%: not negative, a further move.
- 2025-08 39% US tariff: limited bond effect.

### Norway
- 2011-05-12 hike: a single hike before the Dec 2011 cut.
- 2020 cuts: in the COVID row.

### Denmark
- 2008-10 hikes to defend the peg: inside the Lehman window (not listed separately).
- 2014-04 exit from negative rates and 2014-09 return: 10 bp toggles.
- 2026 later moves: following the ECB.

### Japan
- 2007-02-21 hike: a further move after the 2006 exit.
- 2011-03-11 earthquake: see Global.
- 2012-11-14 Noda calls a snap election: found no bond-reaction source; Abenomics is captured by QQE (4 Apr 2013).
- 2013-01-22 2% target: anticipated. It would have led the group and absorbed QQE.
- 2014-10-31 QQE expansion: a further move.
- 2018-07-31, 2021-03-19, 2023-07-28 and 2023-10-31 YCC tweaks: follow-up steps after the Dec 2022 change.
- 2025-07-20 upper-house election: scheduled, a moderate move.
- 2025-09-07 Ishiba resigns: same episode as the Takaichi win (4 Oct), which is used.
- 2025-12-19 and 2026 hikes: continuing the cycle that began in Mar 2024.

### South Korea
- 2008-10-30 Fed swap line: inside the Lehman window.
- 2016-12-09 Park impeachment: mild.
- 2022-09-28 Legoland credit crunch: **candidate not included**; the effect on KTBs is unclear.
- 2025-04-04 Yoon removed and 2025-06-03 election: mild.

## Rows I'm least sure about

- **2020-02-24 COVID.** Dated to the start of the global sell-off (BIS QR Mar 2020), not the WHO declaration (11 Mar, as in the old list). Fed, ECB, BoC, MNB and other March 2020 moves are folded in.
- **2026-07-08 US-Iran ceasefire collapse, scope `all`.** Counted as a "major escalation". The source (Semafor, citing the WSJ) reports US, euro and UK yields rising. For euro countries, Denmark and the Czech Republic it is absorbed by the June 2026 hikes; for the US it absorbs the Fed hike (16 Sep 2026).
- **2025-04-02 tariffs** (typed `financial`, scope all-but-euro after merging): not a war, but a global market shock. US yields rose while Bunds rallied.
- **2016-11-08 Trump**, a scheduled election scoped all-but-Japan; BIS reports a global bond sell-off.
- **2026-01-13 Japan snap election.** First press reports were 9-11 Jan; dated to the first Tokyo session after them. It absorbs the Iran war for Japan.
- **2026-05-12 UK Starmer crisis** (folded into the Iran row for the UK). The pressure built from February; the resignation on 22 Jun drew a muted reaction.
- **2026-10-01 French 2027 budget.** The sell-off was gradual. "Widest since 2011" comes from one source; others say since 2012.
- **2025-09-17 Fed "resumes cutting"**: counted as a new cycle under the 9-month pause rule. The same rule gives Korea 2014-08-14, Poland 2014-10-08 and 2025-05-07, Hungary 2016-03-22 and Norway 2014-12-11.
- **Hungary:** 2023-04-25 "MNB starts easing" (cut the top of the rate corridor; the base rate was unchanged until Sep 2023); 2020-06-23 (a 15 bp cut); 2007-06-25 (dated from the decree list; I didn't check the size).
- **2009-10-20 Greek deficit revision.** The figure was given at the 19-20 Oct Eurogroup and Ecofin and formally notified on 21 Oct; press reports suggest it was known a few days earlier.
- **2011-07-08 euro contagion** (could be 11-12 Jul, when Italian yields broke 6%).
- **2014-12-08 Greece** (announced in the evening, market reaction on 9 Dec).
- **2017-04-23 France**, a scheduled election (spread tightened about 20 bp).
- **2021-02-02 Italy**: the government fell and Draghi was asked to form one. A positive reaction (spread narrowest since 2016).
- **2023-09-08 Greece investment grade** (DBRS first; S&P, the first of the big three, on 20 Oct).
- **2014-01-17 Ireland** (only Moody's had rated Ireland junk).
- **2012-04-23 Netherlands** (AP: Dutch yields +11 bp).
- **2017-10-01 Catalonia** (moderate reaction).
- **QT rows** (Fed 2017-09-20, ECB 2022-12-15) treated as end-of-QE events. The ECB QT row absorbs SVB for euro countries.
- **2008-03-16 Bear Stearns** (US only) and **2011-08-05 S&P downgrade** (US: counted as a budget crisis, the debt ceiling, not a small rating change).
- **2010-04-23 euro row** uses the date of Greece's bailout request (the contagion from 27 Apr and the SMP of 10 May are folded in). The old list used 2010-05-02.
- **2025-03-04 German fiscal package** scoped `euro` (yields rose across the euro area) rather than Germany only.
- **2025-10-04 Takaichi**: an LDP leadership change rather than a government falling (Ishiba resigned on 7 Sep).

### Side effects of the 3-month rule to be aware of

Applying rule 6 strictly means some distinct shocks are absorbed by
unrelated earlier events for some countries:
- Japan: QQE (Apr 2013) absorbs the taper tantrum; YCC (Sep 2016) absorbs Trump; the YCC band change (Dec 2022) absorbs SVB.
- Euro countries: ECB QT (Dec 2022) absorbs SVB; ECB hike (Jun 2026) absorbs the Iran re-escalation.
- Italy: the 2013 election absorbs the taper tantrum.
- Spain: the bank bailout (Jun 2012) absorbs "whatever it takes".
- France: the ECB cut (Jun 2024) absorbs the snap election.
- Hungary: the MNB cut (24 Feb 2026) absorbs the Iran war and the election; the 2007 MNB cut absorbs the BNP shock.
- Poland and Norway: the Apr 2025 tariffs absorb their 2025 cuts.

## Appendix: raw events before merging (180)

| id | date | event | scope | type |
|---|---|---|---|---|
| SK1 | 2007-03-16 | Slovak koruna central rate revalued 8.5% in ERM II | Slovakia | monetary |
| HU01 | 2007-06-25 | MNB starts cutting rates | Hungary | monetary |
| G01 | 2007-08-09 | BNP Paribas freezes funds; global credit crunch begins | all | financial |
| UK01 | 2007-09-14 | Northern Rock bank run; BoE emergency support | United Kingdom | financial |
| US01 | 2007-09-18 | Fed starts cutting rates | United States | monetary |
| CA1 | 2007-12-04 | BoC starts cutting rates | Canada | monetary |
| UK02 | 2007-12-06 | BoE starts cutting rates | United Kingdom | monetary |
| HU02 | 2008-02-25 | Hungary abolishes forint band (free float) | Hungary | monetary |
| US02 | 2008-03-16 | Bear Stearns rescue; Fed lends to dealers | United States | financial |
| HU03 | 2008-03-31 | MNB starts raising rates | Hungary | monetary |
| SK2 | 2008-05-07 | EU backs Slovakia joining the euro in 2009 (conversion rate fixed 8 Jul) | Slovakia | fiscal |
| CZ1 | 2008-08-07 | CNB starts cutting rates | Czech Republic | monetary |
| G02 | 2008-09-15 | Lehman Brothers collapses (global financial crisis) | all | financial |
| IE1 | 2008-09-30 | Irish blanket bank guarantee | Ireland | fiscal |
| CH1 | 2008-10-08 | SNB starts cutting rates (coordinated cut) | Switzerland | monetary |
| E01 | 2008-10-08 | ECB starts cutting rates (coordinated cut) | euro | monetary |
| KR01 | 2008-10-09 | BoK starts cutting rates | South Korea | monetary |
| NO1 | 2008-10-15 | Norges Bank starts cutting rates | Norway | monetary |
| HU04 | 2008-10-22 | MNB emergency hike; IMF/EU bailout for Hungary (28 Oct) | Hungary | fiscal |
| JP01 | 2008-10-31 | BoJ cuts rates | Japan | monetary |
| US03 | 2008-11-25 | Fed announces QE1 (agency debt and MBS) | United States | monetary |
| PL1 | 2008-11-26 | NBP starts cutting rates | Poland | monetary |
| UK03 | 2009-03-05 | BoE cuts to 0.5% and starts QE | United Kingdom | monetary |
| CH2 | 2009-03-12 | SNB starts QE (bond and FX purchases) | Switzerland | monetary |
| US04 | 2009-03-18 | Fed to buy Treasuries (QE1 expanded) | United States | monetary |
| GR1 | 2009-10-20 | Greece revises 2009 deficit up to 12.5% of GDP | Greece | fiscal |
| NO2 | 2009-10-28 | Norges Bank starts raising rates | Norway | monetary |
| E02 | 2010-04-23 | Greece requests EU/IMF bailout; euro debt crisis begins (S&P cuts Greece to junk 27 Apr) | euro | fiscal |
| E03 | 2010-05-10 | ECB starts buying government bonds (SMP); EFSF agreed | euro | monetary |
| CA2 | 2010-06-01 | BoC starts raising rates | Canada | monetary |
| KR02 | 2010-07-09 | BoK starts raising rates | South Korea | monetary |
| IE2 | 2010-09-30 | Ireland puts bank bailout cost at up to EUR 34bn | Ireland | fiscal |
| JP02 | 2010-10-05 | BoJ comprehensive easing (asset purchases, zero rates) | Japan | monetary |
| US05 | 2010-11-03 | Fed announces QE2 | United States | monetary |
| IE3 | 2010-11-21 | Ireland requests EU/IMF bailout | Ireland | fiscal |
| HU05 | 2010-11-29 | MNB starts raising rates | Hungary | monetary |
| PL2 | 2011-01-19 | NBP starts raising rates | Poland | monetary |
| E04 | 2011-04-07 | ECB starts raising rates | euro | monetary |
| E05 | 2011-07-08 | Euro crisis spreads to Italy and Spain | euro | fiscal |
| E06 | 2011-07-21 | Second Greek bailout with private-sector losses | euro | fiscal |
| CH3 | 2011-08-03 | SNB cuts rates to zero, floods liquidity | Switzerland | monetary |
| US06 | 2011-08-05 | S&P downgrades US after debt-ceiling crisis | United States | fiscal |
| E07 | 2011-08-07 | ECB extends bond buying to Italy and Spain | euro | monetary |
| CH4 | 2011-09-06 | SNB sets 1.20 floor against euro | Switzerland | monetary |
| US07 | 2011-09-21 | Fed Operation Twist | United States | monetary |
| UK04 | 2011-10-06 | BoE restarts QE | United Kingdom | monetary |
| E08 | 2011-10-31 | Greek PM calls bailout referendum; euro crisis peaks | euro | political |
| E09 | 2011-11-03 | ECB starts cutting rates (Draghi) | euro | monetary |
| IT1 | 2011-11-09 | Italian 10-year yield above 7%; Berlusconi resigns (12 Nov) | Italy | political |
| HU06 | 2011-11-21 | Hungary seeks IMF/EU aid; Moody's cuts to junk (24 Nov); MNB hikes (29 Nov) | Hungary | fiscal |
| E10 | 2011-12-08 | ECB announces 3-year LTROs | euro | monetary |
| NO3 | 2011-12-14 | Norges Bank starts cutting rates | Norway | monetary |
| GR2 | 2012-02-21 | Second Greek programme and PSI debt restructuring (bond swap 9 Mar) | Greece | fiscal |
| NL1 | 2012-04-23 | Dutch government collapses over budget cuts | Netherlands | political |
| ES1 | 2012-06-09 | Spain requests euro-area bank bailout (after Bankia nationalisation) | Spain | fiscal |
| DK1 | 2012-07-05 | Danmarks Nationalbank introduces negative rates | Denmark | monetary |
| KR03 | 2012-07-12 | BoK starts cutting rates | South Korea | monetary |
| E11 | 2012-07-26 | ECB 'whatever it takes' (Draghi) | euro | monetary |
| HU07 | 2012-08-28 | MNB starts cutting rates | Hungary | monetary |
| E12 | 2012-09-06 | ECB announces OMT | euro | monetary |
| US08 | 2012-09-13 | Fed announces QE3 | United States | monetary |
| PL3 | 2012-11-07 | NBP starts cutting rates | Poland | monetary |
| IT2 | 2013-02-25 | Italian election gives hung parliament | Italy | political |
| JP03 | 2013-04-04 | BoJ launches QQE | Japan | monetary |
| SI1 | 2013-04-30 | Moody's cuts Slovenia to junk amid bank crisis | Slovenia | fiscal |
| G03 | 2013-05-22 | US taper tantrum (Fed signals slower bond buying) | all | monetary |
| CZ2 | 2013-11-07 | CNB sets koruna floor (27 per euro) | Czech Republic | monetary |
| SI2 | 2013-12-12 | Slovenian bank stress tests: EUR 4.8bn recapitalisation, no bailout | Slovenia | fiscal |
| US09 | 2013-12-18 | Fed starts tapering QE3 | United States | monetary |
| IE4 | 2014-01-17 | Moody's returns Ireland to investment grade | Ireland | fiscal |
| LT1 | 2014-06-04 | EU backs Lithuania joining the euro in 2015 (Council decision 23 Jul) | Lithuania | fiscal |
| E13 | 2014-06-05 | ECB introduces negative interest rates | euro | monetary |
| KR04 | 2014-08-14 | BoK resumes cutting rates | South Korea | monetary |
| PL4 | 2014-10-08 | NBP resumes cutting rates | Poland | monetary |
| G11 | 2014-11-27 | OPEC declines to cut output; oil price collapse | Canada;Norway | financial |
| GR3 | 2014-12-08 | Greek presidential vote brought forward; snap election, Syriza wins (25 Jan 2015) | Greece | political |
| NO4 | 2014-12-11 | Norges Bank resumes cutting rates | Norway | monetary |
| CH5 | 2014-12-18 | SNB introduces negative rates | Switzerland | monetary |
| CH6 | 2015-01-15 | SNB drops euro floor; rate to -0.75% | Switzerland | monetary |
| DK2 | 2015-01-19 | Nationalbank cuts rates to defend krone peg | Denmark | monetary |
| CA3 | 2015-01-21 | BoC surprise rate cut | Canada | monetary |
| E14 | 2015-01-22 | ECB announces QE (public sector purchases) | euro | monetary |
| DK3 | 2015-01-30 | Denmark suspends government bond issuance | Denmark | fiscal |
| AT1 | 2015-03-01 | Heta (Hypo Alpe Adria bad bank) debt moratorium | Austria | financial |
| GR4 | 2015-06-26 | Greek bailout referendum called; capital controls; third bailout (13 Jul) | Greece | political |
| US10 | 2015-12-16 | Fed first rate hike since 2006 | United States | monetary |
| JP04 | 2016-01-29 | BoJ introduces negative interest rates | Japan | monetary |
| HU08 | 2016-03-22 | MNB resumes cutting rates | Hungary | monetary |
| HU09 | 2016-05-20 | Fitch returns Hungary to investment grade | Hungary | fiscal |
| UK05 | 2016-06-23 | Brexit referendum | United Kingdom | political |
| UK06 | 2016-08-04 | BoE cuts rate and restarts QE | United Kingdom | monetary |
| JP05 | 2016-09-21 | BoJ introduces yield-curve control | Japan | monetary |
| G04 | 2016-11-08 | Trump elected US president; global bond sell-off | all | political |
| CZ3 | 2017-04-06 | CNB ends koruna floor | Czech Republic | monetary |
| FR1 | 2017-04-23 | French election first round (Macron v Le Pen); OAT spread narrows sharply | France | political |
| CA4 | 2017-07-12 | BoC starts raising rates | Canada | monetary |
| CZ4 | 2017-08-03 | CNB starts raising rates | Czech Republic | monetary |
| US11 | 2017-09-20 | Fed starts shrinking its balance sheet (QT) | United States | monetary |
| ES2 | 2017-10-01 | Catalan independence referendum | Spain | political |
| UK07 | 2017-11-02 | BoE first hike in a decade | United Kingdom | monetary |
| KR05 | 2017-11-30 | BoK starts raising rates | South Korea | monetary |
| IT3 | 2018-05-27 | Italian government crisis (Savona veto); worst bond day since 1992 | Italy | political |
| E15 | 2018-06-14 | ECB announces end of net asset purchases | euro | monetary |
| NO5 | 2018-09-20 | Norges Bank starts raising rates | Norway | monetary |
| IT4 | 2018-09-27 | Italy sets 2.4% deficit target, clash with EU | Italy | fiscal |
| GR5 | 2019-05-26 | Tsipras calls snap election; Greek yields at record lows | Greece | political |
| KR06 | 2019-07-18 | BoK starts cutting rates | South Korea | monetary |
| US12 | 2019-07-31 | Fed starts cutting rates; ends QT | United States | monetary |
| IT5 | 2019-08-08 | Salvini pulls support for Italian government | Italy | political |
| E16 | 2019-09-12 | ECB cuts deposit rate to -0.5% and restarts QE | euro | monetary |
| G05 | 2020-02-24 | COVID-19 market crash (pandemic declared 11 Mar); emergency rate cuts and QE worldwide | all | financial |
| E17 | 2020-03-18 | ECB launches PEPP | euro | monetary |
| CA5 | 2020-03-27 | BoC starts QE | Canada | monetary |
| HU10 | 2020-04-07 | MNB starts government bond purchases (QE) | Hungary | monetary |
| E18 | 2020-05-18 | Franco-German proposal for joint EU recovery fund (NGEU) | euro | fiscal |
| HU11 | 2020-06-23 | MNB cuts base rate (first cut since 2016) | Hungary | monetary |
| IT6 | 2021-02-02 | Conte government falls; Draghi asked to form government | Italy | political |
| HU12 | 2021-06-22 | MNB starts raising rates | Hungary | monetary |
| CZ5 | 2021-06-23 | CNB starts raising rates | Czech Republic | monetary |
| KR07 | 2021-08-26 | BoK starts raising rates | South Korea | monetary |
| NO6 | 2021-09-23 | Norges Bank starts raising rates | Norway | monetary |
| PL5 | 2021-10-06 | NBP starts raising rates | Poland | monetary |
| CA6 | 2021-10-27 | BoC ends QE | Canada | monetary |
| US13 | 2021-11-03 | Fed starts tapering QE | United States | monetary |
| UK08 | 2021-12-16 | BoE starts raising rates | United Kingdom | monetary |
| G06 | 2022-02-24 | Russia invades Ukraine | all | geopolitical |
| CA7 | 2022-03-02 | BoC starts raising rates | Canada | monetary |
| US14 | 2022-03-16 | Fed starts raising rates | United States | monetary |
| US15 | 2022-05-04 | Fed announces QT from June | United States | monetary |
| E19 | 2022-06-09 | ECB announces end of QE and first hike | euro | monetary |
| CH7 | 2022-06-16 | SNB first hike since 2007 (exits negative rates Sep) | Switzerland | monetary |
| IT7 | 2022-07-14 | Draghi government collapses (resigns 21 Jul) | Italy | political |
| DK4 | 2022-07-21 | Nationalbank starts raising rates (exits negative rates 8 Sep) | Denmark | monetary |
| E20 | 2022-07-21 | ECB first hike since 2011; TPI anti-fragmentation tool | euro | monetary |
| UK09 | 2022-09-23 | UK mini-budget gilt crisis (BoE gilt buying 28 Sep) | United Kingdom | fiscal |
| HU13 | 2022-10-14 | Forint slump; MNB emergency 18% deposit tender | Hungary | monetary |
| E21 | 2022-12-15 | ECB announces quantitative tightening (from Mar 2023) | euro | monetary |
| JP06 | 2022-12-20 | BoJ widens YCC band (surprise) | Japan | monetary |
| G07 | 2023-03-10 | Silicon Valley Bank fails; banking stress | all | financial |
| CH8 | 2023-03-19 | Credit Suisse rescued by UBS takeover | Switzerland | financial |
| HU14 | 2023-04-25 | MNB starts easing (cuts top of rate corridor) | Hungary | monetary |
| PL6 | 2023-09-06 | NBP starts cutting rates (surprise 75bp) | Poland | monetary |
| GR6 | 2023-09-08 | Greece regains investment grade (DBRS; S&P 20 Oct) | Greece | fiscal |
| PL7 | 2023-10-15 | Polish election: pro-EU opposition wins | Poland | political |
| CZ6 | 2023-12-21 | CNB starts cutting rates | Czech Republic | monetary |
| JP07 | 2024-03-19 | BoJ ends negative rates and yield-curve control | Japan | monetary |
| CH9 | 2024-03-21 | SNB starts cutting rates | Switzerland | monetary |
| CA8 | 2024-06-05 | BoC starts cutting rates | Canada | monetary |
| DK5 | 2024-06-06 | Nationalbank starts cutting rates | Denmark | monetary |
| E22 | 2024-06-06 | ECB starts cutting rates | euro | monetary |
| FR2 | 2024-06-09 | Macron calls snap election | France | political |
| JP08 | 2024-07-31 | BoJ hikes and sets plan to halve JGB purchases | Japan | monetary |
| UK10 | 2024-08-01 | BoE starts cutting rates | United Kingdom | monetary |
| US16 | 2024-09-18 | Fed starts cutting rates | United States | monetary |
| KR08 | 2024-10-11 | BoK starts cutting rates | South Korea | monetary |
| US17 | 2024-11-05 | Trump re-elected; Treasury yields jump | United States | political |
| FR3 | 2024-12-02 | Barnier forces budget; government toppled (4 Dec) | France | political |
| KR09 | 2024-12-03 | Martial law declared in South Korea | South Korea | political |
| E23 | 2025-03-04 | Germany agrees debt-brake reform and EUR 500bn fund; worst Bund sell-off since 1990 | euro | fiscal |
| G08 | 2025-04-02 | US 'Liberation Day' tariffs; global market turmoil | all | financial |
| PL8 | 2025-05-07 | NBP resumes cutting rates | Poland | monetary |
| NO7 | 2025-06-19 | Norges Bank starts cutting rates | Norway | monetary |
| FR4 | 2025-08-25 | Bayrou calls confidence vote; government falls (8 Sep); Lecornu resigns (6 Oct) | France | political |
| US18 | 2025-09-17 | Fed resumes cutting after 9-month pause | United States | monetary |
| JP09 | 2025-10-04 | Takaichi wins LDP leadership; JGB and yen sell-off | Japan | political |
| US19 | 2025-10-29 | Fed announces end of QT (1 Dec) | United States | monetary |
| JP10 | 2026-01-13 | Takaichi snap-election plan; super-long JGB rout (election 8 Feb) | Japan | political |
| HU15 | 2026-02-24 | MNB starts cutting rates | Hungary | monetary |
| G09 | 2026-02-28 | US and Israel attack Iran; Strait of Hormuz closed, oil surges | all | geopolitical |
| HU16 | 2026-04-12 | Orban loses election; forint and bonds rally | Hungary | political |
| NO8 | 2026-05-07 | Norges Bank starts raising rates | Norway | monetary |
| UK11 | 2026-05-12 | Starmer leadership crisis; gilt yields highest since 2008 (resigns 22 Jun) | United Kingdom | political |
| DK6 | 2026-06-11 | Nationalbank starts raising rates | Denmark | monetary |
| E24 | 2026-06-11 | ECB starts raising rates (energy-driven inflation) | euro | monetary |
| CZ7 | 2026-06-18 | CNB starts raising rates | Czech Republic | monetary |
| G10 | 2026-07-08 | US-Iran ceasefire collapses; new attacks in Strait of Hormuz | all | geopolitical |
| KR10 | 2026-07-16 | BoK starts raising rates | South Korea | monetary |
| US20 | 2026-09-16 | Fed starts raising rates | United States | monetary |
| FR5 | 2026-10-01 | French 2027 budget; OAT-Bund spread widest since 2011 | France | fiscal |
| CA9 | 2026-10-28 | BoC starts raising rates | Canada | monetary |

Sources for each raw event are carried into the merged rows of events_v2_draft.csv.
