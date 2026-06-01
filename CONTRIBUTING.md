
# Contributing to STEP-Q

Maintained by holydraft

---

## 1. Purpose

This document defines the contribution process for the STEP-Q specification.

Its goal is to ensure technical consistency, backward compatibility,
and long-term stability.

---

## 2. Scope

This process applies to contributions affecting:

- Specification documents
- Field registry
- Enumeration registry
- Validation rules
- Examples
- Schemas and tools

---

## 3. Contribution Channels

All contributions shall be submitted via GitHub pull requests.

Direct commits to main branches are restricted to maintainers.

---

## 4. Types of Contributions

### 4.1 Editorial Changes

Includes:

- Typo corrections
- Formatting improvements
- Clarifications

These may be merged after lightweight review.

---

### 4.2 Technical Extensions

Includes:

- New fields
- New enumeration values
- New validation rules
- Schema updates

These require full technical review.

---

### 4.3 Breaking Changes

Includes:

- Removal of fields
- Renaming of fields
- Semantic changes
- Validation tightening

These require major version updates.

---

## 5. Proposal Requirements

All technical proposals must include:

1. Technical description
2. Business rationale
3. Example use cases
4. Backward compatibility analysis
5. Migration strategy (if applicable)

Incomplete proposals will not be reviewed.

For bug reports, conformance questions, or draft feedback, contributors should include the most relevant available evidence, for example:

- affected file or example path
- validator output
- specification section reference
- expected versus actual behavior

---

## 6. Review Process

1. Submission via pull request
2. Automated checks (if applicable)
3. Maintainer technical review
4. Community feedback (optional)
5. Approval or rejection

Standard review period: 30 calendar days.

---

## 7. Decision Authority

Final decisions are made by the maintainers.

Currently:

- holydraft

External advisory input may be considered.

---

## 8. Versioning Impact

| Change Type      | Version Impact |
|------------------|----------------|
| Editorial        | Patch          |
| Extension        | Minor          |
| Breaking         | Major          |

Semantic versioning is applied.

---

## 9. Code of Conduct

Contributors are expected to act professionally and respectfully.

Technical discussions shall be factual and constructive.

---

## 10. Intellectual Property

By submitting contributions, contributors confirm that:

- They have the right to submit the content
- The contribution may be published under the project license
- No third-party rights are violated

---

## 11. Contact

Questions regarding contributions:

manuel@holydraft.com
