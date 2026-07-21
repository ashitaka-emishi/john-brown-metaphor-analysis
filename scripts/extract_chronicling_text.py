#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from john_brown_research.loc_chronicling import extract_full_text
from john_brown_research.util import normalize_text, sha256_file


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract normalized OCR text from a LOC Chronicling America full-text payload."
    )
    parser.add_argument("raw_fulltext_payload", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"READ {args.raw_fulltext_payload}")
    print(f"WRITE {args.output}")
    if args.dry_run:
        return 0

    text = normalize_text(extract_full_text(args.raw_fulltext_payload.read_bytes()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"sha256={sha256_file(args.output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
