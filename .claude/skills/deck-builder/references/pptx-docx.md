# PPTX / DOCX Rendering Reference

Read only when the selected output format is `pptx` or `docx`. Structure rules (Pyramid, core/appendix, brand colors) live in the parent `SKILL.md` and still apply.

## Default palette (only if brand search fails)
Primary `#1A1A2E` (navy) · Secondary `#16213E` · Accent `#0F3460` · Text `#2C2C2C` · Background `#F8F9FA` · Muted `#6C757D`.
Fonts: Calibri or Inter — 24pt title / 18pt section header / 12pt body / 10pt footnote.

## PPTX slide templates
- **Title:** full-bleed primary color, white text, title 28pt bold centered, subtitle 16pt.
- **Executive Summary:** white bg, title = recommendation statement, 3-column Problem|Recommendation|Impact, bottom metric callout.
- **Section Header:** light gray bg, 36pt bold title, 18pt muted subtitle, no bullets.
- **Analysis:** slide title = argument (18pt bold), one of chart/table/bullets (not all three), source footnote bottom-left 9pt.
- **Recommendation:** accent strip top 15%, numbered title, ≤4 bullets, impact in bold accent color.
- **Appendix:** white bg, "Appendix" label, dense formatting acceptable.

## DOCX structure
Title 24pt bold centered → Subtitle 14pt muted → Section headings 16pt bold (arguments, not labels) → Sub-headings 13pt → Body 11pt/1.15 spacing → Bullets 2-level max → Tables alternating row shading → Callout boxes light-blue border/bg for key insights. A4/Letter, 1" margins, page numbers bottom-center.

## Slide count guidance (respect explicit constraints from INPUT.md first)
Exec summary 1 · Product teardown 8–12 · Growth strategy 10–15 · PRD 8–12 · Case study 8–12 · Market research 10–15 · Metrics diagnosis 6–10 · Exec memo 1–3.

## File naming
`OUTPUTS/<Company>_<AssignmentType>_<YYYY-MM-DD>.<ext>` — appendix as `_Appendix_` suffix for PPTX (HTML keeps appendix as a slide group in the same file).

## Placeholder rule
Never leave `[Company Name]`, `[INSERT]`, `[TBD]`, empty text boxes, or lorem ipsum. Grep before completing; report any match as a blocking QA issue.
