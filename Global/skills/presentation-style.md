# Presentation Style — Skill Reference

How to structure and communicate recommendations for interview assignments. Applies to decks, documents, and memos.

---

## Core Principle: Pyramid Principle (Minto)

**Start with the answer. Support it. Never bury the lede.**

Structure:
```
Recommendation / Key Insight (top)
  ├── Argument 1
  │     ├── Evidence
  │     └── Evidence
  ├── Argument 2
  │     ├── Evidence
  │     └── Evidence
  └── Argument 3
        ├── Evidence
        └── Evidence
```

Never: Data → Analysis → Conclusion (bottom-up). That's a mystery novel, not a business recommendation.

---

## Slide Structure Principles

### One message per slide

Each slide has exactly one takeaway. The slide title IS the takeaway — not a topic label.

**Wrong:** "Market Analysis"  
**Right:** "India OTA market is consolidating — top 3 players control 78% of bookings"

### Slide title as the argument

The reader should be able to read only slide titles and understand the full narrative.

### Evidence supports the title — not the reverse

Data visualizations, bullet points, and tables exist to prove the title claim. If data doesn't support the title, rewrite the title or remove the slide.

---

## Deck Structure — Always Bifurcated

Every output has two parts: **Core** (primary argument) and **Appendix** (reference data). These are always separate — never merged.

### Core Deck (10-12 slides)
```
Slide 1:  Executive Summary (recommendation + key supporting points)
Slide 2:  Problem framing (what is this assignment about, why it matters)
Slide 3:  Context / situation (company, market, current state)
Slide 4-N: Analysis (by sub-topic — insights, competitive context, user research)
Slide N+1: Solution / Recommendation (clear, prioritized)
Slide N+2: Tradeoffs / risks
Slide N+3: Metrics / how we measure success
Slide N+4: Roadmap / next steps (if relevant)
```

### Appendix (separate file/section — no slide limit)
```
A1: Supporting data tables and sources
A2: Research methodology
A3: Alternatives considered (and why rejected)
A4: Detailed user research / quotes
A5: Competitive landscape detail
A6: Assumptions register
```

**Core deck rule:** Every slide must earn its place. If a slide is "useful to have," it goes to appendix.
**Appendix rule:** Dense formatting acceptable. Depth over aesthetics. Reviewers who want to go deep can — those who don't, won't.

### Output Format Decision
Format (PPTX / HTML / DOCX) is decided at `/output-select` HITL gate — never pre-committed by Classifier. Supported formats:
- **PPTX:** Standard PowerPoint — send to company via email
- **HTML (reveal.js):** Browser-viewable, web-uploadable, shareable via link, printable to PDF — preferred for portfolio/reuse
- **DOCX:** Written document format — for memo or written case study deliverables

---

## Executive Summary Slide

Always present the summary first. It should standalone — if the reader only reads this slide, they should understand the recommendation.

Format:
- 1-sentence problem statement
- 1-sentence recommendation
- 3 supporting bullets (key reasons / evidence)
- Expected impact (quantified if possible)

---

## Writing Style for Bullets

**Do:**
- Lead with the insight ("Revenue impact is $X, driven by...")
- Use numbers ("Reduces churn by ~15% based on benchmark data")
- Be specific ("Instagram-style reels" not "new content format")

**Don't:**
- Start with "We should..." (tells, doesn't convince)
- Write multi-line bullets (one idea per bullet)
- Use vague adjectives ("significantly", "very", "much better")
- Stack more than 4-5 bullets per slide

---

## Quantification Guidelines

Always attempt to quantify, even if rough:
- Market size estimates: use TAM/SAM/SOM with stated methodology
- Impact estimates: use benchmarks + logic ("D7 retention +5pp → LTV increases ~20% based on industry data")
- Confidence: state explicitly when estimates are rough ("~$50M TAM, bottom-up estimate")

**An informed estimate > no estimate.** State assumptions. Never leave a blank where a number should be.

---

## Assumption Handling

Every ungrounded claim must be:
1. Labeled as an assumption: "Assuming 10% conversion rate (industry benchmark for..."
2. Listed in an Assumptions slide or appendix
3. Accompanied by a falsifier: "This assumption is wrong if conversion is below 3%"

---

## Document Format (for DOCX / written submissions)

```
Title
Executive Summary (1 paragraph — recommendation + top 3 reasons)
Context (1-2 paragraphs)
Analysis (structured sections, each with a clear heading-as-argument)
Recommendation (clear, numbered if multiple)
Tradeoffs and Risks
Metrics for Success
Appendix
```

Use headers as arguments (same as slide titles). Short paragraphs (3-4 sentences max).

---

## Tone Guidelines

**For consumer / startup companies:** Conversational but precise. Avoid corporate jargon.  
**For fintech / enterprise:** More formal. Risk-aware language. Business case framing.  
**For all:** Confident and direct. No excessive hedging. Own the recommendation.

**Avoid:**
- "I think" / "I believe" (just state it)
- "It could be argued that..." (argue it yourself)
- "In conclusion, therefore..." (unnecessary transitions)
- Passive voice where active is possible

---

## Speaker Notes Format

Every slide that will be presented should have speaker notes:
- First sentence: restates the slide title in different words
- Middle: 2-3 sentences of the supporting narrative
- Last sentence: transition to next slide ("This sets up the question of...")

Keep notes under 100 words per slide.

---

## Common Interview Mistakes to Avoid

- **Too many slides** — quality > quantity; cut anything that doesn't move the narrative
- **No prioritization** — never present a flat list; always rank
- **Generic recommendations** — "improve UX" is not a recommendation
- **No tradeoffs** — every recommendation has tradeoffs; show you know what they are
- **Ending weak** — close with a strong, specific recommendation and clear next step
