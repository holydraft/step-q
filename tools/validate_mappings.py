"""Validate platform-neutral STEP-Q mapping libraries."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
MAPPINGS_ROOT = ROOT / "mappings"
SCHEMA_PATH = MAPPINGS_ROOT / "mapping-schema.yaml"
FIELDS_PATH = ROOT / "spec" / "fields.md"
ENUMERATIONS_PATH = ROOT / "spec" / "enumerations.md"
MATERIALS_PATH = ROOT / "spec" / "materials.md"


def load_yaml_json(path: Path | str) -> dict:
    path = Path(path)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path}: expected JSON-compatible YAML: {error}") from error


def registered_fields() -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in FIELDS_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("| `Q_"):
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if len(cells) >= 3:
            fields[cells[0].replace("`", "")] = cells[1]
    return fields


def registered_field_units() -> dict[str, str | None]:
    """Read field units from the same field registry table as field types."""
    units: dict[str, str | None] = {}
    for line in FIELDS_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("| `Q_"):
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if len(cells) < 3:
            continue
        field = cells[0].replace("`", "")
        unit_or_enum = cells[2].replace("`", "").strip()
        if unit_or_enum in {"", "—", "-"} or unit_or_enum.startswith("Q_") or "product-specific" in unit_or_enum:
            unit = None
        else:
            unit = unit_or_enum
        units.setdefault(field, unit)
    return units


def registered_field_enums() -> dict[tuple[str, str | None], set[str]]:
    """Read field-to-enum relationships, including Q_MATERIAL context."""
    relationships: dict[tuple[str, str | None], set[str]] = {}
    product_sections = {"Sheet": "sheet", "Tube": "tube", "Turning": "turning", "Milling": "milling"}
    context: str | None = None
    for line in FIELDS_PATH.read_text(encoding="utf-8").splitlines():
        section_match = re.match(r"^## \d+\. (Common|Sheet|Tube|Turning|Milling) Fields", line.strip())
        if section_match:
            context = product_sections.get(section_match.group(1))
            continue
        if not line.strip().startswith("| `Q_"):
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if len(cells) < 3:
            continue
        field = cells[0].replace("`", "")
        enums = {
            value
            for value in re.findall(r"`(Q_[A-Z0-9_]+)`", cells[2])
        }
        if enums:
            relationships.setdefault((field, context if field == "Q_MATERIAL" else None), set()).update(enums)
    return relationships


def registered_enums() -> dict[str, set[str] | None]:
    enums: dict[str, set[str] | None] = {}
    sections = ENUMERATIONS_PATH.read_text(encoding="utf-8").split("### ")[1:]
    for section in sections:
        lines = section.splitlines()
        if not lines or not lines[0].strip().startswith("Q_"):
            continue
        name = lines[0].strip()
        values: set[str] = set()
        for line in lines[1:]:
            if not line.strip().startswith("|") or "|---" in line or "| Value |" in line:
                continue
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            if cells and cells[0]:
                values.add(cells[0])
        enums[name] = values or None

    material_sections = {
        "Sheet Materials": "Q_SHEET_MATERIAL",
        "Tube Materials": "Q_TUBE_MATERIAL",
        "Turning Materials": "Q_TURNING_MATERIAL",
        "Milling Materials": "Q_MILLING_MATERIAL",
    }
    current_enum: str | None = None
    for line in MATERIALS_PATH.read_text(encoding="utf-8").splitlines():
        section = line.strip()
        if section.startswith("## "):
            title = section.split(". ", 1)[-1]
            current_enum = material_sections.get(title)
            if current_enum:
                enums[current_enum] = set()
            continue
        if current_enum and section.startswith("- "):
            enums[current_enum].add(section[2:].strip())
    return enums


def discover_mapping_libraries(root: Path | str = MAPPINGS_ROOT) -> list[Path]:
    root = Path(root)
    return sorted(path for path in root.glob("*/mapping.yaml") if path.is_file())


def validate_mapping_document(
    library: dict,
    schema: dict,
    fields: dict[str, str] | None = None,
    enums: dict[str, set[str] | None] | None = None,
    seen_ids: set[str] | None = None,
) -> list[str]:
    fields = fields or registered_fields()
    enums = enums or registered_enums()
    units = registered_field_units()
    field_enums = registered_field_enums()
    seen_ids = seen_ids if seen_ids is not None else set()
    errors: list[str] = []
    required = set(schema["required_mapping_fields"])
    directions = set(schema["mapping_directions"])
    lossiness_values = set(schema["lossiness_values"])
    statuses = set(schema["mapping_status_values"])
    value_modes = {"passthrough", "literal"}

    if not library.get("library_id"):
        errors.append("library: missing library_id")
    for index, entry in enumerate(library.get("mappings", []), start=1):
        prefix = f"{library.get('library_id', 'library')} mapping #{index}"
        missing = required - entry.keys()
        if missing:
            errors.append(f"{prefix}: missing fields: {', '.join(sorted(missing))}")
        mapping_id = entry.get("mapping_id")
        if not mapping_id:
            errors.append(f"{prefix}: mapping_id must not be empty")
        elif mapping_id in seen_ids:
            errors.append(f"{prefix}: duplicate mapping_id {mapping_id!r}")
        else:
            seen_ids.add(mapping_id)
        direction = entry.get("direction")
        if direction not in directions:
            errors.append(f"{prefix}: invalid direction {direction!r}")
        lossiness = entry.get("lossiness")
        if lossiness not in lossiness_values:
            errors.append(f"{prefix}: invalid lossiness {lossiness!r}")
        if entry.get("status") not in statuses:
            errors.append(f"{prefix}: invalid status {entry.get('status')!r}")
        if entry.get("status") == "exact" and lossiness != "lossless":
            errors.append(f"{prefix}: exact mappings must use lossless lossiness")
        step_q_field = entry.get("step_q_field")
        if step_q_field not in fields:
            errors.append(f"{prefix}: unknown STEP-Q field {step_q_field!r}")
        elif entry.get("data_type") != fields[step_q_field]:
            errors.append(
                f"{prefix}: data_type {entry.get('data_type')!r} does not match "
                f"field {step_q_field!r} ({fields[step_q_field]!r})"
            )
        expected_unit = units.get(step_q_field)
        declared_unit = entry.get("unit")
        if declared_unit != expected_unit:
            if expected_unit is None:
                errors.append(
                    f"{prefix}: unit {declared_unit!r} is incompatible with STEP-Q field "
                    f"{step_q_field}. Expected unit: none"
                )
            else:
                errors.append(
                    f"{prefix}: unit {declared_unit!r} is incompatible with STEP-Q field "
                    f"{step_q_field}. Expected unit: {expected_unit}"
                )
        value_mode = entry.get("value_mode")
        if value_mode is None:
            value_mode = "literal" if "step_q_enum" in entry or "step_q_value" in entry else "passthrough"
        if value_mode not in value_modes:
            errors.append(f"{prefix}: invalid value_mode {value_mode!r}")
        step_q_enum = entry.get("step_q_enum")
        step_q_value = entry.get("step_q_value")
        has_enum_definition = step_q_enum is not None or step_q_value is not None
        if value_mode == "passthrough" and has_enum_definition:
            errors.append(f"{prefix}: passthrough mappings must not define step_q_enum or step_q_value")
        if value_mode == "literal":
            if step_q_enum is None or step_q_value is None:
                errors.append(f"{prefix}: literal mappings require step_q_enum and step_q_value")
            elif step_q_enum not in enums:
                errors.append(f"{prefix}: invalid STEP-Q enum reference {step_q_enum!r}")
            elif enums[step_q_enum] and step_q_value not in enums[step_q_enum]:
                errors.append(f"{prefix}: value {step_q_value!r} is not registered in {step_q_enum}")
            else:
                product_type = (entry.get("context") or {}).get("product_type")
                allowed = field_enums.get((step_q_field, product_type))
                if step_q_field == "Q_MATERIAL" and not product_type:
                    errors.append(f"{prefix}: Q_MATERIAL enum mappings require context.product_type")
                elif allowed is None or step_q_enum not in allowed:
                    errors.append(
                        f"{prefix}: enum {step_q_enum!r} is not allowed for STEP-Q field {step_q_field!r}"
                    )
        elif step_q_field in fields and fields[step_q_field] == "Enum":
            errors.append(f"{prefix}: Enum fields require value_mode literal with step_q_enum and step_q_value")
        if not isinstance(entry.get("required"), bool):
            errors.append(f"{prefix}: required must be boolean")
        if direction == "bidirectional":
            if lossiness != "lossless":
                errors.append(f"{prefix}: bidirectional mappings must be lossless")
            if entry.get("bidirectional_safe") is not True:
                errors.append(f"{prefix}: bidirectional mappings require bidirectional_safe: true")

    if not library.get("mappings"):
        errors.append(f"{library.get('library_id', 'library')}: contains no mappings")
    return errors


def validate_documents(documents: Iterable[tuple[Path, dict]]) -> list[str]:
    schema = load_yaml_json(SCHEMA_PATH)
    fields = registered_fields()
    enums = registered_enums()
    errors: list[str] = []
    seen_ids: set[str] = set()
    for path, library in documents:
        errors.extend(validate_mapping_document(library, schema, fields, enums, seen_ids))
        if library.get("mapping_schema") != "../mapping-schema.yaml":
            errors.append(f"{path}: mapping_schema must reference ../mapping-schema.yaml")
    return errors


def validate() -> list[str]:
    documents = [(path, load_yaml_json(path)) for path in discover_mapping_libraries()]
    return validate_documents(documents)


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
