# How events_v2.csv was made

1. Rules fixed first: [event_rules.md](event_rules.md).
2. Research agent (blind to all results): 180 events found, merged under
   the 3-month rule into 128 rows: [events_v2_draft.csv](events_v2_draft.csv),
   notes in [events_v2_research_notes.md](events_v2_research_notes.md).
3. Review agent (also blind): 120 keep, 5 fix, 3 drop, 8 additions:
   [events_v2_review.csv](events_v2_review.csv),
   [events_v2_review_notes.md](events_v2_review_notes.md).
4. Merged into [events_v2.csv](events_v2.csv) (133 rows). The open
   questions the reviewer raised were settled by the rules as written, not
   by looking at the scores:

| Question | Decision | Why |
|---|---|---|
| Does the start of QT count? | No: rows 69 (Fed 2017) and 99 (ECB Dec 2022) dropped; SVB (row 101) then covers the euro area too | Rule 3 lists the start or end of QE only |
| When does a move after a pause start a "new cycle"? | After about 9 months or more, as the researcher applied it; the reviewer's 5 rows that follow from it are added (CNB Jun 2012, ECB May 2013, BoK Jun 2016 and Nov 2018, BoE Aug 2018) and Hungary Mar 2016 (8-month pause) is re-dated to Fitch's upgrade | The researcher's convention was set blind; applying it evenly is the smallest change |
| Single-row fixes (Hungary IMF 17 Nov 2011, Greece Scope 4 Aug 2023, Japan Ishiba 7 Sep 2025, BoJ Jul 2024 dropped) | All taken | Each follows the date rule (first news) or the further-move rule |
| Source problems (rows 25, 115, 126; text of row 127) | Wrong links removed, Semafor replaced by AP, "since 2011" corrected to "since 2012" | Review notes |
| The 3-month merge rule lets a small event absorb a big one (e.g. a CNB cut absorbs Lehman for the Czech Republic) | Kept as written | Changing a rule after seeing the scores would let bias in; left for the owner |

5. Matching window: **±3 months** for events_v2.csv (owner's choice, 23 Nov
   2026; events.csv stays at ±6). With about one event per country per
   year, ±6 months lets random breaks match an event about 72% of the time,
   so it can't tell a good model from guessing; at ±3 random precision is
   about 45%. Events are at least 3 months apart, so a ±3 window rarely
   reaches two of them. This was decided after seeing the ±6 scores.

Built by a script from the draft and the review; every country name
matches the data, every row has a source, and no country has two events
less than 3 months apart.
