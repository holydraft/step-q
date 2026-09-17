"""Orderspot-specific source identity and collision checks."""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validate_mappings import load_yaml_json


MAPPING_PATH = ROOT / "mappings" / "orderspot" / "mapping.yaml"
SOURCE_PATH = ROOT / "spec" / "materials_orderspot.csv"
IDENTITY_FIELDS = ("materialTypeNumber", "surfaceNorm", "productionMethod")


def source_rows(path: Path = SOURCE_PATH) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def source_identity(entry: dict) -> tuple[str, str, str] | None:
    identity = entry.get("source_identity")
    if not isinstance(identity, dict) or any(field not in identity for field in IDENTITY_FIELDS):
        return None
    return tuple(str(identity[field]).strip() for field in IDENTITY_FIELDS)


def validate_orderspot(
    library: dict | None = None,
    rows: list[dict[str, str]] | None = None,
) -> list[str]:
    library = library or load_yaml_json(MAPPING_PATH)
    rows = rows if rows is not None else source_rows()
    source_keys = {
        tuple(row[field].strip() for field in IDENTITY_FIELDS)
        for row in rows
    }
    active = [
        entry
        for entry in library.get("mappings", [])
        if entry.get("status") in {"exact", "normalized"}
    ]
    errors: list[str] = []
    by_source: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    by_target: dict[str, list[dict]] = defaultdict(list)

    for entry in active:
        mapping_id = entry.get("mapping_id", "<missing>")
        identity = source_identity(entry)
        if identity is None:
            errors.append(f"{mapping_id}: missing Orderspot source identity fields")
            continue
        by_source[identity].append(entry)
        by_target[str(entry.get("step_q_value"))].append(entry)
        if identity not in source_keys:
            errors.append(
                "ERROR: Orderspot mapping references source identity not found in source dataset:\n"
                f"materialTypeNumber: {identity[0]}\n"
                f"surfaceNorm: {identity[1]}\n"
                f"productionMethod: {identity[2]}"
            )
        if entry.get("status") == "exact" and entry.get("lossiness") != "lossless":
            errors.append(f"{mapping_id}: exact mappings must be lossless")

    for identity, entries in by_source.items():
        if len(entries) > 1:
            ids = ", ".join(entry.get("mapping_id", "<missing>") for entry in entries)
            errors.append(
                "Orderspot source collision for identity "
                f"{identity[0]} / {identity[1]} / {identity[2]}: {ids}"
            )

    for value, entries in by_target.items():
        if len(entries) > 1:
            ids = ", ".join(entry.get("mapping_id", "<missing>") for entry in entries)
            errors.append(f"STEP-Q value collision for {value!r}: {ids}")

    for entry in active:
        if entry.get("direction") != "bidirectional":
            continue
        identity = source_identity(entry)
        target = str(entry.get("step_q_value"))
        if entry.get("lossiness") != "lossless":
            errors.append(f"{entry.get('mapping_id')}: bidirectional mapping is not lossless")
        if identity is None or len(by_source.get(identity, [])) != 1:
            errors.append(f"{entry.get('mapping_id')}: bidirectional source identity is not unique")
        if len(by_target.get(target, [])) != 1:
            errors.append(f"{entry.get('mapping_id')}: bidirectional STEP-Q value is not unique")

    return errors


def main() -> int:
    errors = validate_orderspot()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("Orderspot mapping validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
