# Assignment Type Templates — Skill Reference

10 pipeline templates. Classifier picks one, then sets skip[] and emphasis{} based on assignment specifics.

---

## Template 1: `prd`

**Product Requirements Document**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → exec_review → formatter
```

Key emphasis for case_builder:
- Lead with success metrics (quantified)
- Include: requirements, edge cases, API/integration considerations, rollout plan, risks
- Separate must-haves from nice-to-haves explicitly
- Engineering effort awareness required

Skip conditions:
- `devil_advocate`: skip if assignment is internal/low-stakes PRD exercise
- `exec_review`: skip if interviewer is IC-level, not executive

Success criteria checklist:
- [ ] Clear problem statement
- [ ] Measurable success metrics defined
- [ ] User stories / requirements listed
- [ ] Edge cases addressed
- [ ] Rollout / phasing plan
- [ ] Risks and mitigations
- [ ] Open questions flagged

---

## Template 2: `product_teardown`

**Product Critique / Teardown**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → exec_review → formatter
```

Key emphasis for case_builder:
- Lead with overall verdict (opinionated, not hedged)
- Structure: what works, what doesn't, top 3 recommendations
- Include UX analysis — flows, friction points, aha moments
- Include business model understanding
- End with prioritized recommendations, not a wishlist

Skip conditions:
- `exec_review`: skip if feedback is from IC-level interviewer

Success criteria checklist:
- [ ] Clear overall verdict stated
- [ ] UX + business model both analyzed
- [ ] Specific evidence cited for critiques (not vague)
- [ ] Prioritized recommendations (not a flat list)
- [ ] Competitor comparison where relevant
- [ ] Recommendations connected to user outcomes

---

## Template 3: `growth_strategy`

**Growth Strategy / Growth Plan**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → exec_review → formatter
```

Key emphasis for case_builder:
- Diagnose current state first (where is growth leaking in AARRR?)
- Identify highest-leverage lever with supporting evidence
- Propose experiments, not just initiatives
- Include north star metric and how strategy moves it
- Business model + unit economics awareness

Skip conditions:
- None — all stages run for growth strategy

Success criteria checklist:
- [ ] Current state diagnosis with data/evidence
- [ ] Highest-leverage growth lever identified
- [ ] Experiments proposed (not just features)
- [ ] North star metric defined
- [ ] Prioritization of initiatives with rationale
- [ ] Timeline / phasing realistic

---

## Template 4: `metrics_analytics`

**Metrics Diagnosis / Analytics Case**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → formatter
```

Key emphasis for case_builder:
- Start with a metrics tree (break down the primary metric)
- List hypotheses for the problem (prioritized by likelihood)
- For each hypothesis: what data would confirm/reject it
- Recommend what to instrument / what to look at next
- Propose experiment if root cause identified

Skip conditions:
- `exec_review`: typically skip for analytics assignments

Success criteria checklist:
- [ ] Metrics tree / decomposition of primary metric
- [ ] Hypotheses listed and ranked by likelihood
- [ ] Data sources identified per hypothesis
- [ ] Root cause recommendation (even if hedged with confidence)
- [ ] Instrumentation / data gap identified
- [ ] Next steps clearly defined

---

## Template 5: `case_study`

**Strategic Case Study**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → exec_review → formatter
```

Key emphasis for case_builder:
- Use a clear framework (MECE structure)
- Situation → Complication → Resolution → Recommendation
- Acknowledge tradeoffs explicitly
- Business impact of recommendation quantified

Skip conditions:
- None — full pipeline for case studies

Success criteria checklist:
- [ ] Clear framework applied (MECE)
- [ ] Problem diagnosis supported by evidence
- [ ] Options evaluated (not just one path)
- [ ] Clear recommendation with rationale
- [ ] Tradeoffs acknowledged
- [ ] Business impact quantified (even roughly)

---

## Template 6: `market_research`

**Market Research / Competitive Analysis**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → checker → formatter
```

Key emphasis for case_builder:
- Market sizing (TAM/SAM/SOM)
- Competitive landscape (differentiated view, not just feature list)
- Target segment clearly defined
- Strategic implication of research

Skip conditions:
- `devil_advocate`: skip for pure research assignments (no recommendation to challenge)
- `exec_review`: skip for IC-level assignments

Success criteria checklist:
- [ ] Market size estimated with methodology
- [ ] Competitive landscape structured (not flat list)
- [ ] Clear differentiation identified
- [ ] Target segment defined
- [ ] Strategic implication or recommendation

---

## Template 7: `technical_architecture`

**Technical / System Design**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → formatter
```

Key emphasis for case_builder:
- Define scope and constraints first
- Identify key components and their interactions
- Address scalability, reliability, cost
- Document key tradeoffs explicitly
- PM should show cross-functional awareness, not just functional spec

Skip conditions:
- `exec_review`: skip unless audience is executive

Success criteria checklist:
- [ ] Scope and constraints defined
- [ ] Key components identified
- [ ] Tradeoffs documented
- [ ] Scalability considerations
- [ ] Implementation phasing

---

## Template 8: `exec_memo`

**Executive Memo / Business Case**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → checker → exec_review → formatter
```

Key emphasis for case_builder:
- Lead with recommendation (pyramid principle)
- Maximum conciseness — executive time is scarce
- Clear ask / decision required from reader
- Business impact first, implementation details last

Skip conditions:
- `devil_advocate`: skip — too much time for a brief format

Success criteria checklist:
- [ ] Recommendation stated in first paragraph
- [ ] Business impact quantified
- [ ] Clear ask / decision required
- [ ] Supporting logic MECE
- [ ] Length appropriate (typically 1-2 pages)

---

## Template 9: `pricing_strategy`

**Pricing Strategy**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → exec_review → formatter
```

Key emphasis for case_builder:
- Value metric identification (what drives value for customers)
- Competitive pricing landscape
- Willingness-to-pay estimation
- Pricing model recommendation with tiers
- Revenue impact modeling

Skip conditions:
- None — full pipeline for pricing

Success criteria checklist:
- [ ] Value metric clearly identified
- [ ] Competitive pricing analyzed
- [ ] Customer segments and WTP estimated
- [ ] Pricing model recommended with rationale
- [ ] Revenue impact modeled
- [ ] Implementation risk acknowledged

---

## Template 10: `presentation`

**Presentation / Slides Assignment**

Base pipeline:
```
intake → hiring_signal → intent → classifier → context → research_planner → research → 
synthesis → case_builder → devil_advocate → checker → formatter
```

Key emphasis for case_builder:
- Narrative-first — what is the story arc?
- Each slide has one clear message
- Pyramid principle structure
- Speaker notes required
- Slide count constraint strictly observed

Skip conditions:
- `exec_review`: skip unless presentation is to C-suite

Success criteria checklist:
- [ ] Clear narrative arc
- [ ] One message per slide
- [ ] Slide count within constraint
- [ ] Speaker notes present
- [ ] Visual hierarchy clear (not text-heavy)
- [ ] Strong opening and closing

---

## Adding New Templates

To add a new agent type (e.g., UX Research):
1. Define agent contract in `Documents/AGENT_CONTRACTS.md`
2. Create `.claude/agents/<agent-name>.md`
3. Add agent to relevant template(s) in this file
4. Classifier can now include it in `base_pipeline[]` for matched assignments
