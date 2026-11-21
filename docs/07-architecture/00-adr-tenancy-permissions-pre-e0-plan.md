---
id: PH-AE-DEC-EXEC-001
title: "ProjectHub - Plan d'arbitrage ADR, multi-tenancy et permissions avant E0"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
owner: "ProjectHub Architecture - titulaire à confirmer"
review_status: REQUIRED
adr_status: PROPOSED
poc_status: SYNTHETIC_POC_EXECUTED_IN_PR15
related_open_questions: [PH-OPEN-002, PH-OPEN-006, PH-OPEN-016, PH-OPEN-020]
related_adrs: [ADR-0004, ADR-0005, ADR-0019]
publication_status: REVIEW_REQUIRED
---

# Architecture & Engineering - ADR, isolation multi-tenant et permissions avant E0

> **Édition publique candidate - draft.** Cette page est un **plan d'arbitrage technique**, pas une preuve que les décisions ont été approuvées ou qu'un système ProjectHub a été implémenté. Les responsables restent à désigner. Un **sous-ensemble synthétique** des tests d'isolation, de permissions et du POC PostgreSQL RLS a été exécuté dans la [PR #15](https://github.com/tawounfouet/projecthub/pull/15), avec [preuve CI](../reports/2026-11-21-p1-e0-rls-execution.md) ; cela ne clôt pas les ADR, les exigences ni tous les scénarios prévus. Le démonstrateur E0 n'accorde aucune autorisation de pilote E1.

## 1. Objet et résultat attendu

Avant de développer les ressources métier tenant-scoped du premier incrément E0, ProjectHub doit documenter et arbitrer :

1. **`ADR-0004`** : comment Organization, Workspace, Project et WorkItem sont isolés et reliés ;
2. **`ADR-0005`** : comment les permissions s'obtiennent et sont révoquées, indépendamment des responsabilités métier ;
3. **`ADR-0019`** : si une couche PostgreSQL Row-Level Security (RLS) apporte une défense en profondeur utile dès E0.

Ces décisions doivent être liées aux questions `PH-OPEN-002`, `PH-OPEN-006` et `PH-OPEN-016`, aux exigences, aux tests négatifs et à une autorité de décision identifiée.

La phase d'étude peut utiliser un **POC isolé** pour éclairer les décisions ; le code du POC ne représente pas automatiquement le backend du MVP.

## 2. Référentiel documentaire

| Source publique | Règles à préserver |
|---|---|
| [Questions ouvertes](../00-context/04-open-questions.md) | Les décisions structurantes restent `OPEN` |
| [Règles et permissions](../03-requirements/02-business-rules-and-permissions.md) | Membership, Grant et BusinessMandate sont distincts |
| [NFR](../03-requirements/01-non-functional-requirements.md) | Critères définis avant tests, refus inter-tenant |
| [Modèle de domaine](../04-domain/01-domain-model.md) | Parentages et responsabilités canoniques proposés |
| [Frontières de domaine](../04-domain/02-domain-boundaries.md) | 13 domaines cibles sans imposer 13 modules MVP |
| [MVP](../05-mvp/00-mvp-definition.md) | `SLICE-00`, deux Organizations fictives, E0 vs E1 |
| [Revue Discovery](../06-validation/01-discovery-baseline-review.md) | Réserves et gates E1 encore ouvertes |

**L'[édition exhaustive de la baseline](ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md)**, identifiée `PH-AEB-001`, est désormais **publiée intégralement**, sous `classification: public` depuis la décision de publication [`PH-DEC-019`](../00-context/03-decisions-register.md). Cette décision ne valide ni l'architecture, ni les ADR ; son statut reste `DRAFT / PROPOSED - NOT APPROVED`.

## 3. Gouvernance à instituer

