---
id: PH-DOM-BOUND-001
title: "ProjectHub - Frontières des domaines et contrats (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Domain Architecture - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/04-domain/00-ubiquitous-language.md"
  - "docs/04-domain/01-domain-model.md"
  - "docs/03-requirements/00-functional-requirements.md"
  - "docs/03-requirements/02-business-rules-and-permissions.md"
---

# ProjectHub - Frontières des domaines et contrats inter-domaines

> **Édition publique expurgée - draft.** Cette cartographie est une proposition de conception DDD pour un monolithe modulaire, pas un ensemble de services existants ni des API déployées. Les 32 contrats `PH-BC-001..032` sont candidats. Leur direction indique une relation de collaboration ou de lecture, pas nécessairement une dépendance d'import de code.

## 1. Règles de séparation

- **Un propriétaire canonique par donnée métier.** Les autres domaines utilisent un contrat, une référence ou une projection.
- **Autorisation à chaque frontière.** Aucun service métier ne s'affranchit du tenant, des grants ou du mandat.
- **Vues et reporting sans pouvoir.** Une vue ne crée pas de données canoniques et n'étend jamais les droits.
- **Référence externe sans appropriation.** Git, documents et outils spécialisés restent maîtres de leurs contenus et permissions.
- **Consistance explicite.** Une opération doit définir ce qui est transactionnel et ce qui peut être réconcilié après coup.
- **Monolithe modulaire au départ.** Les modules sont des bounded contexts candidats, non une consigne de microservices.
- **L'implémentation suit le besoin.** Les 13 domaines restent cibles, les tranches MVP n'en utilisent qu'un sous-ensemble.

## 2. Profils des 13 domaines

| Domaine | Propriété canonique candidate | Interfaces autorisées en principe | Éviter |
|---|---|---|---|
| `core` | Contrats techniques, conventions, audit transverse et export | Vérification de contexte, orchestration bornée | Devenir un fourre-tout de modèles métier |
| `identity` | User, Membership, Team, Role/Grant, ServicePrincipal | Réponse sur identité et permissions effectives | Décider seul du résultat métier |
| `organizations` | Organization, Workspace, ClientReference éventuel | Identifier contexte, parentage et scope | Assimiler client à tenant |
| `portfolios` | Portfolio, Program, thème | Référencer les Projects autorisés | Répliquer Projects ou étendre l'accès |
| `projects` | Project, objectifs, Deliverable | Fournir Project accessible et ses changements | Gérer code Git ou workflow technique |
| `workitems` | WorkItem, assignation, transitions et blocages | Lire parent Project et grants, publier événements | Détenir une décision d'approbation |
| `planning` | Milestone, release candidate, phases | Calendriers et projections | Déclencher un déploiement non autorisé |
| `views` | SavedView, filtres et projections | Lectures filtrées par tenant et grant | Modifier les données métiers |
| `collaboration` | DocumentReference, ActivityEvent, Handover | Attacher contexte à cibles autorisées | Transformer référence en transfert de droits |
| `governance` | Decision, Risk et approbations (à trancher) | Publier résultats autorisés, lier actions | Confondre administrateur avec décideur |
| `integrations` | ExternalResource, adaptateurs, configuration | Contrats de lien, import et callbacks vérifiés | Copier des secrets ou supprimer le système maître |
| `automation` | AutomationRule et déclenchements futurs | Demande de commande limitée, ServicePrincipal | Agir avec privilèges implicites |
| `reporting` | MetricDefinition et snapshots bornés | Projections traçables pour views | Produire un super-tenant de reporting |

La propriété des `Decision` et `Risk`, historiquement évoqués dans plusieurs domaines, demeure une **option proposée en faveur de governance** plutôt qu'une décision approuvée (`PH-OPEN-003`).

## 3. Types de contrat

