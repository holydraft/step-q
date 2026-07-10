import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

ASSIGNMENT_STATEMENT = re.compile(
    r"#(?P<id>[0-9]+)\s*=\s*(?P<body>.+)\s*;",
    re.IGNORECASE,
)

ENTITY_INSTANCE = re.compile(
    r"#(?P<id>[0-9]+)\s*=\s*(?P<name>[A-Z0-9_]+)\s*\((?P<args>.*)\)\s*;",
    re.IGNORECASE,
)

MATERIAL_ENUM_BY_PRODUCT = {
    "sheet": "Q_SHEET_MATERIAL",
    "tube": "Q_TUBE_MATERIAL",
    "turning": "Q_TURNING_MATERIAL",
    "milling": "Q_MILLING_MATERIAL",
}


@dataclass
class FieldDefinition:
    field_type: str
    enum_name: str | None


@dataclass
class Registry:
    fields: dict[str, FieldDefinition]
    enums: dict[str, set[str]]


@dataclass
class Message:
    level: str
    field: str | None
    message: str

    def as_dict(self) -> dict:
        result = {"level": self.level, "message": self.message}
        if self.field:
            result["field"] = self.field
        return result


@dataclass
class StepEntity:
    entity_id: str
    name: str
    arguments: list[str]


def load_registry() -> Registry:
    tools_dir = Path(__file__).resolve().parent
    spec_dir = tools_dir.parent / "spec"
    fields_path = spec_dir / "fields.md"
    enums_path = spec_dir / "enumerations.md"
    materials_path = spec_dir / "materials.md"

    if not fields_path.is_file() or not enums_path.is_file() or not materials_path.is_file():
        missing = [
            str(path)
            for path in (fields_path, enums_path, materials_path)
            if not path.is_file()
        ]
        raise FileNotFoundError("Required spec file(s) missing: " + ", ".join(missing))

    fields = parse_fields_registry(fields_path.read_text(encoding="utf-8"))
    enums = parse_enumerations_registry(enums_path.read_text(encoding="utf-8"))
    enums.update(parse_materials_registry(materials_path.read_text(encoding="utf-8")))
    return Registry(fields=fields, enums=enums)


def parse_fields_registry(markdown: str) -> dict[str, FieldDefinition]:
    definitions: dict[str, FieldDefinition] = {}

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line.startswith("| `Q_"):
            continue

        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if len(cells) < 5:
            continue

        field_name = strip_backticks(cells[0]).upper()
        field_type = cells[1]
        unit_or_enum = cells[2]
        enum_name = extract_enum_name(unit_or_enum)
        if field_name == "Q_MATERIAL" and enum_name is None:
            enum_name = "__PRODUCT_DEPENDENT_MATERIAL__"

        incoming = FieldDefinition(field_type=field_type, enum_name=enum_name)
        existing = definitions.get(field_name)
        if existing is None:
            definitions[field_name] = incoming
            continue

        # Keep one stable definition and avoid silent type drift.
        if existing.field_type != incoming.field_type:
            raise ValueError(
                f"Conflicting type definitions for {field_name}: "
                f"{existing.field_type} vs {incoming.field_type}"
            )
        if existing.enum_name is None and incoming.enum_name is not None:
            definitions[field_name] = incoming

    return definitions


def parse_enumerations_registry(markdown: str) -> dict[str, set[str]]:
    enums: dict[str, set[str]] = {}
    sections = markdown.split("### ")[1:]

    for section in sections:
        lines = section.splitlines()
        if not lines:
            continue
        enum_name = lines[0].strip()
        if not enum_name.startswith("Q_"):
            continue

        values: set[str] = set()
        for row in iter_markdown_table_rows(lines[1:]):
            if row:
                values.add(row[0])
        if values:
            enums[enum_name] = values

    return enums


def parse_materials_registry(markdown: str) -> dict[str, set[str]]:
    section_map = {
        "Sheet Materials": "Q_SHEET_MATERIAL",
        "Tube Materials": "Q_TUBE_MATERIAL",
        "Turning Materials": "Q_TURNING_MATERIAL",
        "Milling Materials": "Q_MILLING_MATERIAL",
    }
    materials: dict[str, set[str]] = {name: set() for name in section_map.values()}
    current_enum: str | None = None

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        section_match = re.match(r"^##\s+\d+\.\s+(.+)$", line)
        if section_match:
            current_enum = section_map.get(section_match.group(1))
            continue

        if current_enum and line.startswith("- "):
            value = line[2:].strip()
            if value:
                materials[current_enum].add(value)

    return {key: values for key, values in materials.items() if values}


