# ProjectHub documentation

This directory hosts the **public, non-confidential** documentation for ProjectHub.

## Discovery Baseline V1.0

| Section | Purpose | Status |
|---|---|---|
| [00-context](00-context/) | Project history, provenance, decisions and unknowns | In progress |
| [01-product](01-product/) | Product vision, strategy and scope | Planned |
| [02-discovery](02-discovery/) | Users, problems and workflows | Planned |
| [03-requirements](03-requirements/) | Functional and non-functional requirements | Planned |
| [04-domain](04-domain/) | Shared vocabulary and domain boundaries | Planned |
| [05-mvp](05-mvp/) | MVP scope, journeys and backlog | Planned |
| [06-validation](06-validation/) | Pilot validation and Discovery review | Planned |

The complete target baseline contains **25 Markdown documents** across these seven sections. It is a plan, not a claim that all documents have been completed.

## Source-to-requirement traceability

The intended sequence is:

```text
Source -> Observation -> User need -> Requirement -> Acceptance criterion
                                                  -> MVP / backlog item
```

A historical note is not proof that the corresponding action remains open today. Similarly, a design proposal is not an approved requirement.

## Document rules

- Each substantive document should identify its owner, version, status, classification and sources.
- Preferred lifecycle: `draft`, `in-review`, `approved`, `superseded`.
- Source and requirement IDs must remain stable across revisions.
- Keep the public version generic, minimal and free of sensitive organizational detail.
- Publish pilot-specific information only with explicit authorization and adequate review.
- Store private operational documents and original interviews outside this public repository.
- Do not copy raw AI session transcripts, internal audits or infrastructure details into public issues.

## Proposed next documents

1. `00-context/02-canonical-context.md`
2. `00-context/03-decisions-register.md`
3. `00-context/04-open-questions.md`
4. `01-product/00-product-vision.md`

The initial [public source register](00-context/01-source-register.md) is intentionally a **sanitized index**, not a copy of the private, comprehensive working register.
