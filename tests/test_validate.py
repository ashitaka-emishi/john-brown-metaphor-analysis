from pathlib import Path
import csv

from lincoln_research.schemas import CASE_STUDY_SCHEMA_FILES, read_expected_fields
from lincoln_research.validate import run_validation


def test_scaffold_validates():
    root = Path(__file__).resolve().parents[1]
    assert run_validation(root) == []


def test_methodology_csv_headers_match_schemas():
    root = Path(__file__).resolve().parents[1]
    for csv_name, schema_name in CASE_STUDY_SCHEMA_FILES.items():
        csv_path = root / "case-study" / csv_name
        schema_path = root / "config" / "schemas" / schema_name
        assert csv_path.exists()
        with csv_path.open(newline="", encoding="utf-8") as handle:
            actual = next(csv.reader(handle))
        assert actual == read_expected_fields(schema_path)


def test_process_event_ids_and_capture_modes():
    root = Path(__file__).resolve().parents[1]
    path = root / "case-study" / "process-events.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert rows
    for row in rows:
        assert row["event_id"].startswith("METH-")
        assert row["capture_mode"] in {"retrospective", "prospective"}


def test_interventions_reference_existing_events():
    root = Path(__file__).resolve().parents[1]
    events_path = root / "case-study" / "process-events.csv"
    interventions_path = root / "case-study" / "intervention-log.csv"
    with events_path.open(newline="", encoding="utf-8") as handle:
        event_ids = {row["event_id"] for row in csv.DictReader(handle)}
    with interventions_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert rows
    for row in rows:
        assert row["intervention_id"].startswith("INT-")
        if row["event_id"]:
            assert row["event_id"] in event_ids
