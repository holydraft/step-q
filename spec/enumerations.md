
# STEP-Q214 Enumeration Registry

Version: v0.1  
Status: Draft  
Maintainer: holydraft

---

## 1. Purpose

This document defines all controlled vocabularies (enumerations) used by STEP-Q214.

Only values registered in this document are considered valid for conformant files.

---

## 2. General Rules

### 2.1 Naming

- Enumeration values shall be lowercase
- Words shall be separated by underscores
- No spaces or special characters

### 2.2 Stability

- Existing values shall not be renamed
- Deprecated values remain valid for one major version
- Removal requires a major version update

### 2.3 Extension Process

New enumeration values must be proposed via pull request and include:

- Technical definition
- Manufacturing relevance
- Example use cases
- Compatibility analysis

---

## 3. Enums

### Q_PRIMARY_PROCESS

Defines the main manufacturing process used for quotation.

| Value         | Description                          | Example Application            |
|---------------|--------------------------------------|--------------------------------|
| laser_cutting | Flat sheet laser cutting             | Sheet metal brackets           |
| bending       | Press brake bending                  | Enclosures, flanges            |
| punching      | Turret punching                      | Sheet parts with forms         |
| milling       | CNC milling (3-5 axis)               | Machined housings              |
| turning       | CNC turning                          | Shafts, bushings               |
| grinding      | Precision grinding                   | Bearing seats                  |
| additive      | Additive manufacturing               | Prototypes, lattice parts      |
| casting       | Metal casting                        | Housings, blocks               |
| forging       | Hot or cold forging                  | Structural parts               |
| hybrid        | Combined processes                   | Additive + milling             |

---

### Q_SURFACE

Defines surface finish or treatment.

| Value          | Description                      | Typical Use                  |
|----------------|----------------------------------|------------------------------|
| raw            | Untreated surface                | Internal parts               |
| deburred       | Deburred edges                   | Handling safety              |
| brushed        | Brushed finish                   | Visible aluminum parts       |
| polished       | Polished surface                 | Decorative parts             |
| powder_coated  | Powder coating                   | Enclosures                   |
| anodized       | Anodized aluminum                | Corrosion protection         |
| galvanized     | Zinc coating                     | Outdoor steel parts          |
| passivated     | Chemical passivation             | Stainless steel parts        |
| painted        | Liquid paint coating             | Custom colors                |

---

### Q_CERTIFICATE

Defines required material or compliance certificates.

| Value        | Description                         | Standard Reference |
|--------------|-------------------------------------|--------------------|
| none         | No certificate required             | —                  |
| EN10204-2.1  | Declaration of compliance           | EN 10204           |
| EN10204-3.1  | Inspection certificate              | EN 10204           |
| EN10204-3.2  | Inspection certificate (independent)| EN 10204           |

---

### Q_TOLERANCE_CLASS

Defines general dimensional tolerance classes.

| Value        | Description                       | Standard |
|--------------|-----------------------------------|----------|
| ISO2768-f    | Fine                              | ISO 2768 |
| ISO2768-m    | Medium                            | ISO 2768 |
| ISO2768-c    | Coarse                            | ISO 2768 |
| ISO2768-v    | Very coarse                       | ISO 2768 |
| custom       | Custom tolerances defined elsewhere | —      |

---

### Q_PACKAGING

Defines packaging requirements.

| Value       | Description                       | Typical Use              |
|-------------|-----------------------------------|--------------------------|
| bulk        | Loose bulk packaging              | Standard shipments       |
| individual  | Individually wrapped              | Precision parts          |
| vacuum      | Vacuum sealed                     | Corrosion protection     |
| foam        | Foam-protected packaging          | Sensitive components     |
| custom      | Customer-defined packaging        | Special logistics        |

---

### Q_HOLE_FINISH

Defines a drawing-controlled finishing requirement for holes or bores.

| Value         | Description                         | Typical Use                  |
|---------------|-------------------------------------|------------------------------|
| drilled       | Standard drilled hole               | General fastener holes       |
| reamed        | Precision reamed hole               | Dowel or fit holes           |
| tapped        | Internal thread created in hole     | Screw connections            |
| countersunk   | Countersink added to hole           | Flat-head screws             |
| counterbored  | Counterbore added to hole           | Socket head screws           |
| spotfaced     | Local spotface for seating surface  | Bolted interfaces            |

---

### Q_HEAT_TREATMENT

Defines heat-treatment requirements that are usually specified in the drawing or manufacturing notes.

| Value             | Description                              | Typical Use                    |
|-------------------|------------------------------------------|--------------------------------|
| none              | No additional heat treatment required    | Standard stock material        |
| stress_relieved   | Stress relieving after machining/welding | Distortion-sensitive parts     |
| annealed          | Annealed condition                       | Machinability improvement      |
| normalized        | Normalized material state                | Carbon steel components        |
| hardened          | Hardened state required                  | Wear components                |
| tempered          | Tempered after hardening                 | Toughness adjustment           |
| quenched_tempered | Quenched and tempered                    | Mechanical strength parts      |
| case_hardened     | Surface case hardening                   | Shafts, gears                  |
| nitrided          | Nitrided surface                         | Low-distortion wear surfaces   |

---

### Q_INSPECTION_LEVEL

Defines the inspection depth required by drawing or customer note.

| Value          | Description                              | Typical Use                    |
|----------------|------------------------------------------|--------------------------------|
| none           | No additional inspection note            | Standard production            |
| visual         | Visual inspection required               | Cosmetic parts                 |
| sampling       | Sampling inspection                      | Series parts                   |
| first_article  | First article inspection                 | New or changed parts           |
| full_dimension | Full dimensional inspection              | Tight-tolerance parts          |
| cmm_critical   | CMM inspection for critical features     | Complex precision components   |

---

## 4. Deprecation Registry

Deprecated values shall be listed here with replacement recommendations.

(Currently none.)

---

## 5. Change Log

| Version | Date       | Description          |
|---------|------------|----------------------|
| v0.1    | 2026-02-11 | Initial registry     |
| Unreleased | 2026-05-28 | Added drawing-driven enums for hole finishing, heat treatment, and inspection level |
