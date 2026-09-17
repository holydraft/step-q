import unittest

from tools.validate_mappings import load_yaml_json, validate


class MappingContractTests(unittest.TestCase):
    def test_orderspot_library_matches_current_registries(self):
        self.assertEqual(validate(), [])

    def test_schema_declares_required_mapping_fields(self):
        schema = load_yaml_json("mappings/mapping-schema.yaml")
        required = set(schema["required_mapping_fields"])
        self.assertTrue({"source_field", "step_q_field", "data_type"} <= required)
        self.assertIn("source_to_step_q", schema["mapping_directions"])
        self.assertIn("unmapped", schema["mapping_status_values"])


if __name__ == "__main__":
    unittest.main()