| Type | Interprétation candidate |
|---|---|
| `REF` | Référence stable validée, sans transfert de propriété |
| `READ` | Lecture contrôlée, filtrée et sans autorité de mutation |
| `CMD` | Demande d'action au domaine propriétaire, soumise à vérification |
| `EVT` | Événement publié après mutation réussie, sans grant automatique |
| `PROJ` | Projection ou calcul, dérivé de sources autorisées |
| `ORCH` | Orchestration transverse explicite d'une opération bornée |

Une flèche source/destination n'autorise pas un import Python circulaire ni une requête SQL directe sur une table appartenant à un autre domaine.

## 4. Catalogue des 32 contrats candidats

| ID | Domaine émetteur / demandeur | Domaine concerné | Type | Responsabilité proposée |
|---|---|---|---|---|
| `PH-BC-001` | organizations | identity | REF | Résoudre Organization et Workspace dans leur scope |
| `PH-BC-002` | identity | core | READ | Répondre sur grant actif et révocation |
| `PH-BC-003` | organizations | projects | REF | Rattacher un Project à Workspace valide |
| `PH-BC-004` | identity | projects | READ | Vérifier création et changement de responsable |
| `PH-BC-005` | projects | workitems | READ | Valider parent et scope d'un WorkItem |
| `PH-BC-006` | identity | workitems | READ | Vérifier acteur, assignee et membership |
| `PH-BC-007` | projects | collaboration | REF | Attacher une référence ou passation à Project |
| `PH-BC-008` | identity | collaboration | READ | Vérifier auteur, destinataire et visibilité |
| `PH-BC-009` | projects | views | READ | Projet visible uniquement selon grant |
| `PH-BC-010` | workitems | views | READ | Liste d'actions paginée et filtrée |
| `PH-BC-011` | collaboration | views | READ | Historique et références bornés |
| `PH-BC-012` | core | domaines métier | ORCH | Export autorisé tenant-scoped, provenance et trace |
| `PH-BC-013` | identity | integrations | READ | Rejeter lien/connecteur d'un compte révoqué |
| `PH-BC-014` | organizations | core | EVT | Annoncer création/archivage sans octroyer des droits |
| `PH-BC-015` | identity | core | EVT | Notifier révocation et réévaluation des sessions/caches |
| `PH-BC-016` | projects | collaboration | EVT | Historiser un changement de ProjectLead |
| `PH-BC-017` | workitems | collaboration | EVT | Historiser affectation et statut autorisés |
| `PH-BC-018` | collaboration | projects | EVT | Signaler passation sans changement de grants |
| `PH-BC-019` | organizations | identity | EVT | Initialiser owner via processus contrôlé |
| `PH-BC-020` | governance | workitems | REF | Lier une action à une décision, sans réécrire son état |
| `PH-BC-021` | governance | collaboration | EVT | Publier résultat d'approbation selon visibilité |
| `PH-BC-022` | planning | views | READ | Jalons accessibles dans la vue adéquate |
| `PH-BC-023` | portfolios | projects | READ | Projets accessibles du même tenant |
| `PH-BC-024` | projects | portfolios | REF | Associer un Project validé à un portefeuille |
| `PH-BC-025` | integrations | projects | REF | Lier une référence externe, sans grant tiers |
| `PH-BC-026` | integrations | collaboration | EVT | Historiser un état d'intégration sans secret |
| `PH-BC-027` | workitems | reporting | PROJ | Calculer statuts/actions sans élargir les droits |
| `PH-BC-028` | governance | reporting | PROJ | Agréger décisions et risques selon le scope |
| `PH-BC-029` | automation | projects | CMD | Demander une mutation autorisée avec identité technique |
| `PH-BC-030` | automation | workitems | CMD | Transition autorisée et idempotente |
| `PH-BC-031` | automation | governance | CMD | Refuser approbation sans autorité humaine prévue |
| `PH-BC-032` | reporting | views | READ | Afficher métriques selon les grants de la vue |

Les formulations restent des **résumés publics des contrats source**, non des signatures d'API ou des interfaces déjà développées.

