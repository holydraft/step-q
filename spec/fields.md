
# STEP-Q214 Field Registry

Version: v0.1  
Status: Draft  
Maintainer: holydraft

---

## 1. Purpose

This document defines all registered STEP-Q214 fields, including their
semantics, data types, formats, and interpretation rules.

Only fields defined in this registry are considered normative.

---

## 2. General Rules

### 2.1 Naming

- All fields shall use the prefix `Q_`
- Uppercase letters and underscores only
- No spaces or special characters

### 2.2 Data Types

| Type    | Description                         |
|---------|-------------------------------------|
| String  | UTF-8 text                          |
| Integer | Signed integer (base 10)            |
| Float   | Decimal number (dot as separator)   |
| Enum    | Controlled vocabulary               |
| Date    | ISO 8601 format (YYYY-MM-DD)        |
| Bool    | true / false                        |

### 2.3 Units

All units shall follow SI conventions unless explicitly defined.

Currency values shall be expressed in ISO 4217 format where applicable.

---

## 3. Core Fields

---

### Q_PART_ID

**Type:** String  
**Required:** No  
**Description:**  
Unique identifier for the part or assembly within the RFQ context.

**Format:**  
Free text, recommended pattern: `[A-Z0-9-_]+`

**Examples:**

- HD-2026-001
- PART_4711
- A-9832-B

**Fallback:**  
If missing, internal system IDs shall be assigned.

**Common Errors:**

- Duplicate IDs within one RFQ
- Use of whitespace

---

### Q_MATERIAL

**Type:** String  
**Required:** No  
**Description:**  
Primary material designation of the part.

**Format:**  
Standardized material names according to applicable norms where possible.

**Examples:**

- EN AW-6082
- S355MC
- 1.4301
- PA12

**Fallback:**  
Material must be clarified manually.

**Common Errors:**

- Trade names without specification
- Incomplete alloy definitions

---

### Q_PRIMARY_PROCESS

**Type:** Enum  
**Required:** No  
**Description:**  
Main manufacturing process used for cost estimation.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- milling
- laser_cutting
- additive

**Fallback:**  
Derived from geometry if possible.

**Common Errors:**

- Multiple conflicting processes
- Process not matching geometry

---

### Q_QUANTITY

**Type:** Integer  
**Required:** No  
**Unit:** pcs  
**Description:**  
Requested order quantity.

**Format:**  
Positive integer (>0)

**Examples:**

- 1
- 50
- 1000

**Fallback:**  
Assumed quantity = 1

**Common Errors:**

- Zero or negative values
- Decimal quantities

---

### Q_TOLERANCE_CLASS

**Type:** Enum  
**Required:** No  
**Description:**  
General dimensional tolerance class.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- ISO2768-m
- ISO2768-f

**Fallback:**  
Default: ISO2768-m

**Common Errors:**

- Mixed tolerance systems
- Missing drawing reference

---

### Q_SURFACE

**Type:** Enum  
**Required:** No  
**Description:**  
Surface treatment or finish requirement.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- anodized
- powder_coated
- polished

**Fallback:**  
Assumed: raw / untreated

**Common Errors:**

- Ambiguous terms (e.g. "nice finish")
- Missing specification for visible parts

---

### Q_DRAWING_REFERENCE

**Type:** String  
**Required:** No  
**Description:**  
Reference to external drawing or PMI document.

**Format:**  
File name or document ID.

**Examples:**

- DWG-1023
- 2026-ALU-BRKT-A1.pdf

**Fallback:**  
Geometry and PMI are authoritative.

**Common Errors:**

- Broken references
- Outdated revisions

---

### Q_TARGET_PRICE

**Type:** Float  
**Required:** No  
**Unit:** ISO 4217 currency  
**Description:**  
Target price per unit.

**Format:**  
Decimal, dot as separator.

**Examples:**

- 4.50
- 12.00

**Fallback:**  
Ignored for automatic pricing.

**Common Errors:**

- Total price instead of unit price
- Missing currency context

---

### Q_DELIVERY_DATE

**Type:** Date  
**Required:** No  
**Description:**  
Requested delivery date.

**Format:**  
YYYY-MM-DD

**Examples:**

- 2026-03-15
- 2026-06-01

**Fallback:**  
Standard lead time applies.

**Common Errors:**

- Locale-dependent formats
- Impossible dates

---

### Q_CERTIFICATE

**Type:** Enum  
**Required:** No  
**Description:**  
Material or compliance certificate requirement.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- EN10204-3.1
- EN10204-2.1

**Fallback:**  
No certificate assumed.

**Common Errors:**

- Non-standard certificates
- Missing scope definition

---

### Q_PACKAGING

**Type:** Enum  
**Required:** No  
**Description:**  
Packaging requirements.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- bulk
- individual
- vacuum

**Fallback:**  
Standard bulk packaging.

**Common Errors:**

- Missing protection requirements
- Over-specification

---

### Q_COMMENTS

**Type:** String  
**Required:** No  
**Description:**  
Free-text remarks for special requirements.

**Format:**  
UTF-8 text, max. 1024 characters recommended.

**Examples:**

- Visible surface on side A
- Protect edges

**Fallback:**  
Ignored in automation.

**Common Errors:**

- Critical info hidden in comments
- Unstructured requirements

---

