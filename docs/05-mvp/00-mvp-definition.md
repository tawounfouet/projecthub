---
id: PH-MVP-DEF-001
title: "ProjectHub - Définition candidate du MVP (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Engineering - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/01-product/02-product-scope.md"
  - "docs/05-mvp/01-user-journeys.md"
  - "docs/05-mvp/02-prioritized-backlog.md"
  - "docs/06-validation/00-pilot-validation-plan.md"
---

# ProjectHub - Définition du MVP

> **Édition publique expurgée - draft.** Ce document expose un MVP candidat issu de la Discovery, sans reprendre les informations propres aux organisations étudiées. Le MVP n'est ni développé, ni officiellement approuvé, ni autorisé pour une exploitation réelle par la simple publication de cette proposition.

## 1. Mission et résultat utilisateur

**MVP candidat :** permettre à une équipe de **qualifier, responsabiliser, suivre, documenter, transmettre et exporter** une initiative, avec des droits explicites et une isolation vérifiable entre Organizations.

Cette proposition se distingue d'un simple gestionnaire de tâches par trois résultats à prouver :
1. une personne retrouve l'objectif, l'état, le responsable et les blocages d'un projet ;
2. une personne différente peut reprendre une action en comprenant les références et les décisions pertinentes ;
3. un acteur habilité peut exporter les informations autorisées sans récupérer les données d'une autre Organization.

Il s'agit de **résultats à démontrer**, et non de fonctionnalités déjà testées.

## 2. Les deux états à ne pas confondre

| État | Données et environnement | Objectif | Ce qu'il ne prouve pas |
|---|---|---|---|
| **E0 - Démonstration** | Deux Organizations fictives, projets et identités synthétiques | Exercer les parcours, les refus et la valeur candidate | Accord d'un pilote, sécurité de production, disponibilité Cloud |
| **E1 - Pilote réel restreint** | Données minimales **explicitement autorisées** et environnement contrôlé | Mesurer l'usage dans un périmètre approuvé | Lancement commercial, conformité globale, marché validé |

Le passage d'E0 à E1 requiert une **décision distincte** et la réussite attestée de huit portes de sécurité, de données et d'exploitation. L'état actuel de ces portes est **non évalué**.

## 3. Acteurs prioritaires candidats

| Acteur | Travail attendu | Limites à respecter |
|---|---|---|
| Coordinateur multi-projets | Préparer une revue fiable | Pas de droits globaux implicites |
| ProjectLead | Qualifier objectifs, responsable et actions | Pas de mandat institutionnel automatique |
| Contributeur | Mettre à jour un WorkItem autorisé | Aucune consultation des projets voisins |
| Membre occasionnel | Comprendre la prochaine action | Accessibilité et contexte clair |
| Successeur | Reprendre un projet et réaliser une action | Une invitation n'octroie pas d'accès tiers |
| OrgAdmin habilité | Gérer le périmètre et révoquer un accès | Pas de pouvoir métier illimité |
| Responsable des données | Exporter et organiser la sortie | Pas d'export cross-tenant |

Ces catégories ne sont pas des personnes réelles ni des rôles RBAC définitivement adoptés.

## 4. Les 13 capacités de périmètre candidat

Les IDs ci-dessous correspondent aux **treize premières capacités** du catalogue `PH-SCP-001..025` ; ils ne constituent pas treize modules Django.

| ID | Capacité MVP candidate | Critère de valeur ou de sûreté |
|---|---|---|
| `PH-SCP-001` | Accès contrôlé et séparation des Organizations | Aucun accès non autorisé entre tenants |
| `PH-SCP-002` | Organizations et Workspaces | Parentage et contexte actif explicites |
| `PH-SCP-003` | Members, invitations et appartenance | Aucun droit actif sans processus prévu |
| `PH-SCP-004` | Rôles essentiels et scopes | Refus par défaut, révocation vérifiée |
| `PH-SCP-005` | Fiche Project avec objectif et contexte | Project créé uniquement dans le Workspace autorisé |
| `PH-SCP-006` | ProjectLead et relais | Responsabilité et relève identifiables |
| `PH-SCP-007` | WorkItems simples | Actions rattachées au bon Project |
| `PH-SCP-008` | État, priorité, affectation, échéance et blocage | Actions lisibles et historisées |
| `PH-SCP-009` | Vue Table / Board minimale à arbitrer | Vue filtrée sans divulgation d'objets |
| `PH-SCP-010` | Références documentaires externes | Pas d'import du contenu ni de grant tiers implicite |
| `PH-SCP-011` | Historique pertinent | Auteur, date, provenance et statut interprétables |
| `PH-SCP-012` | Handover / passation simple | Reprise par une autre personne réellement vérifiée |
| `PH-SCP-013` | Export minimal autorisé | Format compréhensible hors ProjectHub |

**Question ouverte :** la priorité de la vue Table par rapport au Board, les rôles exacts et le niveau de formalisation des approbations doivent être arbitrés avec les utilisateurs et l'architecture.

## 5. Sept slices verticales et ordre proposé

| Slice | Epic candidate | Résultat démontrable | Prérequis principal |
|---|---|---|---|
| `SLICE-00` | `EPIC-FOUNDATION` | Tenants A/B isolés, accès et révocation testables | Politique minimale de scope |
| `SLICE-01` | `EPIC-PROJECTS` | Project + WorkItems + responsabilités | `SLICE-00` |
| `SLICE-02` | `EPIC-VISIBILITY` | Table, historique et informations datées | Projets / travail existants |
| `SLICE-03` | `EPIC-KNOWLEDGE` | Références documentaires sans ingestion | Project autorisé |
| `SLICE-04` | `EPIC-HANDOVER` | Dossier puis exercice de reprise | Suivi + documentation |
| `SLICE-05` | `EPIC-EXIT` | Export lisible et sortie du test | Données et autorisations |
| `SLICE-06` | `EPIC-PILOT-READINESS` | Dossier de décision E1 avec huit gates | E0 démontré, accords et preuves E1 |

