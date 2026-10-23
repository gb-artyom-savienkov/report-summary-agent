# Guardians sprint report agent

This repository contains a portable Codex skill, source checks, and a DOCX renderer for Guardians sprint reports. Ask an agent **“Generate the Guardians report for Sprint N”** or invoke `$guardians-sprint-report`. The agent instructions live in `.cursor/skills/guardians-sprint-report/`; `AGENTS.md` points other coding agents to the same workflow. No chat history is needed.

## One-time setup on a new laptop

- Open this repository in Codex or another agent that reads `AGENTS.md` and project skills. Use Python 3.11 or newer and install `requirements.txt` in a virtual environment, or use Codex's bundled document Python runtime.
- Install Poppler so `pdftoppm` is on `PATH`. For visual DOCX review, use Codex's document renderer or a local LibreOffice installation.
- Connect a Jira MCP server with read access to `https://glassboxdigital.atlassian.net`, project `GNG`, and the Guardians sprint issues. The provided Atlassian MCP endpoint is `https://mcp.atlassian.com/v1/mcp/authv2`; an app-managed Atlassian connection also works. The source board URL is `https://glassboxdigital.atlassian.net/jira/software/c/projects/GNG/boards/103/reports/sprint-retrospective`. MCP tool names can differ by laptop; the skill discovers them. A saved Jira Sprint Report HTML is still needed to prove close-time section membership unless complete Jira change history is available. The workflow can use saved HTML and PDF without MCP, but must disclose missing issue enrichment.

## Inputs and output for each sprint

Put the current export in `source/sprint_N/R&D Execution and Quality.pdf` and a saved Jira Sprint Report `.html` in `source/sprint_N/`. The HTML filename is arbitrary; its internally selected sprint must be N. The parser reads only the HTML, so browser-created `_files/` asset folders are unnecessary. Keep the branded DOCX in `template/`. `example/` contains the Sprint 122 DOCX for visual style only.

Run from the repository root:

```bash
python3 .cursor/skills/guardians-sprint-report/scripts/inspect_sources.py --sprint N
```

The command prints a short status and writes `dist/sprint_N/source-manifest.json` plus a new `report-data.draft.json` if neither a draft nor a finished data file exists. The small manifest contains sprint metadata, section counts and keys, and source diagnostics; the draft contains the ticket rows. Review KPI labels and chart values, enrich only material issues from Jira, fill the draft's dates, KPIs, summary, and brief optional comments, then save it as `dist/sprint_N/report-data.json`. The draft is intentionally incomplete and will not render until reviewed.

```bash
python3 .cursor/skills/guardians-sprint-report/scripts/render_report.py dist/sprint_N/report-data.json
```

The final file is `dist/sprint_N/Guardians - Sprint N Summary Report.docx`. Render it to images and inspect every page before delivery. The renderer checks historical issue membership, sprint identity, links, template variables, and chart anchors. The report data uses **repository-relative source paths**, so it works on another laptop.

After changing the scripts or template, run `python3 -m unittest discover -s tests -v` and rerun preflight and rendering for a known sprint. The output DOCX is saved only after validation passes.

## Preflight outcomes

- `ready_for_review`: sources fit the parser; an agent still has to verify KPIs, dates, Jira context, and narrative.
- `source_gap`: a matching saved Jira HTML, PDF, or required chart is missing. Supply the export, or use a labeled placeholder only where the report can remain evidence-based. Historical delivery cannot be inferred from current Jira status.
- `parser_change_needed`: a supplied PDF or template changed shape, or a chart has ambiguous or wrong-sprint content. Inspect that source and update the relevant extractor before rendering. The command reports the exact mismatch.

Do not send full HTML, PDF text, or every Jira comment to the model. Use the small manifest, one paginated field-limited Jira search, and targeted issue-detail requests. The renderer reads each local source once per run and rasterizes each PDF source page once.

## Sprint 123 reference

`dist/sprint_123/report-data.json` is a completed example. It uses a saved HTML whose selected sprint is NG Sprint 123, and the Guardians-filtered PDF exported after the sprint. Its approximate `~46` velocity is a chart-axis reading; `52.65%` is the labeled sprint trend point. A PDF section-label mismatch for Bug Backlog is recorded in source diagnostics and is omitted from the report body.
