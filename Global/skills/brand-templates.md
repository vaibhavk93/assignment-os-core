# Brand Templates — Skill Reference

Visual and formatting guidelines for output generation. Applied by Formatter agent.

---

## Default Professional Template

Use when no company-specific template is provided.

### Colors
- **Primary:** #1A1A2E (deep navy) — headings, titles, strong emphasis
- **Secondary:** #16213E (dark blue) — subheadings, borders
- **Accent:** #0F3460 (medium blue) — chart bars, callout boxes, highlighted data
- **Text:** #2C2C2C (near-black) — body text
- **Light background:** #F8F9FA (off-white) — slide backgrounds
- **Muted:** #6C757D (gray) — footnotes, labels, secondary text

### Fonts
- **Headings:** Calibri or Inter — 24pt slide title, 18pt section header
- **Body:** Calibri or Inter — 12pt body, 10pt footnotes
- **Data labels:** Same family, 9pt minimum

### Slide Layout
- **Title area:** Top 20% of slide — slide title (argument, not topic)
- **Content area:** Middle 70% — evidence, charts, bullets
- **Footer area:** Bottom 10% — slide number, date, confidentiality if needed
- **Margins:** 0.5 inch on all sides

---

## PPTX Slide Templates (by slide type)

### Title / Cover Slide
- Full background color (primary navy)
- White text
- Company logo placeholder (top right)
- Assignment title: 28pt, bold, centered
- Subtitle (company / date): 16pt, centered
- No bullets, no data

### Executive Summary Slide
- White background
- Title: recommendation statement (not "Executive Summary")
- 3-column layout: Problem | Recommendation | Impact
- Each column: icon (optional) + 3-4 bullet points
- Bottom strip: key metric callout (large number, bold)

### Section Header Slide
- Light gray background
- Large section title: 36pt, left-aligned, bold
- 1-line subtitle: 18pt, muted color
- No bullets

### Analysis / Content Slide
- White background
- Slide title (argument): 18pt, bold, top
- Content: chart OR table OR bullet list — not all three
- Source footnote: bottom left, 9pt, muted
- Key callout box (optional): right side, colored background, single insight

### Recommendation Slide
- Light accent background strip at top (15% of slide height)
- Recommendation number + title
- Supporting bullets (max 4)
- Expected impact: bold, accent color

### Appendix Slides
- White background
- "Appendix" watermark or label
- Dense formatting acceptable here

---

## DOCX Document Template

### Structure
- Title: 24pt, bold, centered
- Subtitle: 14pt, muted, centered
- Section headings: 16pt, bold, left — these ARE the arguments (Pyramid principle)
- Sub-headings: 13pt, bold, left
- Body: 11pt, 1.15 line spacing
- Bullets: 11pt, 2-level max depth
- Tables: alternating row shading (light gray + white)
- Callout boxes: light blue border, light blue background — for key insights

### Page setup
- A4 or Letter — 1-inch margins all sides
- Page numbers: bottom center
- Header: document title (shortened), right-aligned

---

## Placeholder Rules

**Never leave these in output:**
- [Company Name], [INSERT], [ADD DATA HERE], [TBD], [PLACEHOLDER]
- Empty text boxes (even if they render as invisible)
- Lorem ipsum or any placeholder text

**Check before completing:** Grep all text content for the above patterns. If found → report as blocking QA issue.

---

## Slide Count Guidelines

| Assignment type | Typical slide count |
|---|---|
| Executive summary | 1 |
| Product teardown | 8-12 |
| Growth strategy | 10-15 |
| PRD (slides) | 8-12 |
| Case study | 8-12 |
| Market research | 10-15 |
| Metrics diagnosis | 6-10 |
| Exec memo | 1-3 |

Always respect explicit slide count constraint from INPUT.md if specified.

---

## HTML Output Template (reveal.js)

Use when format = `html` at /output-select.

### Stack
- **Framework:** reveal.js (CDN — no build step needed)
- **Theme:** custom CSS using brand colors above
- **Fonts:** Google Fonts — Inter (headings) + Inter (body)
- **Transitions:** `slide` for sections, `fade` for content within slides
- **Speaker notes:** included via reveal.js notes plugin

### HTML file structure
```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js/dist/reveal.css">
  <!-- custom theme inline — use brand colors -->
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <!-- Core slides -->
      <section>...</section>
      <!-- Appendix (separate section group) -->
      <section data-separator-notes="^Notes:">
        <section>Appendix</section>
        <section>A1: Supporting Data</section>
      </section>
    </div>
  </div>
</body>
</html>
```

### HTML-specific layout rules
- One `<section>` per slide — same one-message-per-slide rule applies
- Appendix slides grouped under a parent `<section>` marked with `data-state="appendix"`
- Speaker notes inside `<aside class="notes">` blocks
- Charts: use Chart.js inline (CDN) — no external data files
- Output: single self-contained `.html` file — no dependencies except CDN

---

## File Naming Conventions

```
OUTPUTS/
  <Company>_<AssignmentType>_<YYYY-MM-DD>.pptx       ← if PPTX selected
  <Company>_<AssignmentType>_<YYYY-MM-DD>.html        ← if HTML selected (self-contained)
  <Company>_<AssignmentType>_<YYYY-MM-DD>.docx        ← if DOCX selected
  <Company>_<AssignmentType>_Appendix_<YYYY-MM-DD>.pptx  ← appendix (PPTX path)
  <Company>_<AssignmentType>_Appendix_<YYYY-MM-DD>.html  ← appendix (HTML path, same file via reveal.js section)
```

**HTML note:** Core + Appendix can be one `.html` file (appendix as a separate slide group navigable from main deck). PPTX splits into two files.

---

## Visual QA Checklist (for Formatter self-check before handing to Visual QA agent)

- [ ] All slides have a title
- [ ] No slide is blank or has only a title
- [ ] No placeholder text anywhere
- [ ] Font sizes consistent across same-type slides
- [ ] Colors match the template
- [ ] Slide numbers sequential
- [ ] File named per convention above
- [ ] Slide count matches constraint (if specified)
