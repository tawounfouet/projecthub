# 07 - Architecture & Engineering

Ce dossier regroupe les plans d'arbitrage et la baseline technique candidate de **ProjectHub Architecture & Engineering Baseline V1.0**. Aucun ADR n'est considéré comme approuvé, aucun POC comme exécuté et aucun socle E0 comme livré du seul fait de leur publication.

## Documents

| Document | Destination et statut |
|---|---|
| [00-adr-tenancy-permissions-pre-e0-plan.md](00-adr-tenancy-permissions-pre-e0-plan.md) | **Édition publique expurgée**, `draft`, plan d'ADR, isolation et permissions |
| [ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md](ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md) | **Édition exhaustive conservée intégralement**, 1 815 lignes, classée `public` depuis `PH-DEC-019`, toujours `DRAFT / PROPOSED - NOT APPROVED` |
| [01-documentation-quality-ci-plan.md](01-documentation-quality-ci-plan.md) | **Plan public de qualité documentaire**, `draft`, workflow GitHub Actions **proposé / non implémenté** |

## Décision de publication

**`PH-DEC-019` - 2026-11-21.** Le mainteneur a retenu l'option d'acceptation documentée : conserver l'édition exhaustive dans `docs/07-architecture/`, la classer `public` et maintenir son statut `DRAFT / PROPOSED - NOT APPROVED`. Le contenu reste une proposition d'architecture, pas une validation métier ni un ADR approuvé.

Cette décision ne remplace pas la relecture humaine prescrite par la [politique documentaire](../PUBLICATION-POLICY.md) pour toute évolution future du document.

## Étapes de validation technique

- Décider les responsables et les autorités des ADR.
- Comparer les options d'isolation multi-tenant (`ADR-0004`).
- Définir les permissions, memberships, grants et mandats métier (`ADR-0005`).
- Évaluer PostgreSQL RLS par un POC sans présumer de son adoption (`ADR-0019`).
- Préparer des scénarios E0 avec deux Organizations fictives et des tests de refus.
- Maintenir E1 en `No-Go` tant que les autorisations et gates applicables ne sont pas démontrées.

Voir les [règles métier](../03-requirements/02-business-rules-and-permissions.md), les [NFR](../03-requirements/01-non-functional-requirements.md), les [frontières du domaine](../04-domain/02-domain-boundaries.md) et le [plan pilote](../06-validation/00-pilot-validation-plan.md).
