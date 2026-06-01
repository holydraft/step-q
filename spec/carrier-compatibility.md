# STEP-Q Carrier Compatibility

Version: v0.2
Status: Draft
Maintainer: holydraft

---

## 1. Purpose

This document describes how STEP-Q relates to STEP carrier formats.

STEP-Q Core is independent of any single STEP application protocol.

---

## 2. Supported Carrier Model

STEP-Q can be used with AP203, AP214, AP242, or sidecar-based STEP exchange.

AP203, AP214, and AP242 are possible STEP carrier formats for STEP-Q metadata.

The role of the carrier is to transport geometry and, where applicable, a compatible metadata embedding.

---

## 3. Equal Treatment of Carriers

No carrier is the defining profile of STEP-Q.

No carrier is the preferred protocol of STEP-Q.

No carrier-specific variant is defined by STEP-Q Core.

Carrier-specific implementation notes may exist, but they do not redefine the core field model.

---

## 4. Practical Consequences

- Geometry remains governed by the chosen carrier format.
- STEP-Q metadata keeps the same field names and meanings across carriers.
- Exchange implementations may embed metadata directly in the STEP payload or transport it in a linked sidecar.
- Validation of geometry and validation of STEP-Q metadata should be treated as separate concerns.

---

## 5. Scope Discipline

Carrier-specific implementation notes may exist, but they do not redefine the core field model.