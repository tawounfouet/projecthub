---
id: PH-REP-DISC-POST-001
title: "ProjectHub - Bilan de publication de Discovery Baseline V1.0"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub maintainer"
created_at: "2026-11-21"
updated_at: "2026-11-21"
related_documents:
  - "docs/README.md"
  - "docs/PUBLICATION-POLICY.md"
  - "docs/COLLABORATION-BEST-PRACTICES.md"
  - "docs/06-validation/01-discovery-baseline-review.md"
---

# Bilan de publication - ProjectHub Discovery Baseline V1.0

> **Bilan public, rédaction du 21 novembre 2026.** Ce document dresse le retour d'expérience de la **mise en oeuvre du processus documentaire et GitHub**, non d'une application logicielle. La Discovery a été publiée en 25 éditions publiques, mais la baseline métier, le MVP et les pilotes ne sont pas formellement validés par cette publication.

## 1. Résumé

L'objectif du programme était de transformer un corpus de travail détaillé en une **documentation publique de conception autonome et expurgée**, sans diffuser les données internes ou opérationnelles des contextes d'étude.

Résultat **vérifiable sur GitHub** :
- **4 lots documentaires** préparés et fusionnés : PUBLIC-01 à PUBLIC-04 ;
- **25 documents de Discovery** présents sur la branche `main`, répartis dans sept dossiers ;
- **1 guide transversal de collaboration** GitHub / GitLab / Azure DevOps et une illustration PNG ajoutés séparément ;
- **5 Pull Requests** fusionnées par `squash merge` ;
- une [politique de publication](../PUBLICATION-POLICY.md) pour séparer les éditions publiques et les sources privées ;
- une [revue de baseline](../06-validation/01-discovery-baseline-review.md) qui conserve les réserves et les limites de preuve.

**Le programme de publication documentaire est achevé. La validation produit, l'architecture opérationnelle et l'implémentation du MVP restent des chantiers distincts.**

## 2. Inventaire des lots et de leur statut

