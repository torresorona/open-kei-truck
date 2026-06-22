#!/usr/bin/env python3
"""Validate the whole-vehicle component candidate matrix."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "data" / "component-candidates.csv"
STATUS_PATH = REPO_ROOT / "data" / "status-vocabulary.md"

EXPECTED_COLUMNS = [
    "priority",
    "subsystem",
    "part_group",
    "item",
    "qty",
    "reference_spec_or_target",
    "sourcing_strategy",
    "candidate_source",
    "source_url",
    "status",
    "key_questions",
    "notes",
]

UNKNOWN_WORDS = {"unknown", "tbd", "n/a", "na", "none"}
URL_RE = re.compile(r"^(https?://|\.\./|/)")  # allow web and repo-relative references


def load_valid_statuses() -> set[str]:
    statuses: set[str] = set()
    for line in STATUS_PATH.read_text(encoding="utf-8").splitlines():
        match = re.match(r"- `([^`]+)`:", line)
        if match:
            statuses.add(match.group(1))
    return statuses


def load_rows() -> tuple[list[str], list[dict[str, str]]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def row_label(row: dict[str, str], index: int) -> str:
    item = row.get("item", "").strip() or f"row {index}"
    subsystem = row.get("subsystem", "").strip()
    if subsystem:
        return f"row {index} ({subsystem}: {item})"
    return f"row {index} ({item})"


def validate_headers(headers: list[str], errors: list[str]) -> None:
    if headers == EXPECTED_COLUMNS:
        return

    missing = [column for column in EXPECTED_COLUMNS if column not in headers]
    extra = [column for column in headers if column not in EXPECTED_COLUMNS]

    if missing:
        errors.append(f"Missing columns: {', '.join(missing)}")
    if extra:
        errors.append(f"Unexpected columns: {', '.join(extra)}")
    if not missing and not extra:
        errors.append("Columns are present but not in the expected order.")


def validate_rows(rows: list[dict[str, str]], valid_statuses: set[str]) -> list[str]:
    errors: list[str] = []
    seen_priorities: set[int] = set()

    for index, row in enumerate(rows, start=2):
        label = row_label(row, index)

        for column in EXPECTED_COLUMNS:
            value = (row.get(column) or "").strip()
            if not value:
                errors.append(f"{label}: `{column}` is empty. Use `UKN` if the value is unknown.")
                continue
            if value.lower() in UNKNOWN_WORDS:
                errors.append(f"{label}: `{column}` uses `{value}`. Use `UKN` for unknown values.")

        priority_value = (row.get("priority") or "").strip()
        try:
            priority = int(priority_value)
            if priority < 1:
                errors.append(f"{label}: `priority` must be a positive integer.")
            if priority in seen_priorities:
                errors.append(f"{label}: duplicate priority `{priority}`.")
            seen_priorities.add(priority)
        except ValueError:
            errors.append(f"{label}: `priority` must be an integer.")

        status = (row.get("status") or "").strip()
        if status not in valid_statuses:
            errors.append(f"{label}: invalid status `{status}`. Valid statuses: {', '.join(sorted(valid_statuses))}.")

        source_url = (row.get("source_url") or "").strip()
        if source_url and not URL_RE.search(source_url):
            errors.append(f"{label}: `source_url` should be a URL or repo-relative path.")

    return errors


def main() -> int:
    headers, rows = load_rows()
    valid_statuses = load_valid_statuses()

    errors: list[str] = []
    validate_headers(headers, errors)

    if not rows:
        errors.append("CSV contains no candidate rows.")

    errors.extend(validate_rows(rows, valid_statuses))

    if errors:
        print("Errors:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validated {CSV_PATH.relative_to(REPO_ROOT)} ({len(rows)} candidates).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
