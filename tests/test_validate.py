from pathlib import Path

from lincoln_research.validate import run_validation


def test_scaffold_validates():
    root = Path(__file__).resolve().parents[1]
    assert run_validation(root) == []
