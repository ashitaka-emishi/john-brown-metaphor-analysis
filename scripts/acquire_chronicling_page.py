#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from john_brown_research.loc_chronicling import (
    LocChroniclingError,
    acquire_page,
    collection_search_url,
    page_json_url,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Acquire one public LOC Chronicling America newspaper page."
    )
    parser.add_argument("page_url", help="LOC page URL, usually with ?sp=N")
    parser.add_argument("output_prefix", type=Path)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--delay", type=float, default=2.0)
    parser.add_argument("--no-pdf", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--search-url", action="store_true")
    parser.add_argument("--query", help="Show a repeatable collection search URL.")
    parser.add_argument("--date-range", help="Date range for --query, e.g. 1863-11-19/1863-12-05.")
    args = parser.parse_args()

    if args.search_url:
        if not args.query or not args.date_range:
            parser.error("--search-url requires --query and --date-range")
        print(collection_search_url(query=args.query, date_range=args.date_range))
        return 0

    print(f"GET {page_json_url(args.page_url)}")
    print(f"WRITE {args.output_prefix.with_suffix('.loc-page.json')}")
    print(f"WRITE {args.output_prefix.with_suffix('.fulltext.json')}")
    if not args.no_pdf:
        print(f"WRITE {args.output_prefix.with_suffix('.pdf')} when page metadata exposes a PDF URL")
    if args.dry_run:
        return 0

    try:
        result = acquire_page(
            args.page_url,
            args.output_prefix,
            timeout=args.timeout,
            delay=args.delay,
            include_pdf=not args.no_pdf,
        )
    except LocChroniclingError as exc:
        print(f"Acquisition failed: {exc}")
        return 2

    print(f"metadata sha256={result.metadata_sha256}")
    print(f"text sha256={result.text_sha256}")
    if result.pdf_path and result.pdf_sha256:
        print(f"pdf sha256={result.pdf_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
