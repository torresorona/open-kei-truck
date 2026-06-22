#!/usr/bin/env python3
"""Generate the battery shortlist table from the CSV source of truth."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "data" / "battery-candidates.csv"
DOC_PATH = REPO_ROOT / "docs" / "04-battery-shortlist.md"

BEGIN_MARKER = "<!-- BEGIN GENERATED: battery-shortlist -->"
END_MARKER = "<!-- END GENERATED: battery-shortlist -->"
ARTIFACT_LABELS = {
    "datasheet": "datasheet",
    "quote": "quote",
    "cad": "CAD",
    "integration_docs": "integration docs",
}


def is_unknown(value: str) -> bool:
    return value.strip().upper().startswith("UKN")


def sort_priority(row: dict[str, str]) -> int:
    try:
        return int(row.get("priority", "999999"))
    except ValueError:
        return 999999


def escape_markdown(value: str) -> str:
    value = value.strip() or "UKN"
    return value.replace("|", "\\|")


def missing_artifacts(row: dict[str, str]) -> str:
    missing = [
        label
        for column, label in ARTIFACT_LABELS.items()
        if is_unknown(row.get(column, ""))
    ]
    return ", ".join(missing) if missing else "None tracked"


def load_shortlisted_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return sorted(
        [row for row in rows if row.get("status", "").strip() == "shortlisted"],
        key=sort_priority,
    )


def render_table(rows: list[dict[str, str]]) -> str:
    headers = [
        "Priority",
        "Candidate",
        "Supplier",
        "Chemistry",
        "Energy kWh",
        "Nominal V",
        "Voltage range",
        "Continuous kW",
        "Peak kW",
        "Packaging",
        "Weight",
        "Cooling",
        "BMS",
        "Contactors / precharge / isolation",
        "CAN",
        "Missing verification",
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for row in rows:
        values = [
            row["priority"],
            row["candidate"],
            row["supplier"],
            row["chemistry"],
            row["energy_kwh"],
            row["nominal_voltage_v"],
            row["voltage_range_v"],
            row["continuous_power_kw"],
            row["peak_power_kw"],
            row["dimensions_mm"],
            row["weight"],
            row["cooling"],
            row["bms"],
            row["contactors_precharge_isolation"],
            row["can"],
            missing_artifacts(row),
        ]
        lines.append("| " + " | ".join(escape_markdown(value) for value in values) + " |")

    if not rows:
        lines.append("| _No shortlisted candidates._ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")

    return "\n".join(lines)


def update_doc(generated: str, check: bool) -> int:
    doc = DOC_PATH.read_text(encoding="utf-8")
    if BEGIN_MARKER not in doc or END_MARKER not in doc:
        print(f"{DOC_PATH.relative_to(REPO_ROOT)} is missing generated table markers.", file=sys.stderr)
        return 1

    before, rest = doc.split(BEGIN_MARKER, 1)
    _, after = rest.split(END_MARKER, 1)
    updated = f"{before}{BEGIN_MARKER}\n{generated}\n{END_MARKER}{after}"

    if check:
        if updated != doc:
            print(
                f"{DOC_PATH.relative_to(REPO_ROOT)} is out of date. "
                "Run `python3 scripts/generate_battery_shortlist.py`.",
                file=sys.stderr,
            )
            return 1
        print(f"Checked {DOC_PATH.relative_to(REPO_ROOT)}.")
        return 0

    DOC_PATH.write_text(updated, encoding="utf-8")
    print(f"Updated {DOC_PATH.relative_to(REPO_ROOT)}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if the generated table is out of date")
    args = parser.parse_args()

    generated = render_table(load_shortlisted_rows())
    return update_doc(generated, args.check)


if __name__ == "__main__":
    sys.exit(main())