## 5. Contrat minimal proposé

Un contrat inter-domaines devrait expliciter :
- `contract_id`, version et domaine propriétaire ;
- sujet agissant, tenant vérifié et scope cible ;
- commande, lecture, référence ou événement ;
- préconditions, erreurs de refus et invariants ;
- classification, minimisation et provenance des données échangées ;
- idempotence et politique de retry si asynchrone ;
- observabilité et tests positifs/négatifs ;
- compatibilité et stratégie de dépréciation.

```text
Commande demandée
  -> validation du contexte et du grant
  -> appel au propriétaire de l'agrégat
  -> vérification des invariants
  -> commit transactionnel
  -> événement minimal après succès si requis
  -> projections bornées, sans pouvoir de mutation
```

## 6. Dépendances autorisées ou interdites

| Situation | Approche retenue comme candidate |
|---|---|
| `workitems` a besoin de vérifier Project | Port de lecture contrôlé dans `projects`, pas écriture directe de ses tables |
| `collaboration` veut montrer un changement de responsable | Consommer un événement autorisé et minimal |
| `views` veut afficher plusieurs domaines | Projections filtrées ; ne jamais désactiver l'autorisation pour simplifier |
| `reporting` veut consolider | Conserver le scope et la fraîcheur ; aucun accès cross-tenant |
| `governance` souhaite déclencher un WorkItem | Commande auprès du domaine propriétaire, pas mutation cachée |
| `integrations` reçoit un webhook | Authentifier, dédupliquer, vérifier lien et tenant avant action |
| `automation` suggère une approbation | Permission d'agent insuffisante sans mandat humain explicite |
| Projet transféré vers une autre Organization | Processus de migration, pas remplacement direct d'une FK |

**Interdictions candidates :** imports circulaires entre domaines, contournement d'ACL, triggers transverses non tracés, gestion des secrets dans `collaboration`, décision métier cachée dans `views`, accès inter-tenant par une vue de portefeuille ou une relation client.

## 7. Scénarios de tests de frontière

1. **Tenant absent** : commande refusée sans contexte prouvé.
2. **Parent étranger** : WorkItem ne peut appartenir à un Project d'une autre Organization.
3. **Accès révoqué** : cache, job et intégration ne conservent pas un privilège ancien.
4. **Team sans grant** : aucun accès implicite à un Workspace privé.
5. **Responsable sans mandat** : la modification d'un statut ne valide pas un résultat métier.
6. **Passation sans exercice** : `handover.prepared` ne déclenche pas `validated` automatiquement.
7. **Lien externe** : n'ajoute aucun droit GitHub ou document tiers.
8. **Rapport et recherche** : aucun élément de B dans une session A.
9. **Export** : autorisation sur chaque source, fichier protégé après génération.
10. **Agent IA** : demande de mutation réévaluée côté propriétaire avec refus en cas de mandat manquant.

Le modèle source décrit **40 scénarios de tests candidats de frontières**, pas 40 tests exécutés. Ces exemples couvrent les risques dominants sans prétendre reproduire les détails opérationnels privés.

## 8. Préparation de l'Architecture & Engineering Baseline

Avant d'implémenter ces contrats, produire des ADR sur :
- périmètre exact de `identity` et politique RBAC ;
- séparation `governance` / `workitems` ;
- données multi-tenant, indexes, exports et jobs ;
- modes d'événements, cohérence différée, transaction et outbox éventuelle ;
- stratégie d'intégration initiale ;
- migration, stockage et portabilité des données ;
- tests de sécurité et exploitation des données pilotes.

**Aucun de ces choix n'est approuvé uniquement parce que cette cartographie existe.**

Voir [modèle](01-domain-model.md), [glossaire](00-ubiquitous-language.md), [règles métier](../03-requirements/02-business-rules-and-permissions.md) et [traçabilité](../03-requirements/03-requirements-traceability.md).
