# Evidence — `decision-builder` replay vs the original StockFox run

_2026-08-08. Controlled replay: identical research inputs (`intent.md`, `context.md`, `research_plan.md`, `research_q1–q4.md`), run through `decision-builder` instead of the blended `case-builder` that produced the submitted deck._

This is the test of Roadmap Phase 1's premise: *an agent that already knows which recommendation it is about to defend cannot neutrally eliminate the alternatives.*

## The finding

**Original `tradeoffs.md` — four "rejected alternatives", every one a parameter tweak of the already-chosen design:**

| Decision | "Rejected alternative" |
|---|---|
| No score pre-click | show the score with a disclaimer |
| Browsing unmetered | meter card views too |
| No gamification | scope streaks to watchlist actions |
| Peer comparison hidden | show a one-line peer delta on the card |

Not one is a different product. The chosen design — Explore with theme rails — was never compared against anything. This is precisely the failure the roadmap predicted: the options were never real candidates, so the rejects are justification written after the fact.

**Replay `decision.md` — six distinct product paths, generated before a favourite existed:**

A thematic collections · B disclosed-criteria sort · C familiarity-first entry · D question-led guided entry · E social discovery · F learning-layer-as-discovery

Three killed by named hard constraints, pass/fail, never by score:

| Killed | By | Gate, not preference |
|---|---|---|
| E — social discovery | HC3 then HC1 | Cold start is absolute in a metered beta with no user base. StockGro can run this lane *because* it has 35M users; that asset is the option's precondition |
| D — question-led | HC1 | Personalised output on a paid platform is the Investment Adviser definition. Stripped of it, D is a wizard around A or C, not a distinct path |
| F — learning-as-discovery | HC1, then HC2 | "Concept, then the live-priced companies it applies to" is what the ≥3-month-stale-price expectation exists to stop |

## The substantive difference

The two runs reached **different answers**, and the replay's is stronger for a specific reason.

The original treated the non-SRA constraint as a **display rule**: don't show a score. The replay treated it as an **architecture rule**: don't be the party doing the selecting at all. Its decision has the *user* name a company they already buy from, so StockFox nominates nothing pre-Scorecard. Under a regulator's reading that is a strictly better position than curated theme rails, where StockFox still chooses what goes in each rail.

That reframe only surfaces if you hold six options open long enough to notice that "who performs the selection" is the axis that matters. A blended stage that already has theme rails in hand cannot find it.

## Also produced, none of which existed in the original

- **A kill test with thresholds**: two-variant landing card, 50 first-time visitors each. `<8/50 name a company that resolves and open its Scorecard → abandon the default`. Runs in a week, needs no product.
- **A long pole**: the brand→listed-entity map, ~150 names, explicitly *not* parallelisable because the hard cases each need a judgement call — Jio→Reliance, Amul (cooperative), Flipkart (unlisted), Maggi and KitKat both→Nestlé India. Every unhandled case is a dead end on the user's first interaction.
- **"And then what"**: the entry mechanic is copyable in a sprint; the constraint is not. StockGro can attach a registered analyst's view to whatever the user names, and StockFox legally cannot.
- **Two unresolved forks, stated rather than forced.** The F kill rests on a 0.65-confidence reading of secondary reporting, and the file says so: *"This kill is the fragile one… Flagged, not buried."*

## Confounds — read before treating this as proof

1. The replay prompt explicitly warned that strawman options would mean the stage had failed. Some of the improvement is that instruction, not the architecture. **But** the architecture is what makes the instruction credible: you cannot meaningfully tell a stage "don't rationalise" when it already holds the answer it is rationalising toward.
2. The replay read an `intent.md` already refined by the original run, including the SRA insight. It did not have to discover that constraint cold.
3. It knew it was a test. Nothing shipped.

n=1. This is evidence for Phase 1's premise, not proof of it. The next real assignment is the honest test.

## Gate behaviour observed during the replay

The freshness gate **correctly denied** the first attempt: `research_plan.md` had mtime 22:08 while `research_q1/q3/q4` were 18:26, so those answers genuinely predated the current plan. The later edit was cosmetic, which is the documented false-positive mode — `mtime` detects "was written", not "changed meaningfully". Cleared with `gate_override` plus a written reason, the first real use of that escape hatch.
