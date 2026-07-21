from pathlib import Path

from john_brown_research.util import normalize_text, sha256_file


def test_normalize_text():
    assert normalize_text("a  \r\nb\r\n") == "a\nb\n"


def test_sha256_file(tmp_path: Path):
    path = tmp_path / "sample.txt"
    path.write_bytes(b"abc")
    assert sha256_file(path) == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
