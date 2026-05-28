# STEP-Q214

STEP-Q214 defines a standardized metadata layer for STEP AP214 files, focused on quotation (RFQ) and pricing workflows for industrially manufacturable parts and assemblies.

It is designed to work across online platforms, internal ERP/CAM systems, manufacturer software, and hybrid (semi-manual) quotation processes.

Developed and maintained by **holydraft**.

---

## References

STEP-Q214 is based on and aligned with existing STEP standards and organizations:

- ISO 10303-214 — Automotive Design (AP214)
- ISO TC 184/SC 4 — Industrial data
- PDES, Inc. — Product Data Exchange using STEP

Official resources:

- https://www.iso.org/standard/63141.html
- https://www.iso.org/committee/54158.html (https://committee.iso.org/home/tc184sc4)
- https://www.pdesinc.org
- https://www.steptools.com/stds/

---

## Purpose

Manufacturing buyers and quotation teams repeatedly enter the same information into forms and pricing systems (material, quantity, tolerances, surface, certificates, delivery targets, etc.). STEP-Q214 embeds these RFQ-relevant parameters directly into the STEP file in a structured, machine-readable way.

Goal: enable a reliable, low-friction conversion of technical requests into binding quotations by allowing quotation engines to automatically discover and interpret metadata from STEP-Q214 files.

---

## Key Principles

- Based on **ISO 10303-214 (STEP AP214)** geometry and topology
- **Backward compatible** with standard AP214 parsers
- **No modification** of core geometry entities
- Metadata stored only via standard AP214 entities (no proprietary entity types)
- Strong **fallback**: all fields are optional; missing data must not cause parse errors

---

## Repository Structure
    
    /README.md Project overview (this file)
    /SPEC.md Normative core specification
    
    /spec/
    fields.md Field catalog and definitions
    enumerations.md Enumeration registry
    validation.md Validation and conformance rules
    
    /examples/
    minimal.Q.STEP Minimal conformant example
    partial.Q.STEP Partial metadata example (fallback case)
    full.Q.STEP Fully populated metadata example
    
    /CONTRIBUTING.md Contribution guidelines
    /GOVERNANCE.md Maintainer and decision process
    /ROADMAP.md Planned versions and scope growth
    /LICENSE.md License

---

## Documents

### Core Specification
- SPEC.md: Normative core rules (what is required for STEP-Q214 conformance)
- spec/fields.md: Detailed field definitions (types, semantics, examples)
- spec/enumerations.md: Controlled vocabulary (enums) and change process
- spec/validation.md: Technical validation + parser resilience requirements
- QUICKSTART.md: 5-minute evaluation path for the current draft

### Examples
- examples/: Reference STEP files for implementers

### Reference Tooling
- tools/README.md — Current MVP validator scope and usage

### Project Governance
- CONTRIBUTING.md — Contribution process
- GOVERNANCE.md — Maintainer structure
- ROADMAP.md — Planned evolution
- LICENSE — Usage and redistribution

---

## Status

- Current version: **v0.1 (Draft)**
- This is not an ISO standard; it is an open specification under active development.
- Current publication goal: a **v0.2 evaluable public draft** with working examples and minimal reference tooling.

---

## What To Expect Today

STEP-Q214 is currently intended for technical evaluation, early feedback,
and proof-of-implementability work.

It is not yet positioned as a production-ready industrial standard.

Current priorities:

- clarify the normative core for early adopters
- provide real example STEP files
- provide a minimal reference validator/parser
- document a short evaluation path for implementers and partners

Recommended distribution convention:

- STEP-Q214 content is identified by metadata inside the file, not by filename
- `.Q.STEP` is recommended as a visibility convention for STEP-Q214 example, exchange, and marketing artifacts
- raw AP214 exports without STEP-Q214 metadata should keep their normal `.STEP` or `.STP` names

---

## Evaluation Focus

The shortest path to evaluating STEP-Q214 is:

1. Read the normative core in SPEC.md
2. Review the registered fields and enums in spec/
3. Inspect the example STEP files in examples/
4. Run the reference validation tooling for your target draft version

The v0.2 release is intended to make this evaluation path explicit and reproducible.

Current MVP command:

    python tools/validate_step_q214.py examples/minimal.Q.STEP

For a guided first run, see QUICKSTART.md.

---

## Contributing

Contributions are welcome via pull requests.

See **CONTRIBUTING.md**.

---

## Contact

Manuel Scholz
holydraft (manupa GbR)  
https://www.holydraft.de  
manuel@holydraft.com
