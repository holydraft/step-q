# STEP-Q Specification

Version: v0.2 (Evaluable Public Draft)
Status: Public Evaluable Draft
Maintainer: holydraft
Author: Manuel Scholz
Date: 2026-06-01

---

## 1. Purpose

STEP-Q is a lightweight RFQ metadata layer for STEP files.

STEP-Q is application-protocol agnostic. It defines a small, explicit metadata model for quotation and supplier-exchange workflows without redefining the underlying geometry.

STEP-Q makes quotation-relevant manufacturing information explicit and machine-readable.

---

## 2. Scope

This specification applies to:

- individual parts
- assemblies
- industrial manufacturing requests
- supplier-exchange workflows where quotation-relevant metadata must travel with or next to a STEP model

It is intended for use in:

- online manufacturing platforms
- ERP and quotation systems
- procurement and supplier portals
- costing and pre-manufacturing workflows
- hybrid and manual quotation processes

Excluded from scope:

- geometry definition itself
- production planning
- CAM toolpaths
- machine parameters
- quality inspection planning
- shopfloor scheduling
- ERP execution logic

---

## 3. Positioning and Non-Goals

STEP-Q does not redefine geometry.

STEP-Q does not replace AP242, PMI, ISO GPS, technical drawings, CAM, ERP, or quality management systems.

STEP-Q complements STEP-based geometry exchange by defining a stable metadata vocabulary for information that is often needed during request-for-quotation, supplier qualification, manufacturability review, and offer preparation.

---

## 4. Normative References

The following references are relevant to the application context of this draft:

- ISO 10303 as the broader STEP family
- ISO 10303-203 (AP203)
- ISO 10303-214 (AP214)
- ISO 10303-242 (AP242)
- ISO TC 184/SC 4

Informative references:

- STEP Tools — STEP Standards Overview
- PDES, Inc.

This draft does not define a new STEP application protocol.

---

## 5. STEP-Q Core

STEP-Q Core defines:

- registered field names
- data types and allowed formats
- field meanings
- controlled vocabularies
- validation semantics
- parser tolerance requirements

The normative STEP-Q Core registry is defined in:

    spec/fields.md

Controlled vocabularies are defined in:

    spec/enumerations.md

All STEP-Q Core fields shall use the prefix:

    Q_

Only registered fields shall be used in conformant files unless an extension is explicitly documented.

---

## 6. STEP Carrier Compatibility

STEP-Q can be used with AP203, AP214, AP242, or sidecar-based STEP exchange.

AP203, AP214, and AP242 are possible STEP carrier formats for STEP-Q metadata.

Carrier compatibility is defined by the following principles:

1. STEP-Q Core is independent of any single STEP application protocol.
2. Geometry and topology remain governed by the carrier format in use.
3. A carrier format may transport STEP-Q metadata directly inside the p21 payload or indirectly through a linked sidecar.
4. No carrier shall be treated as the sole, preferred, or defining implementation of STEP-Q.

Additional carrier guidance is provided in:

    spec/carrier-compatibility.md

---

## 7. Metadata Embedding Methods

STEP-Q may be exchanged through one of the following embedding methods:

- p21 property-entity embedding inside a STEP file
- sidecar metadata linked to a STEP file
- documented future embedding methods that preserve the STEP-Q Core vocabulary

The current repository examples and reference tools demonstrate a p21/property-entity embedding profile using:

- PROPERTY_SET
- PROPERTY_DEFINITION
- DESCRIPTIVE_REPRESENTATION_ITEM

In this profile, the metadata container shall be identified by:

    PROPERTY_SET('STEP-Q', ...)

Additional embedding guidance is provided in:

    spec/embedding.md

---

## 8. Naming and Distribution Conventions

No special filename suffix is required for STEP payloads that contain STEP-Q metadata.

When an annotated companion file needs to be distinguished from a raw export, implementations may use an explicit workflow suffix before the STEP extension, such as:

    realSample.rfq.STEP

This naming remains informative only and is not required for conformance.

Parsers and validators shall identify STEP-Q by file content, not by filename.

---

## 9. Validation and Parser Requirements

Validation rules are defined in:

    spec/validation.md

Implementations shall comply with the following principles:

- missing fields shall not cause parsing errors
- missing values shall not cause parsing errors
- missing metadata containers shall not cause parser aborts
- unknown or unsupported extensions shall not cause parser aborts
- fallback to manual completion remains mandatory

Parsers and quotation systems shall tolerate:

- incomplete metadata sets
- partial field definitions
- empty values
- unknown future extensions

No hard failures shall occur solely due to metadata issues.

---

## 10. Conformance

For conformance evaluation, STEP-Q distinguishes between parser tolerance and specification conformance.

A STEP payload is fully conformant with STEP-Q if:

- metadata is stored according to a documented STEP-Q embedding method
- only registered Q_ fields are used, except for documented extensions
- values conform to defined data types
- unsupported metadata does not break import continuity

Partial conformance is permitted when:

- metadata is structurally parseable
- registered fields used in the file remain valid
- extension metadata does not invalidate the overall import path

Non-conformance applies when core structural or syntactic rules are violated.

---

## 11. Extensions

Custom extensions are permitted if:

- they use the prefix Q_
- they are documented
- they do not override registered fields

Documented extensions may be used for experimentation and bilateral integration, but they are outside full conformance until officially registered.

Undocumented extensions are non-conformant.

Parsers shall ignore unsupported extensions for import continuity, while validators may report them in conformance output.

---

## 12. Intellectual Property

STEP-Q is developed and maintained by holydraft.

This specification is not an ISO standard and implies no ISO certification.

No rights are waived by publication.

---

## 13. Versioning

Semantic versioning is applied.

- v0.x — Draft
- v1.x — Stable
- v2.x — Major revision

Backward compatibility shall be maintained within a major version.

---

## 14. Governance

Changes to this specification are managed via GitHub pull requests.

All changes are subject to maintainer review.

---

## 15. Document Control

This document is the normative umbrella reference for STEP-Q.

In case of conflicts, this document prevails over supplementary materials.
