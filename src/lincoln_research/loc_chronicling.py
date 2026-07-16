from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_USER_AGENT = "LincolnWarResearch/0.1 (scholarly research; contact=replace-with-email)"
LOC_COLLECTION_URL = "https://www.loc.gov/collections/chronicling-america/"


class LocChroniclingError(RuntimeError):
    pass


@dataclass(frozen=True)
class PageAcquisition:
    page_url: str
    metadata_path: Path
    text_path: Path
    pdf_path: Path | None
    metadata_sha256: str
    text_sha256: str
    pdf_sha256: str | None


def user_agent() -> str:
    agent = os.getenv("LINCOLN_RESEARCH_USER_AGENT", DEFAULT_USER_AGENT)
    if "replace-with-email" in agent:
        raise LocChroniclingError("Configure LINCOLN_RESEARCH_USER_AGENT with a real contact.")
    return agent


def collection_search_url(
    *,
    query: str,
    date_range: str,
    count: int = 10,
    display_level: str = "page",
    operation: str = "AND",
) -> str:
    params = {
        "dl": display_level,
        "dates": date_range,
        "qs": query,
        "ops": operation,
        "fo": "json",
        "c": str(count),
    }
    return LOC_COLLECTION_URL + "?" + urllib.parse.urlencode(params)


def page_json_url(page_url: str) -> str:
    parsed = urllib.parse.urlparse(page_url)
    query = urllib.parse.parse_qs(parsed.query)
    query["fo"] = ["json"]
    encoded = urllib.parse.urlencode(query, doseq=True)
    return urllib.parse.urlunparse(parsed._replace(query=encoded))


def fetch_bytes(url: str, *, timeout: float = 30.0, delay: float = 0.0) -> bytes:
    if delay > 0:
        time.sleep(delay)
    request = urllib.request.Request(url, headers={"User-Agent": user_agent()})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def fetch_json(url: str, *, timeout: float = 30.0, delay: float = 0.0) -> dict[str, Any]:
    data = fetch_bytes(url, timeout=timeout, delay=delay)
    return json.loads(data.decode("utf-8"))


def search_pages(
    *,
    query: str,
    date_range: str,
    count: int = 10,
    operation: str = "AND",
    timeout: float = 30.0,
    delay: float = 0.0,
    max_total: int = 10_000,
) -> dict[str, Any]:
    url = collection_search_url(
        query=query,
        date_range=date_range,
        count=count,
        operation=operation,
    )
    data = fetch_json(url, timeout=timeout, delay=delay)
    total = int(data.get("pagination", {}).get("total") or 0)
    if total > max_total:
        raise LocChroniclingError(
            f"Search returned {total} results; refine query/date range before acquisition."
        )
    return data


def fulltext_url(page_metadata: dict[str, Any]) -> str:
    resource = page_metadata.get("resource") or {}
    url = resource.get("fulltext_file") or page_metadata.get("fulltext_service")
    if not isinstance(url, str) or not url:
        raise LocChroniclingError("Page metadata does not include a full-text service URL.")
    return url


def pdf_url(page_metadata: dict[str, Any]) -> str | None:
    resource = page_metadata.get("resource") or {}
    url = resource.get("pdf")
    return url if isinstance(url, str) and url else None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract_full_text(payload: bytes) -> str:
    text = payload.decode("utf-8-sig", errors="replace")
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return text
    if isinstance(data, dict):
        if isinstance(data.get("full_text"), str):
            return data["full_text"]
        parts: list[str] = []
        for value in data.values():
            if isinstance(value, dict) and isinstance(value.get("full_text"), str):
                parts.append(value["full_text"])
        if parts:
            return "\n\n".join(parts)
    raise LocChroniclingError("Full-text payload did not contain a recognized text field.")


def acquire_page(
    page_url: str,
    output_prefix: Path,
    *,
    timeout: float = 30.0,
    delay: float = 2.0,
    include_pdf: bool = True,
) -> PageAcquisition:
    metadata = fetch_json(page_json_url(page_url), timeout=timeout, delay=delay)
    metadata_bytes = json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8")
    text_bytes = fetch_bytes(fulltext_url(metadata), timeout=timeout, delay=delay)

    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    metadata_path = output_prefix.with_suffix(".loc-page.json")
    text_path = output_prefix.with_suffix(".fulltext.json")
    metadata_path.write_bytes(metadata_bytes)
    text_path.write_bytes(text_bytes)

    pdf_path = None
    pdf_sha = None
    if include_pdf:
        url = pdf_url(metadata)
        if url:
            try:
                pdf_bytes = fetch_bytes(url, timeout=timeout, delay=delay)
            except urllib.error.URLError:
                pdf_bytes = b""
            if pdf_bytes:
                pdf_path = output_prefix.with_suffix(".pdf")
                pdf_path.write_bytes(pdf_bytes)
                pdf_sha = sha256_bytes(pdf_bytes)

    return PageAcquisition(
        page_url=page_url,
        metadata_path=metadata_path,
        text_path=text_path,
        pdf_path=pdf_path,
        metadata_sha256=sha256_bytes(metadata_bytes),
        text_sha256=sha256_bytes(text_bytes),
        pdf_sha256=pdf_sha,
    )
