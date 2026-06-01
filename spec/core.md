# STEP-Q Core

Version: v0.2
Status: Draft
Maintainer: holydraft

---

## 1. Purpose

STEP-Q Core defines the metadata model of STEP-Q independently from any single STEP application protocol.

It covers:

- field names
- data types
- field meanings
- controlled vocabularies
- required or optional status
- validation logic

---

## 2. Core Principles

- STEP-Q is a lightweight RFQ metadata layer for STEP files.
- STEP-Q is application-protocol agnostic.
- STEP-Q does not redefine geometry.
- STEP-Q fields remain stable across carriers.
- Parser tolerance is required for incomplete metadata.

---

## 3. Normative Registries

The normative STEP-Q Core registries are:

- spec/fields.md
- spec/enumerations.md
- spec/validation.md

Only registered fields are part of the conformant core unless a documented extension is explicitly allowed.

---

## 4. Field Prefix

All current core field names use the prefix:

    Q_

This prefix identifies STEP-Q metadata fields independent of the carrier used to exchange them.

---

## 5. Scope Boundary

STEP-Q Core focuses on quotation-relevant manufacturing information.

It does not replace:

- AP203, AP214, or AP242 geometry definitions
- PMI and semantic GD&T
- technical drawings
- CAM toolpaths
- ERP execution data
- quality management systems