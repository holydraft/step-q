# STEP-Q Field Registry

Version: v0.3  
Status: Draft  
Maintainer: holydraft

---

## 1. Purpose

This document defines the registered STEP-Q fields for quotation-, manufacturability-, and production-relevant manufacturing parameters.

Only fields defined in this registry are considered normative. All earlier generic fields not listed here are removed from the active registry.

The same field registry can be used with STEP files independent of whether the carrier is AP203, AP214, or AP242.

---

## 2. General Rules

### 2.1 Naming

- All fields shall use the prefix `Q_`.
- Field names shall use uppercase letters and underscores only.
- Enumeration values are defined in `spec/enumerations.md`.
- Where external or UI keys use camelCase, STEP-Q fields shall use the normalized `Q_` field name.

### 2.2 Data Types

| Type | Description |
|---|---|
| Integer | Signed integer, base 10 |
| Float | Decimal number, dot as separator |
| Enum | Controlled vocabulary from `spec/enumerations.md` |
| Bool | `true` / `false` |

Free-form `String`, `Object`, and `List` values are intentionally not part of the active v0.3 field registry. New fields should prefer explicit scalar fields and registered enums. Exceptions require a documented rationale in the field proposal.

### 2.3 Units

- Length values shall use millimetres (`mm`) unless explicitly stated otherwise.
- Quantity values shall use pieces (`pcs`).

### 2.4 Product Type Applicability

Each field defines the product types currently supported by STEP-Q in the column `Supported Product Types`.

The currently supported values for `Q_PRODUCT_TYPE` are:

| Product Type | Meaning |
|---|---|
| `sheet` | Sheet-metal part, including laser-cut and bent sheet-metal parts |
| `tube` | Tube or profile laser-cut part |
| `turning` | Turned part |
| `milling` | Milled CNC-machined part |

A field is currently defined for the product types listed in its `Supported Product Types` entry. Future STEP-Q versions may extend this set.

---

## 3. Common Fields

| STEP-Q Field | Type | Unit / Enum | Source Key | Supported Product Types | Description |
|---|---|---|---|---|---|
| `Q_PRODUCT_TYPE` | Enum | `Q_PRODUCT_TYPE` | `productType` | `sheet`, `tube`, `turning`, `milling` | Product class for quotation and production routing. |
| `Q_QUANTITY` | Integer | pcs | `quantity` | `sheet`, `tube`, `turning`, `milling` | Requested quantity. |
| `Q_MATERIAL` | Enum | product-specific material registry | `material` | `sheet`, `tube`, `turning`, `milling` | Material designation. Each supported product type has its own material catalog. |
| `Q_TEST_REPORT` | Enum | `Q_TEST_REPORT_TYPE` | `testReport` | `sheet`, `tube`, `turning`, `milling` | Inspection certificate according to EN 10204. |
| `Q_SAMPLE_QUANTITY` | Integer | pcs | `sampleQuantity` | `sheet`, `tube`, `turning`, `milling` | Requested sample-part quantity. |

---

## 4. Sheet Fields

### 4.1 Grund-Spezifikationen

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_QUANTITY` | Integer | pcs | `quantity` | Stückzahl. |
| `Q_THICKNESS` | Enum | `Q_SHEET_THICKNESS` | `thickness` | Dicke. |
| `Q_MATERIAL` | Enum | `Q_SHEET_MATERIAL` | `material` | Material. |

### 4.2 Weiterbearbeitung

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_MICRO_JOINTS` | Bool | — | `microJoints` | Mikrosteg(e) entfernen? |
| `Q_DEBURRING` | Enum | `Q_DEBURRING` | `deburring` | Entgraten. |
| `Q_EDGE_ROUNDING` | Bool | — | `edgeRounding` | Kanten verrunden. |
| `Q_TEXT_ENGRAVING` | Bool | — | `textEngraving` | Gravuren. |
| `Q_SHEET_METAL_FIT_TYPE` | Enum | `Q_SHEET_METAL_FIT_TYPE` | `sheetMetalFits` | Passungen. |
| `Q_QUANTITY_THREADS` | Integer | pcs | `quantityThreads` | Gewinde. |
| `Q_QUANTITY_EXTRUDED_THREADS` | Integer | pcs | `quantityExtrudedThreads` | Gewindedurchzüge. |
| `Q_QUANTITY_COUNTERSINKS` | Integer | pcs | `quantityCountersinks` | Senkungen. |
| `Q_CORNER_RELIEF` | Bool | — | `freecorner` | Ecken freistellen. |
| `Q_LEVELING` | Bool | — | `leveling` | Richten. |
| `Q_QUANTITY_WELDING_STUDS` | Integer | pcs | `quantityWeldingStuds` | Bolzenschweißen. |
| `Q_QUANTITY_PRESS_NUTS` | Integer | pcs | `quantityPressNuts` | Einpressmuttern. |
| `Q_CUTTING_TECHNOLOGY` | Enum | `Q_CUTTING_TECHNOLOGY` | `cuttingTechnology` | Schneidtechnologie. |

