# INPUT

> Immutable record. Written once by `intake-intent` on 2026-08-07. Never overwrite.

## Assignment

**StockFox – Senior Product Manager Assignment.**

Stated objective (verbatim):
> "The objective of this assignment is to understand how you approach product problems, think about users and arrive at product decisions. There is no single right answer. We're far more interested in your thought process, assumptions and product thinking than polished designs."

**Candidate has chosen OPTION 2 (of 2). Option 1 content was not provided.**

Option 2 (verbatim):
> "Option 2 — Stock Discovery for a New Investor. Design a stock discovery experience for someone who wants to invest but doesn't know where to begin. The objective is to make stock discovery simple, exciting and confidence-building. The end goal (JTBD) is that users should naturally feel encouraged to discover companies, click on a stock and explore its StockFox Scorecard."

Questions posed within Option 2 (verbatim):
- How should users discover investment opportunities?
- How do we reduce analysis paralysis?
- How do we make discovery engaging instead of intimidating?
- What information should users see before opening a stock?
- What information should intentionally be hidden until later?
- How can we encourage exploration while keeping the experience simple?

AI usage guidance (verbatim):
> encouraged as a thinking partner, but "your submission should reflect your own product thinking, judgement and decision-making, not AI-generated content copied without meaningful inputs or iteration."

Time expectation (verbatim):
> designed to take ~3–5 hours. "We're not looking for pixel-perfect designs or lengthy documentation."

Next round (verbatim):
> Top shortlisted candidates invited to a final discussion Friday/Saturday to "review your solution together, understand your thought process, discuss trade-offs and answer any questions from both sides."

Closing note (verbatim):
> "we're evaluating how you think—not how much you produce. A simple, well-reasoned solution with clear product thinking is far more valuable than an elaborate presentation."

## Job Description

Not provided.

Only role-level fact available: the assignment is titled "StockFox – Senior Product Manager Assignment." No responsibilities, team structure, reporting line, or requirements list was supplied.

## Interviewer / Hiring Manager

Not provided.

## Target Company

**StockFox.**

Company self-description in the assignment (verbatim):
> "StockFox is building an AI-powered stock analysis platform that helps retail investors make more confident investment decisions by simplifying equity research."

Users, per the assignment (verbatim): retail investors; beginner to intermediate; not finance professionals; "users who find stock analysis overwhelming and lack confidence while making investment decisions."

Goal, per the assignment (verbatim): "simplify stock analysis without compromising on depth or quality."

### Company research supplied with this input (verified from stockfox.pro and press, 2026-08-07)

Supplied by the user as already-completed, high-confidence grounded facts. Recorded verbatim as given.

- Legal entity is DELTA STOCKZ LEARNING PRIVATE LIMITED. Note "LEARNING".
- Site positioning verbatim: "Turn research paralysis into confident decisions by combining AI-guided analysis and expert guidance." Also "faster, high-confidence stock decisions without spending hours in confusion." Education tagline: "Learn Stocks Like It's 2025 (Not 2005)."
- Ideal user, their words: someone who "hate[s] blind tips, value[s] evidence, and want[s] confident, data-driven decisions, faster & effortlessly."
- Existing product surface: Stock Health Scorecard ("200+ Metrics analysed in seconds" across 11 segments); Confidence Journal ("Guided Metric-by-Metric research"); Portfolio Checkup; AI Research Copilot ("Ask anything, get explainable answers"); Forward-Testing Simulator (virtual money); Competitive Lens (peer comparison).
- Heavy learning layer already shipped: bite-sized 4-min/day lessons, interactive quizzes, live expert workshops, community access, leaderboards/rewards, and explicit "confidence score tracking".
- Team background: alumni of Times Internet, Coursera, Harvard Business Review, CA India, CRISIL, Simplilearn, Pearson. Note the EdTech concentration (Coursera, Simplilearn, Pearson).
- HARD REGULATORY CONSTRAINT: the site explicitly states StockFox is "not a SEBI Registered Analyst (SRA) or investment advisor" and directs users to consult registered professionals. Therefore a discovery surface legally cannot make buy recommendations or personalised investment advice.
- Monetisation signal: "Get your first 3 stock analyses FREE—no card needed, instant access." Implies a metered/paywalled analysis model — relevant to what discovery should push users toward.
- No demat account required; research-only positioning, user brings their own broker.