| Lot | Domaine | Documents publics | Pull Request | État |
|---|---|---:|---|---|
| PUBLIC-01 | Context & Product | 8 | [PR #1](https://github.com/tawounfouet/projecthub/pull/1) | Merged |
| PUBLIC-02 | Product Discovery | 5 | [PR #2](https://github.com/tawounfouet/projecthub/pull/2) | Merged |
| PUBLIC-03 | Requirements & Domain | 7 | [PR #4](https://github.com/tawounfouet/projecthub/pull/4) | Merged |
| PUBLIC-04 | MVP & Validation | 5 | [PR #5](https://github.com/tawounfouet/projecthub/pull/5) | Merged |
| **Total Discovery** | **7 dossiers** | **25** | **4 PR** | **Published** |
| Complément | Guide de collaboration et image | Hors 25 | [PR #3](https://github.com/tawounfouet/projecthub/pull/3) | Merged |

### Répartition des 25 éditions

| Dossier | Quantité | Objet |
|---|---:|---|
| `00-context` | 5 | Historique, sources, contexte, décisions, questions |
| `01-product` | 3 | Vision, stratégie et scope |
| `02-discovery` | 5 | Personas, études génériques, besoins et workflows |
| `03-requirements` | 4 | FR, NFR, règles et traçabilité |
| `04-domain` | 3 | Langage, modèle conceptuel et contrats |
| `05-mvp` | 3 | Définition du MVP, parcours et backlog |
| `06-validation` | 2 | Plan pilote et revue de baseline |

Les éditions publiques sont des **synthèses de conception** : elles ne reproduisent pas toutes les fiches, verbatims et annexes du corpus privé.

## 3. Historique vérifiable sur GitHub

| PR | Branche | Commit de fusion | Fusion UTC |
|---|---|---|---|
| [#1](https://github.com/tawounfouet/projecthub/pull/1) | `docs/discovery-public-01` | `7c07e1e` | 20/11/2026 21:38 |
| [#2](https://github.com/tawounfouet/projecthub/pull/2) | `docs/discovery-public-02` | `37d453d` | 20/11/2026 22:06 |
| [#3](https://github.com/tawounfouet/projecthub/pull/3) | `docs/collaboration-best-practices` | `dd0c5db` | 20/11/2026 22:35 |
| [#4](https://github.com/tawounfouet/projecthub/pull/4) | `docs/discovery-public-03` | `41e851c` | 20/11/2026 22:50 |
| [#5](https://github.com/tawounfouet/projecthub/pull/5) | `docs/discovery-public-04` | `1f449f1` | 20/11/2026 23:03 |

La fin du programme public documentaire est matérialisée par le commit [`1f449f1`](https://github.com/tawounfouet/projecthub/commit/1f449f18723270a2705e12d88ad24c5a44de1fdc).

## 4. Workflow de collaboration effectivement utilisé

```text
Sources de travail privées
  -> édition publique autonome / expurgée
  -> contrôles ciblés Markdown et confidentialité
  -> branche GitHub dédiée
  -> PR Draft
  -> relecture du mainteneur
  -> Ready for review + commentaire d'accord
  -> réponse dans la discussion de PR
  -> squash merge
  -> vérification des fichiers sur main
```

Ce circuit a permis de garder les débats et les vérifications dans les PR. Les **commentaires d'accord du mainteneur** ne doivent pas être présentés comme des reviews indépendantes GitHub `APPROVED`.

## 5. Contrôles de qualité et limites

### Vérifications réalisées

- Existence des 25 documents attendus sur `main`.
- Métadonnées publiques et maintien des statuts `draft`.
- Cohérence des liens relatifs, tableaux, blocs de code et grandes familles d'IDs.
- Contrôles ciblés contre les chemins locaux, identifiants opérationnels et informations sensibles.
- Contrôle `GitGuardian Security Checks` terminé en succès sur chacune des cinq PR.
- Vérification de la présence du guide et du fichier PNG référencé par ce guide.

### Limites importantes

- Les contrôles ciblés ne garantissent pas l'absence de toute information confidentielle.
- GitGuardian ne remplace ni une revue de confidentialité, ni une analyse de sécurité complète.
- La présence de documentation et de critères d'acceptation **ne prouve pas une implémentation logicielle**.
- Une publication validée éditorialement n'implique pas l'approbation métier d'un utilisateur ou d'une organisation.
- Les **45 items de backlog** restent un catalogue de conception : ils ne sont pas déclarés créés comme 45 Issues GitHub.

## 6. Retours d'expérience

| Observation | Enseignement | Amélioration proposée |
|---|---|---|
| Une image existait localement mais n'était pas suivie par Git | `git commit` n'ajoute pas automatiquement les fichiers `untracked` | Vérifier `git status --short` et `git diff --cached --stat` |
| Un commentaire d'accord n'alimentait pas `Approvals` | Conversation et review formelle sont différentes | Afficher clairement le type de validation |
| Certains vérificateurs ponctuels ont mal interprété des IDs ou chemins | Les contrôles eux-mêmes nécessitent des tests | Versionner un script de validation documentaire en CI |
| L'index n'était pas actualisé immédiatement après PUBLIC-04 | Un sommaire peut diverger de l'état GitHub | Corriger l'index et contrôler les états après chaque fusion |
| Les besoins de plusieurs contextes ont été normalisés | L'abstraction doit préserver les frontières organisationnelles | Maintenir deux éditions et leur classification |

## 7. Bilan produit : ce qui est acquis et ce qui ne l'est pas

| Dimension | État à ce stade |
|---|---|
| Documentation de Discovery | **25/25 éditions publiques présentes sur main** |
| Modèle de travail documentaire | **Processus éprouvé sur cinq PR** |
| Guide de contribution | **Publié avec illustration** |
| Approbation métier de la baseline | **En attente** |
| Périmètre MVP définitif | **À arbitrer** |
| Prototype applicatif E0 | **Aucune réalisation ni exécution attestée par ce bilan** |
| Pilote E1 sur données réelles | **No-Go tant que les conditions ne sont pas satisfaites** |
| Huit gates E1 | **NOT_ASSESSED** |
| Offre SaaS Cloud | **Non établie comme opérationnelle** |

Le registre [`PH-REV-001..020`](../06-validation/01-discovery-baseline-review.md) documente **20 réserves de revue**. Leur présence dans `main` ne les ferme pas.

## 8. Prochaines actions recommandées

1. **Corriger l'index documentaire** pour refléter la fusion de PUBLIC-04 et référencer le présent bilan.
2. **Suivre les 20 réserves** avec responsables, décisions et preuves, sans déclarer une clôture anticipée.
3. **Trancher les arbitrages d'architecture** : isolation du tenant, RBAC, Client/Organization/Workspace/Team, propriétaire Decision/Risk, passation.
4. **Préparer Architecture & Engineering Baseline V1.0** : ADR, contrats API, architecture Django/DRF + Next.js, tests et exploitation.
5. **Automatiser les contrôles documentaires en CI** : Markdown, liens, frontmatter, IDs et surveillance des informations à exclure.
6. **Définir la démonstration E0 sur données fictives** avec scénarios nominaux et tests négatifs inter-tenant.
7. **Revoir la valeur avec des utilisateurs** avant de figer le MVP et de transformer les items de backlog en plan de livraison.
8. **Conserver E1 en No-Go** jusqu'aux accords institutionnels et aux preuves des huit gates.

## 9. Décision de clôture

Le programme documentaire **PUBLIC-01 à PUBLIC-04** est **terminé et publié**. Les 25 éditions publiques sont présentes dans `main` et les cinq PR, guide compris, sont fusionnées.

En revanche, **Discovery Baseline V1.0 demeure en attente de validation métier** et le produit n'est pas réputé implémenté. La prochaine phase recommandée est **Architecture & Engineering Baseline V1.0**, en parallèle de la résolution des réserves prioritaires.

### Références

- [Index documentaire](../README.md)
- [Politique de publication](../PUBLICATION-POLICY.md)
- [Guide de collaboration](../COLLABORATION-BEST-PRACTICES.md)
- [Revue Discovery](../06-validation/01-discovery-baseline-review.md)
- [PR #1](https://github.com/tawounfouet/projecthub/pull/1), [PR #2](https://github.com/tawounfouet/projecthub/pull/2), [PR #3](https://github.com/tawounfouet/projecthub/pull/3), [PR #4](https://github.com/tawounfouet/projecthub/pull/4), [PR #5](https://github.com/tawounfouet/projecthub/pull/5)
