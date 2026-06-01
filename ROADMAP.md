# STEP-Q Roadmap

Maintained by holydraft

---

## 1. Purpose

This document describes the planned evolution of the STEP-Q specification.

It provides transparency regarding scope, priorities, and development stages.

The roadmap is indicative and may be adjusted based on implementation feedback.

---

## 2. Versioning Model

STEP-Q follows semantic versioning:

- v0.x — Draft and experimental phase
- v1.x — Stable industrial draft release
- v2.x — Major functional revision

Backward compatibility is expected within major versions.

---

## 3. Current Status

### v0.2 — Validation and Examples (Current)

Focus:

- normative clarification for parser tolerance vs. conformance
- complete example STEP files
- minimal reference validator/parser for evaluable draft releases
- local evaluation tooling and quickstart guidance

Status: Released

---

## 4. Short-Term Roadmap (v0.x Series)

### v0.3 — STEP-Q Core Stabilization

Planned features:

- stabilize STEP-Q Core terminology and scope
- align repository documentation to the carrier-agnostic STEP-Q model
- document current examples and tools as AP-agnostic repository assets
- improve extension handling and embedding-profile clarity across current examples and tools

Target: clearer draft semantics and lower implementation ambiguity

---

### v0.4 — Integration and Exchange Profiles

Planned features:

- mapping guides for major platforms
- API integration examples
- metadata extraction libraries
- importer best practices
- documented JSON sidecar exchange profile
- documented comment-block or neutral embedding profile

Target: first production pilots and clearer exchange guidance

---

### v0.5 — Toolchain Support

Planned features:

- JSON Schema
- CLI validation improvements
- automated conformance tests
- clearer profile documentation for direct embedding versus sidecar exchange

Target: repeatable implementation support

---

## 5. Medium-Term Roadmap (v1.x Series)

### v1.0 — Stable STEP-Q Core

Planned features:

- frozen core field set
- stable enumeration registry
- interoperability review cycle
- carrier-agnostic conformance guidance

Target: production-ready core draft

---

### v1.1–v1.5 — Broader Carrier Examples

Planned features:

- curated examples for AP203, AP214, and AP242 carriers
- sidecar JSON examples
- logistics and packaging metadata growth
- certificate and quality handoff refinements
- platform-facing import/export guides

Target: broader industrial adoption without privileging a single carrier

---

## 6. Long-Term Roadmap (v2.x Series)

### v2.0 — Extended Manufacturing Intelligence

Planned features:

- advanced process modeling
- cost estimation models
- sustainability indicators
- CO2 footprint metadata
- energy consumption parameters

Target: decision-support standard

---

### AP242 and MBD Integration Extensions (Concept)

Long-term vision:

- deeper interoperability with AP242-based workflows
- optional MBD and PMI-adjacent integration patterns
- clearer links between STEP-Q quotation metadata and richer engineering datasets

Status: Conceptual

This is an extension path, not a replacement of STEP-Q Core and not a preferred near-term mainline.

---

## 7. Research and Standardization Path

Potential future directions:

- cooperation with research institutions
- industry consortium formation
- DIN or ISO pre-standardization
- public funding projects

These activities are exploratory.

---

## 8. Review and Update Process

The roadmap is reviewed at least once per year.

Updates are published via:

- GitHub releases
- changelog updates
- public announcements

---

## 9. Disclaimer

This roadmap represents current intentions.

No legal or commercial obligations are implied.
