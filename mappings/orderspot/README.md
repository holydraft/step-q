# Orderspot Mapping Library

Orderspot is the first reference implementation of the generic STEP-Q mapping
contract. It is an integration library, not a STEP-Q Core dependency.

## Scope

This first preview is a **verified collision-free preview subset**. It contains
only material mappings that can be resolved against both the canonical STEP-Q
catalog and the current Orderspot CSV source. The library intentionally excludes
`partial` and `unmapped` values from automated conversion.

- STEP-Q catalog: `spec/materials.md`
- Orderspot source: `spec/materials_orderspot.csv`
- Existing analysis: `spec/q-sheet-material-orderspot-mapping.md`
- Declarative mapping: [mapping.yaml](mapping.yaml)
- Enum policy: [enum-mapping.yaml](enum-mapping.yaml)

The STEP-Q field is `Q_MATERIAL`; for sheet materials its controlled enum is
`Q_SHEET_MATERIAL`, and `step_q_value` contains the registered material label.
Orderspot identifiers are lookup coordinates, not replacement values for the
STEP-Q catalog.

The source identity is the tuple
`materialTypeNumber + surfaceNorm + productionMethod`. The Orderspot validator
checks that every active mapping exists in the CSV and that no source identity
or STEP-Q value is mapped more than once. Only lossless, collision-free entries
are marked `bidirectional`; normalized entries remain one-way.

## Validation

```powershell
python tools/validate_mappings.py
python mappings/orderspot/validate.py
```

The validator is deliberately local and deterministic. It does not call an
Orderspot service and does not infer missing mappings.
