# Checker Rubrics — Skill Reference

Quality rubrics for the Strict Checker agent. Per assignment type. Binary Tier 1 gates + graded Tier 2 criteria.

---

## Universal Rules (apply to ALL assignment types)

### Tier 1 — Hard Gates (all must PASS before Tier 2 is evaluated)

Run these deterministically before any LLM-based scoring:

| Check | How to verify | FAIL condition |
|---|---|---|
| Output format present | Check OUTPUTS/ or draft.json format field | Required format missing entirely |
| All sub-questions addressed | Map each Q_id from research_plan to a section in draft.json | Any Q_id with no coverage in any section |
| Quantitative claims cited | For each number in draft.json, check citations[] is non-empty | Number with no citation entry |
| No placeholder text | Grep draft.json content for: TODO, [INSERT], [ADD], lorem, TBD, PLACEHOLDER, XXX | Any match found |
| Assumptions Register present | Check draft.json.assumptions_register is non-empty if any section.is_assumption == true | Ungrounded claims without register entry |
| Hiring signals covered | For each item in workspace/hiring_signal.md core_evaluation_areas[], verify at least one section addresses it | Evaluation area with zero coverage |

### Tier 2 — Graded Criteria (score 0.0-1.0, threshold ≥ 0.8)

For each criterion: reason step by step BEFORE assigning score. Do not score holistically.

**Length-neutral instruction:** A concise response that covers the criterion fully scores equal to or better than a verbose response that covers it partially. Length is not quality.

| Criterion | Scoring guidance |
|---|---|
| Intent alignment | Does the draft answer the exact question in workspace/intent.md, or a related but different question? Score 1.0 = exact; 0.8 = close; <0.6 = misaligned |
| Completeness | Are all success criteria from workspace/intent.md addressed? Count covered vs total; score = covered/total |
| Grounding/faithfulness | Do claims in draft.json match what's in workspace/research_*.md? Sample 5 random claims and verify. Score = verified/sampled |
| Insight quality | Do insights go beyond restating data? Do they have clear implications? Score 1.0 = every insight has implication; 0.8 = most do; <0.6 = mostly data restatement |
| Internal consistency | Do numbers agree across sections? Does the recommendation follow from the analysis? Score 1.0 = fully consistent; 0.5 = minor inconsistencies; 0.0 = contradictions present |

### Tier 3 — Qualitative Notes (advisory only, does not affect PASS/FAIL)

Note any observations on:
- Tone appropriateness for stated audience
- Brand/format conventions followed
- Slide count within stated constraint

---

## Rubric: `prd`

**Additional Tier 1 checks:**
- [ ] Success metrics defined and measurable (not vague)
- [ ] Rollout / phasing plan present
- [ ] At least one risk identified
- [ ] User stories or requirements present

**Additional Tier 2 criteria:**
- Engineering feasibility awareness (0.0-1.0): Does the draft acknowledge implementation complexity?
- Edge case coverage (0.0-1.0): Are non-happy-path scenarios addressed?

**Failure routing guidance:**
- Missing metrics → route to case_builder with: "Add measurable success metrics to section [s_id]"
- Missing rollout → route to case_builder with: "Add phasing plan — what ships in v1 vs later?"
- Missing risks → route to case_builder with: "Add risks section with at least 3 specific risks"

---

## Rubric: `product_teardown`

**Additional Tier 1 checks:**
- [ ] Overall verdict stated explicitly (not implied)
- [ ] At least one specific, actionable recommendation (not generic advice)
- [ ] Evidence cited for each critique (not opinion alone)

**Additional Tier 2 criteria:**
- Opinionatedness (0.0-1.0): Does the draft have a clear, defensible point of view? Or is it excessively hedged?
- Business model awareness (0.0-1.0): Does the analysis connect product decisions to revenue model?

**Failure routing guidance:**
- Vague verdict → route to case_builder with: "State an explicit verdict in executive summary"
- Generic recommendations → route to case_builder with: "Make each recommendation specific and actionable — 'improve onboarding' is not sufficient"
- Opinion without evidence → route to research if evidence gap; route to case_builder if evidence exists but unused

---

## Rubric: `growth_strategy`

**Additional Tier 1 checks:**
- [ ] Current state diagnosis present (not jumping straight to solutions)
- [ ] North star metric or primary metric defined
- [ ] At least one experiment proposed (not just initiatives)
- [ ] Prioritization rationale present (not a flat list)

**Additional Tier 2 criteria:**
- Hypothesis quality (0.0-1.0): Are proposed experiments framed as testable hypotheses?
- Growth lever specificity (0.0-1.0): Is the primary lever specific and evidence-backed, or generic?

**Failure routing guidance:**
- No diagnosis → route to case_builder: "Add current state diagnosis section before recommendations"
- Generic levers → route to research if data is missing; route to case_builder if data exists
- No experiments → route to case_builder: "Convert at least 2 initiatives into testable experiments with hypothesis, metric, and success threshold"

---

## Rubric: `metrics_analytics`

**Additional Tier 1 checks:**
- [ ] Metrics tree / decomposition present
- [ ] At least 3 hypotheses listed and ranked
- [ ] Data sources identified per hypothesis (not just "look at the data")
- [ ] Next steps defined

**Additional Tier 2 criteria:**
- Hypothesis precision (0.0-1.0): Are hypotheses specific and testable, or vague?
- Instrumentation awareness (0.0-1.0): Does the draft identify what data would be needed to validate each hypothesis?

**Failure routing guidance:**
- Missing tree → route to case_builder: "Add a decomposition of the primary metric into its drivers"
- Vague hypotheses → route to case_builder: "Each hypothesis must be testable — 'users are confused' is not a hypothesis; 'users drop off at step 3 because KYC takes >3 minutes' is"

---

## Rubric: `case_study`

**Additional Tier 1 checks:**
- [ ] Framework applied explicitly (MECE, Pyramid, etc.)
- [ ] Options evaluated (not just one path recommended)
- [ ] Tradeoffs acknowledged

**Additional Tier 2 criteria:**
- Framework rigor (0.0-1.0): Is the structure MECE? Are categories clean?
- Business impact quantification (0.0-1.0): Is the impact of the recommendation estimated?

---

## Loop Detection

If `draft.json` content hash matches a prior attempt (within the same checker loop sequence):

**Do not re-score.** Output immediately:
```json
{
  "verdict": "FAIL",
  "routing": {
    "route_to": "hitl",
    "reason": "Draft is near-identical to previous attempt. Auto-correction is not converging.",
    "specific_fix": "Human review required. Best draft + unmet criteria attached."
  }
}
```

---

## Checker Independence Rule

The Strict Checker must:
- Use fresh context (no memory of Case Builder's reasoning process)
- Use a model different from the drafter where possible (Opus when Case Builder used Sonnet)
- Not penalize conciseness — length-neutral scoring always
- Score per criterion before giving overall verdict — never holistic first
