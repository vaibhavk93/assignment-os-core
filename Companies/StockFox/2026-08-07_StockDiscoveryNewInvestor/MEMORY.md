# Assignment Memory — StockFox: Stock Discovery for a New Investor

_Run 2026-08-07 · Submitted 2026-08-08 · **Outcome pending — awaiting reply**_

---

## Outcome (added via `/debrief` on 2026-08-08)

- **Result: pending.** Submitted, no reply yet. The final discussion was scheduled by StockFox for a Friday/Saturday with shortlisted candidates.
- **Interviewer feedback:** none received yet.
- **Predicted vs actual questions:** not yet comparable. The predictions are recorded below so the comparison is evidence rather than recollection when the reply lands.
- **Nothing appended to the `hiring-signal-patterns` learnings log.** No outcome means no evidence, and a speculative entry would corrupt the one mechanism that measures whether this system works. Re-run `/debrief` when there is a real result.

---

## What was submitted

**Explore** — a new home surface for a first-time investor with no candidate in mind. A brand-recognition strip of consumer names, 4–5 theme rails sorted by disclosed objective criteria (never by a score), and an unmetered compare tray. Tapping a card opens the existing Stock Health Scorecard unmodified and spends one of the 3 free analyses. Search demoted but not removed.

Delivered: `presentation.html`, `.pdf`, `.pptx`. 8 body sections + cover, 2 appendix. Checker PASS on loop 0.

**Checker Tier 2:** intent alignment 0.95, completeness 0.90 (14 of 15 success criteria), remainder 0.90–1.0.

---

## The predictions to test when the reply lands

These are what the pre-submission critique said a founder-level evaluator would push on. **This is the testable part of this record** — if the real discussion opens somewhere entirely different, the critique model is miscalibrated and that is the learning.

1. "You just told me our users usually already have a name in mind from a tip or a headline before they even open the app, so why does your very first recommendation bury the search bar?"
2. "What does 'gamify exploration' actually look like on screen? Is there a streak for sectors browsed? Isn't a streak still a streak whether you point it at buying or at browsing?"
3. "We already show a health score in the Scorecard today. What's different, legally, about showing it one tap earlier?"
4. "If I told my growth team to move this number this week, what's the fastest thing they'd change on the card, and would you be okay with what they'd change?"
5. "We already have an AI Copilot that can answer 'what auto stocks look interesting'. Why hand-curated static rails instead of a personalised version of what we've shipped?"
6. "How is a theme rail different from a screener I've seen in five other apps, just with the filters picked for me?"
7. "Walk me through a user who explores every rail, compares three stocks, and never opens a Scorecard. How is that different from the analysis paralysis they showed up with?"

All seven were addressed in a revision pass before submission. The open question is whether they were the *right* seven.

## The hiring-signal read to test

Claimed: this is a **case_study/presentation hybrid** testing (a) whether the candidate can say no to information — three of the six posed questions are about what to show, hide, and keep simple, and the word "intentionally" was read as the tell; (b) concision as a scored signal, since the brief restates it four times; (c) regulatory-constraint literacy as the cheapest differentiator nobody else would use.

**If the discussion barely touches progressive disclosure or the SEBI ceiling, that read was wrong** — and it drove the whole structure.

## Assumptions that were load-bearing and unverified

- **The Loom beta was never watched** (no video capability; user chose to proceed without). Every "current StockFox" claim is marketing-site inference. Confidence that no Explore-style surface already exists: **0.4** — below a coin flip, by the run's own accounting, and it underpinned the top recommendation. If the beta already had discovery, the submission proposed something built.
- Rails clear the SEBI line without constituting a recommendation: **0.4**, and the 2024 RA amendments broadened what counts.
- A pre-click card holds ~4–5 data points before tipping from inviting to intimidating: rests on Miller/Cowan working-memory literature never tested on financial cards. Q2 research explicitly refused to invent a precise threshold, which is defensible but leaves the number arguable.

## Process notes worth carrying

- Q2 research died twice on API errors before completing. Re-running a single failed question in isolation worked; the plan's parallel independence is what made that cheap.
- The critique pass caught three high-severity internal contradictions the build pass did not see, including one — a composite score banned pre-click while the Scorecard shows one post-click — that a founder who knows their own product would catch in seconds. Fresh-context critique earned its keep here.
- **This run predates the 8-stage pipeline.** There was no `decision-builder`: options were never formally generated or eliminated, and `tradeoffs.md` was written after the decision as justification. That specific observation is what motivated Roadmap Phase 1.
