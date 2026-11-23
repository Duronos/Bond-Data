# events_v2 review notes

Second, independent check of `events_v2_draft.csv` under `event_rules.md`
section 9. I did not open `model_testing/results/`, `results/`, `runs/`,
`cache/`, `docs/images/`, README.md or any chart. Verdicts are in
`events_v2_review.csv`.

## Counts

| verdict | rows |
|---|---|
| keep | 120 |
| fix | 5 (rows 30, 61, 101, 103, 119) |
| drop | 3 (rows 69, 99, 110) |
| add | 8 (3 firm, 5 only if the "resumes after ~9 months" convention is kept) |

All events from Feb 2026 on were checked against at least one dated report:
the Iran strikes (28 Feb), MNB cut (24 Feb), Orban's defeat (12 Apr), Norges
Bank hike (7 May), the Starmer gilt sell-off (12 May), ECB and DN hikes
(11 Jun), CNB (18 Jun), the ceasefire collapse (7-8 Jul), BoK (16 Jul), Fed
(16 Sep), the French budget (1 Oct) and BoC (28 Oct). All match. A script
check found no country with two events within 3 months, both on the draft
and after applying my changes, with or without the conditional adds.

## Main problems found

1. **QT counted as end of QE (rows 69, 99: drop).** Rule 3 lists the start or
   end of QE, not the start of QT. For the ECB the end of QE is already in
   row 94, so the Dec 2022 QT row counts the same policy twice and also
   absorbs SVB for every euro country. If 99 is dropped, SVB (row 101) should
   cover the euro area too (fix to row 101; euro yields fell sharply, as the
   row's own Kitco/Reuters source says).
2. **BoJ 31 Jul 2024 (row 110: drop).** The decision to cut JGB buying came
   on 14 Jun 2024, inside the March 2024 window. The July hike was a further
   move in the cycle.
3. **"Resumes cutting" applied unevenly.** MNB 22 Mar 2016 followed an 8-month
   pause, and so did MNB 24 Mar 2015, which isn't listed. I moved row 61 to
   Fitch's investment-grade upgrade (20 May 2016). The same convention also
   leaves out CNB Jun 2012 (25-month pause), ECB May 2013 (10 months), BoK
   Jun 2016 and Nov 2018 (12 months) and BoE Aug 2018 (9 months, the same as
   the Fed Sep 2025 pause that is kept). These are added as **conditional**
   rows.
4. **Dates.** Hungary's IMF request (row 30): the news broke on 17 Nov 2011,
   4 days before 21 Nov. Japan (row 119): the government fell when Ishiba
   resigned on 7 Sep 2025, and long JGB yields rose the next day; Takaichi's
   win falls inside that window. Greece's return to investment grade (row 103)
   came first from Scope on 4 Aug 2023, not DBRS on 8 Sep.
5. **Sources outside the named outlets or off-topic:** row 25 (the Bloomberg
   link is about German exports), 58 (WEF), 115 (the first link is about
   Japanese yields), 126 (Semafor; an AP copy mentioning bond yields is
   given). Dates are fine in all four. Row 127 text: most sources say
   "widest since 2012".

## Additions

- Firm: **NBP first hike 25 Apr 2007** (the rate had been unchanged since Mar
  2006), the **Greek debt relief and buyback, 27 Nov 2012**, and the **Irish
  promissory-note deal, 7 Feb 2013** (debt restructurings under rule 3; both
  fall outside other windows).
- Not added: Nord Stream (2 Sep 2022). For the euro area it falls inside the
  Jun 2022 window, and for the UK it would absorb the mini-budget. S&P Poland
  (Jan 2016) is a one-notch move that stays investment grade, which rule 3
  excludes. The Korea Legoland credit crunch (28 Sep 2022) is a borderline
  case the owner may want. The Aug-Sep 2026 global bond sell-off built up
  gradually and has no single date.

## Rules that are unclear or gave odd results

- **Rule 6 lets small events absorb big shocks.** A 25 bp CNB cut absorbs
  Lehman for the Czech Republic. A 25 bp MNB cut absorbs the BNP shock
  (2007), and another (24 Feb 2026) absorbs both the Iran war and Orban's
  defeat. SNB negative rates (Dec 2014) absorb the floor exit (Jan 2015).
  ECB QT absorbs SVB, and the ECB's Jun 2024 cut absorbs France's snap
  election. This follows the rule as written, but the dates can be weeks
  away from the largest move. The owner could allow the larger shock to lead
  a group, or never absorb `all` events.
- **"New cycle" is not defined for pauses.** The ~9-month threshold is the
  researcher's own. Pick a threshold (for example 12 months) and apply it
  everywhere, or count only changes of direction.
- **QT and taper.** Is a taper start the "end of QE"? I accepted it, because
  it sets the end path. QT start I did not. Owner to decide.
- **Rating events.** "To or from junk" doesn't say which agencies count
  (Scope/R&I vs the big three; Moody's alone for Ireland 2014). The US AAA
  downgrade (row 27) is kept only as a budget crisis.
- **Scope of single-country shocks felt across a region** (German fiscal
  package scoped `euro`, row 115; OPEC scoped Canada and Norway): the rules
  don't say. I accepted both.
- **Scheduled elections** (Trump 2016, France 2017, Italy 2013) are kept
  because a source reports a strong reaction. That's consistent, but it
  depends on how hard someone searched for a source.

## For the owner to decide

The QT convention (rows 69, 99, 101); the "resumes" threshold (row 61, row
118 and the 5 conditional adds); row 119 (7 Sep vs 4 Oct 2025); row 103
(Scope vs DBRS); row 27 (US downgrade); row 56 type; whether rule 6 should
let the larger shock lead.