`SLICE-05` peut avancer avant `SLICE-04` pour réduire les risques de verrouillage. Les gates E1 ne doivent pas être traitées comme une simple fonctionnalité à coder en fin de parcours.

## 6. Chaîne de valeur témoin

```text
Organization / Workspace autorisé
  -> créer Project et objectif
  -> enregistrer ProjectLead et relais
  -> créer WorkItems, échéances et blocages
  -> consulter Table et historique
  -> lier les documents de référence autorisés
  -> préparer un Handover et faire reprendre une action
  -> exporter le périmètre autorisé
```

À chaque étape, vérifier les refus pour les membres sans droits et les utilisateurs d'une autre Organization.

## 7. Dix parcours E0 de validation

| ID | Parcours | Résultat observé à produire ultérieurement |
|---|---|---|
| `MVP-UJ-01` | Choisir un contexte autorisé | Changement de contexte sans fuite |
| `MVP-UJ-02` | Créer une initiative | Project attaché au bon Workspace |
| `MVP-UJ-03` | Suivre action et blocage | Travail et historique retrouvés |
| `MVP-UJ-04` | Préparer une revue | Synthèse sans faux indicateurs |
| `MVP-UJ-05` | Référencer des documents | Accès à la référence sans droit sur la source tierce |
| `MVP-UJ-06` | Vérifier une passation | Successeur accomplit une action |
| `MVP-UJ-07` | Révoquer sans effacer l'histoire | Ancien membre bloqué, activité conservée |
| `MVP-UJ-08` | Exporter et sortir | Fichier ouvert hors produit et sans fuite |
| `MVP-UJ-09` | Refuser une approbation sans mandat | Refus explicite côté serveur |
| `MVP-UJ-10` | Distinguer ClientReference et Organization | Relation client sans accès cross-tenant |

Les parcours sont décrits dans [01-user-journeys.md](01-user-journeys.md). Les 62 critères d'acceptation du corpus privé restent **des conditions de test candidates non exécutées**.

## 8. Hors périmètre du premier incrément

Ne pas assimiler les 13 domaines cibles à 13 modules entièrement développés. Sont différés :
- intégration GitHub bidirectionnelle, synchronisation de PR et gestion du code ;
- GED, stockage universel de fichiers, duplication des systèmes sources ;
- catalogue d'infrastructure, packages, jobs et dépendances techniques détaillées ;
- moteur généraliste de règles, orchestration ou agents IA autonomes ;
- gestion comptable, CRM, gestion de la gouvernance statutaire d'une organisation ;
- reporting prédictif ou promesse d'indicateurs sans source vérifiable ;
- billing Cloud, SLA commercial et exploitation SaaS publique.

**Ne jamais différer pour autant :** l'isolation, les permissions, les refus, la restauration démontrée avant E1, l'accessibilité essentielle et la réversibilité.

## 9. Test et Definition of Done

Un item MVP ne peut être déclaré terminé que si :
1. son résultat utilisateur et ses critères d'acceptation sont identifiés ;
2. le changement est effectivement implémenté et relié à un commit ;
3. les tests utiles sont exécutés et leurs résultats enregistrés ;
4. les contrôles de périmètre et permissions sont vérifiés sur les accès directs ;
5. les erreurs, cas limites et états non vérifiés sont compréhensibles ;
6. la documentation, les migrations et la réversibilité sont cohérentes ;
7. les réserves et décisions ouvertes restent visibles ;
8. un responsable de validation habilité prend une décision dans son périmètre.

Un ticket marqué `done` ou une revue documentaire fusionnée ne prouve pas à lui seul qu'une fonctionnalité fonctionne.

## 10. Critères de passage E0 / E1

**E0 :** démontrer les parcours dans deux Organizations synthétiques, prouver les refus inter-tenant, l'export, une passation et la gestion des erreurs. Documenter les anomalies et la version testée.

**E1 :** fournir en plus des autorisations appropriées, un plan de données minimisées, les preuves de `G-LEGAL-DATA`, `G-ACCESS`, `G-SECRETS`, `G-BACKUP`, `G-OPERATE`, `G-DATA-EXIT`, `G-ACCESSIBILITY`, `G-CHANGE`, ainsi qu'un verdict formel applicable à chaque organisation.

En l'absence de preuves et d'autorisation, **No-Go E1**.

## 11. Décisions de cadrage restant ouvertes

- `PH-OPEN-001` : périmètre MVP définitivement retenu.
- `PH-OPEN-002` : rôles, délégations et héritages.
- `PH-OPEN-003` : propriétaire canonique Decision/Risk.
- `PH-OPEN-006` : isolation des données en architecture.
- `PH-OPEN-016` : Client, tenant, Workspace et Team.
- `PH-OPEN-024` : scénario d'acceptation de la reprise.
- `PH-OPEN-030` : autorité d'approbation de la baseline.

**Statut :** proposition de MVP non approuvée, à soumettre à la revue métier et à des tests E0.

Lire [parcours utilisateurs](01-user-journeys.md), [backlog](02-prioritized-backlog.md), [plan de validation](../06-validation/00-pilot-validation-plan.md) et [revue de baseline](../06-validation/01-discovery-baseline-review.md).
