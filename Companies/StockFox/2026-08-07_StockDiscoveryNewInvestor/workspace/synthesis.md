# Synthesis

## Breaking down the stall

A first-time investor who wants to invest but has no first candidate in mind stalls at three separate points. Together they cover the funnel from "I want to invest" to "I click a stock":

1. **No entry point.** 5,000+ listed names, no query to start from. A search-first product assumes a candidate already exists. This user doesn't have one.
2. **Can't parse what they find.** Once a name surfaces, from a tip, a headline, a friend, the metrics thrown at them exceed what a first glance can hold.
3. **Don't trust it enough to click.** Miscalibrated confidence and fear of repeating a bad-tip mistake stall the decision even after a candidate is legible.

Test: can a finding sit in two parts? Q1's herding/FOMO evidence is entirely part 3. A herding investor already has candidates, chosen badly, not zero candidates. Q2's chunk-limit evidence is entirely part 2, silent on which stock, only on how much a card can say. No overlap found.

Is there a driver with no home? Asset-class confusion (stocks vs. mutual funds) is a plausible fourth stall point, but nothing in this research pass evidences it. Left out rather than invented. Capital/affordability isn't evidenced either, and the brief assumes the user wants to invest. The three-part split holds.

Q3 and Q4 sit outside this decomposition on purpose. Neither describes a reason users stall. Q3 evidences what a metered funnel should measure; Q4 evidences what an engagement mechanic does to trading behavior. Both matter downstream, in the metrics and gamification decisions, but forcing them into the stall-split would blur what they actually prove.

## Insights (each → Q_id)

- **Q1 + context_4:** Choice-overload evidence (Iyengar/Huberman/Jiang, 401(k) enrollment) and bias evidence (overconfidence, disposition, herding) describe different failure points. One is about whether to engage at all, the other about miscalibration after engaging. Fewer visible options helps part 1. Nothing here says fewer options helps part 3. A harm guardrail belongs to part 3, not part 1.
- **Q2:** No study tests an exact pre-click item count for novice investors, a real gap after 9 searches. The ~4–7 chunk figure (Miller/Cowan) is a bridge from general cognitive psychology, not a tested number for stock cards. The resulting card-density call is a labelled assumption, not a finding.
- **Q4:** The same two mechanics that measurably lift engagement (FCA: push notifications, points/prize draws) measurably lift risky-product trade share in the same population. Not "gamification is bad." A paired, quantified trade: benefit and harm come from the identical feature. That pairing is what makes a costed decision possible instead of a vague caution.
- **Q3:** The strongest conversion-predicting behavior in comparable metered products is multi-session breadth, not raw action count. Argues for metering the expensive, high-intent action (Scorecard open) and leaving exploration itself unmetered.
- **context_3:** Whether a disclosed, objectively-sorted list counts as a "recommendation" under SEBI's broadened Research Analyst definition is explicitly unresolved in the research, not found at any primary source checked. The single highest-stakes open question in the deck, carried as an assumption, not asserted as settled.

## Contradiction flagged
Q1's SEBI F&O data (93% of individual traders lost money) is derivatives-specific, not cash-equity stock-picking. Used only as directional evidence that inexperience correlates with worse outcomes, never as a stock-picking loss-rate statistic.

## Weak coverage
Beginner first-person voice (context_1) is the thinnest evidence in the base: one weak-confidence forum quote, the rest convergent pattern, no direct Reddit access this session. Not load-bearing anywhere in the design. Left out of the deck rather than cited as if solid.
