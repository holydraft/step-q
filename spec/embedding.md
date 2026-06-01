# STEP-Q Metadata Embedding Methods

Version: v0.2
Status: Draft
Maintainer: holydraft

---

## 1. Purpose

This document separates STEP-Q Core from the transport methods used to exchange STEP-Q metadata.

The metadata vocabulary is stable across embedding methods.

---

## 2. Direct p21 Embedding

The current repository examples and reference tooling demonstrate a direct p21/property-entity embedding profile.

In that profile, STEP-Q metadata is stored through standard property-style entities such as:

- PROPERTY_SET
- PROPERTY_DEFINITION
- DESCRIPTIVE_REPRESENTATION_ITEM

The metadata container is identified as:

    PROPERTY_SET('STEP-Q', ...)

This profile is useful because it keeps metadata close to the STEP payload already being exchanged.

---

## 3. Sidecar Exchange

STEP-Q metadata may also be transported in a sidecar file linked to the STEP model.

Typical reasons include:

- carrier limitations in existing toolchains
- separation of geometry export and procurement metadata workflows
- API-driven exchange scenarios

JSON sidecar exchange is a planned documentation target in the roadmap.

---

## 4. Other Neutral Embedding Forms

Additional neutral embedding methods may be documented in future versions, including comment-block or envelope-style transports, provided they preserve the STEP-Q Core vocabulary and do not redefine field semantics.

---

## 5. Exchange Discipline

Embedding methods must preserve the STEP-Q Core field model and the canonical metadata container name used by the selected exchange profile.