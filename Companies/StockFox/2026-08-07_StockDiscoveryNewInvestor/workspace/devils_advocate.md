# Devil's Advocate Report

Overall: this is a genuinely thought-through case. The assumptions register is unusually honest about its own weak points, and the gamification and metering tradeoffs show real judgment. It is not a "no major holes" outcome, though: it has at least three internal-consistency problems, visible in its own text, that a founder who knows StockFox's shipped product will catch quickly and not as hypotheticals.

## Challenges to Recommendation

### Challenge 1
- **Issue:** The stall diagnosis (no entry point → can't parse → don't trust) uses "no entry point" to justify the single highest-ranked recommendation: browse-first Explore, search demoted to secondary. But part 2 of the same diagnosis ("can't parse what they find") describes the stock name as surfacing "from a tip, a headline, a friend", conceding that a real share of first-time users already arrive holding a specific name from outside the app. That is search-first behaviour, not blank-slate browsing. No segmentation is offered between the two, and nothing states what a tip-driven user gives up when the fast path to a name they already have is demoted behind rails and a compare tray they do not need yet.
- **Likely interviewer question:** "You just told me our users usually already have a name in mind from a tip or a headline before they even open the app, so why does your very first recommendation bury the search bar?"
- **Severity:** high
- **Suggested fix:** Name two sub-cases explicitly, blank-slate browser vs. tip-driven searcher with an unparsed name, and give search equal visual weight for the second instead of uniformly demoting it. If there is no basis for which segment is bigger, say that out loud rather than defaulting to browse-first.

### Challenge 2
- **Issue:** "Gamify exploration, never trading-adjacent actions" leans on FCA/SEC/Robinhood evidence that specific mechanics (streaks, points, prize draws, leaderboards) measurably raise risky-trade share. None of the four documents name the actual mechanic used for exploration. If sectors-browsed or cards-compared carry a streak, badge, or points, the trigger the regulators flagged has not been removed, only moved one step earlier. Since the product's own loop is browse → Scorecard open → the user's own broker, a habit loop built on browsing can still raise downstream trade frequency with one extra hop. Separately, the evidence base was gathered on apps with in-app trade execution; StockFox is research-only with a broker handoff, so applying that evidence to a browse-only surface is asserted, not demonstrated.
- **Likely interviewer question:** "What does 'gamify exploration' actually look like on screen, is there a streak for sectors browsed? Because if there is, isn't a streak still a streak whether you point it at buying or at browsing?"
- **Severity:** high
- **Suggested fix:** Name the literal mechanic (e.g. a plain, non-rewarded progress indicator, explicitly no streak, points, or push notification) and state in one line why it does not reproduce the habit-loop dynamic FCA measured. If a reward mechanic is genuinely intended, drop the "we don't gamify" framing and argue instead that harm scales with proximity to the trade action, which is narrower and more defensible.

### Challenge 3
- **Issue:** The pre-click card is held to five factual fields with an explicit ban on a composite score, described as "the clearest regulatory lever". But StockFox's own Stock Health Scorecard, named in these documents as an existing shipped surface, already shows a composite score. Nothing here explains why a score is fine one tap later but not before the tap. The rails' sort criterion is separately flagged as a genuinely open regulatory question in the assumptions register, but this specific pre-click/post-click inconsistency is never named or resolved.
- **Likely interviewer question:** "We already show a health score in the Scorecard today, that's a score on a security. What's different, legally, about showing it one tap earlier?"
- **Severity:** high
- **Suggested fix:** Add one sentence distinguishing the two: a bare score with no visible methodology reads as "here's our opinion, act on it", while a score reached after 200+ underlying metrics and caveats are visible is a disclosed analytical output. If that line does not hold up out loud, fall back on the cognitive-load argument the deck already makes separately (novice ceiling) rather than leaning on the regulatory claim as primary justification. If counsel reads the SEBI line more permissively than assumed, the regulatory justification disappears and the deck needs the cognitive-load argument to carry the decision alone.

### Challenge 4
- **Issue:** The metric is tied to Scorecard-open behaviour, the same action the deck's own reasoning calls the expensive, high-intent, metered action. Two problems follow. Incrementality: a raw count or rate of Scorecard opens cannot distinguish a genuinely new open that Explore caused from a user who was always going to open one via a different path, and nothing here describes a baseline or control comparison. Gameability: the fastest way to raise a raw open-rate is a more clickbait card (a score, a "hot pick" badge, bigger numbers), precisely what the card-discipline recommendation argues against. A metric that rewards more taps quietly pressures the design to erode its own progressive-disclosure call over time, and the one named guardrail (confidence inflation) does not check for that failure mode.
- **Likely interviewer question:** "If I told my growth team to move this number this week, what's the fastest thing they'd change on the card, and would you be okay with what they'd change?"
- **Severity:** medium
- **Suggested fix:** Frame the primary metric as a lift (Explore-sourced Scorecard opens vs. a search-only baseline), not a raw count, and add a design-integrity guardrail such as the percentage of card taps that bounce off the Scorecard within a few seconds, to catch a card that starts optimising for taps over informed taps.

