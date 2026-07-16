from __future__ import annotations

import argparse
from pathlib import Path

from .util import sha256_file
from .validate import find_root, run_validation


def main() -> int:
    parser = argparse.ArgumentParser(prog="lincoln-research")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    hash_parser = sub.add_parser("hash")
    hash_parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if args.command == "validate":
        root = find_root()
        errors = run_validation(root)
        if errors:
            print("Validation failed:")
            for error in errors:
                print(f"- {error}")
            return 1
        print("Validation passed.")
        return 0

    if args.command == "hash":
        print(sha256_file(args.path))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
