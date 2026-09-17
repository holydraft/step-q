"""Validate declarative STEP-Q mapping libraries without external dependencies."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "mappings" / "mapping-schema.yaml"
ORDESPOT_MAPPING_PATH = ROOT / "mappings" / "orderspot" / "mapping.yaml"
MATERIALS_PATH = ROOT / "spec" / "materials.md"
ORDESPOT_DATA_PATH = ROOT / "spec" / "materials_orderspot.csv"


def load_yaml_json(path: Path | str) -> dict:
    path = Path(path)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path}: expected JSON-compatible YAML: {error}") from error


def material_labels() -> set[str]:
    labels: set[str] = set()
    for line in MATERIALS_PATH.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            labels.add(stripped[2:].strip())
    return labels


def orderspot_keys() -> set[tuple[str, str, str]]:
    with ORDESPOT_DATA_PATH.open(encoding="utf-8", newline="") as handle:
        return {
            (
                row["materialTypeNumber"].strip(),
                row["surfaceNorm"].strip(),
                row["productionMethod"].strip(),
            )
            for row in csv.DictReader(handle, delimiter=";")
        }


def validate() -> list[str]:
    errors: list[str] = []
    schema = load_yaml_json(SCHEMA_PATH)
    library = load_yaml_json(ORDESPOT_MAPPING_PATH)
    required_fields = set(schema["required_mapping_fields"])
    allowed_directions = set(schema["mapping_directions"])
    allowed_lossiness = set(schema["lossiness_values"])
    allowed_statuses = set(schema["mapping_status_values"])
    labels = material_labels()
    keys = orderspot_keys()

    for index, entry in enumerate(library.get("mappings", []), start=1):
        prefix = f"mapping #{index}"
        missing = required_fields - entry.keys()
        if missing:
            errors.append(f"{prefix}: missing fields: {', '.join(sorted(missing))}")
        if entry.get("direction") not in allowed_directions:
            errors.append(f"{prefix}: invalid direction {entry.get('direction')!r}")
        if entry.get("lossiness") not in allowed_lossiness:
            errors.append(f"{prefix}: invalid lossiness {entry.get('lossiness')!r}")
        if entry.get("status") not in allowed_statuses:
            errors.append(f"{prefix}: invalid status {entry.get('status')!r}")
        if entry.get("step_q_field") != "Q_SHEET_MATERIAL":
            errors.append(f"{prefix}: Orderspot library must target Q_SHEET_MATERIAL")
        if entry.get("step_q_label") not in labels:
            errors.append(f"{prefix}: unknown STEP-Q material label {entry.get('step_q_label')!r}")
        key = (
            str(entry.get("material_type_number", "")),
            str(entry.get("surface_norm", "")),
            str(entry.get("production_method", "")),
        )
        if key not in keys:
            errors.append(f"{prefix}: Orderspot key not found in CSV: {key!r}")
        status = entry.get("status")
        lossiness = entry.get("lossiness")
        if status == "exact" and lossiness != "lossless":
            errors.append(f"{prefix}: exact mappings must be lossless")
        if status == "normalized" and lossiness not in {"lossless", "normalized"}:
            errors.append(f"{prefix}: normalized mappings must be lossless or normalized")

    if not library.get("mappings"):
        errors.append("Orderspot mapping library contains no mappings")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Mapping library validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
