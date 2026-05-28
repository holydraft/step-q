
# STEP-Q214 Validation and Conformance Rules

Version: v0.1  
Status: Draft  
Maintainer: holydraft

---

## 1. Purpose

This document defines validation rules and conformance requirements for STEP-Q214 files.

It enables automated checking of metadata structure, data types, and semantic consistency.

Validation shall primarily be performed by importing systems.
Exporting tools may perform optional pre-validation,
but shall not block file generation based on validation results.

---

## 2. Validation Levels

Validation shall be performed on three levels:

| Level | Name        | Description                                   |
|-------|-------------|-----------------------------------------------|
| L1    | Structural  | STEP/AP214 entity structure                   |
| L2    | Syntactic   | Field types and formats                       |
| L3    | Semantic    | Business and manufacturing plausibility       |

---

## 3. Level 1 – Structural Validation

### 3.1 Metadata Container

A conformant file may contain one (per Part):

PROPERTY_SET('STEP-Q214', ...)

container.

Absence of such containers is permitted.

---

### 3.2 Allowed Entities

Only the following entity types shall be used for STEP-Q214 metadata:

- PROPERTY_SET
- PROPERTY_DEFINITION
- DESCRIPTIVE_REPRESENTATION_ITEM

Use of proprietary entities is forbidden.

---

### 3.3 Container Identification

Metadata containers shall be identified by the name:

STEP-Q214

Case-sensitive.

---

## 4. Level 2 – Syntactic Validation

### 4.1 Field Names

- Must start with Q_
- Must be uppercase
- Must match registered fields

---

### 4.2 Data Types

| Type    | Validation Rule                          |
|---------|------------------------------------------|
| String  | UTF-8, non-control characters            |
| Integer | Base 10, no decimals                     |
| Float   | Dot separator, finite value              |
| Enum    | Must exist in enumeration registry       |
| Date    | ISO 8601 (YYYY-MM-DD)                    |
| Bool    | true / false                             |

---

### 4.3 Numeric Ranges

| Field Type | Rule              |
|------------|-------------------|
| Integer    | > 0 where applicable |
| Float      | ≥ 0 where applicable |

---

### 4.4 Units

Units shall conform to definitions in spec/fields.md.

Non-standard units shall raise warnings.

---

## 5. Level 3 – Semantic Validation

### 5.1 Process vs. Geometry

Declared Q_PRIMARY_PROCESS shall be consistent with geometry.

Examples:

- laser_cutting → planar sheet geometry
- turning → rotational symmetry
- additive → complex internal structures

Inconsistencies shall raise warnings.

---

### 5.2 Tolerances

If Q_TOLERANCE_CLASS is specified, referenced drawings or PMI data shall exist.

Otherwise, a warning shall be raised.

---

### 5.3 Surface Treatment

Surface requirements shall be compatible with base material.

Example:

- anodized → aluminum alloys
- galvanized → steel

Incompatible combinations shall raise warnings.

---

### 5.4 Quantity vs. Process

Low quantities combined with tooling-heavy processes shall raise warnings.

Example:

- forging + quantity = 1

---

## 6. Error Classification

Validation findings shall be classified as follows:

| Level | Type     | Description                          |
|-------|----------|--------------------------------------|
| E     | Error    | Violates core specification          |
| W     | Warning  | Potential business/technical issue  |
| I     | Info     | Informational notice                 |

---

## 7. Mandatory Errors

The following conditions shall produce errors:

- Invalid field names
- Use of undocumented Q_ extensions in conformance validation
- Invalid enum values
- Forbidden entity types
- Broken STEP structure

---

## 8. Non-Blocking Warnings

The following conditions shall produce warnings only:

- Missing optional fields
- Missing values
- Incomplete metadata sets
- Ambiguous comments
- Derived defaults
- Use of documented but unregistered extension fields

---

## 9. Parser Behavior

Parsers shall comply with the following rules:

- Never abort import solely due to metadata issues
- Continue processing on warnings
- Log all validation findings
- Support partial imports
- Ignore unsupported extension fields during import

---

## 10. Fallback Rules

When validation fails, systems shall apply the following defaults:

| Field             | Default Value     |
|-------------------|-------------------|
| Q_QUANTITY        | 1                 |
| Q_TOLERANCE_CLASS | ISO2768-m          |
| Q_SURFACE         | raw               |
| Q_CERTIFICATE     | none              |
| Q_PACKAGING       | bulk              |

---

## 11. Validation Output Format (Recommended)

Validation tools should output findings in structured form:

Example (JSON):

    {
      "file": "part_4711.step",
      "conformance": "partial",
      "errors": 1,
      "warnings": 3,
      "messages": [
        {
          "level": "W",
          "field": "Q_SURFACE",
          "message": "Incompatible with material"
        }
      ]
    }

---

## 12. Conformance Levels

| Level   | Description                          |
|---------|--------------------------------------|
| Full    | No errors, no critical warnings       |
| Partial | Core metadata valid, warnings or extension findings present |
| Non     | Errors present                        |

---

## 13. Change Management

All changes to validation rules require maintainer approval and version increment.
