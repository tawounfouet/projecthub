---
id: PH-DISC-CROSS-001
title: "ProjectHub - Besoins transversaux inter-organisations"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources:
  - PH-OPS-001
  - PH-OPS-002
  - PH-CNV-004
related_documents:
  - "docs/02-discovery/00-stakeholders-and-personas.md"
  - "docs/02-discovery/01-diversite-alternative-needs.md"
  - "docs/02-discovery/02-webtech-solutions-needs.md"
  - "docs/02-discovery/04-current-vs-target-workflows.md"
publication_note: "Synthese anonymisee et non contractuelle"
---

# Besoins transversaux inter-organisations

> **Synthèse analytique publique - draft.** Le corpus privé confronte deux contextes distincts et compte **78 besoins candidats** répartis en **29 familles normalisées**. Ces nombres reflètent un inventaire documentaire interne, non une enquête représentative ou une approbation d'organisations. Les états historiques, les personnes, les fichiers et les exigences locales détaillées ne sont pas publiés.

## 1. Pourquoi comparer deux contextes ?

L'ambition de ProjectHub est de bâtir un **socle générique** sans convertir les spécificités d'une organisation en contraintes imposées à toutes les autres.

Deux situations génériques servent de contraste :

| Contexte d'étude | Préoccupation dominante | Ce que ProjectHub pourrait partager | Ce qui doit rester spécialisé |
|---|---|---|---|
| Coordination associative | Responsabilités, décisions, contribution occasionnelle, transmission | Projects, WorkItems, historique, relais, références | Gouvernance statutaire, finances, annuaire, procédures internes |
| Portefeuille numérique | Projets et livraisons, composants, maintenance, intégrations, exploitation | Projects, WorkItems, dépendances, références, passation | Git, CI/CD, opérations, registries, outils d'incidents |

**Convergence ≠ besoins identiques.** Une correspondance entre deux besoins a été **proposée par analyse**, non démontrée auprès de représentants autorisés.

## 2. Méthode de normalisation

1. Distinguer le besoin utilisateur du nom de son outil actuel.
2. Comparer les objectifs, responsabilités, flux et preuves attendues.
3. Regrouper les besoins analogues dans une famille `PH-XNEED-XXX`.
4. Isoler les contraintes transversales de sécurité et d'accès.
5. Conserver à part les extensions propres à un secteur.
6. Ne pas créer artificiellement de « besoin commun » si la similitude est seulement technique.
7. Rattacher les familles aux workflows et aux capacités de périmètre.
8. Marquer l'état : **hypothèse**, **à tester**, **décision à obtenir**.

Les références privées fines des deux sources ne sont pas reprises dans cette version publique. Les IDs génériques restent stables pour préserver la traçabilité avec les prochains documents publics.

## 3. Catalogue des 29 familles normalisées

Les horizons désignent un **classement candidat**, non une date de livraison :
- **Gate** : condition de sécurité, d'accès ou de sortie avant un usage réel ;
- **MVP** : besoin du premier parcours de valeur à démontrer ;
- **P1** : évolution qui nécessite une preuve supplémentaire ;
- **P2** : spécialisation ou extension avancée.

