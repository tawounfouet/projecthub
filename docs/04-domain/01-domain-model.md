---
id: PH-DOM-MODEL-001
title: "ProjectHub - Modèle de domaine conceptuel (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Domain Modeling - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/04-domain/00-ubiquitous-language.md"
  - "docs/04-domain/02-domain-boundaries.md"
  - "docs/03-requirements/02-business-rules-and-permissions.md"
---

# ProjectHub - Modèle de domaine conceptuel

> **Édition publique expurgée, draft.** Ce modèle est une proposition DDD cohérente avec le glossaire et le catalogue de Requirements. Il ne décrit pas des tables PostgreSQL existantes, ni un schéma Django approuvé. Les cardinalités et événements restent candidats.

## 1. Carte conceptuelle

```text
Organization [tenant logique]
  ├── Workspace [espace de collaboration]
  │     ├── Project [objectif, responsable, livrables]
  │     │     ├── WorkItem [travail, blocages]
  │     │     ├── DocumentReference [lien documentaire]
  │     │     ├── Handover [contexte et reprise]
  │     │     └── ExternalResource [référence vers système tiers]
  │     └── SavedView [projection autorisée]
  └── Membership / Grant [identité, scope et état]

Team, Portfolio, Decision, Risk, Milestone, Integration et reporting
sont reliés par des contrats et autorisations explicites.
```

**Convention :** chaque Workspace appartient à une seule Organization, chaque Project candidat à un seul Workspace et chaque WorkItem candidat à un seul Project. Une personne peut avoir plusieurs memberships sans partager les droits entre tenants.

## 2. Domaines et propriétaires candidats

| Domaine | Propriété principale | Frontière |
|---|---|---|
| `core` | Infrastructure commune, export et conventions | Pas de données métier non justifiées |
| `identity` | Membres, Teams, grants et identités techniques | Ne définit pas les projets |
| `organizations` | Organizations, Workspaces et références de relations | Client ne devient pas tenant |
| `portfolios` | Groupements stratégiques | Ne crée pas de droits supplémentaires |
| `projects` | Project, objectifs et livrables | Project distinct du dépôt Git |
| `workitems` | WorkItem et son cycle de vie | Ne décide pas des approbations métier |
| `planning` | Milestone et périodes | N'opère pas le déploiement |
| `views` | SavedView et projections filtrées | Pas d'accès étendu |
| `collaboration` | Références documentaires, activité, Handover | Pas de GED forcée |
| `governance` | Decision, Risk et approbations (proposition) | Mandat indépendant du rôle technique |
| `integrations` | Liens et adaptateurs externes | Source de vérité tierce préservée |
| `automation` | Règles et actions sous permission | Pas de droits implicites d'agent |
| `reporting` | Indicateurs et calculs explicables | Pas de lecture cross-tenant |

## 3. Registre des 20 agrégats candidats

| ID | Racine candidate | Domaine | Invariant principal |
|---|---|---|---|
| `PH-DM-AGG-001` | Organization | organizations | Identité du tenant explicite |
| `PH-DM-AGG-002` | Workspace | organizations | Un parent Organization |
| `PH-DM-AGG-003` | Membership / Grant | identity | Sujet, périmètre, rôle et état cohérents |
| `PH-DM-AGG-004` | Team | identity | Membres sans ACL implicite |
| `PH-DM-AGG-005` | Project | projects | Workspace unique et responsable traçable |
| `PH-DM-AGG-006` | WorkItem | workitems | Parent et transition autorisés |
| `PH-DM-AGG-007` | Deliverable | projects | Réalisation distincte de l'acceptation |
| `PH-DM-AGG-008` | Decision | governance | Autorité et approbation traçables |
| `PH-DM-AGG-009` | Risk | governance | Évaluation distincte d'un Incident |
| `PH-DM-AGG-010` | DocumentReference | collaboration | Provenance, visibilité, classification |
| `PH-DM-AGG-011` | Handover | collaboration | Préparation distincte de validation |
| `PH-DM-AGG-012` | Milestone | planning | Jalons distincts du déploiement |
| `PH-DM-AGG-013` | Portfolio | portfolios | Regroupement sans droit nouveau |
| `PH-DM-AGG-014` | ExternalResource | integrations | Propriétaire et droits externes préservés |
| `PH-DM-AGG-015` | Integration | integrations | Configuration et credentials isolés |
| `PH-DM-AGG-016` | SavedView | views | Filtres non privilégiés |
| `PH-DM-AGG-017` | MetricDefinition | reporting | Calcul daté et borné |
| `PH-DM-AGG-018` | AutomationRule | automation | Déclenchement autorisé |
| `PH-DM-AGG-019` | ClientReference | organizations (option) | Client sans tenant implicite |
| `PH-DM-AGG-020` | ServicePrincipal | identity | Identité non humaine et droits bornés |

