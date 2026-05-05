"""Split ssd_core/cli.py into focused sub-modules.

Result:
    ssd_core/_types.py     — VERSION, color helpers, constants, enums, dataclasses
    ssd_core/_workflow.py  — file I/O, state machine, WorkflowEngine (all logic)
    ssd_core/_render.py    — print_* functions, demos, CI templates
    ssd_core/cli.py        — _auto_advance, build_parser, main (entry point only)

Public API (ssd_core/__init__.py) is untouched — imports from cli.py still work
because cli.py re-imports everything from the three new modules.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "ssd_core" / "cli.py"

src = CLI.read_text(encoding="utf-8")
lines = src.splitlines(keepends=True)

def block(start: int, end: int) -> str:
    """Return lines[start-1 : end] (1-based, inclusive)."""
    return "".join(lines[start - 1 : end])


# ── _types.py ────────────────────────────────────────────────────────────────
# Content: lines 22-370  (VERSION → WorkflowResult)
TYPES_HEADER = """\
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import ClassVar

"""

types_body = block(22, 370)

(ROOT / "ssd_core" / "_types.py").write_text(
    TYPES_HEADER + types_body + "\n",
    encoding="utf-8",
)
print("wrote _types.py")


# ── _workflow.py ─────────────────────────────────────────────────────────────
# Content: lines 373-2454  (logical_path → end of guard_repository)
WORKFLOW_HEADER = """\
from __future__ import annotations

import hashlib
import json
import shutil
import shlex
import stat
import subprocess
import time
import uuid
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from importlib.resources import files
from pathlib import Path
from typing import ClassVar, Iterable, Protocol

from ._types import (
    VERSION,
    Finding,
    ChangeSummary,
    WorkflowPhase,
    WorkflowFailureKind,
    WorkflowFailure,
    WorkflowState,
    WorkflowResult,
    TemplateResource,
    _PIPELINE_PHASES,
    _use_color,
    _c,
    _green,
    _yellow,
    _red,
    _cyan,
    _bold,
    _dim,
    REQUIRED_DIRECTORIES,
    REQUIRED_ADAPTERS,
    REQUIRED_AGENTS,
    REQUIRED_PROFILES,
    REQUIRED_SCHEMAS,
    REQUIRED_SKILLS,
    PROFILE_ARTIFACTS,
    FOUNDATION_COPY_DIRECTORIES,
    FOUNDATION_COPY_FILES,
    FOUNDATION_DOC_FILES,
    EMPTY_STATE_DIRECTORIES,
    ARTIFACT_STATUSES,
    SCHEMA_PATTERN,
    TOKEN_PATTERN,
    DATE_PATTERN,
    OPEN_TASK_PATTERN,
    MATRIX_PASSING_ROW_PATTERN,
    VERIFICATION_EVIDENCE_BLOCKERS,
    WORKFLOW_STATE_SCHEMA,
    PHASE_ORDER,
    ALLOWED_TRANSITIONS,
)

"""

workflow_body = block(373, 2454)

(ROOT / "ssd_core" / "_workflow.py").write_text(
    WORKFLOW_HEADER + workflow_body + "\n",
    encoding="utf-8",
)
print("wrote _workflow.py")


# ── _render.py ───────────────────────────────────────────────────────────────
# Content: lines 2457-3260 (print_guard → end of run_demo)
RENDER_HEADER = """\
from __future__ import annotations

import tempfile
from pathlib import Path

from ._types import (
    VERSION,
    Finding,
    WorkflowPhase,
    WorkflowFailure,
    WorkflowResult,
    _PIPELINE_PHASES,
    PHASE_ORDER,
    REQUIRED_PROFILES,
    _use_color,
    _c,
    _green,
    _yellow,
    _red,
    _cyan,
    _bold,
    _dim,
)
from ._workflow import (
    validate,
    init_project,
    create_change,
    change_directory,
    status,
    workflow_state,
    infer_phase_from_artifacts,
    Archive_change,
    sync_specs,
    archive_change,
    verify_change,
    discover_test_command,
    guard_repository,
    install_hooks,
    write_ci_template,
    transition_workflow,
    run_workflow,
    print_findings,
    declared_workflow_phase,
    execution_evidence_records,
    execution_evidence_path,
    artifact_checksum,
    _auto_advance,
    _PHASE_ARTIFACT_FILE,
    _CI_TEMPLATES,
    set_frontmatter_value,
    validate_spec_sync,
    check_change_artifacts,
    validate_execution_evidence,
    WorkflowEngine,
    AutoStep,
    EngineStep,
    WorkflowState,
    WorkflowFailureKind,
)

"""

render_body = block(2457, 3260)

(ROOT / "ssd_core" / "_render.py").write_text(
    RENDER_HEADER + render_body + "\n",
    encoding="utf-8",
)
print("wrote _render.py (draft — imports need verification)")


# ── cli.py (rewritten) ───────────────────────────────────────────────────────
# Content: lines 3263-end  (_auto_advance → main)
CLI_HEADER = """\
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Re-export the entire public surface through the sub-modules so that
# `from .cli import (VERSION, Finding, ...)` in __init__.py keeps working.
from ._types import *  # noqa: F401, F403
from ._workflow import *  # noqa: F401, F403
from ._render import *  # noqa: F401, F403

"""

cli_body = block(3263, len(lines))

CLI.write_text(
    CLI_HEADER + cli_body,
    encoding="utf-8",
)
print("rewrote cli.py")
print()
print("Done. Run: python -m pytest tests/ -q")
