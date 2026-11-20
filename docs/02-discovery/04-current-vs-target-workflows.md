---
id: PH-DISC-WF-001
title: "ProjectHub - Processus actuels et cibles candidats"
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
  - "docs/02-discovery/03-cross-organization-needs.md"
  - "docs/01-product/02-product-scope.md"
publication_note: "Comparaisons generiques construites pour la validation, pas audit operationnel public"
---

# Processus actuels et processus cibles (As-Is / To-Be)

> **Édition publique de Discovery - draft.** Le corpus privé documente **32 workflows candidats : 10 transversaux, 10 associés à un contexte collectif et 12 associés à un contexte technique**. Cette édition conserve leurs IDs stables mais **généralise les parcours** : les processus As-Is sont des hypothèses à observer, non une photographie publique du fonctionnement d'un tiers. Les workflows To-Be ne sont pas des fonctions déjà développées.

## 1. Méthode de comparaison

Pour chaque workflow :
- **Déclencheur** : pourquoi l'activité commence ;
- **Acteurs** : responsable, contributeur, approbateur, administrateur, repreneur ;
- **As-Is à vérifier** : déroulement actuel hypothétique et source de vérité ;
- **Friction candidate** : incohérence, perte de contexte, double saisie ou absence de preuve ;
- **To-Be proposé** : résultat attendu avec ProjectHub et outils existants ;
- **Permissions** : accès requis et situations de refus ;
- **Preuve** : observation ou test rendant l'amélioration falsifiable.

Les liens inter-domaines doivent être conçus sans transférer automatiquement les droits ni les données d'un outil externe.

## 2. Les dix workflows transversaux

| ID | Workflow | As-Is à vérifier | To-Be candidat | Preuve attendue |
|---|---|---|---|---|
| `PH-WF-C01` | Qualifier une initiative | Demande dispersée ou ambiguë | Project, objectif, sponsor et prochaine étape explicites | Fiche comprise et qualifiée |
| `PH-WF-C02` | Rattacher et sécuriser | Espaces et accès confondus | Organization / Workspace / memberships séparés | Refus d'un accès non autorisé |
| `PH-WF-C03` | Définir responsables et relais | Attribution informelle | ProjectLead, relais, contributeur et approbateur distincts | Transfert contrôlé de responsabilité |
| `PH-WF-C04` | Suivre les actions | Statuts et dates hétérogènes | WorkItems, échéances, blocages, mises à jour | Action retrouvée avec son état |
| `PH-WF-C05` | Préparer une revue | Consolidation manuelle préalable | Vue filtrée, sujets bloquants et décisions à prendre | Revue conduite sur données traçables |
| `PH-WF-C06` | Contextualiser une décision | Raisons et références difficilement retrouvables | Journal et liens vers documents maîtres | Justification accessible au bon rôle |
| `PH-WF-C07` | Livrer, accepter, clôturer | États confondus | Livraison technique, acceptation métier et clôture distinguées | Cas de refus ou attente explicite |
| `PH-WF-C08` | Transmettre et vérifier | Passation orale ou purement administrative | Dossier de reprise puis action du successeur | Autonomie effectivement observée |
| `PH-WF-C09` | Exporter et sortir | Formats ou périmètres incertains | Export autorisé et procédure de sortie | Données lisibles, aucun accès croisé |
| `PH-WF-C10` | Qualifier la fraîcheur | Information historique supposée actuelle | Date, provenance, statut déclaré / vérifié | Information correctement interprétée |

Ces workflows servent à **définir les tests**, pas à imposer une séquence identique à tous les utilisateurs.

## 3. Dix variantes de contexte collectif

Les codes `PH-WF-DA01` à `DA10` sont **des références de traçabilité**, pas une description nominative de pratiques ou projets existants. Toutes les situations sont fictives.