## Competitors to Reference

Named comparable products in the assignment: **Screener, Tickertape, Trendlyne, StockGro, TradingView.**

Competitive threat supplied with this input (fresh, verbatim as given):
> StockGro launched "Stoxo", press-positioned as "India's First Stock Market AI Research Platform That Turns Confusion into Conviction" — near-identical language to StockFox's own positioning. Stoxo is backed by behavioural data from 35M+ StockGro users AND SEBI-registered analysts. StockFox has neither the scale nor the registration. StockGro's cited research claim: "90% of users who start exploring an investment idea on Google and social media lose conviction before acting" (their own figure — attribute, don't treat as independent).

## Output Format Requirements

Any format permitted (verbatim list): PRD, user flows, wireframes, Figma, presentation, Notion, prototype, combination.

Length (verbatim):
> "Please keep your submission concise. We recommend limiting it to the equivalent of 5–10 pages/slides."

## Deadline

Submission within 48–72 hours (verbatim). Start of the window — i.e. the date the assignment was received — was not provided.

Final discussion for shortlisted candidates: Friday/Saturday (verbatim). Exact dates not provided.

Reference fact only: today's date is 2026-08-07, a Friday.

## Constraints

From the assignment text:
- Equivalent of 5–10 pages/slides recommended.
- ~3–5 hours of effort intended.
- "We're not looking for pixel-perfect designs or lengthy documentation."
- AI permitted as a thinking partner; submission must reflect the candidate's own product thinking, judgement and decision-making, not AI-generated content copied without meaningful inputs or iteration.
- Submission within 48–72 hours.
- Stated JTBD endpoint: users click on a stock and explore its StockFox Scorecard.

From the supplied verified research:
- StockFox is not a SEBI Registered Analyst or investment advisor — no buy recommendations, no personalised investment advice.
- Research-only product; no demat account; user brings their own broker.
- Metered access model: first 3 stock analyses free.

## Notes

### Known gap (supplied with input)
> The assignment links a Loom walkthrough of the current StockFox beta: https://www.loom.com/share/fc6b8c36f94641d7a523655688a6b09a — this could NOT be viewed (no video capability). Everything known about the current beta comes from the public marketing site, not the actual beta build. Record this explicitly as an open question / assumption risk, since the beta may differ from marketed features.

### Candidate's own stance (supplied as input, explicitly NOT gospel — to be challenged if evidence doesn't support it)
> The candidate's instinct is to reframe the brief from "stock discovery" to "reducing decision anxiety for first-time investors" — arguing the real question is "how do beginners build conviction?" rather than "how do users search?". They want to avoid rebuilding Tickertape/Screener (trending lists, top gainers, filters, screeners), which they believe most candidates will do. They read the brief's funnel as: Discovery → Curiosity → Open Stock → Read Scorecard → Trust → Repeat → Investment, and believe the core design problem is manufacturing curiosity. They favour behavioural personas over demographic ones, JTBD split into functional/emotional/social, explicit behavioural-psychology grounding (loss aversion, choice overload, analysis paralysis, decision fatigue), 5 product principles, per-feature tradeoff tables, specific AI implementation thinking (RAG, hallucination prevention, citations, latency, cost), and a metrics tree with a north star like "Meaningful Stock Explorations per WAU" plus guardrails including "false confidence".

### Candidate profile (supplied)
> Senior PM, ~6 years experience, currently at Paytm (fintech/payments), IIT Bombay + IIM Indore. Indian market context is native. Positioning style is understated credibility — never oversell.
