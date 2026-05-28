# STEP-Q214 Quickstart

This quickstart is the fastest way to evaluate the current STEP-Q214 draft.

## Scope

The current repository state is intended for evaluation and proof-of-implementability work.

What you can validate today:

- registered STEP-Q214 field names
- basic data types and enum values
- presence of the STEP-Q214 metadata container
- malformed or unterminated STEP entity statements in the `DATA;` section
- documented versus undocumented extension fields
- example conformance classification: full, partial, non

What is not covered yet:

- full AP214 geometry validation
- geometry-to-process plausibility checks
- production-grade importer behavior
- stable v1.0 compatibility guarantees

## Prerequisite

Python 3.11 or newer available on the command line.

## 5-Minute Evaluation Path

1. Validate the minimal example:

```powershell
python tools/validate_step_q214.py examples/minimal.Q.STEP
```

Expected outcome:

- conformance: `full`
- errors: `0`
- warnings: `0`

2. Validate the partial example with one documented extension:

```powershell
python tools/validate_step_q214.py examples/partial.Q.STEP --documented-extension Q_SPECIAL_THREAD_NOTE
```

Expected outcome:

- conformance: `partial`
- errors: `0`
- warnings: `1`

3. Validate the intentional error case:

```powershell
python tools/validate_step_q214.py examples/invalid_unknown_extension.Q.STEP
```

Expected outcome:

- conformance: `non`
- errors: greater than `0`
- process exit code: `1`

4. Validate a structural L1 error case:

```powershell
python tools/validate_step_q214.py examples/invalid_malformed_entity.Q.STEP
```

Expected outcome:

- conformance: `non`
- errors: greater than `0`
- at least one message about a malformed or unterminated STEP entity statement

## How To Read The Output

The validator prints structured JSON.

Key fields:

- `conformance`: `full`, `partial`, or `non`
- `errors`: count of blocking conformance findings
- `warnings`: count of non-blocking findings
- `fields`: extracted STEP-Q214 metadata fields
- `messages`: individual validator findings

## Where To Go Next

- Read `SPEC.md` for the normative rules.
- Read `spec/fields.md` and `spec/enumerations.md` for the registered metadata model.
- Read `examples/README.md` for the purpose of each example file.
- Read `tools/README.md` for the current validator scope and limits.
