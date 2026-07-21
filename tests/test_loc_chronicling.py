from john_brown_research.loc_chronicling import (
    collection_search_url,
    extract_full_text,
    fulltext_url,
    page_json_url,
)


def test_collection_search_url_encodes_dates_and_query():
    url = collection_search_url(
        query="John Brown",
        date_range="1859-10-16/1859-12-05",
        count=5,
    )
    assert "dl=page" in url
    assert "dates=1859-10-16%2F1859-12-05" in url
    assert "qs=John+Brown" in url
    assert "fo=json" in url
    assert "c=5" in url


def test_page_json_url_preserves_page_sequence():
    url = page_json_url("https://www.loc.gov/resource/sn83030213/1863-11-20/ed-1/?sp=1")
    assert url == "https://www.loc.gov/resource/sn83030213/1863-11-20/ed-1/?sp=1&fo=json"


def test_fulltext_url_uses_resource_link():
    metadata = {"resource": {"fulltext_file": "https://example.test/fulltext"}}
    assert fulltext_url(metadata) == "https://example.test/fulltext"


def test_extract_full_text_from_loc_payload():
    payload = b'{"segment.xml": {"full_text": "Four score\\n"}}'
    assert extract_full_text(payload) == "Four score\n"