### Challenge 5
- **Issue:** The assumptions register rates "no Explore-style discovery surface exists yet" at 0.4 confidence, below a coin flip by the candidate's own accounting, and it underpins the entire premise of the top-ranked recommendation. That is disclosed, with a stated fallback ("this becomes a v2 critique"), which is reasonable. What is not addressed anywhere is the closer, more likely overlap: StockFox already ships an AI Research Copilot, a natural-language surface for exactly the "what should I look at" question Explore answers with static theme rails. Of six named existing surfaces, the design explicitly integrates with only two (Scorecard, Confidence Journal) plus the learning layer. Copilot, Portfolio Checkup, Forward-Testing Simulator and Competitive Lens go unmentioned, and Copilot is the one most likely to prompt "why build this instead of using what we already have".
- **Likely interviewer question:** "We already have an AI Copilot that can answer 'what auto stocks look interesting', why do we need hand-curated static rails instead of a personalised version of what we've already shipped?"
- **Severity:** medium
- **Suggested fix:** Add one line distinguishing Explore from Copilot: Copilot answers a query the user already knows how to ask, Explore is for the user who does not yet have a query to type, which is exactly this brief's population. State it, do not leave it implicit.

### Challenge 6
- **Issue:** intent.md itself names "build a screener" as the most common wrong answer to this brief. Theme rails (a curated set sorted by an objective criterion) plus a compare tray (side-by-side metrics for a shortlist) are, mechanically, a saved-filter screener rendered as shelves instead of a table, plus a screener's compare feature. There is a reasonable rebuttal, that a screener requires the user to already know what to filter by and rails do not, but that sentence does not appear anywhere in these four documents. The distinction currently lives only in the candidate's head.
- **Likely interviewer question:** "How is a theme rail sorted by an objective criterion different from a screener I've already seen in five other apps, just with the filters picked for me instead of by me?"
- **Severity:** medium
- **Suggested fix:** State the rebuttal once, plainly: a screener assumes the user already knows what to filter by, and a zero-candidate first-time investor does not, which is the exact gap rails close.

## Weakest Lens

**User.** It is the shortest of the three, and its one substantive point ("what they give up: a one-glance verdict") is already covered in substance under the Tensions section, so the lens adds little beyond what is said elsewhere. It has no segmentation (one persona, no distinction between a blank-slate browser and a tip-driven searcher, the exact gap Challenge 1 turns on), and no exploration of what happens to a user who browses every rail and never clicks. That failure mode is costed only from the business side ("all cost, zero funnel progress"), never asked from the user's side.

**Question that exposes it:** "Walk me through what a real user who explores every rail, compares three stocks in the tray, and never opens a Scorecard actually experiences. How is that different from the analysis paralysis they showed up with?"

## Missing Tradeoffs

- **Content-ops cost, never priced.** The Product lens names keeping 4-5 theme rails current with defensible sort criteria as "the real build risk", but no tension row states what is traded away to fund it: whose ongoing time, or what a stale rail looks like between refresh cycles.
- **Compare tray held to a looser standard than the card.** The single card is disciplined to five factual fields with no ranking. The compare tray, arguably the most naturally rankable UI in the design since a 2-3 item table invites highlighting a winner, is never explicitly subjected to the same rule. This is the likeliest place a ranked recommendation re-enters through the back door.
- **Unmetered infinite browsing vs. re-creating the stall being solved.** Costed once, from the business side. Never costed from the user side: does a judgment-free, infinitely browsable space let an anxious user avoid the click indefinitely rather than build toward it?
- **Metering evidence basis** (comparable-product pattern, not StockFox's own funnel data) is already flagged as a live-discussion open point in the recommendation text. Good practice, noted here only because it is a real rather than hypothetical live risk.

## Weak Assumptions

- None of the five labelled assumptions exceeds 0.5 confidence. Honest and disclosed, but worth naming as a compounding risk rather than five independent ones: assumptions #1 (no existing discovery surface) and #4 (rails clear the SEBI line) are both the lowest-confidence entries at 0.4 *and* the two with the largest blast radius, since either resolving the wrong way forces a live rebuild of the #1 and #2 ranked recommendations respectively.
- **Assumption #3** (a pre-click card holds ~4-5 data points before it tips from inviting to intimidating) leans on general working-memory literature (Miller 1956, Cowan 2001) never tested on financial data or stock cards. It is the literal number the deck's most-repeated design discipline rests on, and it is worth a ready answer to "why five and not seven".
- **Assumption #5** (the confidence score is a longitudinal, per-user signal) is the sole basis for the one required user-harm guardrail. If it is wrong, nothing here names a second harm guardrail as backup, so the metrics section may end up with zero working harm guardrails rather than a degraded one.

## Counterarguments Not Addressed

- If legal reads the "criteria-based sort" question more permissively than assumed, is "zero score, zero ranking" still the right call, or a stricter-than-required self-imposed ceiling paid for at the cost of the one-glance verdict the user lens already flags as a real loss?
- Does the compare tray follow the same no-ranking discipline as the single card, or can two stocks sit side by side with an implicit winner visible through highlighting or ordering?
- Is unlimited free browsing actually good for a user whose diagnosed problem is stalling, or does a judgment-free space with no prompt to act just make the stall more comfortable?
- Why build a new static surface rather than a more personalised front end on AI Research Copilot, a surface StockFox has already shipped for the same underlying question?

## What Would Make This Stronger

1. **Segment the persona before ranking browse-first over search.** Split "no first candidate in mind" into blank-slate browser vs. tip-driven-but-unparsed searcher, using the deck's own evidence ("a tip, a headline, a friend"), and state what each gives up. The top-ranked recommendation currently optimises for one using language that describes the other.
2. **Name the literal exploration-gamification mechanic and pressure-test it against the same FCA/SEC lens used to reject trading gamification.** The flagship regulatory-judgment recommendation is currently the least mechanically specified, which is exactly where a founder will ask "show me", not "tell me".
3. **Reconcile "no score before the click" with the fact that the Scorecard already shows one after it, in one explicit sentence.** This is the fastest, most checkable inconsistency in the deck for someone who knows their own shipped product, and it is a one-line fix.
