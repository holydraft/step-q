# three91:quote and STEP-Q

Status: Planned integration architecture

## Role

`three91:quote` is a possible STEP-Q producer and an orchestration and
interpretation system for downstream platform, producer, manufacturer, and
fabricator integrations. It is not part of the STEP-Q standard.

The system may receive heterogeneous RFQ inputs such as:

- unstructured email and customer messages
- STEP files
- PDFs and technical drawings
- ERP or platform data

It can extract requirements, resolve conflicts, normalize the result, and export
validated STEP-Q metadata. The same normalized RFQ model may also be handed to
a platform-specific integration without passing through STEP-Q first.

## Boundary to STEP-Q

STEP-Q is the transportable, validated output model for supported requirements.
`three91:quote` may maintain a richer internal model, but the following remain
outside the STEP-Q Core for this preview:

- AI confidence values
- source provenance and evidence graphs
- internal reasoning or agent traces
- orchestration state and platform-specific workflow data

The boundary is therefore:

```text
heterogeneous RFQ inputs
        -> three91:quote orchestration and interpretation
        -> normalized internal RFQ model
                   -> validated STEP-Q output
                   -> platform-specific producer/manufacturer/fabricator integration
```

No public API contract or proprietary field list is implied by this document.
Orderspot is a possible consumer and producer integration. Future platform
integrations should use the generic mapping layer under `mappings/` rather than
adding platform-specific fields to STEP-Q Core.
