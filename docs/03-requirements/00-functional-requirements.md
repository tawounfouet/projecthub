---
id: PH-REQ-FUNC-001
title: "ProjectHub - Exigences fonctionnelles candidates (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Requirements Engineering - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/01-product/02-product-scope.md"
  - "docs/02-discovery/03-cross-organization-needs.md"
  - "docs/03-requirements/01-non-functional-requirements.md"
  - "docs/03-requirements/03-requirements-traceability.md"
---

# ProjectHub - Exigences fonctionnelles

> **Édition publique expurgée, draft.** Le registre privé recense 130 exigences fonctionnelles candidates `PH-REQ-001..130`. Cette édition présente leur organisation, leurs exigences structurantes et les critères d'acceptation génériques, sans diffuser les correspondances opérationnelles privées. Le catalogue n'est ni approuvé ni implémenté.

## 1. Rôle de ce document

Une exigence fonctionnelle exprime **ce que le produit doit permettre ou empêcher**, avec un acteur, un périmètre, une condition et une preuve à définir. La présence d'une exigence ne signifie pas qu'elle a été validée avec des utilisateurs, développée ou testée.

Le cadre de ProjectHub est une plateforme de pilotage de travail et de projets, non un remplaçant des outils de code, des GED ou de l'infrastructure.

## 2. Classification et chiffres du registre source

| Niveau candidat | Nombre | Interprétation |
|---|---:|---|
| `P0-G` | 16 | Conditions fonctionnelles de sécurité ou d'accès pour un pilote réel |
| `P0-C` | 29 | Capacités candidates du coeur MVP |
| `P1` | 50 | Évolutions après validation du parcours principal |
| `P2` | 35 | Extensions à différer |
| **Total** | **130** | **13 domaines cibles** |

**Attention :** `P0-G` n'autorise pas en lui-même un pilote réel. Les NFR, accords et procédures d'exploitation sont des conditions supplémentaires.

## 3. Catalogue de référence par domaine

Les plages conservent les IDs du registre privé. Les descriptions ci-dessous sont des **résumés publics de domaines**, pas la reproduction littérale des fiches détaillées.

| Domaine propriétaire candidat | IDs | Nombre | Responsabilités fonctionnelles |
|---|---|---:|---|
| `core` | `PH-REQ-001..009` | 9 | Contexte d'accès, audit, export, provenance et corrections |
| `identity` | `PH-REQ-010..019` | 10 | Invitations, memberships, révocation, rôles et identités techniques |
| `organizations` | `PH-REQ-020..031` | 12 | Organizations, Workspaces, contextes et références clients distinctes |
| `portfolios` | `PH-REQ-032..037` | 6 | Regroupements, thèmes, indicateurs et dépendances interprojets |
| `projects` | `PH-REQ-038..049` | 12 | Fiches Project, objectifs, responsables, relais et livrables |
| `workitems` | `PH-REQ-050..063` | 14 | Actions, priorités, statuts, échéances, blocages et dépendances |
| `planning` | `PH-REQ-064..071` | 8 | Échéances, jalons, releases et itérations |
| `views` | `PH-REQ-072..079` | 8 | Table, Board et navigation filtrée selon les permissions |
| `collaboration` | `PH-REQ-080..091` | 12 | Références documentaires, activité et passation |
| `governance` | `PH-REQ-092..103` | 12 | États vérifiés, décisions, approbations et risques |
| `integrations` | `PH-REQ-104..116` | 13 | Ressources et dépôts externes, import et synchronisation différée |
| `automation` | `PH-REQ-117..122` | 6 | Déclenchements et agents, avec droits et validation humaine |
| `reporting` | `PH-REQ-123..130` | 8 | Synthèses traçables et indicateurs explicables |

Ces frontières fonctionnelles ne sont ni des microservices obligatoires ni des modules à livrer tous au MVP.

## 4. Exigences structurantes à tester