Le nom d'un agrégat n'est **pas** nécessairement celui d'un modèle ORM. Les unités transactionnelles définitives sont à arbitrer en ADR.

## 4. Les 30 relations et cardinalités candidates

| ID | Relation | Cardinalité ou règle envisagée |
|---|---|---|
| `PH-DM-REL-001` | Organization -> Workspace | 1 vers 0..N, parent unique |
| `PH-DM-REL-002` | Workspace -> Project | 1 vers 0..N, parent unique |
| `PH-DM-REL-003` | Project -> WorkItem | 1 vers 0..N, exception éventuelle à arbitrer |
| `PH-DM-REL-004` | User <-> Organization | N:N par memberships |
| `PH-DM-REL-005` | User <-> Workspace | N:N par grants à définir |
| `PH-DM-REL-006` | User <-> Team | N:N, sans permission automatique |
| `PH-DM-REL-007` | Team <-> Workspace | N:N candidat, non finalisé |
| `PH-DM-REL-008` | User <-> Project | N:N éventuel, héritage ouvert |
| `PH-DM-REL-009` | Project -> ProjectLead | 0..1 actif, vacance à décider |
| `PH-DM-REL-010` | Project -> Substitute | 0..N, pas de grant implicite |
| `PH-DM-REL-011` | WorkItem -> Assignee | 0..1 principal, extension ouverte |
| `PH-DM-REL-012` | WorkItem <-> WorkItem | Dépendances dirigées et cycles contrôlés |
| `PH-DM-REL-013` | Project -> Objective | 0..N |
| `PH-DM-REL-014` | Project -> Deliverable | 0..N |
| `PH-DM-REL-015` | Project <-> Portfolio | N:N intra-tenant, sans élargir les droits |
| `PH-DM-REL-016` | Portfolio -> Program / Theme | À décider |
| `PH-DM-REL-017` | Project -> Milestone | 0..N |
| `PH-DM-REL-018` | Milestone <-> WorkItem | Cardinalité ouverte |
| `PH-DM-REL-019` | Decision -> sujet ciblé | Une portée typée et autorisée |
| `PH-DM-REL-020` | Decision -> Approval | 0..N |
| `PH-DM-REL-021` | Risk -> Project / Workspace | Un scope typé, à décider |
| `PH-DM-REL-022` | Risk -> WorkItem de traitement | 0..N, WorkItem garde son propriétaire |
| `PH-DM-REL-023` | Subject -> DocumentReference | 0..N, accès source non conféré |
| `PH-DM-REL-024` | Project -> Handover | 0..N, successions historisées |
| `PH-DM-REL-025` | Handover -> Validation | 0..N, preuve d'exercice |
| `PH-DM-REL-026` | Project -> ExternalResource | 0..N |
| `PH-DM-REL-027` | Integration -> ExternalResource | 0..N, secrets séparés |
| `PH-DM-REL-028` | Project -> ClientReference | Multiple, principal éventuel |
| `PH-DM-REL-029` | User -> SavedView | 0..N, partage borné |
| `PH-DM-REL-030` | MetricDefinition -> ReportSnapshot | 0..N, date et provenance |

Ces relations sont conceptuelles : FK, table d'association, référence stable ou événement seront déterminés pendant l'Architecture & Engineering Baseline.

## 5. Les 20 commandes métier candidates

| ID | Commande | Racine | Précondition publique |
|---|---|---|---|
| `PH-DM-CMD-001` | `CreateOrganization` | Organization | Autorité de création / provisioning |
| `PH-DM-CMD-002` | `CreateWorkspace` | Workspace | Droit de créer dans Organization |
| `PH-DM-CMD-003` | `InviteMember` | Membership | Invitation autorisée sans accès immédiat |
| `PH-DM-CMD-004` | `ActivateMembership` | Membership | Acceptation et grant cohérents |
| `PH-DM-CMD-005` | `RevokeMembership` | Membership | Droit de révocation et protection owner |
| `PH-DM-CMD-006` | `CreateProject` | Project | Workspace autorisé |
| `PH-DM-CMD-007` | `ChangeProjectLead` | Project | Acteur habilité et responsable éligible |
| `PH-DM-CMD-008` | `CreateWorkItem` | WorkItem | Project parent autorisé |
| `PH-DM-CMD-009` | `AssignWorkItem` | WorkItem | Droit d'assigner et assignee éligible |
| `PH-DM-CMD-010` | `ChangeWorkItemStatus` | WorkItem | Transition autorisée, pas approbation métier |
| `PH-DM-CMD-011` | `AttachDocumentReference` | DocumentReference | Source et portée vérifiées |
| `PH-DM-CMD-012` | `ProposeDecision` | Decision | Sujet et acteur légitimes |
| `PH-DM-CMD-013` | `ApproveDecision` | Decision | Mandat de décision prouvé |
| `PH-DM-CMD-014` | `RecordRisk` | Risk | Portée et acteur habilités |
| `PH-DM-CMD-015` | `PrepareHandover` | Handover | Projet, relais et contexte identifiés |
| `PH-DM-CMD-016` | `ValidateHandover` | Handover | Exercice de reprise et validation autorisée |
| `PH-DM-CMD-017` | `LinkExternalResource` | ExternalResource | Lien et tenant valides, sans sync implicite |
| `PH-DM-CMD-018` | `RequestScopedExport` | Export | Scope, classification et droit vérifiés |
| `PH-DM-CMD-019` | `SaveView` | SavedView | Filtre et éventuel partage autorisés |
| `PH-DM-CMD-020` | `RegisterMilestone` | Milestone | Projet et échéance cohérents |

