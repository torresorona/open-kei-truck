#!/usr/bin/env python3
"""Validate the battery candidate matrix."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "data" / "battery-candidates.csv"
STATUS_PATH = REPO_ROOT / "data" / "status-vocabulary.md"

EXPECTED_COLUMNS = [
    "priority",
    "candidate",
    "supplier",
    "chemistry",
    "status",
    "role",
    "energy_kwh",
    "nominal_voltage_v",
    "voltage_range_v",
    "capacity_ah",
    "continuous_current_a",
    "peak_current_a",
    "continuous_power_kw",
    "peak_power_kw",
    "dimensions_mm",
    "weight",
    "cooling",
    "bms",
    "contactors_precharge_isolation",
    "can",
    "moq",
    "price",
    "key_risk",
    "source",
    "datasheet",
    "quote",
    "cad",
    "integration_docs",
]

NUMERICISH_COLUMNS = {
    "energy_kwh",
    "nominal_voltage_v",
    "voltage_range_v",
    "capacity_ah",
    "continuous_current_a",
    "peak_current_a",
    "continuous_power_kw",
    "peak_power_kw",
    "dimensions_mm",
    "weight",
}

TARGET_CHECK_STATUSES = {"shortlisted", "verified"}
VERIFIED_ARTIFACT_COLUMNS = ["datasheet", "quote", "cad", "integration_docs"]
NUMBER_RE = re.compile(r"\d+(?:\.\d+)?")


def is_unknown(value: str) -> bool:
    return value.strip().upper().startswith("UKN")


def numbers(value: str) -> list[float]:
    return [float(match.group(0)) for match in NUMBER_RE.finditer(value)]


def first_number(value: str) -> float | None:
    parsed = numbers(value)
    return parsed[0] if parsed else None


def row_label(row: dict[str, str], index: int) -> str:
    candidate = row.get("candidate", "").strip() or f"row {index}"
    return f"row {index} ({candidate})"


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


def validate_rows(rows: list[dict[str, str]], valid_statuses: set[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    seen_priorities: set[int] = set()
    seen_candidates: set[str] = set()

    for index, row in enumerate(rows, start=2):
        label = row_label(row, index)

        for column in EXPECTED_COLUMNS:
            value = (row.get(column) or "").strip()
            if not value:
                errors.append(f"{label}: `{column}` is empty. Use `UKN` if the value is unknown.")
                continue
            if value.lower() in {"unknown", "tbd", "n/a", "na", "none"}:
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

        candidate_key = (row.get("candidate") or "").strip().casefold()
        if candidate_key in seen_candidates:
            errors.append(f"{label}: duplicate candidate name.")
        seen_candidates.add(candidate_key)

        status = (row.get("status") or "").strip()
        if status not in valid_statuses:
            errors.append(f"{label}: invalid status `{status}`. Valid statuses: {', '.join(sorted(valid_statuses))}.")

        for column in NUMERICISH_COLUMNS:
            value = (row.get(column) or "").strip()
            if value and not is_unknown(value) and not numbers(value):
                errors.append(f"{label}: `{column}` should include a number or `UKN`.")

        if status == "verified":
            for column in VERIFIED_ARTIFACT_COLUMNS:
                value = (row.get(column) or "").strip()
                if is_unknown(value):
                    errors.append(f"{label}: `verified` status requires `{column}` evidence.")

        if status in TARGET_CHECK_STATUSES:
            energy = first_number(row.get("energy_kwh", ""))
            if energy is not None and not 35 <= energy <= 55:
                warnings.append(f"{label}: energy {energy:g} kWh is outside the 35-55 kWh target.")

            nominal_voltage = first_number(row.get("nominal_voltage_v", ""))
            if nominal_voltage is not None and not 300 <= nominal_voltage <= 430:
                warnings.append(f"{label}: nominal voltage {nominal_voltage:g} V is outside the 300-430 V target.")

            voltage_values = numbers(row.get("voltage_range_v", ""))
            if voltage_values and max(voltage_values) > 430:
                warnings.append(f"{label}: voltage range includes {max(voltage_values):g} V, above the 430 V target.")

            continuous_power = first_number(row.get("continuous_power_kw", ""))
            if continuous_power is not None and continuous_power < 60:
                warnings.append(f"{label}: continuous power {continuous_power:g} kW is below the 60 kW target.")

            peak_power = first_number(row.get("peak_power_kw", ""))
            if peak_power is not None and peak_power < 120:
                warnings.append(f"{label}: peak power {peak_power:g} kW is below the 120 kW target.")

            chemistry = (row.get("chemistry") or "").upper()
            if "LFP" not in chemistry:
                warnings.append(f"{label}: chemistry is not confirmed LFP.")

    return errors, warnings


def main() -> int:
    headers, rows = load_rows()
    valid_statuses = load_valid_statuses()

    errors: list[str] = []
    validate_headers(headers, errors)

    if not rows:
        errors.append("CSV contains no candidate rows.")

    row_errors, warnings = validate_rows(rows, valid_statuses)
    errors.extend(row_errors)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validated {CSV_PATH.relative_to(REPO_ROOT)} ({len(rows)} candidates).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
