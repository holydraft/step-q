# three91:quote and STEP-Q

Status: Planned integration architecture

## Role

`three91:quote` is an orchestration and interpretation system for later
producer, manufacturer, and fabricator integrations. It is not itself a
producer and is not part of the STEP-Q standard.

The system may receive heterogeneous RFQ inputs such as:

- unstructured email and customer messages
- STEP files
- PDFs and technical drawings
- ERP or platform data

It can extract requirements, resolve conflicts, normalize the result, and hand
the resulting RFQ model to a downstream producer or manufacturing integration.
That downstream integration may export validated STEP-Q metadata for its target
platform or workflow.

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
        -> downstream producer/manufacturer/fabricator integration
        -> validated STEP-Q output where supported
```

No public API contract or proprietary field list is implied by this document.
Future producer integrations should use the generic mapping layer under
`mappings/` rather than adding platform-specific fields to STEP-Q Core.
