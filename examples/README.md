## Examples

This directory contains draft STEP-Q214 example files for evaluation.

### minimal.step

Purpose:

- show the smallest useful metadata slice for early validation
- demonstrate the expected STEP-Q214 container name
- provide a stable input for the MVP validator

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

	python tools/validate_step_q214.py examples/minimal.step

### partial.step

Purpose:

- demonstrate a parsable file with an extension field
- show how a documented but unregistered field can be tracked during evaluation

Included fields:

- Q_PART_ID
- Q_PRIMARY_PROCESS
- Q_QUANTITY
- Q_THREAD_SPEC

Expected validator result:

- conformance: partial
- errors: 0
- warnings: 1

Validation command:

	python tools/validate_step_q214.py examples/partial.step --documented-extension Q_THREAD_SPEC

### full.step

Purpose:

- demonstrate the registered core field set in one file
- provide a richer fixture for validator and exporter work

Expected validator result:

- conformance: full
- errors: 0
- warnings: 0

Validation command:

	python tools/validate_step_q214.py examples/full.step

### invalid_unknown_extension.step

Purpose:

- demonstrate a non-conformant file
- verify that the validator reports both range and extension errors

Expected validator result:

- conformance: non
- errors: 2
- warnings: 0

Validation command:

	python tools/validate_step_q214.py examples/invalid_unknown_extension.step

