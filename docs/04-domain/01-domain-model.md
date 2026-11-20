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

| IDs | Commandes | Garantie déterminante |
|---|---|---|
| `PH-DM-CMD-001..002` | `CreateOrganization`, `CreateWorkspace` | Autorité et parentage |
| `PH-DM-CMD-003..005` | `InviteMember`, `ActivateMembership`, `RevokeMembership` | Invitations distinctes des droits |
| `PH-DM-CMD-006..007` | `CreateProject`, `ChangeProjectLead` | Scope et changement historisé |
| `PH-DM-CMD-008..010` | `CreateWorkItem`, `AssignWorkItem`, `ChangeWorkItemStatus` | Affectation et transitions autorisées |
| `PH-DM-CMD-011` | `AttachDocumentReference` | Lien externe sans grant |
| `PH-DM-CMD-012..014` | `ProposeDecision`, `ApproveDecision`, `RecordRisk` | Mandat et décision distincte du risque |
| `PH-DM-CMD-015..016` | `PrepareHandover`, `ValidateHandover` | Préparation puis preuve de reprise |
| `PH-DM-CMD-017` | `LinkExternalResource` | Provenance sans synchronisation |
| `PH-DM-CMD-018` | `RequestScopedExport` | Export contrôlé et tracé |
| `PH-DM-CMD-019` | `SaveView` | Filtre sous autorisation |
| `PH-DM-CMD-020` | `RegisterMilestone` | Jalon sans pilotage d'infrastructure |

Une commande doit vérifier le demandeur, la cible, l'Organization, le grant, le mandat éventuel et les préconditions avant mutation.

## 6. Les 20 événements candidats

| IDs | Événements | Sens |
|---|---|---|
| `PH-DM-EVT-001..002` | `organization.created`, `workspace.created` | Parentage vérifié |
| `PH-DM-EVT-003..005` | `membership.invited`, `membership.activated`, `membership.revoked` | Cycle des accès |
| `PH-DM-EVT-006..008` | `project.created`, `project.lead_changed`, `project.status_changed` | Historique projet |
| `PH-DM-EVT-009..011` | `workitem.created`, `workitem.assignee_changed`, `workitem.status_changed` | Historique d'exécution |
| `PH-DM-EVT-012` | `document_reference.linked` | Lien sans permission externe |
| `PH-DM-EVT-013..015` | `decision.proposed`, `decision.approved`, `risk.recorded` | Gouvernance avec autorité |
| `PH-DM-EVT-016..017` | `handover.prepared`, `handover.validated` | Transmission et reprise distinctes |
| `PH-DM-EVT-018` | `external_resource.linked` | Système externe référencé |
| `PH-DM-EVT-019` | `export.completed` | Export borné et audité |
| `PH-DM-EVT-020` | `saved_view.created` | Vue sans privilège nouveau |

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
