# 07 - Architecture & Engineering

Ce dossier regroupe les plans d'arbitrage et la baseline technique candidate de **ProjectHub Architecture & Engineering Baseline V1.0**. Aucun ADR n'est considéré comme approuvé. Un POC RLS et un sous-ensemble de tests E0 synthétiques ont été exécutés dans la [PR #15](https://github.com/tawounfouet/projecthub/pull/15); ces preuves ne valent ni approbation ADR ni GO officiel E0, même si le code candidat est intégré au dépôt.

## Documents

| Document | Destination et statut |
|---|---|
| [00-adr-tenancy-permissions-pre-e0-plan.md](00-adr-tenancy-permissions-pre-e0-plan.md) | **Édition publique expurgée**, `draft`, plan d'ADR, isolation et permissions |
| [ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md](ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md) | **Édition exhaustive conservée intégralement**, 1 815 lignes, classée `public` depuis `PH-DEC-019`, toujours `DRAFT / PROPOSED - NOT APPROVED` |
| [01-documentation-quality-ci-plan.md](01-documentation-quality-ci-plan.md) | **Plan public de qualité documentaire**, `draft`, workflow et validateur intégrés dans `main` via la PR #14 |
| [02-architecture-authority-register.md](02-architecture-authority-register.md) | **Registre des autorités pré-E0**, `draft`, cumul opérationnel proposé, actes à formaliser et revue indépendante GOV-04 `PENDING` |
| [03-adr-0019-rls-poc-decision.md](03-adr-0019-rls-poc-decision.md) | **Comparatif POC PostgreSQL RLS**, R-2 recommandé mais `PROPOSED`, [issue #16](https://github.com/tawounfouet/projecthub/issues/16) |
| [Bilan d'exécution P1](../reports/2026-11-21-p1-e0-rls-execution.md) | Tests PostgreSQL, Django, Next.js et Compose avec preuves CI |
| [POC et tests E0 synthétiques](https://github.com/tawounfouet/projecthub/pull/15) | Expérimentation sur deux Organizations fictives, sans GO officiel E0 |

## Décision de publication

**`PH-DEC-019` - 2026-11-21.** Le mainteneur a retenu l'option d'acceptation documentée : conserver l'édition exhaustive dans `docs/07-architecture/`, la classer `public` et maintenir son statut `DRAFT / PROPOSED - NOT APPROVED`. Le contenu reste une proposition d'architecture, pas une validation métier ni un ADR approuvé.

Cette décision ne remplace pas la relecture humaine prescrite par la [politique documentaire](../PUBLICATION-POLICY.md) pour toute évolution future du document.

## Étapes de validation technique

- Faire désigner formellement les responsables et les autorités des ADR, selon le [registre de mandat](02-architecture-authority-register.md) et l'[issue #13](https://github.com/tawounfouet/projecthub/issues/13).
- Comparer les options d'isolation multi-tenant (`ADR-0004`).
- Définir les permissions, memberships, grants et mandats métier (`ADR-0005`).
- Examiner les résultats du POC PostgreSQL RLS exécuté dans la PR #15 sans présumer de son adoption (`ADR-0019`).
- Préparer des scénarios E0 avec deux Organizations fictives et des tests de refus.
- Maintenir E1 en `No-Go` tant que les autorisations et gates applicables ne sont pas démontrées.

Voir les [règles métier](../03-requirements/02-business-rules-and-permissions.md), les [NFR](../03-requirements/01-non-functional-requirements.md), les [frontières du domaine](../04-domain/02-domain-boundaries.md) et le [plan pilote](../06-validation/00-pilot-validation-plan.md).