| ID | Variante généralisée | Besoin sous-jacent | Frontière à respecter | Horizon |
|---|---|---|---|---|
| `PH-WF-DA01` | Prioriser un ensemble d'engagements | Clarifier priorités, capacité et échéances | Ne pas remplacer l'instance d'arbitrage | MVP / P1 |
| `PH-WF-DA02` | Préparer le relais d'un outil de travail | Identifier mainteneur, documentation et étapes | Ne jamais copier les secrets | P1 |
| `PH-WF-DA03` | Suivre une livraison reliée à Git | Faire le lien entre travail et résultat métier | Git et CI restent la source technique | P1 |
| `PH-WF-DA04` | Accompagner la première contribution | Permettre l'action d'un utilisateur peu fréquent | Droits limités et interface compréhensible | P1 |
| `PH-WF-DA05` | Retrouver une documentation partagée | Relier projet et contenu documentaire pertinent | Les documents restent dans leur système maître | MVP liens / P1 |
| `PH-WF-DA06` | Demander un indicateur métier | Clarifier question, source, responsable et résultat | Pas de traitement direct de données spécialisées | P2 |
| `PH-WF-DA07` | Suivre une amélioration administrative | Assigner et valider une action métier | Ne pas recréer le logiciel métier | P2 |
| `PH-WF-DA08` | Prévenir une échéance d'exploitation | Visibilité sur date, titulaire et confirmation | Ne pas stocker des secrets ni administrer l'hébergeur | P1 |
| `PH-WF-DA09` | Constituer la mémoire et passer le relais | Documenter et faire reprendre un chantier | La continuité doit fonctionner hors ProjectHub | MVP |
| `PH-WF-DA10` | Respecter la gouvernance d'une initiative | Distinguer décision, mandat et exécution | Administration technique ≠ approbation métier | P1 |

**Limite :** ces variantes illustrent des besoins à étudier, et non des engagements opérationnels d'une association particulière.

## 4. Douze variantes de contexte technique

Les codes `PH-WF-WEB01` à `WEB12` sont conservés pour correspondre aux workflows de la Discovery privée. Les cas ci-dessous sont volontairement synthétiques.

| ID | Variante généralisée | Besoin sous-jacent | Frontière à respecter | Horizon |
|---|---|---|---|---|
| `PH-WF-WEB01` | Réconcilier un inventaire | Vérifier qu'un élément est réellement un projet actif | Ne pas assimiler un dossier à un Project | MVP / P1 |
| `PH-WF-WEB02` | Suivre un plan d'amélioration | Actions, responsables et preuves de clôture | Ne pas divulguer les constats de sécurité | MVP |
| `PH-WF-WEB03` | Cadrer un livrable client | Objectif, responsabilité, preuve d'acceptation | Client distinct de l'Organization | MVP / P1 |
| `PH-WF-WEB04` | Préparer une release | Associer version, dépendances et validation | Ne pas remplacer CI/CD | P1 / P2 |
| `PH-WF-WEB05` | Transférer une maintenance | Contexte, décisions et reprise effective | Les droits Git ne se transfèrent pas implicitement | MVP |
| `PH-WF-WEB06` | Suivre la remédiation d'un risque | Attribuer une action et vérifier sa correction | Traitement d'incident dans son outil dédié | P1 |
| `PH-WF-WEB07` | Maintenir un composant partagé | Dépendances, mainteneur et version | Registry et dépôt restent sources de vérité | P2 |
| `PH-WF-WEB08` | Référencer un traitement ou connecteur | Contexte métier, propriétaire et état | ProjectHub n'est pas ordonnanceur | P2 |
| `PH-WF-WEB09` | Décider d'une expérimentation | Hypothèse, résultats, décision Go/No-Go | Pas de preuve scientifique inventée | P1 / P2 |
| `PH-WF-WEB10` | Suivre une dépendance d'infrastructure | Impact projet et responsabilité | Aucun secret ni supervision native présumée | P2 |
| `PH-WF-WEB11` | Encadrer une contribution IA | Accès bornés, sources et vérification | Pas d'approbation automatique d'actes sensibles | P2 |
| `PH-WF-WEB12` | Séparer relation client et tenant | Comprendre collaboration sans accès croisé | Tests stricts de permissions | Gate / P1 |

## 5. Exemple détaillé : suivre une action et un blocage

**Acteur :** responsable de projet habilité. **Contexte :** projet fictif `Demo-Project-A`, données synthétiques.

### As-Is à examiner

Une action discutée en réunion est conservée dans un document ; ses responsables, sa date de suivi et son état sont à retrouver dans différents outils.

