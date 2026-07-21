#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from john_brown_research.util import normalize_text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(normalize_text(text), encoding="utf-8")
    print(f"Normalized {args.input} -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
