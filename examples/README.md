## Examples

This directory contains STEP fixtures for parser and validator evaluation.

## Important Context

- The validator now checks against the current v0.3 registries from:
  - `spec/fields.md`
  - `spec/enumerations.md`
  - `spec/materials.md`
- Several fixtures in this directory are legacy-style and intentionally contain fields outside the current v0.3 core.
- Conformance is determined from STEP content, not from filename.

## Validation Command

```powershell
python tools/validate_step_q.py examples/<file>.STEP
```

## Current Baseline Outcomes

These outcomes reflect the current validator behavior against v0.3 spec registries.

| File | Expected Conformance | Expected Notes |
|---|---|---|
| `minimal.STEP` | `full` | compact, fully v0.3-conformant fixture |
| `partial.STEP` | `partial` | one documented extension (`Q_SPECIAL_THREAD_NOTE`) with `--documented-extension` |
| `full.STEP` | `full` | broader v0.3-conformant turning fixture |
| `invalid_unknown_extension.STEP` | `non` | intentionally non-conformant extension content |
| `invalid_malformed_entity.STEP` | `non` | intentionally malformed STEP entity statement |
| `realSample.STEP` | `partial` | no STEP-Q metadata container/fields |
| `realSample.annotated.STEP` | `full` | real carrier with v0.3-compliant metadata block |

## Fixture Intent

- `invalid_*` files are negative fixtures and should continue to fail.
- `realSample.STEP` is a raw carrier reference (no STEP-Q metadata).
- legacy positive fixtures are kept for parser/backward-compatibility regression checks while the repository transitions examples to native v0.3 field sets.
