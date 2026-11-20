---
id: PH-DOM-LANG-001
title: "ProjectHub - Langage ubiquitaire (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Domain Modeling - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/00-context/02-canonical-context.md"
  - "docs/03-requirements/02-business-rules-and-permissions.md"
  - "docs/04-domain/01-domain-model.md"
---

# ProjectHub - Langage ubiquitaire

> **Édition publique expurgée, draft.** Le glossaire de conception interne rassemble 145 termes candidats `PH-TERM-001..145` dans 12 groupes. Le présent document en expose la structure et les définitions essentielles, sans reprendre les contre-exemples ou systèmes d'information propres à une organisation. Les termes ne sont pas des classes Django approuvées.

## 1. Pourquoi un langage commun ?

Des mots comme **projet**, **client**, **workspace**, **owner**, **livré** ou **validé** changent de sens selon les équipes. ProjectHub doit éviter de transformer ces ambiguïtés en règles d'accès ou en métriques trompeuses.

Chaque terme canonique doit avoir :
- une définition positive ;
- un usage et un périmètre ;
- des distinctions explicites avec les notions proches ;
- une proposition de propriétaire métier ;
- un statut (`CIBLE`, `PROPOSED`, `OPEN`) ;
- des scénarios ou exigences associés.

## 2. Inventaire des 12 familles de vocabulaire

| Groupe | IDs | Nombre | Sujet |
|---|---|---:|---|
| A | `PH-TERM-001..014` | 14 | Organisation, tenant, Workspace, clients et memberships |
| B | `PH-TERM-015..030` | 16 | Identité, rôles, grants et mandat |
| C | `PH-TERM-031..045` | 15 | Portfolio, Program, Project, objectifs et livrables |
| D | `PH-TERM-046..058` | 13 | WorkItems, tâches, états, assignation et dépendances |
| E | `PH-TERM-059..066` | 8 | Planning, jalons, releases et échéances |
| F | `PH-TERM-067..080` | 14 | Documentation, activité, connaissances et passation |
| G | `PH-TERM-081..090` | 10 | Décision, risque, approbation et gouvernance |
| H | `PH-TERM-091..098` | 8 | Vues, projections, reporting et métriques |
| I | `PH-TERM-099..112` | 14 | Dépôts, ressources externes, intégrations et services |
| J | `PH-TERM-113..118` | 6 | Automatisation, agents IA et déclencheurs |
| K | `PH-TERM-119..131` | 13 | Fiabilité, sécurité, qualité et conformité |
| L | `PH-TERM-132..145` | 14 | Product, Community, Cloud, Pilot et ADR |

Cette grille permet de **préserver la continuité des IDs** même si tous les exemples détaillés du glossaire ne sont pas publiables.

## 3. Concepts structurants

