# STEP-Q

STEP-Q is a lightweight RFQ metadata layer for STEP files.

STEP-Q is application-protocol agnostic. It can be used with AP203, AP214, AP242, or sidecar-based STEP exchange. AP203, AP214, and AP242 are possible STEP carrier formats for STEP-Q metadata.

STEP-Q makes quotation-relevant manufacturing information explicit and machine-readable. It complements existing STEP geometry with structured request, quotation, manufacturing, quality, and commercial metadata that is often scattered across drawings, emails, comments, and assumptions.

Developed and maintained by **holydraft**.

---

## Positioning

STEP-Q does not redefine geometry.

STEP-Q does not replace AP242, PMI, ISO GPS, technical drawings, CAM, ERP, or quality management systems.

Instead, STEP-Q adds a small, explicit metadata layer for supplier exchange and quotation workflows:

- material, quantity, and process assumptions
- drawing-driven requirements that matter for quoting
- quality, certificate, packaging, and delivery signals
- commercial or procurement-side metadata that needs to travel with the technical model

Practical goal:

> Make STEP-based supplier exchange more explicit, structured, and automatable.

---

## Architecture

STEP-Q is organized into four linked parts:

- **STEP-Q Core**: field names, data types, meanings, required or optional status, and validation semantics
- **STEP carrier compatibility**: how the same STEP-Q metadata can travel with AP203, AP214, AP242, or neutral sidecar exchange
- **Metadata embedding methods**: p21 property-entity embedding, sidecar formats, and other transport options
- **Validation rules**: structural, syntactic, and semantic checks plus parser-resilience requirements

The current repository contains working examples and tooling around a p21/property-entity embedding profile.

---

## Repository Structure

    /README.md Project overview (this file)
    /SPEC.md Normative STEP-Q umbrella specification

    /spec/
    core.md STEP-Q Core overview
    carrier-compatibility.md Carrier model and scope
    embedding.md Metadata embedding methods
    fields.md Field catalog and definitions
    enumerations.md Enumeration registry
    validation.md Validation and conformance rules

    /examples/
    minimal.STEP Minimal conformant example
    partial.STEP Partial metadata example (fallback case)
    full.STEP Rich metadata example

    /CONTRIBUTING.md Contribution guidelines
    /GOVERNANCE.md Maintainer and decision process
    /ROADMAP.md Planned versions and scope growth
    /CHANGELOG.md Release history for published drafts
    /LICENSE License

---

## Documents

### Core Specification
- SPEC.md: normative umbrella document for STEP-Q
- spec/core.md: STEP-Q Core structure and principles
- spec/carrier-compatibility.md: equal treatment of AP203, AP214, AP242, and neutral exchange forms
- spec/embedding.md: current embedding profiles and transport options
- spec/fields.md: detailed field definitions
- spec/enumerations.md: controlled vocabulary and change process
- spec/validation.md: validation logic and parser resilience requirements
- QUICKSTART.md: short evaluation path for the current draft

### Examples
- examples/: reference fixtures for current draft tooling

### Reference Tooling
- tools/README.md: current validator and browser-tooling scope
- tools/step_q_form.html: browser UI for reading, validating, and writing STEP-Q data

### Project Governance
- CONTRIBUTING.md: contribution process
- GOVERNANCE.md: maintainer structure
- ROADMAP.md: planned evolution
- CHANGELOG.md: release history
- LICENSE: usage and redistribution terms

### Project Checks
- .github/workflows/validate-examples.yml: example-based validation checks for pull requests and pushes to `main`

---

## Status

- Current version: **v0.2 (Evaluable Public Draft)**
- STEP-Q is not an ISO standard; it is an open draft specification under active development.
- The current publication state is an evaluable public draft with working examples and minimal reference tooling.

If you are evaluating STEP-Q for implementation or public review, start with QUICKSTART.md and treat the current tooling as draft evaluation tooling, not as a production validation stack.

---

## What To Expect Today

STEP-Q is currently intended for technical evaluation, early feedback, and proof-of-implementability work.

It is not yet positioned as a production-ready industrial standard.

Current priorities:

- stabilize STEP-Q Core
- keep examples and tooling aligned with the draft field registry
- document carrier-agnostic usage clearly
- provide a short, reproducible evaluation path for implementers and partners

Current distribution convention:

- STEP-Q content is identified by metadata inside the exchange payload, not by filename
- annotated files may either update the original STEP file or be written as a separate copy
- when a separate annotated copy is created, the copy should carry an explicit user-chosen suffix before `.STEP` or `.STP`, for example `realSample.rfq.STEP`
- raw STEP exports without STEP-Q metadata should keep their normal `.STEP` or `.STP` names

---

## Evaluation Focus

The shortest path to evaluating STEP-Q is:

1. Read the normative core in SPEC.md
2. Review the registered fields and enums in spec/
3. Inspect the example STEP files in examples/
4. Run the reference validation tooling for your target draft version

Current MVP command:

    python tools/validate_step_q.py examples/minimal.STEP

For a guided first run, see QUICKSTART.md.

To use the browser form locally, run a static server from the repository root (for example `python -m http.server 8080`) and open:

    http://localhost:8080/tools/step_q_form.html

For repeatable CLI and CI checks, continue using:

    python tools/validate_step_q.py examples/minimal.STEP

---

## References

STEP-Q is intended to complement existing STEP standards and institutions, including:

- ISO 10303 as the broader STEP family
- ISO 10303-203 (AP203)
- ISO 10303-214 (AP214)
- ISO 10303-242 (AP242)
- ISO TC 184/SC 4
- PDES, Inc.

Official resources:

- https://www.iso.org/committee/54158.html
- https://committee.iso.org/home/tc184sc4
- https://www.pdesinc.org
- https://www.steptools.com/stds/

---

## Contributing

Contributions are welcome via pull requests.

See **CONTRIBUTING.md**.

For bug reports, conformance questions, or draft feedback, open a GitHub issue and link the relevant example file, validator output, or specification section when possible.

---

## Contact

Manuel Scholz
holydraft (manupa GbR)  
https://www.holydraft.de  
manuel@holydraft.com
