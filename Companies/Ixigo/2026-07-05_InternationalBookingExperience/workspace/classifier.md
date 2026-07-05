# Classifier Output
_Written by: Classifier_
_Date: 2026-07-05_

---

## Selected Template
**Template:** `case_study`
**Rationale:** Assignment explicitly calls itself a case study; asks for strategic recommendation ("should ixigo prioritize?"), options evaluation, and end-to-end solution narrative — all core case_study template requirements. PRD-level depth is emphasis, not the base template.

## Pipeline Configuration

### Skip List
```json
["exec_review"]
```
Reason: No JD provided and no indication of executive-level interviewer; exec_review adds cost without calibration signal. Devil's Advocate runs — business case question ("should ixigo prioritize?") needs challenging.

### Emphasis Flags
```json
{
  "case_builder": {
    "lead_with": "AI-native product vision (what the paradigm is), not problem restatement",
    "depth": "deep",
    "india_specificity": "mandatory — every solution section must have India-specific angle",
    "avoid": "plain chatbot framing, generic UX improvements without specifics",
    "quantify": true,
    "ai_native_check": "For every AI element proposed, ask: is this a chatbot? If yes, redesign."
  },
  "research_planner": {
    "focus": "India outbound travel market, ixigo product current state, AI in travel globally, competitor gaps (MakeMyTrip, Cleartrip)",
    "max_questions": 7,
    "priority_questions": [
      "What is ixigo's current international travel product gap vs MakeMyTrip?",
      "What are the specific pain points of Indian first-time international travelers?",
      "What does AI-native look like in travel (not chatbot) — Airbnb, Google Travel, Booking.com examples?",
      "What is the India outbound international travel market size and growth?",
      "What are Indian passport holders' top visa anxiety points and corridors?"
    ]
  },
  "insight_synthesizer": {
    "frame_as": "product paradigm shift opportunity, not incremental improvement"
  },
  "formatter": {
    "slide_count_guidance": "12-15 core slides + appendix (separate)",
    "speaker_notes": true,
    "appendix": true
  }
}
```

## Output Format Decision
**Format:** DEFERRED to /output-select — options are PPTX / HTML / DOCX
**Slide count:** Core deck ~12-15 slides (guidance, not constraint) + Appendix deck separate
**Speaker notes:** Required
**Content split:** Core sections (primary argument) + Appendix sections (supporting data, research, alternatives)

## Effective Pipeline (in order)
1. context_builder
2. research_planner
3. research_executor (×5-7 questions in parallel)
4. insight_synthesizer
5. case_builder
6. devils_advocate
7. strict_checker
8. formatter
9. visual_qa
