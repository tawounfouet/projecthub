# PH - Collaborative Project & Work Management Platform

<p align="center">
  <a href="docs/README.md"><img src="https://img.shields.io/badge/Status-Discovery%20Baseline%20V1.0-blue.svg" alt="Status: Discovery Baseline V1.0"></a>
  <a href="docs/README.md"><img src="https://img.shields.io/badge/Docs-Public%20Baseline-2ea44f.svg" alt="Documentation"></a>
  <a href="docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md"><img src="https://img.shields.io/badge/Target%20Stack-Django%20%7C%20Next.js%20%7C%20Postgres-092E20.svg" alt="Target Stack"></a>
  <a href="#security-and-privacy"><img src="https://img.shields.io/badge/Security-Sanitized%20Public%20Corpus-2088FF.svg" alt="Security: Sanitized Public Corpus"></a>
  <a href="#project-status-and-contributions"><img src="https://img.shields.io/badge/License-To%20be%20determined-lightgrey.svg" alt="License: To be determined"></a>
</p>


[![ProjectHub product vision - conceptual illustration](docs/01-product/assets/00-product-vision.png)](docs/01-product/00-product-vision.md)

*ProjectHub product vision (concept illustration). [Explore the vision](docs/01-product/00-product-vision.md) or [browse the Product documentation](docs/01-product/README.md).*

**ProjectHub** is an evolving project and work management platform designed to connect organizational goals, projects, teams and execution tools.

> Status: **Discovery**. This repository currently contains the public documentation foundation for **ProjectHub Discovery Baseline V1.0**. It is not yet a functional application.

## Product direction

- **Organizations** own their data and define the primary security boundary.
- **Workspaces** organize collaboration, projects and access within an organization.
- **Teams** can work across workspaces.
- **Projects** connect outcomes and deliverables to **WorkItems**.
- **Integrations** can link ProjectHub to external engineering and collaboration tools.

```text
┌───────────────────────────────────────────────────────┐
│                     Organization                      │  ◄── Security & Tenant Boundary
└───────────────────────────┬───────────────────────────┘
                            │ 1..*
            ┌───────────────┴───────────────┐
            ▼                               ▼
┌───────────────────────┐       ┌───────────────────────┐
│       Workspace       │       │       Workspace       │
└───────────┬───────────┘       └───────────┬───────────┘
            │ 1..*                          │
            ▼                               ▼
┌───────────────────────┐       ┌───────────────────────┐
│        Project        │       │        Project        │
└───────────┬───────────┘       └───────────┬───────────┘
            │ 1..*                          │
            ▼                               ▼
┌───────────────────────┐       ┌───────────────────────┐
│       WorkItem        │       │       WorkItem        │
└───────────────────────┘       └───────────────────────┘
```

The long-term direction includes a self-hostable open source distribution and a managed SaaS service. Product scope, pricing and licensing remain subject to validation.

## Target architecture

The [engineering baseline](docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md) proposes a modular monolith. This target stack and its versions remain subject to ADRs and bootstrap validation:

```text
┌────────────────────────────────────────────────────────┐
│                   Next.js Web Client                   │  (SSR / React / TS)
└───────────────────────────┬────────────────────────────┘
                            │  HTTPS / REST JSON
                            ▼
┌────────────────────────────────────────────────────────┐
│             Django + Django REST Framework             │  (Modular Monolith)
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │     Core     │  │ Organizations│  │   Projects   │  │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤  │
│  │  WorkItems   │  │  Governance  │  │ Integrations │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└───────────────────────────┬────────────────────────────┘
                            │  SQL / ORM
                            ▼
┌────────────────────────────────────────────────────────┐
│                   PostgreSQL Database                  │  (Tenant-Scoped Data)
└────────────────────────────────────────────────────────┘
```

### Proposed tech stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django + DRF](https://img.shields.io/badge/Django%20%2B%20DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

### Target domain modules

The target domain map contains 13 modules organized across four functional pillars:

| Pillar | Target modules | Key role |
|---|---|---|
| 🔐 **Foundation & Identity** | `organizations` · `identity` · `core` | Multi-tenant isolation, access management, and cross-cutting audit |
| 🎯 **Planning & Execution** | `portfolios` · `projects` · `workitems` · `planning` | Strategic alignment, milestones, tasks, and deliverable tracking |
| 🤝 **Collaboration & Governance** | `collaboration` · `views` · `governance` · `reporting` | Scoped views, contextual handovers, decisions, and analytics |
| ⚡ **Ecosystem & Automation** | `integrations` · `automation` | External connectors (VCS, webhooks) and reactive rule triggers |

These are **target domain boundaries**, not a commitment to implement every module in the first release. See [domain boundaries and contracts](docs/04-domain/02-domain-boundaries.md).

## Documentation

Start with [docs/README.md](docs/README.md). The public Discovery Baseline is organized under `docs/00-context/` through `docs/06-validation/`.

- [Project history](docs/00-context/00-project-history.md)
- [Public source register](docs/00-context/01-source-register.md)

## Repository audit - 2026-11-21

- [INDEX.md](docs/reports/audit-2026-11-21/INDEX.md) - navigation and measured facts.
- [CODEBASE_ANALYSIS.md](docs/reports/audit-2026-11-21/CODEBASE_ANALYSIS.md) - verified findings, bugs B1..B9 and vulnerabilities.
- [ANALYSE_CRITIQUE.md](docs/reports/audit-2026-11-21/ANALYSE_CRITIQUE.md) - verdict and systemic causes.
- [RECOMMANDATIONS.md](docs/reports/audit-2026-11-21/RECOMMANDATIONS.md) - prioritized fixes and acceptance criteria.
- [DOCUMENTATION-SYSTEM.md](docs/reports/audit-2026-11-21/DOCUMENTATION-SYSTEM.md) - current document system and flows.
- [AGENTS.md](AGENTS.md) - rules for future agents.

There is no application to launch and no environment variables to configure in this repository; the available checks are described in [CODEBASE_ANALYSIS.md](docs/reports/audit-2026-11-21/CODEBASE_ANALYSIS.md).

> Audit follow-up: B1..B9 have been addressed. The exhaustive baseline is now classified `public` under `PH-DEC-019` and remains `DRAFT / PROPOSED - NOT APPROVED`; `resources/` and `archives/` are ignored. Historical findings remain in the [audit report](docs/reports/audit-2026-11-21/INDEX.md).

## Project status and contributions

This is an early-stage project. Issues can be used to discuss candidate, non-sensitive product requirements. Please do **not** publish personal information, third-party documents, credentials or security findings in public issues.

No license has been selected yet. **Public visibility alone does not grant permission to reuse, modify or redistribute the code.** The distribution and contribution policies will be defined before the first public source-code release.

## Security and privacy

Operational documents from pilot organizations, internal analyses, credentials and infrastructure details are **not hosted in this public repository**. The public source register contains sanitized references only.

## Contributors

- `copilot-swe-agent[bot]` (GitHub Copilot) - AI-assisted documentation and repository contributions.
- `Antigravity` (Google DeepMind) - AI-assisted codebase audit, architecture diagrams, documentation reorganization, and README enhancements.
- `OpenCode` (opencode/big-pickle) - AI-assisted repository audit, documentation deliverables, cross-reference validation, and session archiving.

## Maintainer

Project initiated in the [tawounfouet](https://github.com/tawounfouet) GitHub account.
