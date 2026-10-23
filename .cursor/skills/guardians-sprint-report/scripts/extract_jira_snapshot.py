#!/usr/bin/env python3
"""Read a saved Jira sprint report without treating the filename as sprint identity."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from lxml import html


SECTION_NAMES = {
    "Completed Issues": "completed",
    "Issues Not Completed": "not_completed",
    "Issues completed outside of this sprint": "completed_outside",
    "Issues Removed From Sprint": "removed",
}
ROOT = Path(__file__).resolve().parents[4]


def clean(value: str) -> str:
    return " ".join(value.split())


def parse_snapshot(path: Path) -> dict:
    tree = html.parse(str(path))
    selected = tree.xpath('//select[@id="ghx-chart-picker"]/option[@selected]')
    if len(selected) != 1:
        raise ValueError(f"{path}: expected one selected sprint in Jira HTML")
    name = clean(selected[0].text_content())
    match = re.fullmatch(r"NG Sprint (\d+)(?: \(\d{4}\))?", name)
    if not match:
        raise ValueError(f"{path}: unrecognized selected sprint {name!r}")
    sprint_id = selected[0].get("value")
    report = tree.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " ghx-sprint-report-table ")]')
    if len(report) != 1 or report[0].get("data-sprint-id") != sprint_id:
        raise ValueError(f"{path}: selected sprint and report table IDs disagree")
    meta = tree.xpath('//*[@id="ghx-sprint-report-meta"]')
    sections: dict[str, list[dict]] = {v: [] for v in SECTION_NAMES.values()}
    for table in report[0].xpath('./table[@aria-label]'):
        section = SECTION_NAMES.get(table.get("aria-label"))
        if section is None:
            if table.xpath('.//tr[td]'):
                raise ValueError(f"{path}: unknown Jira report section {table.get('aria-label')!r}; update SECTION_NAMES")
            continue
        for row in table.xpath('.//tr[td]'):
            cells = row.xpath('./td')
            if len(cells) < 6:
                raise ValueError(f"{path}: {section} row has {len(cells)} cells, expected at least 6")
            key_cell = clean(cells[0].text_content())
            key_match = re.search(r"\bGNG-\d+\b", key_cell)
            if not key_match:
                raise ValueError(f"{path}: {section} row has no GNG issue key")
            links = cells[0].xpath('.//a/@href')
            if not links or not clean(cells[1].text_content()):
                raise ValueError(f"{path}: {section} row for {key_match.group()} lacks a ticket link or summary")
            sections[section].append({
                "key": key_match.group(),
                "summary": clean(cells[1].text_content()),
                "issue_type": clean(cells[2].text_content()),
                "priority": clean(cells[3].text_content()),
                "snapshot_status": clean(cells[4].text_content()),
                "story_points_display": clean(cells[5].text_content()),
                "added_after_start": "*" in key_cell,
                "url": links[0] if links else None,
            })
    if not any(sections.values()):
        raise ValueError(f"{path}: saved report has no issue rows")
    all_keys = [x["key"] for rows in sections.values() for x in rows]
    if len(all_keys) != len(set(all_keys)):
        raise ValueError(f"{path}: an issue appears in multiple report sections")
    dates = {}
    if meta:
        for span in meta[0].xpath('.//span[@title]'):
            dates[span.get("title")] = clean(span.text_content())
    return {
        "sprint_number": int(match.group(1)),
        "sprint_name": name,
        "sprint_id": sprint_id,
        "snapshot_path": str(path.resolve()),
        "snapshot_start_display": dates.get("Start Date"),
        "snapshot_completion_display": dates.get("Completion Date"),
        "sections": sections,
        "section_counts": {name: len(rows) for name, rows in sections.items()},
    }


def find_snapshot(source_root: Path, sprint: int) -> tuple[dict | None, list[str], list[str]]:
    """Search the requested folder first; scan other sprints only if necessary."""
    warnings = []
    parse_errors = []
    preferred = sorted((source_root / f"sprint_{sprint}").glob("*.html"))
    candidates = preferred or sorted(source_root.glob("sprint_*/*.html"))
    matches = []
    for path in candidates:
        try:
            snapshot = parse_snapshot(path)
        except (ValueError, OSError) as exc:
            parse_errors.append(str(exc))
            continue
        if snapshot["sprint_number"] == sprint:
            matches.append(snapshot)
        elif path in preferred:
            warnings.append(f"{path}: selected {snapshot['sprint_name']}, expected Sprint {sprint}")
    if preferred and not matches:
        for path in sorted(source_root.glob("sprint_*/*.html")):
            if path in preferred:
                continue
            try:
                snapshot = parse_snapshot(path)
            except (ValueError, OSError):
                continue
            if snapshot["sprint_number"] == sprint:
                matches.append(snapshot)
    if len(matches) != 1:
        warnings.append(f"Expected one saved Jira HTML snapshot for Sprint {sprint}; found {len(matches)}")
        return None, warnings, parse_errors
    if Path(matches[0]["snapshot_path"]).parent.name != f"sprint_{sprint}":
        warnings.append(f"Sprint {sprint} HTML is outside source/sprint_{sprint}/")
    return matches[0], warnings + parse_errors, []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sprint", type=int, required=True)
    parser.add_argument("--source-root", type=Path, default=ROOT / "source")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    if args.sprint < 1:
        parser.error("sprint must be a positive integer")
    data, warnings, errors = find_snapshot(args.source_root, args.sprint)
    for warning in warnings + errors:
        print(f"Warning: {warning}", file=sys.stderr)
    if data is None:
        return 2
    output = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
