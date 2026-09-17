# STEP-Q Q_SHEET_MATERIAL to Orderspot Mapping

Version: v0.3  
Status: Draft  
Source catalog: `spec/materials.md`, section 3  
Orderspot source: `spec/materials_orderspot.csv`

## 1. Purpose

This document maps every registered `Q_SHEET_MATERIAL` catalog label to the
closest Orderspot material record. The STEP-Q catalog label remains the
canonical value. Orderspot is referenced by `materialTypeNumber` and
`surfaceNorm` because one material number can have multiple production and
surface variants.

## 2. Match status

- **exact**: material designation, production method, and surface variant are represented by a matching Orderspot row.
- **normalized**: the same material and variant are represented with different naming, punctuation, or language.
- **partial**: the material is close, but a designation, condition, or surface detail is not represented exactly in the Orderspot source.
- **unmapped**: no sufficiently reliable Orderspot record was found.

For `unmapped` rows, `materialTypeNumber`, `surfaceNorm`, and `productionMethod` are intentionally left blank. These rows must not be silently mapped to a generic material.

## 3. Mapping

| # | STEP-Q `Q_SHEET_MATERIAL` label | materialTypeNumber | surfaceNorm | productionMethod | materialGroup | Status |
|---:|---|---|---|---|---|---|
| 1 | Beliebiges Aluminium·blank |  |  |  | Aluminium | unmapped |
| 2 | EN AW-5754 (AlMg3) 3.3535·H111 Mill-finish | 33.535 | wb | gewalzt H111 | Aluminium | normalized |
| 3 | EN AW-7020 (AlZn4,5Mg1) 3.4335·T651 |  |  |  | Aluminium | unmapped |
| 4 | EN AW 1050A (Al99,5) 3.0255·H14/H24 | 30.255 | wb | gewalzt H14/24 | Aluminium | normalized |
| 5 | EN AW-5754 (AlMg3) 3.3535·H22 Mill-finish | 33.535 | wb | gewalzt H22 | Aluminium | normalized |
| 6 | EN AW-5754 (AlMg3) 3.3535·H111 Mill-finish · Laserfolie einseitig | 33.535 | 1sF | gewalzt H111 | Aluminium | exact |
| 7 | EN AW-5754 (AlMg3) 3.3535·H114 Mill-finish · Riffelblech Quintett | 33.535 | 1MRQ | gewalzt H114 | Aluminium | exact |
| 8 | EN AW-5005 (AlMg1)·H14/24 · farblos bandeloxiert · Laserfolie einseitig | 33.315 | elo1sF | gewalzt H14/24 | Aluminium | normalized |
| 9 | EN AW-5005 (AlMg1)·H14/24 · bandeloxiert E6/EV1 · Laserfolie einseitig | 33.315 | elo1sF | gewalzt H14/24 | Aluminium | normalized |
| 10 | EN AW-5005A (AlMg1) 3.3315·H14/24 · walzblank | 33.315 | wb | gewalzt H14/24 | Aluminium | exact |
| 11 | EN AW-5083 (AlMg4,5Mn0,7) 3.3547·H111 Mill-finish | 33.547 | wb | gewalzt H111 | Aluminium | normalized |
| 12 | EN AW-5083 (AlMg4,5Mn0,7) 3.3547·H22 Mill-finish | 33.547 | wb | gewalzt H22 | Aluminium | normalized |
| 13 | EN AW-6082 (AlMgSi1) 3.2315·T6 Mill-finish | 32.315 | wb | T6 | Aluminium | partial |
| 14 | EN AW-7075 (AlZnMgCu1,5) 3.4365·T6 · walzblank | 34.365 | wb | T6 | Aluminium | exact |
| 15 | EN AW-7075 (AlZnMgCu1,5) 3.4365·T651 · walzblank | 34.365 | wb | T651 | Aluminium | exact |
| 16 | Allgemeiner Baustahl·gebeizt geölt | 10.038 | 1Dg | warmgewalzt | Baustahl | partial |
| 17 | 1.0038·S235JR · warmgewalzt · gebeizt + geölt | 10.038 | 1Dg | warmgewalzt | Baustahl | exact |
| 18 | 1.0038·S235JR · warmgewalzt · walzblau | 10.038 | 1E | warmgewalzt | Baustahl | exact |
| 19 | 1.0038·S235JR · warmgewalzt | 10.038 | 1C | warmgewalzt | Baustahl | normalized |
| 20 | 1.0038·S235JR · warmgewalzt · Tränenblech | 10.038 | 1MT | warmgewalzt | Baustahl | exact |
| 21 | 1.0045·S355JR+N · warmgewalzt · gebeizt + geölt | 10.577 | 1Dg | warmgewalzt | Baustahl | partial |
| 22 | 1.0226·DX51D+Z · gewalzt · feuerverzinkt | 10.226 | FVZ | gewalzt | Baustahl | exact |
| 23 | 1.0226·DX51D+AS120 · gewalzt · AS-beschichtet |  |  |  | Baustahl | unmapped |
| 24 | 1.0242·S250GD+ZM310 · Magnelis |  |  |  | Baustahl | unmapped |
| 25 | 1.0330·DC01 · kaltgewalzt · geölt | 10.330 | 2Dg | kaltgewalzt | Baustahl | exact |
| 26 | 1.0330·DC01 + ZE 25/25 · kaltgewalzt · elektrolytisch verzinkt | 10.330 | EVZ25-25 | kaltgewalzt | Baustahl | exact |
| 27 | 1.0332·DD11 · warmgewalzt · gebeizt + geölt | 10.332 | 1Dg | warmgewalzt | Baustahl | exact |
| 28 | 1.0347·DC03 · kaltgewalzt · walzblank | 10.347 | wb | kaltgewalzt | Baustahl | exact |
| 29 | 1.0398·DD12 · warmgewalzt · gebeizt + geölt | 10.398 | 1Dg | warmgewalzt | Baustahl | exact |
| 30 | 1.0398·DD12 · warmgewalzt · walzblank | 10.398 | wb | warmgewalzt | Baustahl | exact |
| 31 | 1.0425·P265GH · warmgewalzt · walzblau | 10.425 | 1C | warmgewalzt | Baustahl | exact |
| 32 | 1.0425·P265GH · warmgewalzt | 10.425 | 1C | warmgewalzt | Baustahl | exact |
| 33 | 1.0503·C45 · warmgewalzt · walzblau | 10.503 | 1C | warmgewalzt | Baustahl | exact |
| 34 | 1.0577·S355J2+N · warmgewalzt · walzblau | 10.577 | 1E | warmgewalzt | Baustahl | exact |
| 35 | 1.0577·S355J2+N · warmgewalzt | 10.577 | 1C | warmgewalzt | Baustahl | exact |
| 36 | 1.0579·S355J2C+N · warmgewalzt · gebeizt + geölt | 10.577 | 1Dg | warmgewalzt | Baustahl | partial |
| 37 | 1.0976·S355MC · warmgewalzt · gebeizt + geölt | 10.976 | 1Dg | warmgewalzt | Baustahl | exact |
| 38 | 1.0976·S355MC · warmgewalzt · walzblau | 10.976 | 1C | warmgewalzt | Baustahl | exact |
| 39 | 1.0980·S420MC · warmgewalzt · gebeizt + geölt | 10.980 | 1Dg | warmgewalzt | Baustahl | exact |
| 40 | 1.0980·S420MC · warmgewalzt · walzblau | 10.980 | 1C | warmgewalzt | Baustahl | normalized |
| 41 | 1.0984·S500MC · warmgewalzt · gebeizt + geölt | 10.984 | 1Dg | warmgewalzt | Baustahl | exact |
| 42 | 1.0984·S500MC · warmgewalzt · walzblau | 10.984 | 1C | warmgewalzt | Baustahl | exact |
| 43 | 1.5415·16Mo3 · warmfester Baustahl |  |  |  | Baustahl | unmapped |
| 44 | 1.8928·S690QL · warmgewalzt · walzblau |  |  |  | Baustahl | unmapped |
| 45 | 1.8946·S355J2WP (COR-TEN A) · warmgewalzt · blank | 18.946 | wb | warmgewalzt | Baustahl | exact |
| 46 | 1.8965·COR-TEN B (S355J2W) · warmgewalzt · blank | 18.965 | wb | warmgewalzt | Baustahl | exact |
| 47 | 1.8974·S700MC · warmgewalzt · gebeizt + geölt | 18.974 | 1Dg | warmgewalzt | Baustahl | exact |
| 48 | 1.8974·S700MC · warmgewalzt · walzblau | 18.974 | 1C | warmgewalzt | Baustahl | exact |
| 49 | Beliebiger Edelstahl·blank |  |  |  | Nichtrostender Stahl | unmapped |
| 50 | 1.4016·2B · kaltgewalzt | 14.016 | 2B | kaltgewalzt | Nichtrostender Stahl | exact |
| 51 | 1.4016·2R · kaltgewalzt · blankgeglüht | 14.016 | 2R | kaltgewalzt | Nichtrostender Stahl | exact |
| 52 | 1.4016·Korn 240 · einseitig geschliffen, einseitig foliert | 14.016 | K2401sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 53 | 1.4301·1D (alt: III A) · warmgewalzt | 14.301 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 54 | 1.4301·1D (alt: III A) · warmgewalzt · Tränenblech | 14.301 | 1MT | warmgewalzt | Nichtrostender Stahl | exact |
| 55 | 1.4301·2B (alt: III C) · kaltgewalzt | 14.301 | 2B | kaltgewalzt | Nichtrostender Stahl | exact |
| 56 | 1.4301·2B (alt: III C) · kaltgewalzt · Laserfolie einseitig | 14.301 | 2B1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 57 | 1.4301·2G · kaltgewalzt · Laserfolie einseitig · einseitig geschliffen Korn 240 | 14.301 | K2401sF | kaltgewalzt | Nichtrostender Stahl | partial |
| 58 | 1.4301·2G · warmgewalzt · Laserfolie einseitig · einseitig geschliffen Korn 240 | 14.301 | K2401sF | warmgewalzt | Nichtrostender Stahl | partial |
| 59 | 1.4301·2G · kaltgewalzt · Laserfolie einseitig · einseitig geschliffen Korn 320 | 14.301 | K3201sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 60 | 1.4301·2J · kaltgewalzt · Laserfolie einseitig · einseitig gebürstet | 14.301 | G1sF | kaltgewalzt | Nichtrostender Stahl | partial |
| 61 | 1.4301·Korn 180 · einseitig geschliffen, einseitig foliert | 14.301 | K1801sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 62 | 1.4301·Korn 240 · beidseitig geschliffen, beidseitig foliert | 14.301 | K240-2sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 63 | 1.4301·Korn 240 · beidseitig geschliffen, einseitig foliert | 14.301 | 2sK240-1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 64 | 1.4301·Korn 320 · einseitig geschliffen, einseitig foliert | 14.301 | K3201sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 65 | 1.4301·5WL · mustergewalzt, einseitig foliert | 14.301 | 5WL1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 66 | 1.4301·Karo · mustergewalzt, einseitig foliert | 14.301 | Karo1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 67 | 1.4301·Leinen · mustergewalzt, einseitig foliert | 14.301 | Lein1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 68 | 1.4301·Raute · mustergewalzt, einseitig foliert | 14.301 | Raut1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 69 | 1.4301·spiegelpoliert No. 8 | 14.301 | 2P8 | kaltgewalzt | Nichtrostender Stahl | exact |
| 70 | 1.4301·warmgewalzt · Tränenblech | 14.301 | 1MT | warmgewalzt | Nichtrostender Stahl | exact |
| 71 | 1.4401·warmgewalzt · gebeizt | 14.401 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 72 | 1.4401·kaltgewalzt · visuell glatte Oberfläche | 14.401 | 2B | kaltgewalzt | Nichtrostender Stahl | exact |
| 73 | 1.4401·kaltgewalzt · visuell glatte Oberfläche, einseitig foliert | 14.401 | 2B1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 74 | 1.4401·Korn 320 · einseitig geschliffen, einseitig foliert | 14.401 | K3201sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 75 | 1.4404·1D (alt: III A) · warmgewalzt | 14.404 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 76 | 1.4404·1D (alt: III A) · warmgewalzt · Riffelblech | 14.404 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 77 | 1.4404·2B (alt: III C) · kaltgewalzt | 14.404 | 2B | kaltgewalzt | Nichtrostender Stahl | exact |
| 78 | 1.4404·2B (alt: III C) · kaltgewalzt · Laserfolie einseitig | 14.404 | 2B1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 79 | 1.4404·2G · kaltgewalzt · Laserfolie einseitig · einseitig geschliffen Korn 240 | 14.404 | K2401sF | kaltgewalzt | Nichtrostender Stahl | partial |
| 80 | 1.4404·gebürstet · foliert | 14.404 | G1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 81 | 1.4404·kaltgewalzt · blank, reflektierend | 14.404 | 2R | kaltgewalzt | Nichtrostender Stahl | exact |
| 82 | 1.4404·kaltgewalzt · federhart | 14.404 | 2H | kaltgewalzt | Nichtrostender Stahl | exact |
| 83 | 1.4404·Korn 320 · einseitig geschliffen, einseitig foliert | 14.404 | K3201sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 84 | 1.4462·1D (alt: IIA) · warmgewalzt | 14.462 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 85 | 1.4462·kaltgewalzt · rau, stumpf, mechanisch entzundert | 14.462 | 2E | kaltgewalzt | Nichtrostender Stahl | exact |
| 86 | 1.4501·warmgewalzt · gebeizt | 14.501 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 87 | 1.4509·2B (alt: IIIC) · kaltgewalzt | 14.509 | 2B | kaltgewalzt | Nichtrostender Stahl | partial |
| 88 | 1.4539·X1NiCrMoCu 25-20-5 · kaltgewalzt | 14.539 | 2E | kaltgewalzt | Nichtrostender Stahl | normalized |
| 89 | 1.4541·2B (alt: III C) · kaltgewalzt | 14.541 | 2B | kaltgewalzt | Nichtrostender Stahl | exact |
| 90 | 1.4571·1D (alt: III A) · warmgewalzt | 14.571 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 91 | 1.4571·2B (alt: III C) · kaltgewalzt | 14.571 | 2B | kaltgewalzt | Nichtrostender Stahl | exact |
| 92 | 1.4571·Korn 240 · einseitig geschliffen, einseitig foliert | 14.571 | K2401sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 93 | 1.4571·kaltgewalzt · visuell glatte Oberfläche, einseitig foliert | 14.571 | 2B1sF | kaltgewalzt | Nichtrostender Stahl | exact |
| 94 | 1.4828·1D (alt: III A) · warmgewalzt | 14.828 | 1D | warmgewalzt | Nichtrostender Stahl | exact |
| 95 | 1.4828·2B (alt: III C) · kaltgewalzt | 14.828 | 2B | kaltgewalzt | Nichtrostender Stahl | exact |
| 96 | 1.4841·1D (alt: III A) · warmgewalzt |  |  |  | Nichtrostender Stahl | unmapped |
| 97 | 1.4841·2B (alt: III C) · kaltgewalzt |  |  |  | Nichtrostender Stahl | unmapped |
| 98 | 1.4310·Festigkeit 1300 - 1500 N/mm² | 14.310 | 2H | kaltgewalzt | Nichtrostender Stahl | partial |
| 99 | 1.3401·Manganstahl |  |  |  | Baustahl | unmapped |
| 100 | 1.4713·X10CrAlSi7 |  |  |  | Baustahl | unmapped |
| 101 | HB 300·warmgewalzt · schwarz | 18.704 | 1C | warmgewalzt | Baustahl | exact |
| 102 | HB 400·warmgewalzt · schwarz | 18.714 | 1C | warmgewalzt | Baustahl | normalized |
| 103 | HB 450·warmgewalzt · schwarz | 18.722 | 1C | warmgewalzt | Baustahl | exact |
| 104 | HB 500·warmgewalzt · schwarz | 18.734 | 1C | warmgewalzt | Baustahl | exact |
| 105 | 2.0060·Kupfer CW004A | 20.060 | wb | gewalzt | Kupfer | exact |
| 106 | 2.009·Kupfer CW021A | 2.009 | wb | gewalzt | Kupfer | exact |
| 107 | 2.0090·Kupfer CW024A | 20.090 | wb | gewalzt | Kupfer | exact |
| 108 | 2.0321·Messing CW508L (CuZn37) | 20.321 | wb | gewalzt | Messing | exact |
| 109 | 2.0321·Messing CW508L · geschliffen · foliert | 20.321 | K2401sF | gewalzt | Messing | exact |
| 110 | 2.0402·Messing CW612N | 20.402 | wb | gewalzt | Messing | exact |
| 111 | 2.4610·NiMo16Cr16Ti · warmgewalzt · gebeizt | 24.610 | 1D | warmgewalzt | Nickellegierung | exact |
| 112 | 2.4610·NiMo16Cr16Ti · kaltgewalzt · visuell glatte Oberfläche | 24.610 | 2B | kaltgewalzt | Nickellegierung | exact |
| 113 | 2.4668·NiCr19Fe19Nb5Mo3 · kaltgewalzt · visuell glatte Oberfläche | 24.668 | 2B | kaltgewalzt | Nickellegierung | exact |
| 114 | 2.4819·NiMo16Cr15W · kaltgewalzt · visuell glatte Oberfläche | 24.819 | 2B | kaltgewalzt | Nickellegierung | exact |
| 115 | 3.7025·Ti995-Ti-grade1 · gewalzt · walzblank | 37.025 | wb | gewalzt | Titan | exact |
| 116 | 3.7035·Ti994-Ti-grade2 · gewalzt · walzblank | 37.035 | wb | gewalzt | Titan | exact |

## 4. Open mapping items

The following STEP-Q values need a new or clarified Orderspot source record before they can be mapped without qualification:

- generic values `Beliebiges Aluminium·blank` and `Beliebiger Edelstahl·blank`
- `DX51D+AS120`, `S250GD+ZM310`, `16Mo3`, and `S690QL`
- `1.4301` with `Korn 320` on the both-rolled / mixed-surface variants where no exact Orderspot row is available
- `1.4841` in `1D` and `2B` condition
- `1.3401` Manganstahl and `1.4713` X10CrAlSi7

The following partial mappings also need domain confirmation before being used for automated conversion: `EN AW-7020`, `EN AW-6082`, generic Baustahl, `S355JR+N`, `S355J2C+N`, sheet `S235JR` chequer plate, stainless chequer plate, `1.4301`/`1.4404` `2G` variants, `1.4301` `2J`, and `1.4509`.

## 5. Mapping policy

Automated consumers may use `exact` and `normalized` mappings. `partial` mappings require an explicit compatibility decision in the integration layer. `unmapped` values shall remain valid STEP-Q values and shall be reported as unmapped rather than replaced by a generic material.