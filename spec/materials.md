# STEP-Q Material Catalog

Version: v0.3  
Status: Draft  
Maintainer: holydraft

---

## 1. Purpose

This document defines the registered material catalog values referenced by the product-specific STEP-Q material enums:

- `Q_SHEET_MATERIAL`
- `Q_TUBE_MATERIAL`
- `Q_TURNING_MATERIAL`
- `Q_MILLING_MATERIAL`

The material catalog is separated from `spec/enumerations.md` because material display labels must preserve standard material designations, condition details, and supplier-facing terminology.

---

## 2. Catalog Rules

- Material entries are grouped by `Q_PRODUCT_TYPE` and material family.
- Each list item is a registered material catalog label.
- Catalog labels may contain spaces, punctuation, material numbers, alloy names, finish details, and condition details.
- When a material label is embedded as a STEP-Q enum identifier, it shall be normalized according to the enum naming rules in `spec/enumerations.md`.
- Descriptive UI helper text such as application notes is not part of the registered material value.

---

## 3. Sheet Materials

Registered values for `Q_SHEET_MATERIAL`.

### Aluminium

- Beliebiges Aluminium·blank
- EN AW-5754 (AlMg3) 3.3535·H111 Mill-finish
- EN AW-7020 (AlZn4,5Mg1) 3.4335·T651
- EN AW 1050A (Al99,5) 3.0255· H14/H24
- EN AW-5754 (AlMg3) 3.3535·H22 Mill-finish
- EN AW-5754 (AlMg3) 3.3535·H111 Mill-finish · Laserfolie einseitig
- EN AW-5754 (AlMg3) 3.3535·H114 Mill-finish · Riffelblech Quintett
- EN AW-5005 (AlMg1)·H14/24 · farblos bandeloxiert · Laserfolie einseitig
- EN AW-5005 (AlMg1)·H14/24 · bandeloxiert E6/EV1 · Laserfolie einseitig
- EN AW-5083 (AlMg4,5Mn0,7) 3.3547·H111 Mill-finish
- EN AW-5083 (AlMg4,5Mn0,7) 3.3547·H22 Mill-finish
- EN AW-6082 (AlMgSi1) 3.2315·T6 Mill-finish

### Stahl

- Allgemeiner Baustahl·gebeizt geölt
- 1.0038·S235JR · warmgewalzt · gebeizt + geölt
- 1.0038·S235JR · warmgewalzt · walzblau
- 1.0038·S235JR · warmgewalzt
- 1.0038·S235JR · warmgewalzt · schwarz Tränenblech
- 1.0045·S355JR+N · warmgewalzt · gebeizt + geölt
- 1.0226·DX51D+Z · gewalzt · feuerverzinkt
- 1.0226·DX51D+AS120 · gewalzt · AS-beschichtet
- 1.0242·S250GD+ZM310 · Magnelis
- 1.0330·DC01 · kaltgewalzt · geölt
- 1.0330·DC01 + ZE 25/25 · kaltgewalzt · elektrolytisch verzinkt
- 1.0332·DD11 · warmgewalzt · gebeizt + geölt
- 1.0425·P265GH · warmgewalzt · walzblau
- 1.0425·P265GH · warmgewalzt
- 1.0503·C45 · warmgewalzt · walzblau
- 1.0577·S355J2+N · warmgewalzt · walzblau
- 1.0577·S355J2+N · warmgewalzt
- 1.0579·S355J2C+N · warmgewalzt · gebeizt + geölt
- 1.0976·S355MC · warmgewalzt · gebeizt + geölt
- 1.0976·S355MC · warmgewalzt · walzblau
- 1.0980·S420MC · warmgewalzt · gebeizt + geölt
- 1.5415·16Mo3 · warmfester Baustahl
- 1.8928·S690QL · warmgewalzt · walzblau
- 1.8965·COR-TEN B (S355J2W) · warmgewalzt · blank
- 1.8974·S700MC · warmgewalzt · gebeizt + geölt
- 1.8974·S700MC · warmgewalzt · walzblau

### Edelstahl