### 4.3 Oberfläche

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_TOP_SIDE` | Enum | `Q_TOP_SIDE` | `topSide` | Oberseite. |
| `Q_ROLLING_DIRECTION` | Enum | `Q_ORIENTATION` | `rotation` | Walzrichtung. |
| `Q_GALVANIZING` | Enum | `Q_GALVANIZING` | `galvanizing` | Verzinken. |
| `Q_POWDER_COATING_APPLICATION` | Enum | `Q_POWDER_COATING_APPLICATION` | `powderCoating.application` | Pulverbeschichtungsanwendung. |
| `Q_POWDER_COATING_GLOSS` | Enum | `Q_POWDER_COATING_GLOSS` | `powderCoating.gloss` | Pulverbeschichtungs-Glanzgrad. |
| `Q_POWDER_COATING_TEXTURE` | Enum | `Q_POWDER_COATING_TEXTURE` | `powderCoating.texture` | Pulverbeschichtungs-Textur. |

### 4.4 Zertifikate & Sonstiges

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_TEST_REPORT` | Enum | `Q_TEST_REPORT_TYPE` | `testReport` | Abnahmeprüfzeugnis nach EN 10204. |
| `Q_SAMPLE_QUANTITY` | Integer | pcs | `sampleQuantity` | Musterteile. |

---

## 5. Tube Fields

### 5.1 Grund-Spezifikationen

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_QUANTITY` | Integer | pcs | `quantity` | Stückzahl. |
| `Q_MATERIAL` | Enum | `Q_TUBE_MATERIAL` | `material` | Material. |

### 5.2 Weiterbearbeitung

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_TUBE_LASER_CUTTING_METHOD` | Enum | `Q_TUBE_LASER_CUTTING_METHOD` | `laserCuttingMethod` | Laserschnittverfahren. |
| `Q_TEXT_ENGRAVING` | Bool | — | `textEngraving` | Gravuren. |
| `Q_QUANTITY_THREADS` | Integer | pcs | `quantityThreads` | Gewinde. |
| `Q_QUANTITY_COUNTERSINKS` | Integer | pcs | `quantityCountersinks` | Senkungen. |

### 5.3 Zertifikate & Sonstiges

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_TEST_REPORT` | Enum | `Q_TEST_REPORT_TYPE` | `testReport` | Abnahmeprüfzeugnis nach EN 10204. |
| `Q_SAMPLE_QUANTITY` | Integer | pcs | `sampleQuantity` | Musterteile. |

---

## 6. Turning Fields

### 6.1 Grund-Spezifikationen

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_QUANTITY` | Integer | pcs | `quantity` | Stückzahl. |
| `Q_MATERIAL` | Enum | `Q_TURNING_MATERIAL` | `material` | Material. |

### 6.2 Weiterbearbeitung

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_GENERAL_TOLERANCE_LENGTH_ANGLE` | Enum | `Q_GENERAL_TOLERANCE_LENGTH_ANGLE` | `tolerances.lengthsAndAngles` | Allgemeintoleranzen für Längen und Winkel. |
| `Q_GENERAL_TOLERANCE_SHAPE_POSITION` | Enum | `Q_GENERAL_TOLERANCE_SHAPE_POSITION` | `tolerances.shapeAndPosition` | Allgemeintoleranzen für Form und Lage. |
| `Q_ADDITIONAL_TOLERANCE_IT_CLASS` | Enum | `Q_IT_CLASS` | `fineTolerancesAndFits.it` | Weitere Toleranzen: IT-Klasse. |
| `Q_ADDITIONAL_TOLERANCE_RANGE` | Enum | `Q_TOLERANCE_RANGE` | `fineTolerancesAndFits.tolerance` | Weitere Toleranzen: Toleranzbereich. |
| `Q_THREAD_TYPE` | Enum | `Q_THREAD_TYPE` | `turningThreads.type` | Gewindeart. |

### 6.3 Oberfläche

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_SURFACE_FINISH` | Enum | `Q_SURFACE_FINISH_RZ` | `surfaceFinish` | Oberflächengüte. |
| `Q_GALVANIZING` | Enum | `Q_GALVANIZING` | `galvanizing` | Verzinken. |
| `Q_ANODIZING` | Enum | `Q_PROCESS_SELECTION` | `anodizing` | Eloxieren. |
| `Q_BURNISHING` | Enum | `Q_PROCESS_SELECTION` | `burnishing` | Brünieren. |
| `Q_POWDER_COATING_APPLICATION` | Enum | `Q_POWDER_COATING_APPLICATION` | `powderCoating.application` | Pulverbeschichtungsanwendung. |
| `Q_POWDER_COATING_GLOSS` | Enum | `Q_POWDER_COATING_GLOSS` | `powderCoating.gloss` | Pulverbeschichtungs-Glanzgrad. |
| `Q_POWDER_COATING_TEXTURE` | Enum | `Q_POWDER_COATING_TEXTURE` | `powderCoating.texture` | Pulverbeschichtungs-Textur. |