| ID | Terme | Définition publique | À distinguer de |
|---|---|---|---|
| `PH-TERM-001` | `Organization` | Conteneur propriétaire de Workspaces, candidat à l'isolation du tenant | Client, Team, Partner |
| `PH-TERM-002` | `Tenant` | Unité logique d'isolation des données et autorisations, associée ici à Organization | Abonnement ou Workspace |
| `PH-TERM-003` | `Workspace` | Espace de collaboration attaché à une Organization unique | Répertoire de fichiers, Team |
| `PH-TERM-004` | `Team` | Collectif de membres pouvant intervenir dans plusieurs Workspaces | Membership ou tenant |
| `PH-TERM-005` | `Client` | Relation ou bénéficiaire commercial du travail réalisé | Organization utilisatrice |
| `PH-TERM-008` | `OrganizationMembership` | Lien d'appartenance au périmètre organisationnel | Rôle de ProjectLead |
| `PH-TERM-012` | `ActiveContext` | Organization et Workspace explicitement actifs | Permission implicite |
| `PH-TERM-013` | `ClientReference` | Référence au client, indépendante d'une habilitation | Nouvelle Organization automatique |
| `PH-TERM-014` | `BillingAccount` | Référence de facturation Cloud éventuelle | Tenant par définition |
| `PH-TERM-015` | `Person` | Personne du monde métier | Compte utilisateur |
| `PH-TERM-016` | `User` | Identité applicative authentifiable | Personne physique sans compte |
| `PH-TERM-017` | `Persona` | Modèle de besoins utilisé en Discovery | Utilisateur ou rôle RBAC |
| `PH-TERM-019` | `Role` | Regroupement de permissions dans un périmètre | Mandat métier |
| `PH-TERM-020` | `Permission` | Action autorisée sur une catégorie de ressources | Habilitation institutionnelle |
| `PH-TERM-021` | `Grant` | Octroi explicite de droit avec scope et état | Responsabilité non technique |
| `PH-TERM-023` | `Authorization` | Décision d'autoriser une opération | Authentication |
| `PH-TERM-024` | `Authentication` | Vérification de l'identité de la session | Contrôle d'accès métier |
| `PH-TERM-025` | `BusinessMandate` | Autorité légitime pour un acte métier | Administration technique |
| `PH-TERM-026` | `Approver` | Personne autorisée à valider un acte spécifique | Assignee |
| `PH-TERM-027` | `ServicePrincipal` | Identité non humaine avec droits limités | User humain |
| `PH-TERM-031` | `Portfolio` | Ensemble cohérent de projets suivis transversalement | Tenant |
| `PH-TERM-032` | `Program` | Groupement éventuel d'initiatives liées | Project obligatoire |
| `PH-TERM-034` | `Project` | Initiative métier avec résultat attendu et responsables | Repository |
| `PH-TERM-035` | `Initiative` | Proposition de travail à qualifier | Project approuvé |
| `PH-TERM-136` | `Workflow` | Enchaînement d'activités métier et décisions | Machine technique obligée |
| `PH-TERM-137` | `MVP` | Version minimale destinée à tester une valeur vérifiable | Produit commercial terminé |
| `PH-TERM-138` | `PilotOrganization` | Organisation évaluant éventuellement le produit après accord | Client acquis |
| `PH-TERM-139` | `CommunityEdition` | Distribution auto-hébergeable envisagée | Produit déjà licencié |
| `PH-TERM-140` | `CloudEdition` | Service managé futur envisagé | SaaS déjà commercialisé |
| `PH-TERM-141` | `EnterpriseEdition` | Hypothèse future de service ou hébergement | Version disponible |
| `PH-TERM-142` | `OpenCore` | Modèle de séparation éventuelle de fonctions ouvertes et commerciales | Choix validé |
| `PH-TERM-143` | `Baseline` | Référence documentaire et ses réserves | Approbation automatique |
| `PH-TERM-144` | `DecisionRecord` | Enregistrement motivé d'un choix | Validation implicite |
| `PH-TERM-145` | `ADR` | Fiche de décision architecturale motivée | Code déjà implémenté |

Les libellés de ce tableau sont volontairement **synthétiques** ; les 145 définitions privées ne sont pas reproduites intégralement.

## 4. Distinctions anti-ambiguïtés

### 4.1. Structure

`Organization` n'est pas `Client` ; `Workspace` n'est pas `Team` ; `Project` n'est pas `Repository`. Une même personne peut être membre de deux Organizations, mais ses droits ne se propagent pas.

### 4.2. Responsabilité

`Owner` peut signifier propriétaire juridique, détenteur des données, responsable de projet, assignee, mainteneur de composant ou compte de facturation. Il faut toujours spécifier **ce dont on est owner**.

### 4.3. Livraison et décision

`done`, `deployed`, `delivered`, `approved`, `accepted` et `closed` sont des événements ou états différents. Une action technique réussie ne prouve ni acceptation métier ni décision institutionnelle.

### 4.4. Observations et actualité

`ObservedAt`, `RecordedAt`, `VerifiedAt` et `EffectiveAt` ne sont pas équivalents. Une note ancienne ne devient pas un statut courant lorsqu'elle est importée.

### 4.5. Références externes et droits

`DocumentReference` ou `ExternalResource` ne confèrent pas automatiquement l'accès à leur source. Un lien n'est ni une copie ni une synchronisation.

### 4.6. Passation

`HandoverPrepared` n'est pas `HandoverValidated`. Seule une vérification réelle peut démontrer qu'un repreneur comprend et continue le travail.

## 5. Nommage envisagé

- Dans Django/DRF et TypeScript : classes et types anglais stables, par exemple `Organization`, `Workspace`, `Project`, `WorkItem`.
- Dans l'interface : libellés traduits pour les profils non techniques, sans modifier les invariants.
- Dans la documentation : employer les IDs du glossaire pour éviter les synonymes imprécis.
- Aucun renommage de domaine ne doit être appliqué silencieusement à tous les contrats et migrations.

## 6. Gouvernance du vocabulaire

La révision d'un terme doit indiquer le sens actuel, la proposition, les impacts sur FR/NFR/BR, les cas d'usage et la décision d'approbation. Une définition candidate ne doit pas être présentée comme une implémentation Django ou un schéma définitif.

**À valider :** rôles et scopes `PH-OPEN-002`, décisions/risques `PH-OPEN-003`, client/tenant `PH-OPEN-016`, langage des statuts et passation `PH-OPEN-024`.

Voir [modèle de domaine](01-domain-model.md), [frontières](02-domain-boundaries.md), [permissions](../03-requirements/02-business-rules-and-permissions.md).
