---
id: PH-REQ-BRP-001
title: "ProjectHub - Règles métier et permissions candidates (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Security / Domain - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/03-requirements/00-functional-requirements.md"
  - "docs/03-requirements/01-non-functional-requirements.md"
  - "docs/04-domain/01-domain-model.md"
---

# ProjectHub - Règles métier, rôles et permissions

> **Édition publique générique - draft.** Le registre de conception privé comprend 111 règles candidates `PH-BR-001..111` et 35 scénarios d'accès `PH-SEC-T01..T35`. Cette édition présente leurs frontières et les tests clés, sans publier les responsabilités institutionnelles nominatives ni une politique RBAC prétendument approuvée.

## 1. Les trois dimensions de l'autorisation

**Rôle applicatif** : ensemble de capacités dans un contexte donné.  
**Grant / Membership** : droit ou appartenance explicite, avec portée, état et éventuelle date de fin.  
**Mandat métier** : légitimité à accepter un livrable ou prendre une décision dans une organisation.

Ces dimensions ne sont pas interchangeables : `OrgAdmin` n'est pas automatiquement `DecisionAuthority`, `ProjectLead` n'accorde aucun droit sur un système tiers, et une Team ne confère pas automatiquement accès à tous les Workspaces.

## 2. Périmètres et hiérarchie candidate

```text
User / ServicePrincipal
  -> Membership ou Grant actif dans une Organization
      -> Workspace autorisé
          -> Project autorisé
              -> WorkItem, Decision, Reference, Handover...
```

`Organization` est la frontière d'isolation du tenant candidat ; `Workspace` est une subdivision collaborative ; `Team` est un collectif et `ClientReference` représente une relation métier sans droits automatiques.

Une personne peut appartenir à deux Organizations **sans partage de données par défaut**. L'héritage de rôles et le nombre exact de niveaux restent à décider (`PH-OPEN-002`).

## 3. Catalogue des 111 règles par famille

| Domaine des règles | Plage | Nombre | Objet |
|---|---|---:|---|
| Tenancy et cohérence entre ressources | `PH-BR-001..012` | 12 | Contextes, liens autorisés, caches, exports et refus |
| Identité, invitations et memberships | `PH-BR-013..023` | 11 | Invitation, activation, révocation et délégation |
| Organizations, Workspaces, Teams et portefeuilles | `PH-BR-024..038` | 15 | Scopes et associations sans droits implicites |
| Projects et responsabilités | `PH-BR-039..050` | 12 | Attribution, changements et résultats |
| WorkItems et échéances | `PH-BR-051..062` | 12 | Travail actionnable et transitions |
| Décisions, approbations et risques | `PH-BR-063..073` | 11 | Mandat, preuve et séparation des acteurs |
| Documentation et transmission | `PH-BR-074..081` | 8 | Références, continuité et reprise effective |
| Clients, collaborations et séparation institutionnelle | `PH-BR-082..087` | 6 | Relation partenaire distincte d'un tenant |
| Connecteurs, agents IA et services techniques | `PH-BR-088..099` | 12 | Identités techniques, secrets et permissions bornées |
| Historique, exports et sortie | `PH-BR-100..111` | 12 | Traces, audit, réversibilité et droits |

Les intitulés restent des thèmes de source ; leur présence n'implique pas une implémentation du domaine complet au MVP.

## 4. Règles structurantes retenues comme candidats

