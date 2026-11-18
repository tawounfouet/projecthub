---
id: PH-CTX-HIST-001
title: "ProjectHub - Public Project History"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-18"
updated_at: "2026-11-18"
sources:
  - PH-CNV-001
  - PH-CNV-002
  - PH-CNV-003
  - PH-CNV-004
---

# ProjectHub - Project History

> Public, high-level history of **product discussions**. This is not a release history or a statement that described features are implemented.

## Timeline

| Date | Discussion milestone | Interpretation |
|---|---|---|
| 2026-06-30 | Initial exploration of a project management platform with backlog, labels, milestones, GitHub Projects, Table/Board/Roadmap views and reproducible CLI workflows | Early technical and product framing; only partial historical excerpts are currently available |
| 2026-09-11 | Request for a clear project presentation covering vision, problem, solution, architecture, users, features, roadmap and value | A product narrative beyond technical components |
| 2026-11-18 | Engineering-first approach discussed | Quality, testing, architecture and operational excellence emphasized |
| 2026-11-18 | Target of 13 domains reaffirmed and Workspaces retained as first-class concepts | Organization, Workspace, Team and Project must not be conflated |
| 2026-11-18 | Potential internal adoption, open source distribution and managed SaaS explored | Compatible strategic directions, not separate finished products |
| 2026-11-18 | Pilot needs and operational continuity explored | Product discovery should start from real coordination and knowledge-transfer problems |
| 2026-11-18 | Discovery Baseline V1.0 outlined as a traceable Markdown corpus | Documented rationale and requirements before large-scale implementation |
| 2026-11-18 | Public GitHub repository initialized | First public documentation foundation; no application release implied |

## Stable intentions

- Design a generic platform for managing organizations, workspaces, projects and work.
- Use **Django/DRF** and **React/Next.js**, with PostgreSQL as the proposed persistence layer.
- Preserve the **13 target domains**: `core`, `identity`, `organizations`, `portfolios`, `projects`, `workitems`, `planning`, `views`, `collaboration`, `governance`, `integrations`, `automation`, `reporting`.
- Treat a **Workspace** as a collaboration and authorization area within an Organization, not as a filesystem directory.
- Investigate a future self-hostable edition and managed SaaS using a common product core.

## Open decisions

The following are **not yet approved**:

- Final MVP scope and delivery dates
- Open source license and contribution governance
- Commercial pricing and SaaS deployment architecture
- Precise permissions model, tenancy safeguards and integration boundaries
- Institutional participation in proposed pilot programs

## Evidence limitations

Only summaries or extracts of some early conversations are available in the current working corpus. Full historical transcripts are still to be incorporated into the private audit before this history can be considered exhaustive.

No completed application, deployment, customer validation or organizational approval is claimed here.

See [01-source-register.md](01-source-register.md) for the public provenance index.