## 4. Drawing-Driven Supplementary Fields

The following fields capture manufacturing requirements that are often added in drawings,
PMI, or manufacturing notes and are not reliably inferable from bare STEP geometry alone.

---

### Q_THREAD_SPEC

**Type:** String  
**Required:** No  
**Description:**  
Thread specification called out in the drawing or PMI.

**Format:**  
Free text, recommended to include nominal size, pitch, and tolerance class where applicable.

**Examples:**

- M8x1.25-6H
- M12-6H THRU
- G1/4

**Fallback:**  
No thread requirement shall be assumed unless confirmed by drawing or PMI.

**Common Errors:**

- Missing pitch or tolerance class
- Hole diameter used instead of thread designation

---

### Q_THREAD_DEPTH

**Type:** Float  
**Required:** No  
**Unit:** mm  
**Description:**  
Required thread engagement depth when it is not evident from the geometry.

**Format:**  
Positive decimal (>0)

**Examples:**

- 8.0
- 12.5

**Fallback:**  
Thread depth must be clarified from the drawing note or manually.

**Common Errors:**

- Total hole depth confused with thread depth
- Missing unit context

---

### Q_HOLE_FINISH

**Type:** Enum  
**Required:** No  
**Description:**  
Required post-drilling or post-boring feature state called out on the drawing.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- reamed
- tapped
- countersunk

**Fallback:**  
Standard drilled state is assumed unless otherwise specified.

**Common Errors:**

- Multiple incompatible finishes for the same feature
- Finish specified without identifying the affected holes

---

### Q_SURFACE_ROUGHNESS_RA

**Type:** Float  
**Required:** No  
**Unit:** um  
**Description:**  
Arithmetic average surface roughness value specified on the drawing.

**Format:**  
Positive decimal (>0)

**Examples:**

- 1.6
- 3.2
- 6.3

**Fallback:**  
Standard process capability applies unless a drawing note overrides it.

**Common Errors:**

- Rz or Rt values entered as Ra
- Roughness value given without stating the affected surface

---

### Q_HEAT_TREATMENT

**Type:** Enum  
**Required:** No  
**Description:**  
Heat-treatment requirement defined by the drawing or manufacturing note.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- stress_relieved
- quenched_tempered
- nitrided

**Fallback:**  
No additional heat treatment is assumed.

**Common Errors:**

- Treatment incompatible with material
- Heat treatment specified without final hardness or acceptance criteria where needed

---

### Q_HARDNESS

**Type:** String  
**Required:** No  
**Description:**  
Required final hardness after heat treatment or material conditioning.

**Format:**  
Free text, recommended to include hardness scale and allowed range.

**Examples:**

- 58-62 HRC
- 220 HBW
- 700 HV min

**Fallback:**  
Material standard applies unless a specific hardness note is given.

**Common Errors:**

- Missing hardness scale
- Pre-treatment hardness specified instead of final condition

---

### Q_EDGE_BREAK

**Type:** String  
**Required:** No  
**Description:**  
General deburring, chamfer, or radius note for edges that are not individually modeled.

**Format:**  
Free text, recommended to include size and note scope.

**Examples:**

- 0.2-0.5 deburr all edges
- C0.5
- R0.2 max

**Fallback:**  
Standard deburring only.

**Common Errors:**

- Ambiguous scope such as "all around" without context
- Max and nominal requirements mixed in one note

---

### Q_COATING_THICKNESS

**Type:** Float  
**Required:** No  
**Unit:** um  
**Description:**  
Required coating or layer thickness when specified separately from the surface process.

**Format:**  
Positive decimal (>0)

**Examples:**

- 12.0
- 25.0

**Fallback:**  
Thickness follows the referenced surface or coating standard if available.

**Common Errors:**

- Coating thickness specified without identifying the coating process
- Micrometer and millimeter values mixed up

---

### Q_FIT_CLASS

**Type:** String  
**Required:** No  
**Description:**  
Fit or tolerance system callout for bores, shafts, or bearing seats.

**Format:**  
Free text according to the applicable fit system.

**Examples:**

- H7
- H7/g6
- P9

**Fallback:**  
General tolerances apply unless a fit callout is specified.

**Common Errors:**

- Hole and shaft basis mixed without clear pairing
- Nominal dimension given without the fit designation

---

### Q_INSPECTION_LEVEL

**Type:** Enum  
**Required:** No  
**Description:**  
Inspection depth or method required by the drawing, customer note, or quality note.

**Reference:**  
See `spec/enumerations.md`

**Examples:**

- first_article
- full_dimension
- cmm_critical

**Fallback:**  
Standard inspection practice applies.

**Common Errors:**

- Inspection requirement stated without identifying the affected features
- Visual-only approval used for dimension-critical parts

---

## 5. Deprecation Policy

Deprecated fields shall be marked explicitly.

They remain supported for at least one major version.

---

## 6. Change Management

All new fields must be proposed via pull request.

Each proposal shall include:

- Technical description
- Business rationale
- Examples
- Backward compatibility analysis

---

## 7. Change Log

| Version | Date       | Description          |
|---------|------------|----------------------|
| v0.1    | 2026-02-11 | Initial registry     |
| Unreleased | 2026-05-28 | Added drawing-driven supplementary fields for threads, hole finishing, roughness, heat treatment, coating, fit, and inspection |