| ID | Exigence candidate publique | Priorité source | Scénario d'acceptation envisagé |
|---|---|---|---|
| `PH-REQ-001` | Toute opération métier porte un contexte Organization autorisé | P0-G | Rejeter une opération sans contexte autorisé |
| `PH-REQ-003` | Vérifier les autorisations dans l'API, les listes, recherches et exports | P0-G | Refuser une lecture directe d'objet d'un autre tenant |
| `PH-REQ-004` | Exporter les données autorisées dans un format documenté | P0-G | Export A sans donnée de B |
| `PH-REQ-010` | Inviter un membre dans un périmètre explicite | P0-G | L'invitation n'ouvre aucun accès non accepté |
| `PH-REQ-011` | Révoquer effectivement un membre | P0-G | Rejeter les actions et sessions révoquées |
| `PH-REQ-012` | Autoriser plusieurs memberships sans partage de droits | P0-G | Changer de tenant sans voir ses données voisines |
| `PH-REQ-013` | Borner un rôle à son scope d'attribution | P0-G | Refuser une action hors périmètre |
| `PH-REQ-020` | Créer une Organization comme conteneur de données | P0-G | Identifier le tenant sans ambiguïté |
| `PH-REQ-021` | Rattacher Workspace à une Organization unique | P0-G | Rejeter un rattachement non autorisé |
| `PH-REQ-022` | Isoler les Workspaces entre Organizations | P0-G | Interdire consultation ou modification inter-tenant |
| `PH-REQ-025` | Afficher Organization et Workspace actifs | P0-C | Montrer clairement le contexte de modification |
| `PH-REQ-026` | Distinguer Client et Organization | P0-G | Référencer un client sans créer un accès |
| `PH-REQ-038` | Créer une fiche Project contextualisée | P0-C | Projet visible uniquement dans le bon Workspace |
| `PH-REQ-040` | Désigner un ProjectLead autorisé | P0-C | Conserver l'ancien responsable dans l'historique |
| `PH-REQ-041` | Désigner un relais de reprise | P0-C | Relais distinct, sans permission automatique |
| `PH-REQ-042` | Dater et qualifier l'état déclaré du projet | P0-C | Statut ancien identifié comme tel |
| `PH-REQ-050` | Créer un WorkItem rattaché à un Project | P0-C | Auteur et parentage traçables |
| `PH-REQ-051` | Affecter ou laisser une action non attribuée | P0-C | Assignee autorisé et état non attribué explicite |
| `PH-REQ-055` | Enregistrer blocage, responsable et prochaine action | P0-C | Blocage visible en revue, résolution historisée |
| `PH-REQ-072` | Afficher une Table des projets accessibles | P0-C | Pas de projet étranger dans la vue |
| `PH-REQ-080` | Associer une référence documentaire externe à un Project | P0-C | Aucune permission tiers conférée |
| `PH-REQ-082` | Préparer un dossier minimal de reprise | P0-C | Contexte, références, actions et lacunes accessibles au bon rôle |
| `PH-REQ-083` | Distinguer transfert proposé, revu et confirmé | P0-C | Checklist non confondue avec une reprise effective |
| `PH-REQ-094` | Refuser une approbation sans mandat | P0-G | Le contributeur ne peut approuver une décision |
| `PH-REQ-104` | Référencer un dépôt GitHub | P1 | Lien externe sans synchronisation ni droit présumé |
| `PH-REQ-123` | Produire une synthèse d'activités autorisées | P0-C | Périmètre, date et filtres explicites |

La sélection de cette table n'est pas le contenu exhaustif des 130 fiches. Les spécifications détaillées seront publiées progressivement après examen des droits de diffusion.

## 5. Parcours MVP transversal candidat

```text
Accéder à une Organization et un Workspace autorisés
  -> qualifier un Project, objectif, responsable et relais
  -> suivre les WorkItems, dates et blocages
  -> consulter une Table / vue adaptée et l'activité
  -> référencer les documents maîtres sans les dupliquer
  -> préparer et vérifier une transmission
  -> exporter son périmètre autorisé
```

Le scénario doit être démontré avec deux Organizations fictives et des utilisateurs aux droits différents.

## 6. Critères d'acceptation transversaux

- **Contexte** : une action sans Organization valide ou avec Workspace étranger est refusée.
- **Délégation** : le nom d'un responsable de projet ne lui attribue pas des droits d'administration.
- **Historique** : le changement de statut ou de personne ne gomme pas les informations précédentes.
- **Statut** : un état déclaré n'est pas un état vérifié, et une livraison n'est pas une acceptation métier.
- **Ressource externe** : un lien GitHub ou documentaire n'implique pas l'accès au contenu tiers.
- **Passation** : un dossier préparé ne prouve pas l'autonomie du successeur.
- **Sortie** : un export n'inclut que les données autorisées de l'Organization.
- **Accessibilité** : la réalisation du parcours ne dépend pas de la couleur ni d'un dispositif de pointage unique.

## 7. Non-objectifs et extensions

**Hors noyau MVP :** synchronisation GitHub avancée, moteur généraliste d'automatisation, agents IA autonomes, gestion complète d'infrastructure, stockage universel de documents, facturation Cloud et ensemble complet des vues Portfolio/Roadmap/Calendar.

La suppression de fonctions avancées ne doit jamais servir à reporter l'isolation, la protection des accès, la confidentialité ou la capacité de quitter un pilote réel.

## 8. Validation, versionnement et changements

Chaque exigence doit être reliée à son besoin et à un critère d'acceptation, puis documenter les résultats d'essais. Cycle proposé : `candidate -> reviewed -> approved -> implemented -> verified`, en conservant les états rejeté ou remplacé lorsqu'ils s'appliquent.

**À cette date :** IDs et priorités = inventaire de conception ; aucune preuve de développement, revue utilisateur ou validation institutionnelle n'est revendiquée.

Voir [NFR](01-non-functional-requirements.md), [règles métier](02-business-rules-and-permissions.md), [traçabilité](03-requirements-traceability.md) et [périmètre produit](../01-product/02-product-scope.md).
