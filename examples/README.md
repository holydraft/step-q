## Examples

This directory contains draft STEP-Q example files for evaluation.

Example naming convention in this repository:

- annotated example fixtures use ordinary `.STEP` names when no raw counterpart exists
- annotated companion files use a descriptive suffix before the STEP extension when they must sit next to a raw export
- the local workbench requires the user to enter that suffix whenever it creates a copy on the write side
- conformance is determined from file content, not from filename

## Validation Fixtures

These files are controlled fixtures for validator behavior, conformance classes,
and expected findings.

All positive fixtures include a compact STEP product and shape scaffold,
so STEP-Q metadata is shown in the context of a part representation,
not as a metadata-only shell.

The invalid fixtures also keep a small carrier scaffold,
so their STEP-Q numbering and block placement still mirror realistic annotated files.

### minimal.STEP

Purpose:

- show the smallest useful metadata slice for early validation
- demonstrate a conformant annotated STEP container
- provide a stable input for the MVP validator
- include a minimal product definition and shape representation

Included fields:

- Q_PART_ID
- Q_MATERIAL
- Q_PRIMARY_PROCESS
- Q_QUANTITY

Expected validator result:

- conformance: full
- errors: 0
- warnings: 0

Validation command:

	python tools/validate_step_q.py examples/minimal.STEP

### partial.STEP

Purpose:

- demonstrate a parsable file with an extension field
- show how registered drawing-driven fields and a documented extension can coexist during evaluation

Included fields:

- Q_PART_ID
- Q_PRIMARY_PROCESS
- Q_QUANTITY
- Q_THREAD_SPEC
- Q_THREAD_DEPTH
- Q_SPECIAL_THREAD_NOTE

Expected validator result:

- conformance: partial
- errors: 0
- warnings: 1

Validation command:

	python tools/validate_step_q.py examples/partial.STEP --documented-extension Q_SPECIAL_THREAD_NOTE

### full.STEP

Purpose:

- demonstrate the registered core field set in one file
- provide a richer fixture for validator and exporter work
- exercise drawing-driven supplementary fields alongside the core RFQ fields

Expected validator result:

- conformance: full
- errors: 0
- warnings: 0

Validation command:

	python tools/validate_step_q.py examples/full.STEP

### invalid_unknown_extension.STEP

Purpose:

- demonstrate a non-conformant file
- verify that the validator reports both range and extension errors

Expected validator result:

- conformance: non
- errors: 2
- warnings: 0

Validation command:

	python tools/validate_step_q.py examples/invalid_unknown_extension.STEP

Expected shell behavior:

- exit code: 1
- this is intentional because the file is designed to demonstrate non-conformance

### invalid_malformed_entity.STEP

Purpose:

- demonstrate a structural L1 error inside the DATA section
- verify that the parser reports malformed or unterminated STEP entity statements

Expected validator result:

- conformance: non
- errors: greater than `0`
- at least one message about a malformed or unterminated STEP entity statement

Validation command:

	python tools/validate_step_q.py examples/invalid_malformed_entity.STEP

## Reference Artifacts

These files represent real-world CAD exports and their STEP-Q annotation path.

### realSample.STEP

Purpose:

- provide a raw SolidWorks AP214 export as parser reference input
- demonstrate real geometry complexity without STEP-Q metadata
- serve as the baseline for the annotated companion file

Expected validator result:

- conformance: partial
- errors: 0
- warnings: 2

Expected warnings:

- `STEP-Q PROPERTY_SET container not found`
- `No STEP-Q metadata fields found`

Validation command:

	python tools/validate_step_q.py examples/realSample.STEP

### realSample.annotated.STEP

Purpose:

- demonstrate the same SolidWorks export with a minimal STEP-Q metadata overlay
- provide a realistic adoption example for early implementers
- show one concrete repository convention for the user-chosen copy suffix workflow

Included fields:

- Q_QUANTITY
- Q_SURFACE
- Q_CERTIFICATE
- Q_THREAD_SPEC
- Q_THREAD_DEPTH

Expected validator result:

- conformance: full
- errors: 0
- warnings: 0

Validation command:

	python tools/validate_step_q.py examples/realSample.annotated.STEP

