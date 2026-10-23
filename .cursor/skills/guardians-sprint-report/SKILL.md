---
name: guardians-sprint-report
description: Generate or revise a Guardians sprint summary DOCX for an explicitly requested sprint from saved Jira sprint HTML, Jira MCP issue details, the sprint PDF, and the branded template.
---

# Guardians sprint report

Read [SYSTEM_PROMPT.md](SYSTEM_PROMPT.md) for source authority, writing, and layout rules. Work from the repository root. Use only the requested sprint's sources; Sprint 122 in `example/` is a style reference.

1. Run `python3 .cursor/skills/guardians-sprint-report/scripts/inspect_sources.py --sprint N`. Read its short output, then `dist/sprint_N/source-manifest.json`; use its generated `report-data.draft.json` for a new sprint or the existing `report-data.json` for a revision. The script checks selected sprint identity, PDF chart anchors, and template shape. It never overwrites existing report data.
2. If preflight says `parser_change_needed`, stop report generation and explain the exact source structure mismatch. Update the relevant parser only after inspecting the changed source, then rerun preflight. If it says `source_gap`, state which export is missing; use a labeled placeholder only for genuinely absent KPI or chart data. Historical Delivered classification requires a matching HTML snapshot or sufficiently complete Jira change history.
3. Discover the available Jira MCP search and issue-detail tools. Make one paginated, field-limited search for the requested sprint's issue keys; fetch individual issues or comments only where they could change the summary or add material release, process, dependency, root-cause, or logic context. Use the HTML snapshot for historical Completed/Removed membership; current Jira status alone cannot reconstruct it. If Jira MCP is unavailable, use the saved HTML and PDF within their limits and disclose missing enrichment.
4. Review the PDF KPI labels and chart visually. Record exact values; mark an axis-only reading with `~`. Complete `report-data.json` from the draft: verified dates, KPIs, four or five concise summary paragraphs, sparse optional comments, and material discrepancies. Do not copy the example sprint's facts.
5. Run `python3 .cursor/skills/guardians-sprint-report/scripts/render_report.py dist/sprint_N/report-data.json`. Render the DOCX to page images with the available document renderer, inspect every page, and correct layout defects. Verify all issue links, Calibri 11 pt single-spaced body cells including Comment, charts, and no blank final page.

The scripts derive paths from this repository, not the current laptop. Dependencies and cross-machine setup are in the root [README.md](../../../README.md). Read the [product glossary](../../../instructions/sprint-summary.md) only when an unfamiliar product acronym needs clarification. Do not paste complete HTML, PDF text, or every Jira comment into model context; use the manifest and targeted queries.
