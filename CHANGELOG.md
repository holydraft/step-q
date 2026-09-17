# Changelog

All notable changes to published STEP-Q draft releases are documented in this file.

## v0.3.0 - Integration Preview (planned)

### Added

- first public mapping-library architecture under `mappings/`
- first platform mapping preview: Orderspot, outside STEP-Q Core
- deterministic local validation for mapping libraries
- bidirectional mapping semantics with collision safeguards
- `three91:quote` documented as a possible STEP-Q producer and orchestration layer

### Changed

- clarified that mappings normalize external RFQ data to registered STEP-Q fields without extending the Core
- documented `partial` and `unmapped` integration values as explicit non-automated outcomes
- cleaned up specification structure and documentation terminology

## v0.2 - 2026-05-28

### Added

- quickstart guidance for a reproducible evaluation path
- a reference validator and metadata parser
- a shared STEP-Q registry module for tooling
- a local browser-based workbench for reading and writing STEP-Q metadata
- realistic `.STEP` example fixtures, including raw and annotated real-world samples
- GitHub Actions checks for the documented example validation path

### Changed

- promoted the repository state to an evaluable public draft
- aligned the specification, registries, and supporting docs to the v0.2 release state
- removed the earlier `.Q.STEP` naming recommendation in favor of content-based identification
- normalized example fixture names to ordinary `.STEP` filenames

## v0.1 - 2026-02-11

### Added

- initial public draft of the core STEP-Q specification
- field registry, enumeration registry, and validation rules
- contribution, governance, roadmap, and licensing documents