# Reference Tooling

This directory contains the current STEP-Q214 reference tooling for draft evaluation.

## validate_step_q214.py

`validate_step_q214.py` is the current MVP reference validator and metadata parser.

Current behavior:

- reads the STEP file header and trailer
- isolates the `DATA;` section
- parses STEP entity assignments line-by-line
- reports malformed or unterminated STEP entity statements inside the `DATA;` section
- detects the `PROPERTY_SET('STEP-Q214', ...)` metadata container
- extracts `DESCRIPTIVE_REPRESENTATION_ITEM` entries whose names begin with `Q_`
- validates registered fields against the draft registry embedded in the script
- distinguishes documented extensions from undocumented extensions
- emits structured JSON findings

Current limits:

- no full AP214 entity graph validation
- no topology or geometry plausibility analysis
- no semantic cross-checks such as material versus surface compatibility
- registry definitions are still embedded in the script, not yet generated from the spec documents

## Usage

Minimal example:

```powershell
python tools/validate_step_q214.py examples/minimal.Q.STEP
```

Partial example with a documented extension:

```powershell
python tools/validate_step_q214.py examples/partial.Q.STEP --documented-extension Q_SPECIAL_THREAD_NOTE
```

Intentional non-conformant example:

```powershell
python tools/validate_step_q214.py examples/invalid_unknown_extension.Q.STEP
```

Structural error example:

```powershell
python tools/validate_step_q214.py examples/invalid_malformed_entity.Q.STEP
```

## Exit Codes

- `0`: no validation errors were reported
- `1`: at least one validation error was reported

Warnings do not change the exit code unless errors are also present.

## Intended Role In v0.2

This validator is intended to prove that STEP-Q214 metadata can be found, extracted, and checked in a reproducible way.

It is not yet intended to serve as a production importer or as a complete STEP/AP214 validator.
