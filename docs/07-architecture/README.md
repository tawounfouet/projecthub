# 07 - Architecture & Engineering

Ce dossier regroupe les plans d'arbitrage et la baseline technique candidate de **ProjectHub Architecture & Engineering Baseline V1.0**. Aucun ADR n'est considéré comme approuvé, aucun POC comme exécuté et aucun socle E0 comme livré du seul fait de leur publication.

## Documents

| Document | Destination et statut |
|---|---|
| [00-adr-tenancy-permissions-pre-e0-plan.md](00-adr-tenancy-permissions-pre-e0-plan.md) | **Édition publique expurgée**, `draft`, plan d'ADR, isolation et permissions |
| [ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md](ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md) | **Source exhaustive conservée intégralement**, 1 815 lignes, encore marquée `INTERNAL` et `DRAFT / PROPOSED` |

## Avertissement de publication

**Exception explicite à examiner avant fusion :** le document exhaustif a été reproduit **sans modifier sa classification** `INTERNAL - exhaustive working edition`, conformément à la demande de dépôt intégral. Il ne s'agit donc pas d'une édition publique expurgée au sens de la [politique documentaire](../PUBLICATION-POLICY.md).

La présence de ce document sur une branche d'un **dépôt public** le rend accessible même avant fusion. Le mainteneur doit relire **l'intégralité du document** et confirmer explicitement les droits de publication de cette exception. Les contrôles automatisés de noms, chemins et secrets ne constituent pas une garantie absolue de confidentialité.

## Étapes de validation technique

- Décider les responsables et les autorités des ADR.
- Comparer les options d'isolation multi-tenant (`ADR-0004`).
- Définir les permissions, memberships, grants et mandats métier (`ADR-0005`).
- Évaluer PostgreSQL RLS par un POC sans présumer de son adoption (`ADR-0019`).
- Préparer des scénarios E0 avec deux Organizations fictives et des tests de refus.
- Maintenir E1 en `No-Go` tant que les autorisations et gates applicables ne sont pas démontrées.

Voir les [règles métier](../03-requirements/02-business-rules-and-permissions.md), les [NFR](../03-requirements/01-non-functional-requirements.md), les [frontières du domaine](../04-domain/02-domain-boundaries.md) et le [plan pilote](../06-validation/00-pilot-validation-plan.md).
