# Reference Tooling

This directory contains the current STEP-Q reference tooling for draft evaluation.

Runtime expectations:

- Python 3.11 or newer
- current scripts use the Python standard library only
- the workbench is primarily documented for local desktop use and relies on the local file dialog plus an auto-opened browser window

## validate_step_q.py

`validate_step_q.py` is the current MVP reference validator and metadata parser.

Current behavior:

- reads the STEP file header and trailer
- isolates the `DATA;` section
- parses STEP entity assignments line-by-line
- reports malformed or unterminated STEP entity statements inside the `DATA;` section
- detects the `PROPERTY_SET('STEP-Q', ...)` metadata container
- extracts `DESCRIPTIVE_REPRESENTATION_ITEM` entries whose names begin with `Q_`
- validates registered fields against the shared STEP-Q registry used by the tooling
- distinguishes documented extensions from undocumented extensions
- emits structured JSON findings

Current limits:

- no full carrier entity graph validation
- no topology or geometry plausibility analysis
- no semantic cross-checks such as material versus surface compatibility
- registry definitions are maintained in the shared Python registry module, not yet generated from the spec documents

## Usage

Minimal example:

```powershell
python tools/validate_step_q.py examples/minimal.STEP
```

Partial example with a documented extension:

```powershell
python tools/validate_step_q.py examples/partial.STEP --documented-extension Q_SPECIAL_THREAD_NOTE
```

Intentional non-conformant example:

```powershell
python tools/validate_step_q.py examples/invalid_unknown_extension.STEP
```

Structural error example:

```powershell
python tools/validate_step_q.py examples/invalid_malformed_entity.STEP
```

## Exit Codes

- `0`: no validation errors were reported
- `1`: at least one validation error was reported

Warnings do not change the exit code unless errors are also present.

## Intended Role In v0.2

This validator is intended to prove that STEP-Q metadata can be found, extracted, and checked in a reproducible way.

It is not yet intended to serve as a production importer or as a complete STEP carrier validator.

## step_q_workbench_web.py

`step_q_workbench_web.py` is the current local browser UI for both writing and reading STEP-Q data.

Current behavior:

- runs as a local web application on `127.0.0.1`
- opens the local browser automatically when started
- presents a responsive two-column layout that stacks on narrower screens
- requires source STEP files to be chosen through a Windows file dialog on both panels
- defaults to modifying the original file unless the user switches the write panel to copy mode
- presents a focused starter field set on the write side
- loads existing STEP-Q values from the selected write source into the form when present
- warns below the write inputs that loaded STEP-Q values will be overwritten when writing
- reads and validates STEP-Q metadata on the right side without modifying the selected file
- renders enum fields as dropdown selections from the shared registry
- inserts STEP-Q metadata at the start of the `DATA;` section
- requires a user-defined suffix whenever it writes a separate copy
- updates `FILE_DESCRIPTION` and `FILE_NAME` in the HEADER to reflect the file that was actually written
- validates the written or read file immediately

Usage:

```powershell
python tools/step_q_workbench_web.py
```

Optional arguments:

```powershell
python tools/step_q_workbench_web.py --host 127.0.0.1 --port 8765
```

Current limits:

- focused starter field set only, not the complete registry UI
- existing STEP-Q metadata is replaced by the new form values in the written file
- no multi-user or remote deployment support
