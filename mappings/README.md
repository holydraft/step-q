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

## Creating a Mapping Library and Source

Use the following workflow when adding an integration for a platform,
manufacturer, ERP, or other external system. The process is a recommended
working standard; projects may add stricter checks for their own integrations.

### 1. Define the boundary

- Keep STEP-Q fields, enums, meanings, and validation semantics in `spec/`.
- Keep external datasets in `sources/<system>/`.
- Keep translation rules and integration policy in `mappings/<system>/`.
- Decide whether the library imports into STEP-Q, exports from STEP-Q, or does
	both. Do not add platform-specific fields to STEP-Q Core.

### 2. Register the external source

Create `sources/<system>/` and add the source dataset only when its license,
provenance, and maintenance status permit repository storage. Add a
`sources/<system>/README.md` that records:

- system or provider name and source URL or other origin
- export or snapshot date and source version, if available
- file format, delimiter, encoding, and relevant schema details
- whether the file is a complete export, a filtered extract, or a fixture
- license, redistribution constraints, and responsible contact if known
- stable source identifiers used by mappings

If raw data cannot be committed, document the external reference and provide a
sanitized fixture or schema where practical. Never copy external data into
`spec/` merely to make a mapping validator convenient.

### 3. Create the library structure

Create `mappings/<system>/` with, at minimum:

```text
mappings/<system>/
	README.md
	mapping.yaml
	tests/
```

Add `enum-mapping.yaml`, examples, or a library-specific validator when the
integration needs them. In `mapping.yaml`:

- set a stable `library_id` and library version
- reference `../mapping-schema.yaml` through `mapping_schema`
- use `source_catalog` only for the relevant STEP-Q catalog
- use `source_data` for the path under `sources/<system>/`, when applicable
- define the external source identity and the STEP-Q target field or enum
- document direction, data type, units, requiredness, fallback, and rationale

### 4. Classify every mapping

Use the least optimistic status supported by evidence:

- `exact`: source meaning and relevant details are represented losslessly
- `normalized`: equivalent meaning with naming, punctuation, or language changes
- `partial`: some relevant detail is missing or only approximately represented
- `unmapped`: no sufficiently reliable target exists

`exact` mappings must be `lossless`. Use `bidirectional` only when source
identity and STEP-Q value are both unique and the conversion is lossless;
otherwise use a one-way direction. Do not silently replace `partial` or
`unmapped` values with generic materials or fields.

### 5. Add source-specific checks and tests

The generic validator checks the mapping contract, but each integration should
also verify its source-specific invariants. Typical checks include:

- every active mapping references an existing source record
- the source identity is present and unique where required
- no STEP-Q target is unintentionally mapped more than once
- bidirectional mappings are lossless and reversible
- source parsing handles the documented encoding and delimiter

Put these checks in `mappings/<system>/validate.py` and cover important edge
cases in `mappings/<system>/tests/`. Add representative source-to-STEP-Q and
STEP-Q-to-source examples when the direction is supported.

### 6. Validate and prepare review

Run the generic validator and the integration-specific checks from the
repository root:

```powershell
python tools/validate_mappings.py
python mappings/<system>/validate.py
python -m unittest discover -s mappings/<system>/tests
```

Before opening a pull request, confirm that source provenance is documented,
all referenced paths exist, no platform-specific metadata was added to
`spec/`, and the pull request explains direction, status, lossiness, fallback,
and any limitations or unmapped values.

### Minimum checklist

- [ ] The boundary between `spec/`, `sources/`, and `mappings/` is respected.
- [ ] Source provenance and redistribution status are documented.
- [ ] Source identifiers and their uniqueness rules are defined.
- [ ] `mapping.yaml` follows the generic mapping schema.
- [ ] Direction, status, lossiness, units, fallback, and rationale are explicit.
- [ ] `partial` and `unmapped` values are reported rather than hidden.
- [ ] Source-specific validation and focused tests exist where needed.
- [ ] Generic and integration-specific validation commands pass.