| ID | Famille de besoin | Nature de la convergence | Horizon candidat |
|---|---|---|---|
| `PH-XNEED-001` | Organisations, accès, confidentialité et périmètre d'essai | Invariant commun | Gate |
| `PH-XNEED-002` | Inventaire, vocabulaire de projet et états | Problème partagé | MVP |
| `PH-XNEED-003` | Responsable principal, relais et réaffectation | Problème partagé | MVP |
| `PH-XNEED-004` | Objectifs, livrables et acceptation | Problème partagé | MVP minimal / P1 |
| `PH-XNEED-005` | Travail actionnable, priorités et échéances | Problème partagé | MVP |
| `PH-XNEED-006` | Blocages, arbitrages et points de synchronisation | Problème partagé | MVP / P1 |
| `PH-XNEED-007` | Historique, provenance et changements significatifs | Problème partagé | MVP |
| `PH-XNEED-008` | Liens documentaires et recherche contextuelle | Problème partagé | MVP liens / P1 recherche |
| `PH-XNEED-009` | Vues de coordination et indicateurs explicables | Problème partagé | MVP vue / P1 indicateurs |
| `PH-XNEED-010` | Export, portabilité et sortie | Invariant commun | Gate |
| `PH-XNEED-011` | Décisions et risques liés au travail | Problème partagé | P1 |
| `PH-XNEED-012` | Références GitHub et frontières des outils | Convergence technique partielle | P1 liens / P2 sync |
| `PH-XNEED-013` | Échéances critiques et maintenance périodique | Convergence par usage | P1 |
| `PH-XNEED-014` | Versions, recette et releases techniques | Spécialisation technique | P1 / P2 |
| `PH-XNEED-015` | Onboarding et première contribution | Problème partagé | P1 |
| `PH-XNEED-016` | Dossier de transmission et autonomie du repreneur | Problème partagé | MVP |
| `PH-XNEED-017` | Dépendances et impacts entre activités | Analogie à tester | P1 / P2 |
| `PH-XNEED-018` | Qualité et vérification des statuts | Problème partagé | MVP / P1 |
| `PH-XNEED-019` | Accessibilité et parcours inclusifs | Invariant produit | Gate |
| `PH-XNEED-020` | Collaboration et contributions asynchrones | Analogie à tester | P1 |
| `PH-XNEED-021` | Données métier spécialisées et référentiels | Spécialisation d'organisation | P2 |
| `PH-XNEED-022` | IA, comptes techniques et agents de connaissance | Extension partagée distincte | P2 |
| `PH-XNEED-023` | Environnements et exploitation technique | Spécialisation technique | P2 |
| `PH-XNEED-024` | Correctifs, incidents et preuves de remédiation | Spécialisation technique | P1 / P2 |
| `PH-XNEED-025` | Catalogue de packages réutilisables | Spécialisation technique | P2 |
| `PH-XNEED-026` | Intégrations, jobs et flux de données | Spécialisation technique | P2 |
| `PH-XNEED-027` | Décisions d'exploration et R&D | Spécialisation technique | P1 / P2 |
| `PH-XNEED-028` | Import initial contrôlé d'inventaires | Besoin particulier, extension possible | P1 |
| `PH-XNEED-029` | Client, partenaire et séparation des tenants | Distinction transversale de sécurité | Gate / P1 |

Les 29 IDs correspondent aux familles du document de normalisation interne, mais **les libellés et justifications ont été généralisés**.

## 4. Six capacités qui dessinent le socle commun

### 4.1. Pilotage

Qualifier projets, objectifs et livrables ; retrouver leur état, leurs échéances et leur contexte. `PH-XNEED-002`, `004`, `005`, `009`.

### 4.2. Coordination

Rendre visibles responsables, relais, tâches et blocages ; préparer les arbitrages. `PH-XNEED-003`, `005`, `006`.

### 4.3. Connaissance

Conserver la provenance, l'historique et les références externes ; éviter de dupliquer le contenu spécialisé. `PH-XNEED-007`, `008`.

### 4.4. Continuité

Préparer une passation et vérifier qu'une autre personne peut réellement poursuivre le travail. `PH-XNEED-016`, `003`.

### 4.5. Interopérabilité

Relier le Project à ses ressources existantes tout en conservant les systèmes maîtres. `PH-XNEED-008`, `012`.

### 4.6. Gouvernance et confiance

Appliquer les permissions, isoler les organisations, permettre l'export et tester l'accessibilité. `PH-XNEED-001`, `010`, `019`, `029`.

## 5. Tensions de modélisation à trancher