Une commande doit vérifier le demandeur, la cible, l'Organization, le grant, le mandat éventuel et les préconditions avant mutation.

## 6. Les 20 événements candidats

| ID | Événement | Domaine source | Invariant |
|---|---|---|---|
| `PH-DM-EVT-001` | `organization.created` | organizations | Bootstrap borné |
| `PH-DM-EVT-002` | `workspace.created` | organizations | Scope vérifié |
| `PH-DM-EVT-003` | `membership.invited` | identity | Invitation distincte des droits |
| `PH-DM-EVT-004` | `membership.activated` | identity | Grants mis à jour |
| `PH-DM-EVT-005` | `membership.revoked` | identity | Caches et sessions réévalués |
| `PH-DM-EVT-006` | `project.created` | projects | Tenant borné |
| `PH-DM-EVT-007` | `project.lead_changed` | projects | Historique des responsables |
| `PH-DM-EVT-008` | `project.status_changed` | projects | Date et scope fiables |
| `PH-DM-EVT-009` | `workitem.created` | workitems | Parent valide |
| `PH-DM-EVT-010` | `workitem.assignee_changed` | workitems | Affectation autorisée |
| `PH-DM-EVT-011` | `workitem.status_changed` | workitems | Pas de validation automatique |
| `PH-DM-EVT-012` | `document_reference.linked` | collaboration | Aucun grant externe |
| `PH-DM-EVT-013` | `decision.proposed` | governance | Décision non approuvée |
| `PH-DM-EVT-014` | `decision.approved` | governance | Mandat prouvé |
| `PH-DM-EVT-015` | `risk.recorded` | governance | Risque distinct de l'incident |
| `PH-DM-EVT-016` | `handover.prepared` | collaboration | Préparation distincte de reprise |
| `PH-DM-EVT-017` | `handover.validated` | collaboration | Reprise vérifiée |
| `PH-DM-EVT-018` | `external_resource.linked` | integrations | Lien, pas synchronisation |
| `PH-DM-EVT-019` | `export.completed` | core | Tenant et export auditables |
| `PH-DM-EVT-020` | `saved_view.created` | views | Filtres protégés |

Un événement ne doit jamais servir à contourner une autorisation ni déclencher une cascade métier implicite. Le choix d'un broker d'événements n'est pas arrêté.

## 7. Invariants et scénarios négatifs

- Toute relation entre entités porte un tenant et une vérification du parentage.
- Un ClientReference, un Portfolio ou une Team n'accorde pas automatiquement de droits aux Projects reliés.
- Une décision approuvée suppose une autorité prouvée ; un admin de la plateforme n'est pas toujours approbateur.
- Une Handover préparée ne prouve pas la capacité de reprise.
- Un statut historique importé n'est pas une information actuelle vérifiée.
- Le passage d'un Project dans une autre Organization ne se résume pas à modifier sa clé étrangère.
- Une SavedView, une métrique ou un export applique les mêmes droits que les objets sources.
- Une ressource externe conserve son système maître, ses droits et ses politiques propres.

**Tests à préparer :** lectures directes cross-tenant, ID falsifiés, accès révoqués, création d'enfant dans un parent étranger, approbation sans mandat, export mixte, accès par cache, lien externe et reprise non vérifiée.

## 8. Décisions d'architecture encore ouvertes

- Modèle exact des grants et héritages : `PH-OPEN-002`.
- Propriété définitive Decision/Risk : `PH-OPEN-003`.
- Isolation des données, migrations et services Cloud : `PH-OPEN-006`.
- Identité Client / Organization / Team : `PH-OPEN-016`.
- Modèle des références externes et premiers connecteurs : `PH-OPEN-004`.
- Export, rétention et suppression : `PH-OPEN-026`.

**Le modèle est documenté mais non approuvé.** Voir [langage ubiquitaire](00-ubiquitous-language.md), [frontières](02-domain-boundaries.md) et [règles d'accès](../03-requirements/02-business-rules-and-permissions.md).
