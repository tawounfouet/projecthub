---
id: PH-DISC-WEB-001
title: "ProjectHub - Besoins génériques d'un portefeuille technique multi-projets"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources:
  - PH-OPS-002
  - PH-OPS-003
  - PH-CNV-004
related_documents:
  - "docs/02-discovery/03-cross-organization-needs.md"
  - "docs/02-discovery/04-current-vs-target-workflows.md"
publication_note: "Edition de recherche generique, sans inventaire interne ni information client"
---

# Besoins candidats d'une équipe technique multi-projets

> **Édition publique abstraite.** Le nom du fichier reste celui annoncé dans le plan initial de publication. Le texte ne constitue **ni un inventaire de l'activité réelle de l'organisation évoquée dans ce nom, ni une validation de ses besoins**, et ne reproduit aucun document interne, nom de client, dépôt, package, incident ou information d'infrastructure.

## 1. Problème métier à tester

Une équipe de réalisation numérique peut gérer simultanément :
- des projets et prestations pour différents clients ;
- des produits ou outils internes ;
- des composants ou bibliothèques réutilisables ;
- des intégrations avec des systèmes externes ;
- des opérations récurrentes et de la maintenance ;
- des expérimentations et de la recherche.

**Hypothèse :** il manque parfois une couche commune pour retrouver les objectifs, responsables, décisions, échéances, dépendances et modalités de reprise entre ces activités. Mais des outils spécialisés peuvent déjà couvrir une grande partie des besoins ; il faudra vérifier ce qui justifie réellement un outil supplémentaire.

Le **dossier informatique** n'est pas un Project, le **dépôt Git** n'est pas une organisation et le **Client** n'est pas nécessairement un tenant ProjectHub.

## 2. Catégories de portefeuille à ne pas confondre

| Catégorie conceptuelle | Exemples fictifs | Responsabilité de ProjectHub candidate | Source de vérité externe possible |
|---|---|---|---|
| Projets clients | Refonte d'un portail fictif | Objectifs, responsables, livrables, échéances | Outil de contractualisation ou dépôt Git |
| Produit interne | Portail d'équipe fictif | Roadmap et avancement | Gestion du code et documentation produit |
| Composants partagés | Bibliothèque utilitaire fictive | Référence, responsable, dépendances | Registry de packages, dépôt source |
| Intégrations | Connexion API de démonstration | Contexte et statut métier | Système d'intégration |
| Jobs / traitements | Traitement quotidien synthétique | Responsabilité et suivi des engagements | Ordonnanceur ou moteur de workflow |
| Infrastructure | Environnement de test fictif | Référence et risque lié à un projet | Plateforme d'hébergement/observabilité |
| Recherche | Prototype sans données réelles | Hypothèse, apprentissage, décision Go/No-Go | Dépôt expérimental et carnet de recherche |

Ce tableau est une **typologie générique**, pas le contenu du système d'information d'une agence.

## 3. Personas candidats

| Acteur | Travail à accomplir | Contrôle à préserver |
|---|---|---|
| Responsable de portefeuille | Avoir une vision fiable des engagements | Séparer clients et droits d'accès |
| Chef de projet / lead technique | Connecter travail, ressources et livraison | Ne pas dupliquer l'outil technique maître |
| Contributeur | Connaître la prochaine action et son périmètre | Accès limité au projet autorisé |
| Responsable de maintenance | Comprendre versions et dépendances utiles | Documentation de reprise et historique |
| Responsable d'exploitation | Qualifier un risque et ses conséquences | Ne pas exposer les informations sensibles |
| Repreneur d'un projet | Réaliser une action sans dépendance permanente | Vérification de la capacité de reprise |
| Référent métier / client | Comprendre ce qui est livré ou accepté | Ne pas confondre lecture et approbation |

Un client, une entreprise utilisatrice et un membre de l'équipe d'un prestataire doivent rester trois concepts indépendants.

## 4. Familles de besoins de pilotage transversal

| Famille | Besoin générique candidat | Parcours synthétique de preuve | Horizon |
|---|---|---|---|
| `PH-XNEED-002` | Inventaire cohérent de projets | Distinguer projet, archive et ressource associée | MVP |
| `PH-XNEED-003` | Responsable et relais de maintenance | Retrouver qui peut reprendre et sous quelles conditions | MVP |
| `PH-XNEED-004` | Résultats et livrables acceptés | Séparer travail réalisé, livré et validé | MVP / P1 |
| `PH-XNEED-005` | Actions, priorités, échéances | Retrouver le travail bloquant un livrable | MVP |
| `PH-XNEED-006` | Préparation des revues de portefeuille | Identifier arbitrages et blocages | MVP |
| `PH-XNEED-007` | Historique et provenance | Expliquer un changement de propriétaire ou de statut | MVP |
| `PH-XNEED-008` | Liens vers documentation existante | Référencer la documentation source sans la recopier | MVP |
| `PH-XNEED-009` | Visibilité filtrée, métriques fiables | Filtrer par projet et date de fraîcheur | MVP |
| `PH-XNEED-010` | Portabilité | Export d'un périmètre autorisé sans fuite | Gate |
| `PH-XNEED-016` | Passation et reprise | Une nouvelle personne poursuit la maintenance | MVP |
| `PH-XNEED-018` | Qualité des statuts | Distinguer constat historique et état vérifié | MVP / P1 |
| `PH-XNEED-029` | Séparation Client / tenant | Une relation client n'ouvre aucun accès croisé implicite | Gate / P1 |

La liste se concentre sur le **socle candidat**, non sur une promesse d'importer l'intégralité d'un portefeuille réel.

