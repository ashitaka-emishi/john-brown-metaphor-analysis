from __future__ import annotations

from pathlib import Path

SCHEMA_FILES = {
    "source-register.csv": "source-register.fields",
    "evidence-matrix.csv": "evidence-matrix.fields",
    "claims.csv": "claims.fields",
}


def read_expected_fields(schema_path: Path) -> list[str]:
    return [
        line.strip()
        for line in schema_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
