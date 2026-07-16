#!/usr/bin/env python3
# Safely fetch one authorized public source. This does not crawl or bypass controls.

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output", type=Path)
    parser.add_argument("--delay", type=float, default=float(os.getenv("LINCOLN_RESEARCH_REQUEST_DELAY", "2.0")))
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    agent = os.getenv(
        "LINCOLN_RESEARCH_USER_AGENT",
        "LincolnWarResearch/0.1 (scholarly research; contact=replace-with-email)",
    )
    if "replace-with-email" in agent:
        print("Configure a real contact in LINCOLN_RESEARCH_USER_AGENT.", file=sys.stderr)
        return 2

    print(f"GET {args.url} -> {args.output}")
    if args.dry_run:
        return 0

    time.sleep(max(args.delay, 0))
    request = urllib.request.Request(args.url, headers={"User-Agent": agent})
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            data = response.read()
    except urllib.error.URLError as exc:
        print(f"Fetch failed: {exc}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(data)
    print(f"Wrote {len(data)} bytes; sha256={hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
