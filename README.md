# ProjectHub

**ProjectHub** is an evolving project and work management platform designed to connect organizational goals, projects, teams and execution tools.

> Status: **Discovery**. This repository currently contains the public documentation foundation for **ProjectHub Discovery Baseline V1.0**. It is not yet a functional application.

[![ProjectHub product vision - conceptual illustration](docs/01-product/assets/00-product-vision.png)](docs/01-product/00-product-vision.md)

*ProjectHub product vision (concept illustration). [Explore the vision](docs/01-product/00-product-vision.md) or [browse the Product documentation](docs/01-product/README.md).*

## Product direction

- **Organizations** own their data and define the primary security boundary.
- **Workspaces** organize collaboration, projects and access within an organization.
- **Teams** can work across workspaces.
- **Projects** connect outcomes and deliverables to **WorkItems**.
- **Integrations** can link ProjectHub to external engineering and collaboration tools.

The long-term direction includes a self-hostable open source distribution and a managed SaaS service. Product scope, pricing and licensing remain subject to validation.

## Target architecture

The [engineering baseline](docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md) proposes a modular monolith. This target stack and its versions remain subject to ADRs and bootstrap validation:

**Application and data:**<br>
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django + DRF](https://img.shields.io/badge/Django%20%2B%20DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

**Development and CI:**<br>
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

The target domain map contains 13 modules:

```text
core · identity · organizations · portfolios · projects · workitems
planning · views · collaboration · governance · integrations
automation · reporting
```

These are **target domain boundaries**, not a commitment to implement every module in the first release.

## Documentation

Start with [docs/README.md](docs/README.md). The public Discovery Baseline is organized under `docs/00-context/` through `docs/06-validation/`.

- [Project history](docs/00-context/00-project-history.md)
- [Public source register](docs/00-context/01-source-register.md)

## Project status and contributions

This is an early-stage project. Issues can be used to discuss validated, non-sensitive product requirements. Please do **not** publish personal information, third-party documents, credentials or security findings in public issues.

No license has been selected yet. **Public visibility alone does not grant permission to reuse, modify or redistribute the code.** The distribution and contribution policies will be defined before the first public source-code release.

## Security and privacy

Operational documents from pilot organizations, internal analyses, credentials and infrastructure details are **not hosted in this public repository**. The public source register contains sanitized references only.

## Contributors

- `copilot-swe-agent[bot]` (GitHub Copilot) — AI-assisted documentation and repository contributions.

## Maintainer

Project initiated in the [tawounfouet](https://github.com/tawounfouet) GitHub account.
