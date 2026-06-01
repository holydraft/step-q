# STEP-Q vs. STEP AP242

Maintained by holydraft

---

## 1. Purpose of This Document

This document explains the relationship between STEP-Q and ISO 10303-242 (STEP AP242).

Core statement:

> STEP-Q and AP242 are not competing standards. They answer different questions and can be used together.

AP242 addresses rich engineering, MBD, PMI, and lifecycle-oriented product data exchange.

STEP-Q addresses a narrower operational question: which quotation-relevant manufacturing and commercial metadata does a supplier, platform, or RFQ system need in order to assess a part reliably?

---

## 2. Short Answer

AP242 asks:

> How can rich engineering and product-definition data be exchanged across design, manufacturing, and lifecycle processes?

STEP-Q asks:

> Which offer-relevant and manufacturing-relevant metadata should travel with a STEP-based part request so quotation workflows become more explicit and machine-readable?

That difference in question matters more than any specific STEP carrier file.

---

## 3. Scope Demarcation

### AP242

AP242 is a broad STEP application protocol for managed model-based 3D engineering. It is commonly associated with:

- rich geometry exchange
- PMI and semantic GD&T
- model-based definition workflows
- assemblies, configurations, and lifecycle-related engineering data
- integration with PLM-style environments

### STEP-Q

STEP-Q is a lightweight RFQ metadata layer for STEP files. It is intended to make quotation-relevant manufacturing information explicit and machine-readable without redefining geometry.

Typical STEP-Q content includes registered fields such as:

- Q_MATERIAL
- Q_PRIMARY_PROCESS
- Q_QUANTITY
- Q_TOLERANCE_CLASS
- Q_SURFACE
- Q_CERTIFICATE
- Q_PACKAGING
- drawing-driven supplementary fields from the current field registry

STEP-Q does not replace AP242, PMI, ISO GPS, technical drawings, CAM, ERP, or quality management systems.

---

## 4. Workflow Perspective

| Workflow question | AP242 | STEP-Q |
|---|---|---|
| Exchange full engineering model intent | Primary fit | Not the purpose |
| Carry semantic PMI and GD&T | Primary fit | Out of scope in the current draft |
| Provide a normalized RFQ field vocabulary | Not the main focus of the standard | Core purpose |
| Help supplier quotation systems extract quote inputs consistently | Possible only through implementation-specific modeling choices | Primary fit |
| Replace production planning, CAM, ERP, or QM systems | No | No |

STEP-Q is therefore complementary to AP242 rather than an alternative to it.

---

## 5. Data Overlap

Some information relevant to quotation can also appear in AP242-based datasets. That does not create a conflict.

The practical difference is usually this:

- AP242 can represent rich engineering meaning in many valid ways depending on the authoring system and modeling approach.
- STEP-Q defines a smaller, direct vocabulary for quotation-relevant metadata using registered field names and simpler extraction expectations.

This means AP242 may carry more engineering context, while STEP-Q may provide a clearer RFQ-oriented access layer for a narrower set of questions.

---

## 6. What STEP-Q Does Not Claim

STEP-Q does not claim that AP242 is obsolete.

STEP-Q does not claim that AP242 cannot represent related information.

STEP-Q does not claim that AP214 is the preferred path, the reference profile, or the main supported protocol.

STEP-Q does not replace technical drawings, PMI, CAM data, ERP execution logic, or quality planning.

---

## 7. Carrier Neutrality

STEP-Q is application-protocol agnostic.

AP203, AP214, and AP242 are possible STEP carrier formats for STEP-Q metadata.

The current repository includes p21 examples and tools that demonstrate one practical embedding style. Those examples are implementation artifacts of the current draft repository, not a statement that STEP-Q is bound to one specific carrier.

---

## 8. Summary

AP242 is about rich engineering data exchange.

STEP-Q is about making supplier-facing quotation metadata explicit, structured, and automatable.

AP242 and STEP-Q can coexist in the same ecosystem. In some workflows AP242 may carry the engineering definition while STEP-Q provides a simpler RFQ-oriented metadata layer for procurement, supplier onboarding, costing, or quotation automation.