### To-Be proposé

1. Le responsable ouvre le bon contexte Organization / Workspace.
2. Il retrouve le Project et son objectif.
3. Il crée ou met à jour un WorkItem avec un titulaire, un état et une échéance.
4. Il déclare un blocage et lie la référence documentaire autorisée.
5. Une vue de suivi rend le blocage visible.
6. Une autre personne habilitée retrouve l'action et son historique.
7. Une personne non habilitée ne peut ni modifier ni lire le WorkItem.

**Critères d'évaluation :** compréhension de la tâche, absence de double saisie, mise à jour attribuée à un acteur et contrôle d'accès côté serveur.

## 6. Exemple détaillé : transmission

```text
Projet à transmettre
  -> résumé de contexte, objectifs et résultats
  -> liens vers références autorisées
  -> tâches, blocages et responsabilités
  -> vérification des accès du repreneur
  -> démonstration par le repreneur d'une prochaine action
  -> validation de la passation par l'autorité compétente
```

Le transfert d'un rôle ProjectHub ne transfère pas automatiquement l'accès au dépôt Git, à une boîte mail, à une application tiers ou à des secrets. Les démarches de passation organisationnelle sont **indépendantes du développement du logiciel**.

## 7. Test négatif obligatoire : isolation

Deux organisations fictives `Demo-Org-A` et `Demo-Org-B` possèdent chacune un Workspace et un Project portant un titre semblable.

Un utilisateur de A doit être refusé lorsqu'il tente, par l'interface, l'API, la recherche, une référence directe ou l'export, d'obtenir des données de B, sauf autorisation explicitement conçue et testée.

**La simple absence d'un bouton ne constitue pas une preuve d'isolation.**

## 8. Carte As-Is / To-Be des frictions et preuves

| Friction candidate | Amélioration visée | Preuve à produire |
|---|---|---|
| Inventaires incohérents | Project identifié et qualifié | Échantillon réconcilié, états expliqués |
| Responsabilités implicites | Titulaire, relais et approbateur distingués | Réaffectation testée |
| Historique dispersé | Changements significatifs traçables | Auteur et date consultables |
| Revue fastidieuse | Vue de coordination fiable | Temps observé avant/après |
| Documents introuvables | Références contextualisées | Lien source et permission préservés |
| Passation incomplète | Autonomie du successeur | Action réalisée par repreneur |
| États ambigus | Livré, accepté, terminé distincts | Cas d'attente d'acceptation |
| Sortie difficile | Export compréhensible | Réimport partiel ou lecture indépendante |
| Accès confondus | Refus par défaut | Tests API négatifs |
| Parcours inaccessibles | Interaction inclusive | Tests clavier et technologies d'assistance |

## 9. Priorités candidates et dépendances

- **Gate E0** : capacité à tester les droits et une isolation minimale sur données fictives.
- **Cœur MVP** : `PH-WF-C01` à `C04`, `C06`, `C08`, `C09`, `C10` en versions limitées et compréhensibles.
- **Extensions P1** : arbitrages formalisés, releases, onboarding avancé, recherche interprojets, planning étendu.
- **Extensions P2** : catalogue technique, orchestration, agents autonomes et synchronisation avancée.

Le premier MVP doit **prouver un cycle complet**, pas la couverture de 32 processus en production.

## 10. Validation et statut

Les 32 workflows restent des **hypothèses de conception**. Pour les approuver :
1. confronter le As-Is à au moins un utilisateur habilité ;
2. documenter les différences entre contextes et outils maîtres ;
3. rendre explicites les droits de chaque acteur ;
4. tester les cas alternatifs, les erreurs et les rejets ;
5. évaluer la reprise par une personne distincte ;
6. recueillir les objections et enregistrer les décisions.

Les scénarios ci-dessus **n'ont pas été exécutés**. Les seuils de réussite et toute organisation pilote restent à confirmer.

**Liens :** [personas](00-stakeholders-and-personas.md), [besoins associatifs](01-diversite-alternative-needs.md), [besoins techniques](02-webtech-solutions-needs.md), [analyse transversale](03-cross-organization-needs.md), [scope](../01-product/02-product-scope.md).
