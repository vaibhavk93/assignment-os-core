---
description: HITL gate — choose output format(s) before Formatter runs.
---

1. Ask the user which output format(s) they want: `html` (default, self-contained deck), `pptx`, `docx`, or a combination. Also ask whether to run the optional Executive Reviewer pass (default: no — only worth it if the audience is genuinely executive-level).
2. Write the answer into `state.json.selected_outputs` (and add `exec_review` to a `state.json.optional_stages` array if requested).
3. This gate must run before `formatter` — never let Formatter run with `selected_outputs` empty.
