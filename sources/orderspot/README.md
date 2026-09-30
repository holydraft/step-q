# Orderspot Source Data

This directory contains external Orderspot catalog data used by the
Orderspot mapping library. It is not part of the STEP-Q specification.

## Dataset

`materials.csv` is a semicolon-delimited material catalog snapshot. Its
identifiers are used by `mappings/orderspot-materials/` as source identity fields:
`materialTypeNumber`, `surfaceNorm`, and `productionMethod`.

The dataset is kept separate from `spec/` because it belongs to the external
platform rather than to the STEP-Q Core vocabulary or normative specification.

## Provenance

The current file is a repository snapshot supplied for the Orderspot mapping
library. The source URL, export date, source version, license, and responsible
contact were not included with the imported CSV and must be recorded before a
future refresh or redistribution decision. The snapshot must not be presented
as a complete or live Orderspot catalog without confirmation from the provider.