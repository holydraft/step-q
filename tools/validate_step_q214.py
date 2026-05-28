import argparse
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


REGISTERED_FIELDS = {
    "Q_PART_ID": {"type": "String"},
    "Q_MATERIAL": {"type": "String"},
    "Q_PRIMARY_PROCESS": {
        "type": "Enum",
        "values": {
            "laser_cutting",
            "bending",
            "punching",
            "milling",
            "turning",
            "grinding",
            "additive",
            "casting",
            "forging",
            "hybrid",
        },
    },
    "Q_QUANTITY": {"type": "Integer", "min": 1},
    "Q_TOLERANCE_CLASS": {
        "type": "Enum",
        "values": {"ISO2768-f", "ISO2768-m", "ISO2768-c", "ISO2768-v", "custom"},
    },
    "Q_SURFACE": {
        "type": "Enum",
        "values": {
            "raw",
            "deburred",
            "brushed",
            "polished",
            "powder_coated",
            "anodized",
            "galvanized",
            "passivated",
            "painted",
        },
    },
    "Q_DRAWING_REFERENCE": {"type": "String"},
    "Q_TARGET_PRICE": {"type": "Float", "min": 0},
    "Q_DELIVERY_DATE": {"type": "Date"},
    "Q_CERTIFICATE": {
        "type": "Enum",
        "values": {"none", "EN10204-2.1", "EN10204-3.1", "EN10204-3.2"},
    },
    "Q_PACKAGING": {
        "type": "Enum",
        "values": {"bulk", "individual", "vacuum", "foam", "custom"},
    },
    "Q_COMMENTS": {"type": "String"},
}

METADATA_CONTAINER = re.compile(r"PROPERTY_SET\('STEP-Q214'", re.IGNORECASE)
REPRESENTATION_ITEM = re.compile(
    r"DESCRIPTIVE_REPRESENTATION_ITEM\('(?P<field>Q_[A-Z0-9_]+)'\s*,\s*'(?P<value>[^']*)'\)",
    re.IGNORECASE,
)


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


def validate_type(field: str, value: str) -> list[Message]:
    messages: list[Message] = []
    definition = REGISTERED_FIELDS[field]
    field_type = definition["type"]

    if field_type == "String":
        if any(ord(char) < 32 and char not in {"\t", "\n", "\r"} for char in value):
            messages.append(Message("E", field, "String value contains control characters"))
        return messages

    if field_type == "Integer":
        if not re.fullmatch(r"[0-9]+", value):
            messages.append(Message("E", field, "Integer value must be base-10 without decimals"))
            return messages
        if int(value) < definition.get("min", 0):
            messages.append(Message("E", field, "Integer value is below the allowed minimum"))
        return messages

    if field_type == "Float":
        try:
            parsed = float(value)
        except ValueError:
            messages.append(Message("E", field, "Float value must use dot notation"))
            return messages
        if not math.isfinite(parsed):
            messages.append(Message("E", field, "Float value must be finite"))
        if parsed < definition.get("min", 0):
            messages.append(Message("E", field, "Float value is below the allowed minimum"))
        return messages

    if field_type == "Enum":
        if value not in definition["values"]:
            messages.append(Message("E", field, "Enum value is not registered"))
        return messages

    if field_type == "Date":
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            messages.append(Message("E", field, "Date value must use YYYY-MM-DD format"))
        return messages

    return messages


def validate_file(path: Path, documented_extensions: set[str]) -> dict:
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
    if not METADATA_CONTAINER.search(text):
        messages.append(Message("W", None, "STEP-Q214 PROPERTY_SET container not found"))

    for match in REPRESENTATION_ITEM.finditer(text):
        field = match.group("field").upper()
        value = match.group("value")
        fields[field] = value

        if field not in REGISTERED_FIELDS:
            if field in documented_extensions:
                messages.append(Message("W", field, "Documented extension field is outside the registered core"))
            else:
                messages.append(Message("E", field, "Undocumented extension field is non-conformant"))
            continue

        messages.extend(validate_type(field, value))

    if not fields:
        messages.append(Message("W", None, "No STEP-Q214 metadata fields found"))

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
    parser = argparse.ArgumentParser(description="Validate STEP-Q214 draft metadata in STEP files.")
    parser.add_argument("files", nargs="+", help="STEP files to validate")
    parser.add_argument(
        "--documented-extension",
        action="append",
        default=[],
        help="Mark a Q_ field as a documented extension so it is reported as a warning instead of an error.",
    )
    args = parser.parse_args()

    documented_extensions = {field.upper() for field in args.documented_extension}
    reports = [validate_file(Path(file_name), documented_extensions) for file_name in args.files]
    print(json.dumps(reports, indent=2))
    return 1 if any(report["errors"] for report in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())