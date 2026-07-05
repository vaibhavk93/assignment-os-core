# WORKSPACE: Ixigo — International Booking Experience
_Auto-generated. Do not edit manually._
_Last updated: 2026-07-05_

---

## Pipeline Status

| Stage | Status | File |
|---|---|---|
| Intake | ✅ complete | workspace/intake.md |
| Hiring Signal | ✅ complete | workspace/hiring_signal.md |
| Intent | ✅ complete | workspace/intent.md |
| Classifier | ✅ complete | workspace/classifier.md |
| Context Builder | ⏳ pending | workspace/context.md |
| Research Planner | ⏳ pending | workspace/research_plan.md |
| Research Executor | ⏳ pending | workspace/research_q*.md |
| Insight Synthesizer | ⏳ pending | workspace/synthesis.md |
| Case Builder | ⏳ pending | draft.json |
| Devil's Advocate | ⏳ pending | workspace/devils_advocate.md |
| Strict Checker | ⏳ pending | workspace/check_report.json |
| Formatter | ⏳ pending | OUTPUTS/ |
| Visual QA | ⏳ pending | OUTPUTS/ |

_exec_review: SKIPPED (no JD provided)_

---

## [Section: Intake]

Assignment type: `case_study` (PRD-heavy variant)
Core task: Design AI-First, AI-Native international travel experience for ixigo
Constraint: Solution must NOT be plain vanilla AI chatbot

---

## [Section: Hiring Signal]

**Primary signal:** Can this PM design a genuinely AI-native product experience — not a feature add — that tells a coherent end-to-end story for Indian international travelers, and back it with a credible business case?

**Top evaluation areas:** AI-native thinking (PRIMARY), End-to-end systems thinking (PRIMARY), Indian customer depth (PRIMARY), Business judgment (PRIMARY), Metrics fluency (PRIMARY)

**Red flags:** Plain chatbot solution, feature list without priority, ignoring Indian-specific friction, weak metrics

---

## [Section: Intent]

**The real question:** What is the AI-native product architecture that makes international travel on ixigo feel as effortless as booking a domestic train ticket — and is this the right bet for ixigo to make right now?

**9 success criteria defined** — see workspace/intent.md for full testable checklist

**Output format assumption:** PPTX (10-15 slides) + DOCX appendix

---

## [Section: Classifier]

**Template:** `case_study`
**Skipped:** exec_review
**Running:** context_builder → research_planner → research_executor(×5-7) → insight_synthesizer → case_builder → devils_advocate → strict_checker → formatter → visual_qa