Le [registre des autorités et mandats pré-E0](02-architecture-authority-register.md) établit les fonctions, les approbations distinctes et la procédure de nomination. Les titulaires restent `UNASSIGNED` jusqu'à une décision formelle ; voir l'[issue ACT-03 #13](https://github.com/tawounfouet/projecthub/issues/13).

| Décision | Responsable de la préparation | Autorité d'approbation | Situation |
|---|---|---|---|
| `ADR-0004` - Tenancy | Architecture / modèle de données | Autorité architecture | À désigner |
| `ADR-0005` - Permissions | Product/domain + sécurité | Autorité métier, avec revue technique | À désigner |
| `ADR-0019` - RLS | Architecture / DB + sécurité | Autorité architecture | À désigner |
| Protocole de test | QA + backend | Responsable qualité et sécurité selon portée | À désigner |
| Go/No-Go E0 | Référents produit et technique | Autorités compétentes | À désigner |

**Le mainteneur GitHub peut approuver un document public sans devenir par cette approbation l'autorité de décision technique ou métier.** L'examen d'un ADR doit comporter des options, des conséquences, un décideur et une preuve de validation datée.

## 4. Registre des 20 ADR conservés

| ID | Sujet candidat | Priorité de travail |
|---|---|---|
| `ADR-0001` | Architecture modulaire initiale | Bootstrap |
| `ADR-0002` | Versions et upgrades | Bootstrap |
| `ADR-0003` | Session web et identité | E0 |
| `ADR-0004` | Multi-tenancy et parentage | **Critique avant modèles métier** |
| `ADR-0005` | RBAC scoped et mandat métier | **Critique avant permissions métier** |
| `ADR-0006` | Décisions et risques | Avant gouvernance avancée |
| `ADR-0007` | Contrats Domain | Élevée |
| `ADR-0008` | API, erreurs et OpenAPI | Élevée |
| `ADR-0009` | Source de vérité et audit | Élevée |
| `ADR-0010` | Transactions et événements | À calibrer |
| `ADR-0011` | Références externes / GitHub | Selon slice |
| `ADR-0012` | Passation et autonomie | Selon MVP |
| `ADR-0013` | Export et rétention | Critique pour E1 |
| `ADR-0014` | Environnements et déploiement | E0 |
| `ADR-0015` | CI et tests | E0 |
| `ADR-0016` | Observabilité, sauvegarde, rollback | Critique pour E1 |
| `ADR-0017` | Confidentialité, licence, Community/Cloud | Avant diffusion code |
| `ADR-0018` | Accessibilité | Avant pilote |
| `ADR-0019` | RLS PostgreSQL | À décider avec tenancy |
| `ADR-0020` | Releases et migrations | Avant hébergement |

Toutes les entrées sont des **candidates, statut `PROPOSED`**, en l'absence d'une approbation enregistrée dans le registre.

## 5. `ADR-0004` - Options de multi-tenancy

### 5.1. Invariants

- `Organization` est la frontière tenant candidate.
- `Workspace` appartient à une Organization, `Project` à un Workspace et `WorkItem` à un Project.
- Un utilisateur peut appartenir à A et B, mais ses droits ne se propagent pas automatiquement.
- `ClientReference`, `Team`, `Portfolio` et `Repository` n'accordent pas de droits par simple association.
- Toutes les listes, recherches, mutations, exports et projections appliquent les mêmes contrôles tenant.
- L'identifiant Organization demandé par une requête doit être **vérifié côté serveur**.

### 5.2. Comparaison des alternatives

| Option | Description | Principal avantage | Risque / coût |
|---|---|---|---|
| `T-A` | Schéma partagé PostgreSQL, colonnes Organization, contrôles serveur et contraintes DB | Simple pour un premier MVP | Oubli de filtre, parentage incohérent |
| `T-B` | Schéma PostgreSQL par tenant | Séparation logique plus forte | Migrations et maintenance par tenant |
| `T-C` | Base PostgreSQL par tenant | Isolation opérationnelle plus nette | Provisioning, coût et reporting |
| `T-D` | Schéma partagé avec RLS en supplément | Défense contre certaines requêtes SQL mal filtrées | Rôles, sessions SQL et transactions à maîtriser |

**Proposition d'étude :** construire un POC de `T-A`, vérifier le parentage et comparer le surcroît de protection de `T-D` avant toute adoption. Ne pas confondre cette proposition avec un choix approuvé.

### 5.3. Mesures à vérifier

- Une requête A ne peut accéder directement à un objet B.
- Un WorkItem A ne peut être créé sous un Project B.
- Un utilisateur A+B ne subit pas de fuite lors d'une bascule explicite A / B.
- L'export de A ne contient ni données ni références privées de B.
- Le filtre s'applique aussi aux recherches, agrégats, cache et éventuels jobs.

## 6. `ADR-0005` - Permissions et BusinessMandate

### 6.1. Séparation à décider

| Dimension | Rôle |
|---|---|
| `User` | Identité authentifiée |
| `OrganizationMembership` | Appartenance active au tenant |
| `WorkspaceGrant` | Permissions accordées sur un périmètre |
| `Role` | Ensemble d'actions autorisées |
| `ProjectLead` | Responsabilité sur un projet, sans droit admin implicite |
| `BusinessMandate` | Autorité particulière pour une décision ou acceptation |
| `ServicePrincipal` | Identité technique aux droits limités, si nécessaire |

**Hypothèse de conception :** RBAC à portée Organization/Workspace, grants explicites, refus par défaut et mandat métier séparé. L'héritage des droits et les projets privés restent à arbitrer.

### 6.2. Matrice minimale à approuver

| Action | Viewer | Contributor | WorkspaceAdmin | OrgAdmin | Autorité métier |
|---|---|---|---|---|---|
| Lire les Projects autorisés | À définir | À définir | À définir | À définir | Selon grant |
| Créer un WorkItem | Non | Selon grant | Selon politique | Selon politique | Non par défaut |
| Inviter un membre | Non | Non | Selon scope | Selon politique | Non par défaut |
| Exporter | Droit explicite requis | Droit explicite requis | Selon politique | Selon politique | Droit explicite requis |
| Approuver un résultat métier | Non | Non | Non par défaut | Non par défaut | Selon mandat |
| Lire une autre Organization | **Non** | **Non** | **Non** | **Non** | **Non** |

Aucune permission marquée « à définir » ne doit être codée comme autorisation implicite. Il faut aussi traiter : dernière propriété OrgOwner, session révoquée, export déjà créé et droits d'un job différé.

## 7. `ADR-0019` - PostgreSQL RLS : adoption ou report motivé

| Option | Principe | Décision à établir |
|---|---|---|
| `R-0` | Contrôles applicatifs et DB sans RLS au départ | Quels contrôles compensent les risques ? |
| `R-1` | RLS sur tables tenant-scoped dès E0 | Peut-on prouver l'absence de bypass et la sûreté du contexte SQL ? |
| `R-2` | POC RLS puis adoption différée | Quelles preuves déclencheront le réexamen ? |

Une expérimentation RLS doit notamment vérifier le rôle SQL sans `BYPASSRLS`, la propriété des tables, les transactions, l'absence de contexte, la réutilisation des connexions, les requêtes brutes et les migrations. **RLS ne remplace pas le contrôle des memberships et des mandats.**

## 8. Ateliers et livrables proposés

| Atelier | Objectif | Livrable candidat |
|---|---|---|
| `W-AE-01` | Nommer les autorités, cadrer E0 | Mandats et registre d'ADR |
| `W-AE-02` | Comparer les options de tenant et parentage | `ADR-0004` prêt pour revue |
| `W-AE-03` | Résoudre permissions et révocation | `ADR-0005` et matrice de droits |
| `W-AE-04` | Tester le gain d'une RLS | Rapport POC et `ADR-0019` |
| `W-AE-05` | Examiner preuves et risques | Go / No-Go de démarrage E0 |

Aucune réunion n'est présentée comme réservée ou tenue.

## 9. Plan de validation technique E0

**Fixture :** `Demo-Org-A` et `Demo-Org-B`, utilisateurs indépendants et multi-affiliés, membre révoqué, viewer, OrgAdmin sans mandat, Projects de mêmes titres et données fictives clairement distinctes.

### 9.1. Tests d'isolation candidats

| Famille | Scénarios représentatifs | Résultat attendu |
|---|---|---|
| Tenant et objet | Liste, lecture directe, édition de B depuis A | Refus sans fuite |
| Parentage | WorkItem de A relié à Project B | Rejet par modèle et base |
| Identité | Bascule A / B, contexte usurpé, membership supprimé | Droits réévalués |
| Sources dérivées | Recherche, cache, reporting | Aucun objet étranger |
| Export et accès ultérieur | Export A, téléchargement après révocation | Périmètre et droit recontrôlés |
| Services et administration | Job différé, Django admin, service technique | Aucun bypass implicite |

### 9.2. Tests de permissions candidats

- Invitation en attente non égale à membership actif.
- Viewer sans droit d'écriture.
- Contribution limitée au bon Project et Workspace.
- Approbation sans mandat refusée même pour OrgAdmin.
- Revocation effective, y compris session ancienne et éventuels traitements différés.
- Aucune élévation de privilèges par champ ID, rôle ou scope transmis par le navigateur.

Les cas complets sont détaillés dans le document interne, sans résultat prétendu. Un seul défaut de divulgation ou de mutation cross-tenant dans un test critique doit bloquer la décision correspondante.

### 9.3. Modèle de preuve

```yaml
scenario_id: TEN-02
decision: ADR-0004
environment: null
commit_sha: null
fixture: synthetic-org-a-b-v1
expected: "Refus d'accès A vers ressource B"
observed: null
executed_at: null
status: NOT_RUN
reviewer: null
```

`NOT_RUN` et les valeurs nulles sont volontaires. Aucun test n'est réputé réalisé par la publication du protocole.

## 10. Registre de travail préalable à E0

| Séquence | Activité | État |
|---|---|---|
| `P01` | Nommer responsables et pouvoirs d'approbation | `NOT_STARTED` |
| `P02` | Constituer registre des 20 ADR | `NOT_STARTED` |
| `P03` | Comparer alternatives `ADR-0004` | `NOT_STARTED` |
| `P04` | Résoudre scopes et matrice `ADR-0005` | `NOT_STARTED` |
| `P05` | Concevoir deux Organizations fictives | `EXECUTED_IN_PR15_SYNTHETIC` |
| `P06` | Faire POC tenancy et permission | `EXECUTED_IN_PR15_SYNTHETIC` |
| `P07` | Comparer RLS et option sans RLS | `EXECUTED_IN_PR15_SYNTHETIC` |
| `P08` | Exécuter les tests négatifs prioritaires | `PARTIAL_IN_PR15_SYNTHETIC` |
| `P09` | Recueillir les approbations des ADR | `NOT_STARTED` |
| `P10` | Prononcer Go/No-Go de `SLICE-00` | `NOT_STARTED` |

Ces séquences sont des **propositions**, pas des Issues GitHub déjà ouvertes, des travaux effectués ou un calendrier validé.

## 11. Conditions de Go/No-Go

| Condition | État de référence |
|---|---|
| Responsables architecture, produit et sécurité désignés | `NOT_ASSESSED` |
| `ADR-0004` accepté avec son périmètre | `NOT_ASSESSED` |
| `ADR-0005` accepté, matrice de permissions résolue | `NOT_ASSESSED` |
| `ADR-0019` statué (adopter, rejeter ou différer avec motif) | `NOT_ASSESSED` |
| POC et tests d'isolation / révocation exécutés sur données fictives | `NOT_ASSESSED` |
| Risques résiduels traités et décision écrite | `NOT_ASSESSED` |
| Démarrage de `SLICE-00` approuvé | `NOT_ASSESSED` |

**No-Go E1 conservé** : huit gates E1 et accords institutionnels distincts demeurent requis avant toute utilisation de données réelles.

## 12. Modèle simplifié de fiche ADR

```markdown
# ADR-XXXX - Titre

- Statut : PROPOSED
- Date de décision : null
- Autorité : À désigner
- Portée : E0 uniquement si pertinent
- Questions : PH-OPEN-...

## Contexte et contraintes
## Alternatives examinées
## Choix proposé et risques
## Tests prévus et preuves réellement observées
## Approbation / rejet, date, limites
## Déclencheurs de réexamen
```

Une décision `ACCEPTED` doit résulter d'un accord explicite, pas d'une fusion documentaire automatique.

## 13. Décisions encore ouvertes et étapes suivantes

- `PH-OPEN-002` : permissions, scopes, grants et révocation.
- `PH-OPEN-006` : isolation, contraintes et Cloud futur.
- `PH-OPEN-016` : ClientReference, Organization, Workspace et Team.
- `PH-OPEN-020` : environnement et mode de déploiement.
- `PH-OPEN-003` : propriétaire Decision/Risk (domaine `governance` proposé, non approuvé).
- `PH-OPEN-026` : export, rétention et sortie.

Ces décisions doivent rester coordonnées avec Product Discovery, notamment `PH-OPEN-007`, `PH-OPEN-001` et `PH-OPEN-024`, sans figer un MVP non validé.

**Prochaine action recommandée :** désigner le décideur architecture et le responsable des permissions, approuver le protocole POC, puis préparer `ADR-0004` et `ADR-0005` pour leur première revue. Aucun commit de code métier E0 ne doit présumer que leurs règles sont déjà décidées.

### Références de gouvernance

- [Index documentaire](../README.md)
- [Politique de publication](../PUBLICATION-POLICY.md)
- [Guide de collaboration](../COLLABORATION-BEST-PRACTICES.md)
- [PostgreSQL - Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- [Django - Security](https://docs.djangoproject.com/en/stable/topics/security/)
