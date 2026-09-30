# Orderspot Processing Mapping

This library maps screenshot-confirmed Orderspot sheet-processing controls to
existing STEP-Q fields. It is separate from `mappings/orderspot-materials/`, whose
source-specific validator is designed for material identities.

## Supported mappings

- `edgeRounding` maps directly to `Q_EDGE_ROUNDING`.
- `countersinksAmount` and `threadCuttingsAmount` map to the corresponding
  STEP-Q counts. Their selection switches gate the counts; an unselected
  operation maps to zero.
- `galvanizing` maps electrolytic and hot-dip galvanizing to the registered
  `Q_GALVANIZING` values. "Kein Verzinken" means the field is omitted.
- When `respectDirection` is enabled, horizontal 0 degrees maps to `parallel`
  and vertical 90 degrees maps to `perpendicular`. When it is disabled,
  `Q_ROLLING_DIRECTION` is `arbitrary`.

The mapping entries are declarative contracts; this repository does not yet
contain an Orderspot processing-data adapter that executes their named
transforms. Source values in the screenshots are UI labels. Confirm the raw
Orderspot API/export codes and their Boolean/null representations before using
these mappings in a production integration.

## Not mapped

- `deburring`: the UI only specifies whether "Entgraten / gratarm geschnitten"
  is selected, while STEP-Q `Q_DEBURRING` requires a specific deburring method.
- `certificates`: the UI switch requests a certificate but does not select an
  EN 10204 type, which is required by STEP-Q `Q_TEST_REPORT`.
- `grindingLock`: this is a UI lock/control state, not a manufacturing
  requirement in the current STEP-Q field registry.
- `hotDipGalvanizing`: not mapped independently because the visible galvanizing
  selector already expresses the selected method; mapping both risks conflict.
- `amount`, `batchSize`, `respectDirection`-independent grinding metadata,
  `powdering`, `surface`, and `overwrite`: the screenshots do not establish
  target semantics or a registered STEP-Q field for these values. Material
  and surface selection remains in the separate material mapping.

## Validation

```powershell
python tools/validate_mappings.py
python -m unittest discover -s mappings/orderspot-processing/tests -p "test_*.py"
python mappings/orderspot-materials/validate.py
```

The discovery command supports the hyphenated library directory name.