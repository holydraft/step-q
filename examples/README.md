## Examples

This directory contains draft STEP-Q214 example files for evaluation.

Recommended naming convention:

- files that already contain STEP-Q214 metadata use the suffix `.Q.STEP`
- raw source exports without STEP-Q214 metadata keep their original `.STEP` or `.STP` names
- the suffix is recommended for visibility only; conformance is still determined from file content

## Validation Fixtures

These files are controlled fixtures for validator behavior, conformance classes,
and expected findings.

All positive fixtures include a minimal AP214-style product and shape scaffold,
so STEP-Q214 metadata is shown in the context of a part representation,
not as a metadata-only shell.

### minimal.Q.STEP

Purpose:

- show the smallest useful metadata slice for early validation
- demonstrate the expected STEP-Q214 container name
- provide a stable input for the MVP validator
- include a minimal AP214-style product definition and shape representation

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

	python tools/validate_step_q214.py examples/minimal.Q.STEP

### partial.Q.STEP

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

	python tools/validate_step_q214.py examples/partial.Q.STEP --documented-extension Q_SPECIAL_THREAD_NOTE

### full.Q.STEP

Purpose:

- demonstrate the registered core field set in one file
- provide a richer fixture for validator and exporter work
- exercise drawing-driven supplementary fields alongside the core RFQ fields

Expected validator result:

- conformance: full
- errors: 0
- warnings: 0

Validation command:

	python tools/validate_step_q214.py examples/full.Q.STEP

### invalid_unknown_extension.Q.STEP

Purpose:

- demonstrate a non-conformant file
- verify that the validator reports both range and extension errors

Expected validator result:

- conformance: non
- errors: 2
- warnings: 0

Validation command:

	python tools/validate_step_q214.py examples/invalid_unknown_extension.Q.STEP

Expected shell behavior:

- exit code: 1
- this is intentional because the file is designed to demonstrate non-conformance

### invalid_malformed_entity.Q.STEP

Purpose:

- demonstrate a structural L1 error inside the DATA section
- verify that the parser reports malformed or unterminated STEP entity statements

Expected validator result:

- conformance: non
- errors: greater than `0`
- at least one message about a malformed or unterminated STEP entity statement

Validation command:

	python tools/validate_step_q214.py examples/invalid_malformed_entity.Q.STEP

## Reference Artifacts

These files represent real-world CAD exports and their STEP-Q214 annotation path.

### realSample.STEP

Purpose:

- provide a raw SolidWorks AP214 export as parser reference input
- demonstrate real geometry complexity without STEP-Q214 metadata
- serve as the baseline for the annotated companion file

Expected validator result:

- conformance: partial
- errors: 0
- warnings: 2

Validation command:

	python tools/validate_step_q214.py examples/realSample.STEP

### realSample.Q.STEP

Purpose:

- demonstrate the same SolidWorks export with a minimal STEP-Q214 metadata overlay
- provide a realistic adoption example for early implementers

Included fields:

- Q_PART_ID
- Q_MATERIAL
- Q_PRIMARY_PROCESS
- Q_QUANTITY
- Q_DRAWING_REFERENCE

Expected validator result:

- conformance: full
- errors: 0
- warnings: 0

Validation command:

	python tools/validate_step_q214.py examples/realSample.Q.STEP

