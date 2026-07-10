# STEP-Q Enumeration Registry

Version: v0.3  
Status: Draft  
Maintainer: holydraft

---

## 1. Purpose

This document defines the controlled vocabularies used by STEP-Q for quotation-, manufacturability-, and production-relevant manufacturing parameters.

Only values registered in this document, or material values referenced through `spec/materials.md`, are considered valid for conformant files.

---

## 2. General Rules

### 2.1 Naming

- Enumeration values shall be lowercase.
- Words shall be separated by underscores.
- Enumeration values shall not contain spaces.
- Where external systems use different labels, values shall be normalized to the STEP-Q registry values defined here.
- Material catalog display labels may contain standard material designations, spaces, punctuation, and condition details. When embedded as enum identifiers, material labels shall be normalized according to the same lowercase-and-underscore convention.

### 2.2 Product Types

The currently supported `Q_PRODUCT_TYPE` values are `sheet`, `tube`, `turning`, and `milling`. Future STEP-Q versions may add further product types.

### 2.3 Stability

- Existing values shall not be renamed.
- Deprecated values remain valid for one major version.
- Removal requires a major version update.

### 2.4 Extension Process

New enumeration values must be proposed via pull request and include:

- Technical definition
- Manufacturing relevance
- Example use cases
- Compatibility analysis

---

## 3. Enums

### Q_PRODUCT_TYPE

Defines the manufacturing product class used for quotation and configuration.

| Value | Description | Typical Use |
|---|---|---|
| sheet | Sheet-metal part | Laser-cut and/or bent sheet part |
| tube | Tube or profile cut part | Tube laser cutting |
| turning | Turned part | CNC turning |
| milling | Milled part | CNC milling |

---

### Q_CUTTING_TECHNOLOGY

Defines the selected sheet cutting method.

| Value | Description |
|---|---|
| 2d_cutting | 2D laser cutting |
| 3d_cutting | 3D laser cutting |
| plasma_cutting | Plasma cutting |
| flame_cutting | Flame cutting |

---

### Q_SHEET_THICKNESS

Defines selectable sheet thickness values.

| Value | Description |
|---|---|
| thickness_0_5_mm | 0,5 mm |
| thickness_0_75_mm | 0,75 mm |
| thickness_0_8_mm | 0,8 mm |
| thickness_0_88_mm | 0,88 mm |
| thickness_0_9_mm | 0,9 mm |
| thickness_1_mm | 1 mm |
| thickness_1_25_mm | 1,25 mm |
| thickness_1_5_mm | 1,5 mm |
| thickness_2_mm | 2 mm |
| thickness_2_5_mm | 2,5 mm |
| thickness_3_mm | 3 mm |
| thickness_3_5_mm | 3,5 mm |
| thickness_4_mm | 4 mm |
| thickness_5_mm | 5 mm |
| thickness_6_mm | 6 mm |
| thickness_8_mm | 8 mm |
| thickness_10_mm | 10 mm |
| thickness_12_mm | 12 mm |
| thickness_15_mm | 15 mm |
| thickness_20_mm | 20 mm |
| thickness_25_mm | 25 mm |
| thickness_30_mm | 30 mm |
| thickness_40_mm | 40 mm |
| thickness_45_mm | 45 mm |
| thickness_50_mm | 50 mm |
| thickness_55_mm | 55 mm |
| thickness_70_mm | 70 mm |
| thickness_75_mm | 75 mm |
| thickness_90_mm | 90 mm |

---

### Q_TEST_REPORT_TYPE

Defines inspection certificate types according to EN 10204.

| Value | Description |
|---|---|
| en_10204_2_1 | EN 10204 type 2.1 certificate |
| en_10204_2_2 | EN 10204 type 2.2 certificate |
| en_10204_3_1 | EN 10204 type 3.1 inspection certificate |
| en_10204_3_2 | EN 10204 type 3.2 inspection certificate |

---

### Q_TUBE_LASER_CUTTING_METHOD

Defines the selected tube laser cutting method.

| Value | Description |
|---|---|
| 2d_cutting | 2D tube laser cutting |
| 3d_cutting | 3D tube laser cutting |

---

### Q_TOP_SIDE

Defines the visible or preferred upper side of a sheet part.

| Value | Description |
|---|---|
| top_view | Top side corresponds to the top view |
| bottom_view | Top side corresponds to the bottom view |
| pdf_file | Top side is defined in an uploaded drawing/PDF |

---

### Q_ORIENTATION

Defines rolling, grinding, or brushing direction.

| Value | Description |
|---|---|
| arbitrary | Free or arbitrary direction |
| perpendicular | Perpendicular direction, 90 degrees |
| parallel | Parallel direction, 180 degrees |
| see_pdf | Direction is defined in an uploaded drawing/PDF |

---

### Q_DEBURRING

Defines deburring requirement.

| Value | Description |
|---|---|
| one_sided_rear | One-sided rear-side deburring |
| two_sided | Two-sided deburring |
| barrel_finish | Barrel finishing / tumbling |
| manual_rear | Manual rear-side deburring |

---

### Q_PROCESS_SELECTION

Defines an explicit process selection state for binary manufacturing operations.

