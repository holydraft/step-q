# STEP-Q Quickstart

This quickstart is the fastest way to evaluate the current STEP-Q draft.

## Scope

The current repository state is intended for evaluation and proof-of-implementability work.

What you can validate today:

- registered STEP-Q field names
- basic data types and enum values
- presence of the STEP-Q metadata container
- malformed or unterminated STEP entity statements in the `DATA;` section
- documented versus undocumented extension fields
- example conformance classification: full, partial, non

What is not covered yet:

- full carrier-specific geometry validation
- geometry-to-process plausibility checks
- production-grade importer behavior
- stable v1.0 compatibility guarantees

## Prerequisite

Python 3.11 or newer available on the command line.

## 5-Minute Evaluation Path

1. Validate the minimal example:

```powershell
python tools/validate_step_q.py examples/minimal.STEP
```

Expected outcome:

- conformance: `full`
- errors: `0`
- warnings: `0`

2. Validate the partial example with one documented extension:

```powershell
python tools/validate_step_q.py examples/partial.STEP --documented-extension Q_SPECIAL_THREAD_NOTE
```

Expected outcome:

- conformance: `partial`
- errors: `0`
- warnings: `1`

3. Validate the intentional error case:

```powershell
python tools/validate_step_q.py examples/invalid_unknown_extension.STEP
```

Expected outcome:

- conformance: `non`
- errors: greater than `0`
- process exit code: `1`

4. Validate a structural L1 error case:

```powershell
python tools/validate_step_q.py examples/invalid_malformed_entity.STEP
```

Expected outcome:

- conformance: `non`
- errors: greater than `0`
- at least one message about a malformed or unterminated STEP entity statement

5. Validate the raw carrier sample without STEP-Q metadata:

```powershell
python tools/validate_step_q.py examples/realSample.STEP
```

Expected outcome:

- conformance: `partial`
- errors: `0`
- warnings: at least `2` (`PROPERTY_SET` missing and no STEP-Q fields found)

## How To Read The Output

The validator prints structured JSON.

Key fields:

- `conformance`: `full`, `partial`, or `non`
- `errors`: count of blocking conformance findings
- `warnings`: count of non-blocking findings
- `fields`: extracted STEP-Q metadata fields
- `messages`: individual validator findings

## Where To Go Next

- Read `SPEC.md` for the normative rules.
- Read `spec/fields.md` and `spec/enumerations.md` for the registered metadata model.
- Read `examples/README.md` for the purpose of each example file.
- Read `tools/README.md` for the current validator scope and limits.

## Browser Form

Use the HTML/JS form as the primary interactive workflow:

```powershell
python -m http.server 8080
```

Then open:

- `http://localhost:8080/tools/step_q_form.html`

The form lets you:

- choose product type and fill v0.3 fields from spec-driven catalogs
- load STEP files and prefill existing STEP-Q metadata
- overwrite the original file (with file-handle permission) or create a copy
- validate syntax before writing metadata
