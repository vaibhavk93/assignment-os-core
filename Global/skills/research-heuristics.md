# Research Heuristics — Skill Reference

How to plan, execute, and evaluate research efficiently for interview assignments.

---

## Source Priority Hierarchy

Use sources in this order (highest to lowest reliability):

1. **Official company sources** — investor relations, annual reports, press releases, official blog
2. **Regulatory filings** — SEBI, SEC, MCA filings (public companies)
3. **Reputable press** — Economic Times, Mint, Bloomberg, TechCrunch, Entrackr (India), The Information
4. **Industry reports** — Redseer, KPMG, BCG, McKinsey, Bernstein (use for market sizing)
5. **App store reviews** — Google Play / App Store (user sentiment, specific pain points)
6. **Social media / Reddit / Twitter** — user conversations, complaints, feature requests
7. **Product screenshots / media** — visual analysis (from MEDIA_REGISTRY if available)
8. **LinkedIn** — hiring signals, team structure, recent priorities
9. **SimilarWeb / App Annie / Sensor Tower** — traffic, download trends
10. **Your own analysis / inference** — mark as assumption with confidence score

**Never use:** Random blogs, Medium posts without attribution, outdated data (>2 years for dynamic fields).

---

## Question Decomposition Method

Break any research question into sub-questions using this structure:

```
Main question: "Why is Ixigo's retention lower than MakeMyTrip?"

Sub-questions:
  1. What are Ixigo's and MMT's D30 retention rates? (quantitative)
  2. What do user reviews say about reasons for churning? (qualitative)
  3. What is different about MMT's product experience vs Ixigo? (comparative)
  4. What retention-driving features does MMT have that Ixigo lacks? (feature analysis)
  5. Are there market/demographic differences that explain retention gap? (contextual)
```

**Each sub-question should:**
- Be independently researchable
- Have a clear "done" state
- Map to a specific source type

---

## Effort Level Guidelines

**Simple** (1 agent, 3-10 searches):
- Single fact lookup (company founding year, revenue figures)
- Pricing check
- App store rating
- Executive biography

**Comparison** (2-4 searches per side):
- Feature comparison between 2-3 products
- Market share across 3-5 players
- User review sentiment comparison

**Complex** (10+ searches, multiple angles):
- Full competitive landscape analysis
- User behavior root cause analysis
- Market sizing with bottoms-up + top-down validation
- Growth lever analysis requiring multiple data sources

---

## Confidence Scoring

Rate confidence on every finding:

| Score | Definition |
|---|---|
| 0.9 - 1.0 | Direct quote from official source; recent (< 6 months) |
| 0.7 - 0.89 | Strong secondary source; slightly older or inferred from credible data |
| 0.5 - 0.69 | Indirectly inferred; multiple hops from primary source; aggregated from user reviews |
| 0.3 - 0.49 | Significant inference; limited evidence; anecdotal |
| < 0.3 | Assumption; no supporting evidence found |

**Label all findings below 0.5 explicitly as "Assumption" in output.**

---

## When to Stop Researching

Stop when any of these are true:
- Success criteria for the question is met (defined in research_plan.md)
- You've hit the effort budget (simple: 10 searches, complex: 30 searches)
- Marginal searches are returning duplicate information
- The remaining gap is better served by assumptions + caveats than more research

**Never stop because you're unsure — note the gap and flag confidence as low.**

---

## Media First Rule

Before searching the web for UI/UX information:
1. Check `MEDIA_REGISTRY.json` for relevant screenshots
2. Read `.meta.json` for existing analysis
3. If `analysis_confidence == "high"` → use `analysis_summary` directly (no tokens burned on image)
4. Only fetch and analyze the actual image if the question requires visual detail not in summary

---

## Avoiding Duplicate Research

Each research subagent owns a specific topic. Before starting a search:
- Check your assigned question's topic boundary in `workspace/research_plan.md`
- Check `workspace/context.md` — the context builder may have already found this fact
- If the fact is already in context.md with `confidence > 0.7` → reuse it; don't re-search

---

## Common Research Patterns by Assignment Type

### Product teardown
- What to research: App store reviews (last 3 months), Glassdoor, Twitter/Reddit complaints, SimilarWeb traffic trends, Play Store description + screenshots, competitor apps

### Growth strategy  
- What to research: User acquisition channels (SimilarWeb), retention signals (review sentiment), competitor growth moves, market size data, unit economics signals

### Metrics diagnosis
- What to research: Industry benchmarks for the metric, known factors that affect it, competitor positioning, user complaints that could explain the drop

### Market research
- What to research: TAM data (industry reports), key players + positioning, regulatory environment, consumer behavior data, whitespace analysis

---

## Freshness Rules for Company Research

| Data type | Max acceptable age |
|---|---|
| Revenue / funding | 6 months (quarterly filings preferred) |
| Product features | 2 weeks (apps update constantly) |
| Leadership team | 1 month |
| Market share | 1 year (industry reports) |
| User reviews | Always fresh — get last 90 days |
| Pricing | 2 weeks |
| Competitors | 1 month |