| Tension | Risque si non résolue | Orientation à tester |
|---|---|---|
| `Organization` versus `Client` | Attribution de droits entre tenants par confusion commerciale | Client comme relation métier distincte du tenant |
| `Workspace` versus `Team` | Autorisations héritées implicitement | Collaboration et appartenance comme objets distincts |
| `Project` versus `Repository` | Inventaire incohérent, doublons de suivi | Project comme initiative ; Repository comme référence |
| Responsable versus approbateur | Validation illégitime d'une décision | Permissions selon mandat et périmètre |
| Livré versus accepté | Indicateurs trompeurs | États métier distincts |
| Statut historique versus actuel | Faux sentiment de progression | Provenance et fraîcheur explicites |
| Passation créée versus reprise réussie | Faux transfert de compétence | Scénario d'acceptation avec action effectuée |
| Vue de synthèse versus copie de toutes les données | Coût et risques de sécurité | Références et API ciblées |

Ces tensions guident la Discovery ; elles ne suffisent pas à constituer un modèle Django final.

## 6. Proposition de MVP à confronter aux utilisateurs

```text
Contextualiser l'Organization et le Workspace
  -> enregistrer Project, objectif, responsable et relais
  -> suivre WorkItems, priorités et blocages
  -> afficher une vue de coordination à jour
  -> conserver l'historique et les liens de référence
  -> constituer une passation
  -> vérifier l'autonomie du repreneur
  -> exporter son périmètre autorisé
```

**Gates préalables à tout essai avec des données réelles :** autorisations institutionnelles, isolation, protections des accès et secrets, restauration de sauvegardes, exploitation, accessibilité, réversibilité et maîtrise du changement.

Le MVP candidat ne dépend pas de la présence des familles spécialisées `PH-XNEED-014`, `021` à `028`.

## 7. Parcours témoins et preuves possibles

| Parcours témoin | Contexte de démonstration | Preuve nécessaire |
|---|---|---|
| Coordonner un ensemble d'initiatives | Deux Workspaces fictifs | Les responsables et blocages sont retrouvés |
| Reprendre un projet | Projet fictif avec historique et documents | Le repreneur réalise la prochaine action |
| Suivre un livrable technique | Projet fictif lié à un dépôt de démonstration | Le statut métier n'est pas confondu avec le statut CI |
| Refuser un accès croisé | Deux Organizations synthétiques | API et exports ne divulguent aucune donnée |
| Sortir du produit | Export de test | La structure reste exploitable hors plateforme |

Aucun test décrit ici n'est présenté comme déjà exécuté.

## 8. Risques de généralisation

- Les sources analysées ne sont ni un échantillon statistique ni une enquête de marché.
- L'expérience du concepteur peut influencer la priorité donnée à des problèmes techniques.
- Un besoin commun documentaire peut masquer des processus très différents.
- Une fonctionnalité générique mal conçue risque d'imposer une gouvernance inadaptée à une organisation.
- Un nombre élevé de besoins normalisés ne justifie pas un MVP riche.

## 9. Protocole de validation transverse

1. Sélectionner des acteurs de contextes et fréquences d'usage différents.
2. Documenter une tâche récente, ses étapes et les sources faisant foi.
3. Montrer un scénario E0 synthétique, tester les exceptions et permissions.
4. Mesurer le temps nécessaire, la qualité de l'information et l'autonomie de reprise.
5. Recueillir les objections et les solutions alternatives à ProjectHub.
6. Ajuster les familles et le MVP sur la base des preuves, pas du nombre de catégories.

**Décisions encore ouvertes :** valeur prioritaire, choix de vues, sémantique des décisions, RBAC, calendrier d'implémentation, licence et cadre des pilotes.

**Liens :** [personas](00-stakeholders-and-personas.md), [étude associative](01-diversite-alternative-needs.md), [étude technique](02-webtech-solutions-needs.md), [workflows](04-current-vs-target-workflows.md), [périmètre](../01-product/02-product-scope.md).