- Beliebiger Edelstahl·blank
- 1.4301·2B (alt: III C) · kaltgewalzt
- 1.4301·1D (alt: III A) · warmgewalzt
- 1.4301·1D (alt: III A) · warmgewalzt · Tränenblech
- 1.4404·1D (alt: III A) · hot-rolled · chequer plate
- 1.4301·2B (alt: III C) · kaltgewalzt · Laserfolie einseitig
- 1.4301·2G · kaltgewalzt · Laserfolie einseitig · eins. geschliffen Korn 240
- 1.4301·2G · warmgewalzt · Laserfolie einseitig · eins. geschliffen Korn 240
- 1.4301·2G · kaltgewalzt · Laserfolie einseitig · eins. geschliffen Korn 32
- 1.4301·2J · kaltgewalzt · Laserfolie einseitig · eins. gebürstet
- 1.4016·2B · kaltgewalzt
- 1.4016·2R · kaltgewalzt · blankgeglüht
- 1.4404·1D (alt: III A) · warmgewalzt
- 1.4404·2B (alt: III C) · kaltgewalzt
- 1.4404·2B (alt: III C) · kaltgewalzt · Laserfolie einseitig
- 1.4404·2G · kaltgewalzt · Laserfolie einseitig · eins. geschliffen Korn 240
- 1.4462·1D (alt: IIA) · hot-rolled
- 1.4509·2B (alt: IIIC) · cold-rolled
- 1.4539·X1NiCrMoCu 25-20-5 · kaltgewalzt
- 1.4541·2B (alt: III C) · kaltgewalzt
- 1.4571·1D (alt: III A) · warmgewalzt
- 1.4571·2B (alt: III C) · kaltgewalzt
- 1.4828·1D (alt: III A) · warmgewalzt
- 1.4828·2B (alt: III C) · kaltgewalzt
- 1.4841·1D (alt: III A) · warmgewalzt
- 1.4841·2B (alt: III C) · kaltgewalzt

### Federstahl

- 1.4310·Festigkeit 1300 - 1500 N/mm²

### Stahl verschleißfest

- 1.3401·Manganstahl
- 1.4713·X10CrAlSi7
- HB 400·warmgewalzt · schwarz
- HB 500·warmgewalzt · schwarz

### Kupferlegierung

- 2.0060·Kupfer CW004A
- 2.0321·Messing CW508L (CuZn37)

---

## 4. Tube Materials

Registered values for `Q_TUBE_MATERIAL`.

### Aluminium

- Beliebiges Aluminium·blank
- EN AW-6060 (AlMgSi0,5) 3.3206·T66 Mill-finish

### Stahl

- Allgemeiner Baustahl·schwarz
- E235 S2 (EN 10305-1)·nahtlos · kaltgefertigt · gebeizt
- E235 S2 (EN 10305-3)·geschweißt · kaltgefertigt · gebeizt
- P235GH (1.0345)·geschweißt · kaltgefertigt · schwarz
- S195T (1.0026)·mittelschwer · nahtlos · kaltgefertigt · schwarz
- S235JRH (1.0039)·kaltgefertigt · schwarz
- S355J2H (1.0576)·kaltgefertigt · schwarz
- S355J2H (1.0576)·geschweißt · warmgefertigt · schwarz
- S355J2H (1.0576)·nahtlos · kaltgefertigt · schwarz
- S355J2H (1.0576)·warmgewalzt · nahtlos · schwarz

### Edelstahl

- Beliebiger Edelstahl·blank
- 1.4301·geschweißt · geglüht
- 1.4301·geschweißt · geschliffen Korn 240
- 1.4301·geschweißt · unbehandelte Oberfläche
- 1.4301·nahtlos · unbehandelte Oberfläche
- 1.4571·geschweißt · unbehandelte Oberfläche
- 1.4571·seamless · untreated surface

---

## 5. Turning Materials

Registered values for `Q_TURNING_MATERIAL`.

### Aluminium

- Beliebiges Aluminium
- 3.0615·EN AW-6012 · AlMgSiPb
- 3.1325·EN AW-2017A · AlCu4MgSi
- 3.1645·EN AW-2007 · AlCu4PbMgMn · gepresst
- 3.1645·EN AW-2007 · AlCuMgPb · gezogen
- 3.1655·EN AW-2011 · AlCu6BiPb
- 3.2315·EN AW-6082 · AlMgSi1 · gepresst
- 3.2347·EN AW-6023 · AlSi1Sn1MgBi
- 3.3205·EN AW-6060 · AlMgSi
- 3.3535·EN AW-5754 · AlMg3
- 3.3547·EN AW-5083 · AlMg4,5Mn0,7
- 3.4335·EN AW-7020 · AlZn4,5Mg1
- 3.4365·EN AW-7075 · AlZn5,5MgCu · gepresst
- EN AW-6026LF·AlMgSiBi

### Stahl

- Beliebiger Stahl
- 1.0038·S235JR
- 1.0122·S235JRC · kaltgezogen · h9
- 1.0501·C35
- 1.0503·C45 · kaltgezogen · h9
- 1.0503·C45 · warmgewalzt
- 1.0504·C45Pb
- 1.0577·S355J2 · warmgewalzt
- 1.0579·S355J2C · kaltgezogen · h9
- 1.0715·11SMn30 · kaltgezogen · h9
- 1.0718·11SMnPb30
- 1.2210·115CrV3
- 1.6580·30CrNiMo8
- 1.6582·34CrNiMo6
- 1.7131·16MnCr5 · warmgewalzt
- 1.7139·16MnCrS5 · kaltgezogen · h9
- 1.7225·42CrMo4 · warmgewalzt · vergütet
- 1.7227·42CrMoS4
- 1.8838·S460ML
- 1.8915·P460NL1
- 1.8918·P460NL2
- 1.8928·S690QL
- 1.8983·S890QL

