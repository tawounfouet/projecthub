---
id: PH-CTX-SRC-001
title: "ProjectHub - Public Source Register"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-18"
updated_at: "2026-11-18"
baseline: "ProjectHub Discovery Baseline V1.0"
related_documents:
  - "docs/00-context/00-project-history.md"
---

# ProjectHub - Public Source Register

> **Public sanitized edition.** The more detailed working register and original organizational records remain private. This document deliberately excludes internal filenames, personal machine paths, security findings, operational identifiers and confidential discussions.

## Purpose

This register makes it possible to trace publicly stated product context to its source **category** without disclosing the source material itself.

A source being listed does not imply permission to publish it, endorsement by any third party, or proof that a historical operational condition remains current.

## Source statuses

| Status | Meaning |
|---|---|
| `excerpt` | Only an excerpt or high-level historical context is available |
| `reviewed-private` | Source studied in a private workspace; contents are not public |
| `current-discussion` | Statement or intention expressed in the working conversation |
| `derived` | Assistant-created synthesis; not an independent primary source |
| `pending` | Source not yet received or reviewed |

## Registered sources

| Source ID | Date / period | Category | Access | Use for ProjectHub |
|---|---|---|---|---|
| `PH-CNV-001` | 2026-06-30 | Initial ProjectHub design conversation | `excerpt` | GitHub Projects, planning primitives, reproducible CLI, initial stack |
| `PH-CNV-002` | 2026-09-11 | Project introduction conversation | `excerpt` | Product presentation context |
| `PH-CNV-003` | 2026-09-11 | Eight-part product presentation request | `excerpt` | Vision-to-value narrative |
| `PH-CNV-004` | 2026-11-18 | Current ProjectHub design discussion | `current-discussion` | Workspaces, target domains, strategy, Discovery program |
| `PH-OPS-001` | 2026-08 | Nonprofit IT coordination record | `reviewed-private` | Work tracking, ownership, knowledge transfer |
| `PH-OPS-002` | 2026-07 | Technical portfolio and work-management documents | `reviewed-private` | Project inventory, prioritization, operational quality |
| `PH-OPS-003` | 2026-11 | Technical workspace structure shared for analysis | `reviewed-private` | Distinctions between projects, packages, integrations and infrastructure |
| `PH-DER-001` | 2026-11-18 | Internal strategic synthesis | `derived` | Recap of product hypotheses |
| `PH-DER-002` | 2026-11-18 | Internal historical audit | `derived` | Provenance checking and unresolved questions |
| `PH-DER-003` | 2026-11-18 | Internal canonical context | `derived` | Cross-session continuity |

The full private register uses finer-grained source IDs and page references. Those identifiers can be mapped to public requirements only after privacy and publication review.

## Publicly established product context

| Statement | Source | Evidence status |
|---|---|---|
| ProjectHub is intended as a generic project and work management platform | `PH-CNV-001`, `PH-CNV-004` | Explicit product intent |
| Workspaces remain a first-class domain concept | `PH-CNV-004` | Explicit product direction |
| The target architecture lists 13 functional domains | `PH-CNV-001`, `PH-CNV-004` | Target scope, not delivered scope |
| Self-hosted and SaaS editions are considered | `PH-CNV-004` | Strategy under evaluation |
| Coordination and continuity are relevant user problems | `PH-OPS-001`, `PH-OPS-002` | Candidate needs; formal validation pending |

## Known gaps

| Gap ID | Missing evidence | Required action |
|---|---|---|
| `PH-GAP-001` | Complete early design conversation exports | Recover and reconcile privately |
| `PH-GAP-002` | Confirmed requirements from pilot users | Conduct interviews and record approvals |
| `PH-GAP-003` | Up-to-date operational status of historical work items | Verify with authorized source owners |
| `PH-GAP-004` | Final MVP, licensing and SaaS choices | Record formal decisions |
| `PH-GAP-005` | Authorization to quote third-party source material | Obtain before publishing any excerpts |

## Rules for future updates

1. Give each new source a stable ID.
2. State collection date, source type, access status, owner and classification in the **private** register.
3. Distinguish user observations from assistant proposals and validated product requirements.
4. Refer to private sources in public documents by **sanitized ID only**.
5. Never commit credentials, private meeting transcripts, client datasets, vulnerability details or personal contact information.
6. Review sensitive material before referencing it in a public issue or pull request.

## Next planned documents

- `02-canonical-context.md`
- `03-decisions-register.md`
- `04-open-questions.md`

These will be public drafts until reviewed and explicitly approved.
