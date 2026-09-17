# STEP-Q Mapping Libraries

This directory defines the integration layer between external RFQ systems and
STEP-Q. Mapping libraries are implementation assets, not part of the STEP-Q
Core vocabulary.

## Principles

- `spec/` remains the source of truth for STEP-Q fields, enums, materials, and validation.
- A mapping library declares how an external source is translated to or from registered STEP-Q fields and their controlled enums.
- A mapping must state direction, data type, unit, enum transformation, requiredness, lossiness, fallback behavior, and rationale.
- `exact` and `normalized` mappings may be automated when their library policy permits it.
- `partial` and `unmapped` values remain visible and must not silently fall back to a generic material or field.
- `source_to_step_q` imports external semantics into STEP-Q; `step_q_to_source` exports STEP-Q into an external system.
- `bidirectional` is reserved for mappings that are lossless and unique in both directions. A normalized or ambiguous mapping must use separate directions or remain one-way.
- Enum mappings use `value_mode: literal`, `step_q_enum`, and `step_q_value`.
- Direct field mappings use `value_mode: passthrough` without enum metadata, for example `Q_QUANTITY` or `Q_MICRO_JOINTS`.
- `status` is required; `exact` mappings must be `lossless`.
- `context` is optional and generic; it can carry minimal disambiguating context such as `product_type`.
- A declared `unit` must match the unit in the STEP-Q field registry.
- Mapping metadata does not extend the STEP-Q Core and must not be embedded as core fields.

## Schema

[mapping-schema.yaml](mapping-schema.yaml) is JSON-compatible YAML so the
reference validator can use Python's standard library without adding a runtime
dependency. It defines the common contract shared by platform libraries.

`value_mode: literal` is used for an external discrete value mapped to a
registered STEP-Q enum value. `value_mode: passthrough` is used for direct
field mappings such as integer quantities or Boolean flags and omits enum
metadata. Existing enum mappings without an explicit `value_mode` remain
backward-compatible and are interpreted as literal mappings by the validator.

## Libraries

- [Orderspot](orderspot/README.md): first reference material mapping library.

## Validation

Validate the mapping libraries locally with:

```powershell
python tools/validate_mappings.py
```

The generic check discovers `mappings/*/mapping.yaml` automatically and
validates the common contract against the STEP-Q field and enum registries.
Platform-specific source checks run separately in each mapping library.