### Edelstahl

- Beliebiger Edelstahl
- 1.1191·C45e
- 1.2436·X210CrW12
- 1.4021·X20Cr13
- 1.4034·X46Cr13
- 1.4057·X17CrNi16-2
- 1.4060·X35Cr16N
- 1.4104·X14CrMoS17
- 1.4112·X90CrMoV18
- 1.4122·X39CrMo17-1
- 1.4301·X5CrNi18-10 · blankgezogen · h9
- 1.4301·X5CrNi18-10 · warmgewalzt
- 1.4305·X8CrNiS18-9 · blankgezogen · h9
- 1.4305·X8CrNiS18-9 · warmgewalzt
- 1.4404·X2CrNiMo17-12-2 · blankgezogen · h9
- 1.4404·X2CrNiMo17-12-2 · warmgewalzt
- 1.4435·X2CrNiMo18-14-3
- 1.4462·X2CrNiMoN22-5-2
- 1.4539·X1NiCrMo­CuN25-20-5
- 1.4541·X6CrNiTi18-10
- 1.4571·X6CrNiMoTi17-12-2 · blankgezogen · h9
- 1.4571·X6CrNiMoTi17-12-2 · warmgewalzt
- 1.4828·X15CrNiSi20-12
- 1.4841·X15CrNiSi25-21

---

## 6. Milling Materials

Registered values for `Q_MILLING_MATERIAL`.

### Aluminium

- Beliebiges Aluminium
- 3.0615·EN AW-6012 · AlMgSiPb
- 3.1325·EN AW-2017A · AlCu4MgSi
- 3.1645·EN AW-2007 · AlCu4PbMgMn
- 3.1655·EN AW-2011 · AlCu6BiPb
- 3.2315·EN AW-6082 · AlSi1MgMn
- 3.3205·EN AW-6060 · AlMgSi
- 3.3535·EN AW-5754 · AlMg3
- 3.3547·EN AW-5083 · AlMg4,5Mn0,7
- 3.4335·EN AW-7020 · AlZn4,5Mg1
- 3.4365·EN AW-7075 · AlZn5,5MgCu
- EN AW-6026LF·AlMgSiBi

### Stahl

- Beliebiger Stahl
- 1.0038·S235JR
- 1.0122·S235JRC+C
- 1.0501·C35
- 1.0503·C45+C
- 1.0504·C45Pb
- 1.0577·S355J2
- 1.0579·S355J2C+C
- 1.0715·11SMn30+C
- 1.0718·11SMnPb30
- 1.2210·115CrV3
- 1.6580·30CrNiMo8
- 1.6582·34CrNiMo6
- 1.7131·16MnCr5
- 1.7225·42CrMo4
- 1.7227·42CrMoS4
- 1.8838·S460ML
- 1.8915·P460NL1
- 1.8918·P460NL2
- 1.8928·S690QL
- 1.8983·S890QL

### Edelstahl

- Beliebiger Edelstahl
- 1.1191·C45e
- 1.2436·X210CrW12
- 1.4021·X20Cr13
- 1.4034·X46Cr13
- 1.4057·X17CrNi16-2
- 1.4060·X35Cr16N
- 1.4104·X14CrMoS17
- 1.4112·X90CrMoV18
- 1.4122·X39CrMo17-1
- 1.4301·X5CrNi18-10
- 1.4305·X8CrNiS18-9
- 1.4404·X2CrNiMo17-12-2
- 1.4418·X4CrNiMo16-5-1
- 1.4435·X2CrNiMo18-14-3
- 1.4462·X2CrNiMoN22-5-2
- 1.4539·X1NiCrMo­CuN25-20-5
- 1.4541·X6CrNiTi18-10
- 1.4571·X6CrNiMoTi17-12-2
- 1.4828·X15CrNiSi20-12
- 1.4841·X15CrNiSi25-21

---

## 7. Change Management

Material catalog changes shall be proposed via pull request. Each proposal shall include:

- Product-type applicability
- Material family
- Material designation and condition
- Business rationale
- Backward compatibility analysis

---

## 8. Change Log

| Version | Date | Description |
|---|---|---|
| v0.3 | 2026-07-02 | Added product-specific material catalogs for sheet, tube, turning, and milling |