## 5. Familles techniques spécialisées à différer

| Famille | Capacité envisagée | Limite nécessaire | Horizon |
|---|---|---|---|
| `PH-XNEED-012` | Référencer un dépôt Git | Pas de synchronisation complète automatique au départ | P1/P2 |
| `PH-XNEED-014` | Releases et versionnement | Les builds restent dans CI/CD | P1/P2 |
| `PH-XNEED-017` | Dépendances entre activités | Liens explicites avant graphe automatisé | P1/P2 |
| `PH-XNEED-023` | Références d'environnements | Pas de secrets ni d'administration native d'infra | P2 |
| `PH-XNEED-024` | Correctifs et risques | Suivi du travail sans remplacer les outils de réponse incident | P1/P2 |
| `PH-XNEED-025` | Catalogue de packages | Usage et propriétaires à valider avant indexation | P2 |
| `PH-XNEED-026` | Jobs, connexions et traitements | Références descriptives, pas orchestration généralisée | P2 |
| `PH-XNEED-027` | Expérimentations de R&D | Hypothèses, apprentissages et décisions | P1/P2 |
| `PH-XNEED-028` | Import d'inventaire | Prévisualisation, dédoublonnage et confirmation | P1 |
| `PH-XNEED-022` | Agents IA | Droits minimaux et approbation humaine | P2 |

**Principes** : aucune dépendance automatique à des composants internes tiers, aucun stockage de tokens et aucun couplage forcé à un hébergeur ou fournisseur d'IA.

## 6. As-Is à observer, pas à présumer

Dans un environnement technique générique, un état actuel possible est :

```text
Un besoin métier est identifié
  -> un Project est suivi dans un ou plusieurs outils
  -> des dépôts, livraisons et environnements ont leurs propres états
  -> les responsables maintiennent notes et tâches
  -> une revue nécessite de réunir plusieurs sources
  -> une reprise peut exiger une transmission orale
```

**Inconnues importantes :** que fournissent déjà les outils utilisés ? Quelles mises à jour sont doublement saisies ? Quel coût a réellement une revue ? Quelle quantité de données est nécessaire pour prendre une décision ?

Un inventaire technique historique n'est **pas** une photographie à jour. Les risques constatés dans un document ancien doivent être réévalués par les responsables, hors communication publique.

## 7. To-Be candidat de ProjectHub

```text
Qualifier un Project et son résultat attendu
  -> désigner responsable et relais
  -> lier les WorkItems et références externes utiles
  -> tracer les blocages et changements significatifs
  -> distinguer version technique et acceptation métier
  -> préparer la revue
  -> transmettre le contexte et tester la reprise
  -> exporter les données autorisées
```

**Source de vérité :** Git héberge le code et la revue de code ; CI/CD gère les builds et déploiements ; le service de facturation traite les transactions ; la documentation technique autorisée reste dans son système. ProjectHub en organise le **contexte de pilotage**.

## 8. Scénarios de validation synthétiques

### A. Réviser l'état de trois projets fictifs

Un lead ouvre un Workspace de démonstration, filtre trois projets et identifie les dépendances bloquantes.

**Preuve demandée :** précision des statuts, absence de duplication et temps réel nécessaire pour préparer la revue.

### B. Reprendre une maintenance

Une personne chargée de la relève reçoit l'objectif, les références, les actions ouvertes, les dépendances et le journal. Elle réalise une action de démonstration.

**Preuve demandée :** autonomie du repreneur, documents accessibles et aucun transfert de secrets par ProjectHub.

### C. Séparer un client d'une Organization

Un utilisateur autorisé décrit un Client dans une Organization, mais ne peut pas accéder aux données d'une autre Organization en modifiant un identifiant dans l'API.

**Preuve demandée :** tests d'autorisation négatifs, y compris recherche, export et API.

### D. Préparer une livraison sans remplacer la CI/CD

Une équipe rattache une release fictive à un Project et pointe vers la preuve de déploiement dans un système externe.

**Preuve demandée :** pas de copie du code, statut de livraison distinct du statut d'acceptation métier.

## 9. Exigences de qualité non négociables avant un pilote réel

- Contrôle serveur et isolation des Organizations, y compris comptes multi-appartenances.
- Identités techniques et permissions limitées ; journalisation et révocation.
- Sauvegarde et restauration démontrées, pas seulement une sauvegarde configurée.
- Gestion des incidents, confidentialité, export, suppression et sortie documentés.
- Tests de parcours inclusifs et compréhension des erreurs.
- Cadre contractuel et autorisation de données réelles.
- Validation explicite des responsabilités d'exploitation.

**Aucun de ces contrôles n'est déclaré réussi dans cette édition.**

## 10. Questions à valider

- L'inventaire des projets suffit-il à répondre au problème sans un nouveau catalogue technique ?
- Où se trouvent les statuts et références de confiance ?
- Quels acteurs ont réellement besoin d'une vue portefeuille ?
- Quels liens externes évitent de la saisie plutôt que d'en ajouter ?
- Le scénario de reprise est-il utilisable par une autre personne ?
- Quelles données peuvent servir à un pilote, et avec quelle approbation ?
- Une organisation paierait-elle pour un Cloud managé, et pourquoi ?

Les réponses nécessitent des entretiens et des mesures. La valeur du **cas générique** ne constitue pas une validation par une agence particulière.

**Liens :** [personas](00-stakeholders-and-personas.md), [besoins communs](03-cross-organization-needs.md), [workflows](04-current-vs-target-workflows.md), [scope](../01-product/02-product-scope.md).