| ID | Règle publique reformulée | Exemple de test |
|---|---|---|
| `PH-BR-001` | Toute opération possède un tenant vérifié | API refuse une requête sans contexte autorisé |
| `PH-BR-002` | Aucun enfant lié au mauvais tenant | Rejeter WorkItem dont Project appartient à B |
| `PH-BR-003` | Un Workspace dépend d'une Organization unique | Parent obligatoire et cohérent |
| `PH-BR-004` | Un Project a un Workspace unique | Rejeter parentage contradictoire |
| `PH-BR-005` | Visibilité déduite des autorisations effectives | Requête par ID et liste filtrées |
| `PH-BR-006` | Export borné au tenant | Export A sans objet de B |
| `PH-BR-007` | Tâches asynchrones bornées | Job garde un contexte contrôlé lors de l'exécution |
| `PH-BR-008` | Recherche et caches isolés | A ne lit pas une projection de B |
| `PH-BR-009` | Le nom d'un client n'accorde pas d'accès | Référence client sans membership |
| `PH-BR-010` | Contexte visible et vérifié | Bascule explicite sans privilège caché |
| `PH-BR-011` | Changement d'Organization sans fuite | Navigation A -> B -> A contrôlée |
| `PH-BR-012` | Refus sans divulguer l'existence | Erreur neutre pour une ressource étrangère |
| `PH-BR-013` | Un User peut appartenir à plusieurs Organizations | Membership indépendant par tenant |
| `PH-BR-014` | Invitations portées et expirantes | Invitation sans capacité supérieure |
| `PH-BR-015` | Invitation ne signifie pas accès activé | Rejet avant validation requise |
| `PH-BR-017` | Protéger le dernier OrgOwner | Refuser sa révocation sans procédure sûre |
| `PH-BR-023` | Un Membership inactif annule les délégations | Ancien grant inutilisable |
| `PH-BR-024` | Aucun accès implicite à des Workspaces privés | Membre d'une Team sans grant refusé |
| `PH-BR-027` | Voir la structure administrative n'est pas voir tout le contenu | Séparer métadonnées et objets privés |
| `PH-BR-032` | Transfert inter-tenant impossible par simple édition | Migration dédiée et autorisée |
| `PH-BR-033` | Référence client distincte d'un tenant | Aucun octroi implicite |
| `PH-BR-035` | Team ne donne pas de permissions par défaut | Test d'appartenance sans grant |
| `PH-BR-085` | Un rôle dans l'Organization A ne donne pas accès à B | Accès cross-tenant refusé |
| `PH-BR-102` | Les rectifications restent historisées | Nouvelle valeur et provenance conservées |
| `PH-BR-103` | Les journaux ne contiennent pas de secrets | Vérification des événements sensibles |
| `PH-BR-104` | Un export respecte les droits | Exclure champs et objets non autorisés |
| `PH-BR-105` | Un fichier d'export reste protégé | Accès sans droit refusé même après génération |
| `PH-BR-106` | La sortie de pilote doit être préparée | Export, rétention, révocation, confirmation |
| `PH-BR-111` | Exporter n'est pas céder la propriété de données | Préserver les obligations des systèmes maîtres |

Le libellé de `PH-BR-085` est **volontairement généralisé** : seul l'invariant inter-tenant est public.

## 5. Modèle d'évaluation de permission proposé

```text
Authorize(subject, action, resource, request_context):
  identifier le sujet authentifié
  dériver le tenant vérifié côté serveur
  valider Membership / Grant actif et sa portée
  valider le tenant et le parentage de la ressource
  contrôler permission applicative + mandat métier si nécessaire
  appliquer la politique de refus par défaut
  journaliser les actes sensibles sans exposer de secrets
```

Ceci est un **algorithme conceptuel** et non du code prêt à déployer. Les politiques d'héritage et les ressources sensibles exigent des ADR et des tests.

## 6. Matrice simplifiée de droits à arbitrer

| Opération | Membre autorisé | ProjectLead | WorkspaceAdmin | OrgAdmin | DecisionAuthority |
|---|---|---|---|---|---|
| Lire un Project de son périmètre | Selon grant | Selon grant | Selon politique | Selon politique | Selon grant |
| Modifier une action assignée | Selon grant | Selon grant | Selon politique | Selon politique | Selon grant |
| Inviter un membre | Non par défaut | Non par défaut | À décider | Selon mandat admin | Non par défaut |
| Révoquer un membership | Non | Non | Selon scope à arbitrer | Selon politique | Non par défaut |
| Approuver une décision | **Non par défaut** | Non par défaut | Non par défaut | Non automatique | Avec mandat ciblé |
| Exporter des données | Selon droit explicite | Selon droit explicite | Selon politique | Selon politique | Selon droit explicite |
| Lire un autre tenant | **Non** | **Non** | **Non** | **Non** | **Non**, sauf règle explicite et testée |

Les cellules indiquent une **orientation de contrôle**, pas une matrice RBAC définitivement validée.

## 7. Tests d'accès obligatoires avant E1

Le corpus source comprend 35 scénarios `PH-SEC-T01..T35`. Les catégories prioritaires sont :
- accès direct à une ressource étrangère et objets imbriqués ;
- appartenance multiple avec contexte actif erroné ;
- invitation en attente, accès révoqué ou session ancienne ;
- élévation de privilèges par modification d'ID ou de rôle ;
- recherche et export inter-tenant ;
- absence de mandat pour approbation ;
- délégation à soi-même non autorisée ;
- fuite dans activités, métriques, logs et tâches asynchrones ;
- agent/service technique actif sans grant valable.

**Aucun scénario n'est déclaré exécuté ou réussi.** Le futur registre de preuve doit enregistrer données fictives, version, acteur et résultat observé.

## 8. Questions ouvertes et décision

- `PH-OPEN-002` : catalogue de rôles, héritage, portée et projets privés.
- `PH-OPEN-003` : propriété canonique Decision/Risk.
- `PH-OPEN-006` : stratégie d'isolation multi-tenant.
- `PH-OPEN-016` : Client / Organization / Workspace / Team.
- `PH-OPEN-021` : contrôles avant pilotes réels.
- `PH-OPEN-026` : conservation, export et suppression.

Les rôles administratifs du produit ne remplacent **jamais une habilitation institutionnelle**. Voir [NFR](01-non-functional-requirements.md), [modèle de domaine](../04-domain/01-domain-model.md), [questions ouvertes](../00-context/04-open-questions.md).
