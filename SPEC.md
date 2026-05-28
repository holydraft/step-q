# STEP-Q214 Specification

Version: v0.1 (Draft)  
Status: Public Draft  
Maintainer: holydraft  
Author: Manuel Scholz  
Date: 2026-02-11

---

## 1. Purpose

STEP-Q214 defines a standardized metadata layer for STEP AP214 files focused on quotation and RFQ workflows.

It enables automated and semi-automated interpretation of commercial and technical parameters for industrial manufacturing.

---

## 2. Scope

This specification applies to:

- Individual parts
- Assemblies
- Industrial manufacturing requests

It is intended for use in:

- Online manufacturing platforms
- ERP and quotation systems
- CAM-related costing workflows
- Hybrid and manual quotation processes

Excluded from scope:

- Production planning
- CAM toolpaths
- Machine parameters
- Quality inspection planning
- Shopfloor scheduling

---

## 3. Normative References

The following documents are indispensable for the application of this specification:

- ISO 10303-214 — Automotive Design (AP214)
- ISO TC 184/SC 4 — Industrial data

Informative references:

- STEP Tools — STEP Standards Overview
- PDES, Inc.

---

## 4. Base Standard

STEP-Q214 is based exclusively on ISO 10303-214 (STEP AP214).

All geometric and topological data shall conform to AP214.

No proprietary or non-standard entity types shall be introduced.

---

## 5. Design Principles

STEP-Q214 implementations shall follow these principles:

1. Backward compatibility with AP214 parsers
2. No modification of core geometry entities
3. Use of standard AP214 property entities only
4. Machine-readable structure
5. Human-readable values where applicable
6. Clear separation of quotation and production data

---

## 6. Metadata Architecture

STEP-Q214 metadata shall be stored using the following AP214 entities:

- PROPERTY_SET
- PROPERTY_DEFINITION
- DESCRIPTIVE_REPRESENTATION_ITEM

Metadata containers shall be identified by:

    PROPERTY_SET('STEP-Q214', ...)

No proprietary entities or extensions are permitted.

---

## 7. Naming Convention

All STEP-Q214 fields shall use the prefix:

    Q_

Example:

    Q_MATERIAL

No special filename suffix is required for STEP files that contain STEP-Q214 metadata.
When an annotated companion file needs to be distinguished from a raw export,
implementations may use an explicit workflow suffix before the STEP extension, such as:

    realSample.rfq.STEP

This naming remains informative only and is not required for conformance.
Tools that generate annotated companion copies may require the user to choose that suffix explicitly.
Parsers and validators shall identify STEP-Q214 by file content,
not by filename.

---

## 8. Core Field Registry

The normative list of registered fields is defined in:

    spec/fields.md

Only registered fields shall be used in conformant files.

---

## 9. Enumeration Registry

All controlled vocabularies and enumerations are defined in:

    spec/enumerations.md

Only registered enumeration values shall be used.

---

## 10. Validation and Parser Requirements

Validation rules are defined in:

    spec/validation.md

Implementations shall comply with the following principles:

- Missing fields shall not cause parsing errors
- Missing values shall not cause parsing errors
- Missing PROPERTY_SET containers shall not cause parsing errors
- Unknown or unsupported extensions shall not cause parser aborts

Fallback to manual completion is mandatory.

---

## 11. Parser Resilience

Parsers and quotation systems shall tolerate:

- Incomplete metadata sets
- Partial field definitions
- Empty values
- Unknown future extensions

No hard failures shall occur solely due to metadata issues.

Validators may still classify metadata issues as warnings or errors
for conformance reporting.

---

## 12. Conformance

For conformance evaluation, STEP-Q214 distinguishes between
parser tolerance and specification conformance.

A STEP file is fully conformant with STEP-Q214 if:

- Metadata is stored according to this specification
- Only registered Q_ fields are used
- Values conform to defined data types
- No proprietary entities are present

Partial conformance is permitted when:

- metadata is structurally parseable
- registered fields used in the file remain valid
- unsupported or extension metadata does not invalidate the overall import path

Non-conformance applies when core structural or syntactic rules are violated.

---

## 13. Extensions

Custom extensions are permitted if:

- They use the prefix Q_
- They are documented
- They do not override registered fields

Documented extensions may be used for experimentation and bilateral integration,
but they are outside full conformance until officially registered.

Undocumented extensions are non-conformant.

Parsers shall ignore unsupported extensions for import continuity,
while validators may report them in conformance output.

---

## 14. Intellectual Property

STEP-Q214 is developed and maintained by holydraft.

This specification is not an ISO standard and implies no ISO certification.

No rights are waived by publication.

---

## 15. Versioning

Semantic versioning is applied.

- v0.x — Draft
- v1.x — Stable
- v2.x — Major revision

Backward compatibility shall be maintained within a major version.

---

## 16. Governance

Changes to this specification are managed via GitHub pull requests.

All changes are subject to maintainer review.

---

## 17. Document Control

This document is the normative reference for STEP-Q214.

In case of conflicts, this document prevails over supplementary materials.
