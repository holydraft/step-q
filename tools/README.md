# Reference Tooling

This directory contains the current STEP-Q reference tooling for v0.3 evaluation.

## Current Stack

- `step_q_form.html`: primary browser UI for reading, validating, and writing STEP-Q metadata.
- `validate_step_q.py`: CLI validator for reproducible checks in terminal and CI.
- `StepViewer_HTML/js/step-3d-viewer.js`: minimal viewer wrapper used by `step_q_form.html`.

The preferred workflow is HTML/JS-first. Python is retained only for validator automation.

## validate_step_q.py

`validate_step_q.py` validates STEP-Q content against the current spec registries:

- `spec/fields.md`
- `spec/enumerations.md`
- `spec/materials.md`

Current behavior:

- validates STEP envelope (`ISO-10303-21;` ... `END-ISO-10303-21;`)
- isolates and parses the `DATA;` section
- reports malformed or unterminated STEP entity statements
- detects `PROPERTY_SET('STEP-Q', ...)`
- extracts `DESCRIPTIVE_REPRESENTATION_ITEM('Q_*', '...')`
- validates field names and value types from the spec-driven registry
- validates enum values from `enumerations.md` and material values from `materials.md`
- supports documented extension fields via `--documented-extension`
- emits structured JSON findings

Current limits:

- no full carrier entity graph validation
- no topology or geometry plausibility analysis
- no process plausibility checks across multiple fields

## Usage

Validate one or more STEP files:

```powershell
python tools/validate_step_q.py examples/minimal.STEP
```

Mark extension fields as documented (warning instead of error):

```powershell
python tools/validate_step_q.py examples/partial.STEP --documented-extension Q_SPECIAL_THREAD_NOTE
```

## Exit Codes

- `0`: no validation errors were reported
- `1`: at least one validation error was reported

Warnings do not change the exit code unless errors are also present.

## Notes

- The validator now follows the v0.3 spec files directly and no longer uses a separate Python field registry.
- Legacy example files may contain fields that are intentionally outside the current v0.3 core registry.
