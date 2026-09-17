import copy
import tempfile
import unittest
from pathlib import Path

from mappings.orderspot.validate import source_rows, validate_orderspot
from tools.validate_mappings import (
    SCHEMA_PATH,
    discover_mapping_libraries,
    load_yaml_json,
    registered_enums,
    registered_fields,
    validate_documents,
    validate_mapping_document,
)


class MappingContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_yaml_json(SCHEMA_PATH)
        cls.fields = registered_fields()
        cls.enums = registered_enums()

    def base_entry(self, **overrides):
        entry = {
            "mapping_id": "test.mapping",
            "source_field": "platform.material",
            "step_q_field": "Q_MATERIAL",
            "step_q_enum": "Q_SHEET_MATERIAL",
            "step_q_value": "EN AW-5754 (AlMg3) 3.3535·H111 Mill-finish",
            "data_type": "Enum",
            "value_mode": "literal",
            "context": {"product_type": "sheet"},
            "unit": None,
            "enum_transform": "resolve_material",
            "direction": "source_to_step_q",
            "required": True,
            "lossiness": "lossless",
            "fallback": None,
            "comment": "test mapping",
            "status": "exact",
        }
        entry.update(overrides)
        return entry

    def library(self, *entries, library_id="test-library"):
        return {
            "library_id": library_id,
            "mapping_schema": "../mapping-schema.yaml",
            "mappings": list(entries),
        }

    def test_valid_source_to_step_q_mapping(self):
        self.assertEqual(
            validate_mapping_document(
                self.library(self.base_entry()), self.schema, self.fields, self.enums
            ),
            [],
        )

    def test_quantity_passthrough_without_enum_is_valid(self):
        entry = self.base_entry(
            mapping_id="test.quantity",
            source_field="platform.quantity",
            step_q_field="Q_QUANTITY",
            step_q_enum=None,
            step_q_value=None,
            data_type="Integer",
            value_mode="passthrough",
            context=None,
            unit="pcs",
        )
        self.assertEqual(
            validate_mapping_document(self.library(entry), self.schema, self.fields, self.enums),
            [],
        )

    def test_boolean_passthrough_without_enum_is_valid(self):
        entry = self.base_entry(
            mapping_id="test.micro-joints",
            source_field="platform.microJoints",
            step_q_field="Q_MICRO_JOINTS",
            step_q_enum=None,
            step_q_value=None,
            data_type="Bool",
            value_mode="passthrough",
            context=None,
        )
        self.assertEqual(
            validate_mapping_document(self.library(entry), self.schema, self.fields, self.enums),
            [],
        )

    def test_mapping_without_status_is_invalid(self):
        entry = self.base_entry()
        del entry["status"]
        errors = validate_mapping_document(
            self.library(entry), self.schema, self.fields, self.enums
        )
        self.assertTrue(any("missing fields: status" in error for error in errors))

    def test_mapping_with_optional_context_is_valid(self):
        entry = self.base_entry(
            mapping_id="test.quantity.optional-context",
            source_field="platform.quantity",
            step_q_field="Q_QUANTITY",
            step_q_enum=None,
            step_q_value=None,
            data_type="Integer",
            value_mode="passthrough",
            unit="pcs",
        )
        del entry["context"]
        errors = validate_mapping_document(
            self.library(entry), self.schema, self.fields, self.enums
        )
        self.assertEqual(errors, [])

    def test_exact_lossless_is_valid(self):
        errors = validate_mapping_document(
            self.library(self.base_entry(status="exact", lossiness="lossless")),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertEqual(errors, [])

    def test_exact_normalized_is_invalid(self):
        errors = validate_mapping_document(
            self.library(self.base_entry(status="exact", lossiness="normalized")),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("exact mappings must use lossless" in error for error in errors))

    def test_exact_lossy_is_invalid(self):
        errors = validate_mapping_document(
            self.library(self.base_entry(status="exact", lossiness="lossy")),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("exact mappings must use lossless" in error for error in errors))

    def test_quantity_unit_from_field_registry_is_valid(self):
        entry = self.base_entry(
            mapping_id="test.quantity.unit",
            source_field="platform.quantity",
            step_q_field="Q_QUANTITY",
            step_q_enum=None,
            step_q_value=None,
            data_type="Integer",
            value_mode="passthrough",
            context=None,
            unit="pcs",
        )
        self.assertEqual(
            validate_mapping_document(self.library(entry), self.schema, self.fields, self.enums),
            [],
        )

    def test_quantity_wrong_unit_is_invalid(self):
        entry = self.base_entry(
            mapping_id="test.quantity.wrong-unit",
            source_field="platform.quantity",
            step_q_field="Q_QUANTITY",
            step_q_enum=None,
            step_q_value=None,
            data_type="Integer",
            value_mode="passthrough",
            context=None,
            unit="kg",
        )
        errors = validate_mapping_document(
            self.library(entry), self.schema, self.fields, self.enums
        )
        self.assertTrue(any("Expected unit: pcs" in error for error in errors))

    def test_boolean_without_unit_is_valid(self):
        entry = self.base_entry(
            mapping_id="test.boolean.unitless",
            source_field="platform.microJoints",
            step_q_field="Q_MICRO_JOINTS",
            step_q_enum=None,
            step_q_value=None,
            data_type="Bool",
            value_mode="passthrough",
            context=None,
            unit=None,
        )
        self.assertEqual(
            validate_mapping_document(self.library(entry), self.schema, self.fields, self.enums),
            [],
        )

    def test_valid_step_q_to_source_mapping(self):
        errors = validate_mapping_document(
            self.library(self.base_entry(direction="step_q_to_source")),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertEqual(errors, [])

    def test_valid_bidirectional_mapping(self):
        errors = validate_mapping_document(
            self.library(
                self.base_entry(
                    direction="bidirectional",
                    bidirectional_safe=True,
                )
            ),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertEqual(errors, [])

    def test_invalid_step_q_field(self):
        errors = validate_mapping_document(
            self.library(self.base_entry(step_q_field="Q_NOT_REGISTERED")),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("unknown STEP-Q field" in error for error in errors))

    def test_invalid_enum_reference(self):
        errors = validate_mapping_document(
            self.library(self.base_entry(step_q_enum="Q_NOT_REGISTERED")),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("invalid STEP-Q enum reference" in error for error in errors))

    def test_enum_must_belong_to_step_q_field(self):
        errors = validate_mapping_document(
            self.library(
                self.base_entry(
                    step_q_field="Q_TEST_REPORT",
                    step_q_enum="Q_PRODUCT_TYPE",
                    step_q_value="sheet",
                    context=None,
                )
            ),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("not allowed for STEP-Q field" in error for error in errors))

    def test_enum_value_must_exist(self):
        errors = validate_mapping_document(
            self.library(self.base_entry(step_q_value="not-a-material")),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("is not registered" in error for error in errors))

    def test_enum_mapping_requires_enum_metadata(self):
        errors = validate_mapping_document(
            self.library(
                self.base_entry(
                    step_q_enum=None,
                    step_q_value=None,
                    value_mode="literal",
                )
            ),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("require step_q_enum and step_q_value" in error for error in errors))

    def test_non_enum_mapping_rejects_enum_definition(self):
        errors = validate_mapping_document(
            self.library(
                self.base_entry(
                    step_q_field="Q_QUANTITY",
                    data_type="Integer",
                    value_mode="passthrough",
                    context=None,
                )
            ),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("passthrough mappings must not define" in error for error in errors))

    def test_material_sheet_context_is_valid(self):
        self.assertEqual(
            validate_mapping_document(
                self.library(self.base_entry()), self.schema, self.fields, self.enums
            ),
            [],
        )

    def test_material_wrong_context_enum_is_rejected(self):
        errors = validate_mapping_document(
            self.library(
                self.base_entry(
                    step_q_enum="Q_TUBE_MATERIAL",
                    step_q_value="E235 S2 (EN 10305-1)·nahtlos · kaltgefertigt · gebeizt",
                    context={"product_type": "sheet"},
                )
            ),
            self.schema,
            self.fields,
            self.enums,
        )
        self.assertTrue(any("not allowed for STEP-Q field" in error for error in errors))

    def test_duplicate_mapping_id(self):
        first = self.base_entry()
        second = self.base_entry()
        errors = validate_documents(
            [
                (Path("first/mapping.yaml"), self.library(first, library_id="first")),
                (Path("second/mapping.yaml"), self.library(second, library_id="second")),
            ]
        )
        self.assertTrue(any("duplicate mapping_id" in error for error in errors))

    def test_orderspot_source_collision(self):
        library = load_yaml_json("mappings/orderspot/mapping.yaml")
        duplicate = copy.deepcopy(library["mappings"][0])
        duplicate["mapping_id"] = "orderspot.test.collision"
        library["mappings"].append(duplicate)
        errors = validate_orderspot(library, source_rows())
        self.assertTrue(any("Orderspot source collision" in error for error in errors))

    def test_orderspot_source_identity_missing(self):
        library = load_yaml_json("mappings/orderspot/mapping.yaml")
        library["mappings"][0]["source_identity"]["surfaceNorm"] = "NOT_IN_SOURCE"
        errors = validate_orderspot(library, source_rows())
        self.assertTrue(any("source identity not found" in error for error in errors))

    def test_bidirectional_mapping_rejected_when_ambiguous(self):
        library = load_yaml_json("mappings/orderspot/mapping.yaml")
        second = copy.deepcopy(library["mappings"][1])
        second["mapping_id"] = "orderspot.test.ambiguous"
        second["source_identity"] = {
            "materialTypeNumber": "33.535",
            "surfaceNorm": "1sF",
            "productionMethod": "gewalzt H111",
        }
        library["mappings"].append(second)
        errors = validate_orderspot(library, source_rows())
        self.assertTrue(any("bidirectional source identity is not unique" in error for error in errors))

    def test_generic_discovery_finds_multiple_libraries(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ("platform_a", "platform_b"):
                library_dir = root / name
                library_dir.mkdir()
                (library_dir / "mapping.yaml").write_text("{}", encoding="utf-8")
            self.assertEqual(
                [path.parent.name for path in discover_mapping_libraries(root)],
                ["platform_a", "platform_b"],
            )


if __name__ == "__main__":
    unittest.main()