def iter_markdown_table_rows(lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if "---" in stripped or "| Value |" in stripped or "| STEP-Q Field |" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.split("|")[1:-1]]
        if cells and cells[0]:
            rows.append(cells)
    return rows


def strip_backticks(value: str) -> str:
    return value.replace("`", "").strip()


def extract_enum_name(unit_or_enum: str) -> str | None:
    match = re.search(r"`(Q_[A-Z0-9_]+)`", unit_or_enum)
    return match.group(1) if match else None


def has_balanced_step_delimiters(text: str) -> bool:
    nested_depth = 0
    in_string = False
    index = 0

    while index < len(text):
        character = text[index]

        if character == "'":
            if in_string and index + 1 < len(text) and text[index + 1] == "'":
                index += 1
            else:
                in_string = not in_string
        elif not in_string and character == '(':
            nested_depth += 1
        elif not in_string and character == ')':
            nested_depth -= 1
            if nested_depth < 0:
                return False

        index += 1

    return not in_string and nested_depth == 0


def extract_data_section(text: str) -> str | None:
    upper_text = text.upper()
    data_start = upper_text.find("DATA;")
    if data_start == -1:
        return None

    section_start = data_start + len("DATA;")
    section_end = upper_text.find("ENDSEC;", section_start)
    if section_end == -1:
        return None

    return text[section_start:section_end]


def split_step_arguments(raw_arguments: str) -> list[str]:
    arguments: list[str] = []
    current: list[str] = []
    in_string = False
    nested_depth = 0
    index = 0

    while index < len(raw_arguments):
        character = raw_arguments[index]

        if character == "'":
            current.append(character)
            if in_string and index + 1 < len(raw_arguments) and raw_arguments[index + 1] == "'":
                current.append(raw_arguments[index + 1])
                index += 1
            else:
                in_string = not in_string
        elif not in_string and character == '(':
            nested_depth += 1
            current.append(character)
        elif not in_string and character == ')':
            nested_depth = max(0, nested_depth - 1)
            current.append(character)
        elif not in_string and nested_depth == 0 and character == ',':
            arguments.append("".join(current).strip())
            current = []
        else:
            current.append(character)

        index += 1

    remainder = "".join(current).strip()
    if remainder:
        arguments.append(remainder)

    return arguments


def parse_string_argument(value: str) -> str | None:
    stripped = value.strip()
    if len(stripped) < 2 or not stripped.startswith("'") or not stripped.endswith("'"):
        return None
    return stripped[1:-1].replace("''", "'")


def parse_step_entities(data_section: str) -> tuple[list[StepEntity], list[Message]]:
    entities: list[StepEntity] = []
    messages: list[Message] = []
    statement_parts: list[str] = []

    for line in data_section.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue

        statement_parts.append(stripped_line)
        if not stripped_line.endswith(';'):
            continue

        statement = " ".join(statement_parts)
        statement_parts = []
        match = ENTITY_INSTANCE.fullmatch(statement)
        if match:
            entities.append(
                StepEntity(
                    entity_id=match.group("id"),
                    name=match.group("name").upper(),
                    arguments=split_step_arguments(match.group("args")),
                )
            )
            continue

        assignment_match = ASSIGNMENT_STATEMENT.fullmatch(statement)
        if assignment_match and has_balanced_step_delimiters(assignment_match.group("body")):
            entities.append(
                StepEntity(
                    entity_id=assignment_match.group("id"),
                    name="COMPLEX_ENTITY",
                    arguments=[assignment_match.group("body").strip()],
                )
            )
            continue

        messages.append(Message("E", None, "Malformed STEP entity statement in DATA section"))

    if statement_parts:
        messages.append(Message("E", None, "Unterminated STEP entity statement in DATA section"))

    return entities, messages


def extract_metadata_fields(entities: list[StepEntity]) -> tuple[bool, dict[str, str]]:
    has_metadata_container = False
    fields: dict[str, str] = {}

    for entity in entities:
        if entity.name == "PROPERTY_SET" and entity.arguments:
            container_name = parse_string_argument(entity.arguments[0])
            if container_name == "STEP-Q":
                has_metadata_container = True
            continue

        if entity.name != "DESCRIPTIVE_REPRESENTATION_ITEM" or len(entity.arguments) < 2:
            continue

        field_name = parse_string_argument(entity.arguments[0])
        field_value = parse_string_argument(entity.arguments[1])
        if field_name is None or field_value is None or not field_name.upper().startswith("Q_"):
            continue

        fields[field_name.upper()] = field_value

    return has_metadata_container, fields


