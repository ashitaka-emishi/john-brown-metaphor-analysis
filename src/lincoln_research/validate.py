from __future__ import annotations

import csv
from pathlib import Path

from .schemas import SCHEMA_FILES, read_expected_fields


def find_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "AGENTS.md").exists() and (candidate / "config").exists():
            return candidate
    raise FileNotFoundError("Could not locate project root")


def validate_csv_headers(root: Path) -> list[str]:
    errors: list[str] = []
    for csv_name, schema_name in SCHEMA_FILES.items():
        csv_path = root / "research" / "data" / csv_name
        schema_path = root / "config" / "schemas" / schema_name
        expected = read_expected_fields(schema_path)
        if not csv_path.exists():
            errors.append(f"Missing {csv_path.relative_to(root)}")
            continue
        with csv_path.open(newline="", encoding="utf-8") as handle:
            actual = next(csv.reader(handle), [])
        if actual != expected:
            errors.append(f"Header mismatch in {csv_path.relative_to(root)}")
    return errors


def validate_source_rows(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "research" / "data" / "source-register.csv"
    if not path.exists():
        return errors
    with path.open(newline="", encoding="utf-8") as handle:
        for line_no, row in enumerate(csv.DictReader(handle), start=2):
            source_id = (row.get("source_id") or "").strip()
            if source_id and not source_id.startswith("SRC-"):
                errors.append(f"{path.relative_to(root)}:{line_no}: invalid source_id")
            if row.get("verification_status") == "verified" and not row.get("sha256"):
                errors.append(f"{path.relative_to(root)}:{line_no}: verified source lacks sha256")
    return errors


def run_validation(root: Path) -> list[str]:
    return validate_csv_headers(root) + validate_source_rows(root)