### 6.4 Zertifikate & Sonstiges

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_TEST_REPORT` | Enum | `Q_TEST_REPORT_TYPE` | `testReport` | Abnahmeprüfzeugnis nach EN 10204. |
| `Q_SAMPLE_QUANTITY` | Integer | pcs | `sampleQuantity` | Musterteile. |

---

## 7. Milling Fields

### 7.1 Grund-Spezifikationen

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_QUANTITY` | Integer | pcs | `quantity` | Stückzahl. |
| `Q_MATERIAL` | Enum | `Q_MILLING_MATERIAL` | `material` | Material. |

### 7.2 Weiterbearbeitung

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_GENERAL_TOLERANCE_LENGTH_ANGLE` | Enum | `Q_GENERAL_TOLERANCE_LENGTH_ANGLE` | `tolerances.lengthsAndAngles` | Allgemeintoleranzen für Längen und Winkel. |
| `Q_GENERAL_TOLERANCE_SHAPE_POSITION` | Enum | `Q_GENERAL_TOLERANCE_SHAPE_POSITION` | `tolerances.shapeAndPosition` | Allgemeintoleranzen für Form und Lage. |
| `Q_ADDITIONAL_TOLERANCE_IT_CLASS` | Enum | `Q_IT_CLASS` | `fineTolerancesAndFits.it` | Weitere Toleranzen: IT-Klasse. |
| `Q_ADDITIONAL_TOLERANCE_RANGE` | Enum | `Q_TOLERANCE_RANGE` | `fineTolerancesAndFits.tolerance` | Weitere Toleranzen: Toleranzbereich. |
| `Q_THREAD_TYPE` | Enum | `Q_THREAD_TYPE` | `threads.type` | Gewindeart. |

### 7.3 Oberfläche

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_SURFACE_FINISH` | Enum | `Q_SURFACE_FINISH_RZ` | `surfaceFinish` | Oberflächengüte. |
| `Q_GALVANIZING` | Enum | `Q_GALVANIZING` | `galvanizing` | Verzinken. |
| `Q_ANODIZING` | Enum | `Q_PROCESS_SELECTION` | `anodizing` | Eloxieren. |
| `Q_BURNISHING` | Enum | `Q_PROCESS_SELECTION` | `burnishing` | Brünieren. |
| `Q_POWDER_COATING_APPLICATION` | Enum | `Q_POWDER_COATING_APPLICATION` | `powderCoating.application` | Pulverbeschichtungsanwendung. |
| `Q_POWDER_COATING_GLOSS` | Enum | `Q_POWDER_COATING_GLOSS` | `powderCoating.gloss` | Pulverbeschichtungs-Glanzgrad. |
| `Q_POWDER_COATING_TEXTURE` | Enum | `Q_POWDER_COATING_TEXTURE` | `powderCoating.texture` | Pulverbeschichtungs-Textur. |

### 7.4 Zertifikate & Sonstiges

| STEP-Q Field | Type | Unit / Enum | Source Key | Description |
|---|---|---|---|---|
| `Q_TEST_REPORT` | Enum | `Q_TEST_REPORT_TYPE` | `testReport` | Abnahmeprüfzeugnis nach EN 10204. |
| `Q_SAMPLE_QUANTITY` | Integer | pcs | `sampleQuantity` | Musterteile. |

---

## 8. Compatibility Notes

- `turning` and `milling` use the same field set except for the material enum referenced by `Q_MATERIAL`.
- Product-specific material enum values for `Q_SHEET_MATERIAL`, `Q_TUBE_MATERIAL`, `Q_TURNING_MATERIAL`, and `Q_MILLING_MATERIAL` are maintained in `spec/materials.md`.
- `String`, `Object`, and `List` are not active v0.3 field types. Proposed exceptions must include a rationale and validation semantics.

---

## 9. Deprecation Policy

Deprecated fields shall be marked explicitly. All previous v0.2 fields not listed in this registry are removed from the active v0.3 registry.

---

## 10. Change Management

All new fields must be proposed via pull request. Each proposal shall include:

- Technical description
- Business rationale
- Examples
- Backward compatibility analysis
- Product-type applicability

---

## 11. Change Log

| Version | Date | Description |
|---|---|---|
| v0.1 | 2026-02-11 | Initial registry |
| v0.2 | 2026-05-28 | Added drawing-driven supplementary fields |
| v0.3 | 2026-07-02 | Defined current product type support as sheet, tube, turning, and milling; reduced field registry to the requested product-specific metadata fields |
