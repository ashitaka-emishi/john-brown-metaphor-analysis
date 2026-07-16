#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


def main() -> int:
    path = Path("research/data/evidence-matrix.csv")
    highest = 0
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            value = row.get("evidence_id", "")
            if value.startswith("PASS-"):
                try:
                    highest = max(highest, int(value.split("-", 1)[1]))
                except ValueError:
                    pass
    print(f"PASS-{highest + 1:04d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
