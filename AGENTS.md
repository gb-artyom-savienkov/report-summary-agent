# Report agent entrypoint

For any Guardians sprint report request, read `.cursor/skills/guardians-sprint-report/SKILL.md` and its linked `SYSTEM_PROMPT.md`. Use the requested sprint number; never select the current sprint implicitly. Run `inspect_sources.py` first and use its manifest and draft instead of parsing the full source files into model context. If preflight reports a changed source structure, fix the extractor and rerun it before rendering. Keep reusable decisions and workflow changes in the skill, scripts, and README so the next run needs no chat history.