| Value | Description |
|---|---|
| required | Process is selected or required |
| see_pdf | Process requirement is defined in an uploaded drawing/PDF |

---

### Q_SHEET_METAL_FIT_TYPE

Defines sheet-metal fit categories.

| Value | Description |
|---|---|
| tolerance_fit | Tolerance or fit is specified in the drawing |
| press_fit | Press fit requirement |
| slip_fit | Slip or clearance fit requirement |
| see_pdf | Fit requirement is defined in an uploaded drawing/PDF |

---

### Q_GALVANIZING

Defines galvanizing method.

| Value | Description |
|---|---|
| electro_galvanizing | Electrolytic galvanizing |
| hot_dip_galvanizing | Hot-dip galvanizing |

---

### Q_POWDER_COATING_APPLICATION

Defines powder-coating application environment.

| Value | Description |
|---|---|
| interior | Interior application |
| exterior | Exterior application |

---

### Q_POWDER_COATING_GLOSS

Defines powder-coating gloss level.

| Value | Description |
|---|---|
| glossy | Glossy |
| semi_gloss | Semi-gloss |
| satin_matt | Satin matt |
| matt | Matt |

---

### Q_POWDER_COATING_TEXTURE

Defines powder-coating texture.

| Value | Description |
|---|---|
| smooth | Smooth |
| fine_texture | Fine texture |
| texture | Structured texture |
| coarse_texture | Coarse texture |

---

### Q_SURFACE_FINISH_RZ

Defines general surface finish for machined parts.

| Value | Description | Approximate Ra Reference |
|---|---|---|
| rz_4 | Rz 4 | approx. Ra 1.0 |
| rz_6_3 | Rz 6.3 | approx. Ra 1.6 |
| rz_12_5 | Rz 12.5 | approx. Ra 3.2 |
| rz_16 | Rz 16 | approx. Ra 4.0 |
| rz_25 | Rz 25 | approx. Ra 6.3 |
| rz_50 | Rz 50 | approx. Ra 12.5 |

---

### Q_GENERAL_TOLERANCE_LENGTH_ANGLE

Defines general tolerances for linear and angular dimensions.

| Value | Description |
|---|---|
| din_iso_2768_1_m | DIN ISO 2768-1 m, medium |
| din_iso_2768_1_f | DIN ISO 2768-1 f, fine |

---

### Q_GENERAL_TOLERANCE_SHAPE_POSITION

Defines general tolerances for shape and position.

| Value | Description |
|---|---|
| din_iso_2768_2_k | DIN ISO 2768-2 K, medium |
| din_iso_2768_2_h | DIN ISO 2768-2 H, fine |

---

### Q_IT_CLASS

Defines fit/tolerance IT class category.

| Value | Description |
|---|---|
| lte_it5 | IT class 5 or smaller |
| it_6 | IT 6 |
| it_7 | IT 7 |
| it_8 | IT 8 |
| it_9 | IT 9 |
| gte_it10 | IT 10 or greater |

---

### Q_TOLERANCE_RANGE

Defines tolerance-span category in millimetres.

| Value | Description |
|---|---|
| ge_0_008 | Tolerance span >= 0.008 mm |
| lt_0_008 | Tolerance span < 0.008 mm |
| ge_0_01 | Tolerance span >= 0.01 mm |
| lt_0_01 | Tolerance span < 0.01 mm |
| ge_0_02 | Tolerance span >= 0.02 mm |
| lt_0_02 | Tolerance span < 0.02 mm |
| ge_0_05 | Tolerance span >= 0.05 mm |
| ge_0_1 | Tolerance span >= 0.1 mm |
| ge_0_25 | Tolerance span >= 0.25 mm |

---

### Q_THREAD_TYPE

Defines thread standard categories.

| Value | Description |
|---|---|
| isometric | ISO metric thread |
| whitworth | Whitworth / inch thread |
| uts | Unified Thread Standard |
| pipe | Pipe thread |
| trapezoidal | Trapezoidal thread |

---

### Q_SHEET_MATERIAL

Defines the material catalog for sheet-metal parts.

The registered values are maintained in `spec/materials.md`, section `materials for Q_PRODUCT_TYPE = sheet`.

---

### Q_TUBE_MATERIAL

Defines the material catalog for tube and profile parts.

The registered values are maintained in `spec/materials.md`, section `materials for Q_PRODUCT_TYPE = tube`.

---

### Q_TURNING_MATERIAL

Defines the material catalog for turned parts.

The registered values are maintained in `spec/materials.md`, section `materials for Q_PRODUCT_TYPE = turning`.

---

### Q_MILLING_MATERIAL

Defines the material catalog for milled parts.

The registered values are maintained in `spec/materials.md`, section `materials for Q_PRODUCT_TYPE = milling`.

---

## 4. Deprecation Registry

All previous v0.2 enumeration values not listed in this registry are removed from the active v0.3 registry.

---

## 5. Change Log

| Version | Date | Description |
|---|---|---|
| v0.1 | 2026-02-11 | Initial registry |
| v0.2 | 2026-05-28 | Added drawing-driven supplementary enums |
| v0.3 | 2026-07-02 | Defined current product type support as sheet, tube, turning, and milling; reduced enum registry to the requested field set and supplemented product-specific enum groups from app configuration logic |