def resolve_field_enum_name(field: str, fields: dict[str, str], definition: FieldDefinition) -> str | None:
    if definition.enum_name != "__PRODUCT_DEPENDENT_MATERIAL__":
        return definition.enum_name

    product_type = fields.get("Q_PRODUCT_TYPE", "").strip().lower()
    if not product_type:
        return None
    return MATERIAL_ENUM_BY_PRODUCT.get(product_type)


def validate_type(field: str, value: str, fields: dict[str, str], registry: Registry) -> list[Message]:
    messages: list[Message] = []
    definition = registry.fields[field]
    field_type = definition.field_type

    if field_type == "Integer":
        if not re.fullmatch(r"-?[0-9]+", value):
            messages.append(Message("E", field, "Integer value must be base-10 without decimals"))
        return messages

    if field_type == "Float":
        if not re.fullmatch(r"-?[0-9]+(\.[0-9]+)?", value):
            messages.append(Message("E", field, "Float value must use dot notation"))
        return messages

    if field_type == "Bool":
        if value not in {"true", "false"}:
            messages.append(Message("E", field, "Bool value must be true or false"))
        return messages

    if field_type == "Enum":
        enum_name = resolve_field_enum_name(field, fields, definition)
        if enum_name is None:
            messages.append(
                Message(
                    "E",
                    field,
                    "Field requires Q_PRODUCT_TYPE for product-specific enum validation",
                )
            )
            return messages

        allowed_values = registry.enums.get(enum_name)
        if not allowed_values:
            messages.append(Message("E", field, f"Enum registry {enum_name} not found"))
            return messages

        if value not in allowed_values:
            messages.append(Message("E", field, "Enum value is not registered"))
        return messages

    return messages


def validate_file(path: Path, documented_extensions: set[str], registry: Registry) -> dict:
    text = path.read_text(encoding="utf-8")
    messages: list[Message] = []
    fields: dict[str, str] = {}

    stripped = text.strip()
    if not stripped:
        messages.append(Message("E", None, "File is empty"))
        return build_report(path, fields, messages)

    if not stripped.startswith("ISO-10303-21;"):
        messages.append(Message("E", None, "Missing ISO-10303-21 header"))
    if not stripped.endswith("END-ISO-10303-21;"):
        messages.append(Message("E", None, "Missing END-ISO-10303-21 trailer"))

    data_section = extract_data_section(text)
    if data_section is None:
        messages.append(Message("E", None, "Missing DATA section"))
        return build_report(path, fields, messages)

    entities, entity_messages = parse_step_entities(data_section)
    messages.extend(entity_messages)
    has_metadata_container, fields = extract_metadata_fields(entities)

    if not has_metadata_container:
        messages.append(Message("W", None, "STEP-Q PROPERTY_SET container not found"))

    for field, value in fields.items():
        if field not in registry.fields:
            if field in documented_extensions:
                messages.append(Message("W", field, "Documented extension field is outside the registered core"))
            else:
                messages.append(Message("E", field, "Undocumented extension field is non-conformant"))
            continue

        messages.extend(validate_type(field, value, fields, registry))

    if not fields:
        messages.append(Message("W", None, "No STEP-Q metadata fields found"))

    return build_report(path, fields, messages)


def build_report(path: Path, fields: dict[str, str], messages: list[Message]) -> dict:
    errors = sum(1 for message in messages if message.level == "E")
    warnings = sum(1 for message in messages if message.level == "W")
    if errors:
        conformance = "non"
    elif warnings:
        conformance = "partial"
    else:
        conformance = "full"

    return {
        "file": str(path),
        "conformance": conformance,
        "errors": errors,
        "warnings": warnings,
        "fields": fields,
        "messages": [message.as_dict() for message in messages],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate STEP-Q v0.3 metadata against spec/*.md registries.")
    parser.add_argument("files", nargs="+", help="STEP files to validate")
    parser.add_argument(
        "--documented-extension",
        action="append",
        default=[],
        help="Mark a Q_ field as a documented extension so it is reported as a warning instead of an error.",
    )
    args = parser.parse_args()

    registry = load_registry()
    documented_extensions = {field.upper() for field in args.documented_extension}
    reports = [validate_file(Path(file_name), documented_extensions, registry) for file_name in args.files]
    print(json.dumps(reports, indent=2))
    return 1 if any(report["errors"] for report in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())