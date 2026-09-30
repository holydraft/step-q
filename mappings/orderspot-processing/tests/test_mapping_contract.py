import unittest

from tools.validate_mappings import (
    SCHEMA_PATH,
    load_yaml_json,
    registered_enums,
    registered_fields,
    validate_mapping_document,
)


MAPPING_PATH = "mappings/orderspot-processing/mapping.yaml"
ENUM_MAPPING_PATH = "mappings/orderspot-processing/enum-mapping.yaml"


class OrderspotProcessingMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_yaml_json(SCHEMA_PATH)
        cls.fields = registered_fields()
        cls.enums = registered_enums()
        cls.library = load_yaml_json(MAPPING_PATH)

    def test_mapping_satisfies_generic_contract(self):
        errors = validate_mapping_document(
            self.library, self.schema, self.fields, self.enums
        )
        self.assertEqual(errors, [])

    def test_screenshot_confirmed_enum_choices_are_registered(self):
        mappings = {
            entry["mapping_id"]: entry
            for entry in self.library["mappings"]
        }
        expected_values = {
            "orderspot.processing.galvanizing.electro": "electro_galvanizing",
            "orderspot.processing.galvanizing.hot-dip": "hot_dip_galvanizing",
            "orderspot.processing.rolling-direction.unrestricted": "arbitrary",
            "orderspot.processing.rolling-direction.horizontal": "parallel",
            "orderspot.processing.rolling-direction.vertical": "perpendicular",
        }

        for mapping_id, expected_value in expected_values.items():
            with self.subTest(mapping_id=mapping_id):
                entry = mappings[mapping_id]
                self.assertEqual(entry["step_q_value"], expected_value)
                self.assertIn(expected_value, self.enums[entry["step_q_enum"]])

    def test_enum_labels_remain_manual_until_raw_source_codes_are_confirmed(self):
        partial_mappings = {
            entry["mapping_id"]
            for entry in self.library["mappings"]
            if entry["status"] == "partial"
        }
        self.assertEqual(
            partial_mappings,
            {
                "orderspot.processing.galvanizing.electro",
                "orderspot.processing.galvanizing.hot-dip",
                "orderspot.processing.rolling-direction.unrestricted",
                "orderspot.processing.rolling-direction.horizontal",
                "orderspot.processing.rolling-direction.vertical",
            },
        )

    def test_unmapped_switches_explain_target_semantic_gap(self):
        enum_policy = load_yaml_json(ENUM_MAPPING_PATH)
        unmapped = {
            entry["source_field"]: entry
            for entry in enum_policy["enum_mappings"]
            if entry.get("status") == "unmapped"
        }

        self.assertIn("orderspot.deburring", unmapped)
        self.assertIn("concrete deburring method", unmapped["orderspot.deburring"]["reason"])
        self.assertIn("orderspot.certificates", unmapped)
        self.assertIn("EN 10204 test-report type", unmapped["orderspot.certificates"]["reason"])


if __name__ == "__main__":
    unittest.main()