# Orderspot Mapping Library

Orderspot is the first reference implementation of the generic STEP-Q mapping
contract. It is an integration library, not a STEP-Q Core dependency.

## Scope

This first preview contains only material mappings that can be resolved against
both the canonical STEP-Q catalog and the current Orderspot CSV source. The
library intentionally excludes `partial` and `unmapped` values from automated
conversion.

- STEP-Q catalog: `spec/materials.md`
- Orderspot source: `spec/materials_orderspot.csv`
- Existing analysis: `spec/q-sheet-material-orderspot-mapping.md`
- Declarative mapping: [mapping.yaml](mapping.yaml)
- Enum policy: [enum-mapping.yaml](enum-mapping.yaml)

The STEP-Q material label remains canonical. Orderspot identifiers are lookup
coordinates, not replacement values for the STEP-Q catalog.

## Validation

```powershell
python tools/validate_mappings.py
```

The validator is deliberately local and deterministic. It does not call an
Orderspot service and does not infer missing mappings.
