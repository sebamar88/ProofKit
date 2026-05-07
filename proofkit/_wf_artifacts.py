"""Artifact body generation and YAML frontmatter parsing.

Depends only on _types.  No circular imports.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from ._types import REQUIRED_PROFILES


def artifact_name(filename: str) -> str:
    return filename.removesuffix(".md")


def frontmatter(schema: str, artifact: str, change_id: str, profile: str, today: str) -> str:
    return "\n".join(
        [
            "---",
            f"schema: {schema}",
            f"artifact: {artifact}",
            f"change_id: {change_id}",
            f"profile: {profile}",
            "status: draft",
            f"created: {today}",
            f"updated: {today}",
            "---",
            "",
        ]
    )


def living_spec_frontmatter(change_id: str, today: str) -> str:
    return "\n".join(
        [
            "---",
            "schema: sdd.living-spec.v1",
            "artifact: spec",
            f"change_id: {change_id}",
            "status: active",
            f"created: {today}",
            f"updated: {today}",
            "---",
            "",
        ]
    )


def artifact_title(filename: str) -> str:
    words = artifact_name(filename).replace("-", " ").split()
    return " ".join(word.capitalize() for word in words)


def artifact_body(filename: str, change_id: str, title: str, profile: str, today: str) -> str:
    artifact = artifact_name(filename)
    header = frontmatter("sdd.artifact.v1", artifact, change_id, profile, today)
    heading = f"# {artifact_title(filename)}"

    if filename == "proposal.md":
        return (
            header
            + f"{heading}\n\n"
            + f"## Intent\n\n{title}\n\n"
            + "## Scope\n\n- Define the intended change.\n\n"
            + "## Non-Scope\n\n- Record what this change will not address.\n\n"
            + "## Risks\n\n- Record known risks or write `None`.\n"
        )
    if filename == "delta-spec.md":
        return (
            header
            + f"{heading}\n\n"
            + "## ADDED\n\n- List new observable behavior.\n\n"
            + "## MODIFIED\n\n- List changed observable behavior.\n\n"
            + "## REMOVED\n\n- List removed observable behavior.\n"
        )
    if filename == "design.md":
        return (
            header
            + f"{heading}\n\n"
            + "## Approach\n\n- Describe the technical approach.\n\n"
            + "## Decisions\n\n- Record important decisions and rationale.\n\n"
            + "## Alternatives Rejected\n\n- Record alternatives and why they were rejected.\n"
        )
    if filename == "tasks.md":
        return (
            header
            + f"{heading}\n\n"
            + "- [ ] T-001 Define the first concrete task.\n"
            + "  - Requirement: proposal\n"
            + "  - Evidence: verification.md\n"
        )
    if filename == "verification.md":
        return (
            frontmatter("sdd.verification.v1", artifact, change_id, profile, today)
            + f"{heading}\n\n"
            + "## Matrix\n\n"
            + "| Requirement | Scenario | Tasks | Evidence | Status |\n"
            + "| --- | --- | --- | --- | --- |\n"
            + "| proposal | initial scenario | T-001 | pending verification evidence | not-run |\n\n"
            + "## Commands\n\n- Record host-project verification actions.\n\n"
            + "## Manual Checks\n\n- Record manual evidence when relevant.\n\n"
            + "## Gaps\n\n- Record known gaps or write `None`.\n"
        )
    if filename == "critique.md":
        return (
            header
            + f"{heading}\n\n"
            + "## Verdict\n\n- draft\n\n"
            + "## Findings\n\n- Record blocking and non-blocking findings.\n\n"
            + "## Required Fixes\n\n- Record required fixes or write `None`.\n"
        )
    if filename == "archive.md":
        return (
            header
            + f"{heading}\n\n"
            + "## Archive Status\n\n- draft\n\n"
            + "## Spec Sync\n\n- Record living spec updates.\n\n"
            + "## Final Evidence\n\n- Link verification and critique evidence.\n"
        )
    if filename == "findings.md":
        return (
            header
            + f"{heading}\n\n"
            + "## Research Question\n\n{title}\n\n"
            + "## Sources Inspected\n\n- Record sources, files, commands, or URLs.\n\n"
            + "## Findings\n\n- Record findings.\n\n"
            + "## Unresolved Questions\n\n- Record remaining uncertainty or write `None`.\n"
        )
    if filename == "decision.md":
        return (
            header
            + f"{heading}\n\n"
            + "## Recommendation\n\n- Record the recommendation.\n\n"
            + "## Rationale\n\n- Record the rationale.\n\n"
            + "## Tradeoffs\n\n- Record tradeoffs.\n"
        )
    return header + f"{heading}\n"


def read_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing opening frontmatter marker"

    close_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            close_index = index
            break

    if close_index is None:
        return {}, "missing closing frontmatter marker"

    result: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:close_index], start=2):
        stripped = line.strip()
        if not stripped:
            continue
        if ":" not in stripped:
            return {}, f"invalid frontmatter line {line_number}: expected key: value"
        key, raw_value = stripped.split(":", 1)
        key = key.strip()
        value = raw_value.strip().strip('"').strip("'")
        if not key:
            return {}, f"invalid frontmatter line {line_number}: empty key"
        result[key] = value

    return result, None
