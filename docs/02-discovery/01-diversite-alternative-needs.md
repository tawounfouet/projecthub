---
id: PH-DISC-DIV-001
title: "ProjectHub - Besoins génériques de coordination associative"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources:
  - PH-OPS-001
  - PH-CNV-004
related_documents:
  - "docs/02-discovery/03-cross-organization-needs.md"
  - "docs/02-discovery/04-current-vs-target-workflows.md"
publication_note: "Edition de recherche générique sans restitution d'informations opérationnelles"
---

# Besoins candidats d'un environnement associatif

> **Édition publique abstraite.** Ce fichier reprend l'emplacement prévu dans l'index initial de Discovery, mais **ne publie pas le compte rendu de l'organisation évoquée dans son nom**, ni ses projets, personnes, statuts, outils configurés, incidents ou décisions. Il ne constitue pas une expression des besoins validée, un accord de pilote ou une communication au nom d'un tiers.

## 1. Question de recherche

**Comment une organisation avec plusieurs initiatives et des contributions de disponibilité variable peut-elle suivre ses engagements, clarifier les responsabilités et transmettre son activité sans dépendre de la mémoire d'une seule personne ?**

L'enjeu se décompose en quatre difficultés candidates :
- vision transversale des initiatives ;
- coordination de responsables aux mandats et disponibilités différents ;
- conservation du contexte et des décisions ;
- reprise des activités lors d'un changement de responsables.

Ces difficultés sont des **hypothèses générales éclairées par des sources privées**, non un état actuel vérifié d'une organisation nommée.

## 2. Acteurs génériques et responsabilités

| Acteur | Attente candidate | Ne lui confère pas automatiquement |
|---|---|---|
| Coordination | Identifier les chantiers prioritaires et les blocages | Droit de modifier toute donnée |
| Responsable d'initiative | Définir objectifs et état des actions | Pouvoir statutaire d'approbation |
| Contributeur occasionnel | Trouver une action faisable et son contexte | Accès administrateur |
| Référent métier | Vérifier un livrable et formuler un retour | Droit de transférer les secrets |
| Responsable des accès | Révoquer et attribuer les permissions | Droit d'approuver les objectifs métier |
| Successeur | Comprendre les tâches, décisions et documents | Accès automatique aux systèmes externes |

`Organization`, `Workspace`, `Project` et `WorkItem` doivent être distingués, y compris si l'association n'utilise qu'un seul espace au lancement.

## 3. Besoins candidats, regroupés par familles transversales

| Famille | Besoin métier à tester | Illustration synthétique | Horizon candidat |
|---|---|---|---|
| `PH-XNEED-002` | Retrouver toutes les initiatives pertinentes | Une liste d'initiatives avec responsable et date de mise à jour | MVP |
| `PH-XNEED-003` | Connaître le titulaire et le relais | Une fiche indique qui agit et qui peut reprendre | MVP |
| `PH-XNEED-004` | Séparer résultat livré et résultat accepté | Une réalisation reste en attente de validation métier | MVP minimal / P1 |
| `PH-XNEED-005` | Suivre le travail et les échéances | Action avec échéance, statut et auteur de mise à jour | MVP |
| `PH-XNEED-006` | Préparer une revue de blocages | Les éléments à arbitrer sont visibles avant la réunion | MVP / P1 |
| `PH-XNEED-007` | Retrouver les changements | L'historique montre une réaffectation sans l'effacer | MVP |
| `PH-XNEED-008` | Conserver des références de documents | Lien autorisé vers la source documentaire d'origine | MVP |
| `PH-XNEED-009` | Obtenir une vue simple de coordination | Vue filtrée par priorité et par responsable | MVP |
| `PH-XNEED-010` | Pouvoir quitter le service | Export limité à son périmètre légitime | Porte de sûreté |
| `PH-XNEED-015` | Faciliter la première contribution | Un nouvel arrivant sait quoi faire et où demander de l'aide | P1 |
| `PH-XNEED-016` | Organiser une passation testable | Le repreneur retrouve contexte, blocages et prochaine action | MVP |
| `PH-XNEED-019` | Permettre l'usage inclusif | Navigation clavier et informations compréhensibles | Porte de qualité |

La liste illustre **des besoins génériques** et n'expose aucun identifiant interne d'action ou de source associative. L'appartenance de ces familles au MVP doit être confirmée par validation utilisateur.

## 4. Processus actuel à observer (As-Is)

Le processus de référence à **enquêter**, non à attribuer à une association particulière, pourrait être :

```text
Une initiative apparaît
  -> différentes personnes échangent dans plusieurs canaux
  -> le suivi dépend de documents ou notes
  -> les responsabilités évoluent
  -> les informations sont réconciliées avant la prochaine réunion
  -> un successeur doit reconstruire une partie du contexte
```

**Questions à vérifier :** où naît la demande, quelle est la référence faisant foi, qui peut arbitrer, que signifie « terminé », et quelles informations restent disponibles après un changement d'équipe ?

## 5. Processus cible hypothétique (To-Be)

```text
Qualifier l'initiative et son objectif
  -> désigner responsable et relais
  -> enregistrer actions, échéances et blocages
  -> relier les documents de référence sans copie inutile
  -> préparer la revue et identifier les décisions en attente
  -> préparer une fiche de transmission
  -> faire réaliser une action au successeur
  -> exporter les données autorisées
```

Le processus cible conserve **les décisions institutionnelles et les systèmes spécialisés dans leurs outils ou instances compétentes**.

## 6. Scénarios d'acceptation synthétiques

### A. Préparer une revue

Un coordinateur autorisé consulte trois projets fictifs, identifie deux blocages, rattache une demande d'arbitrage et produit une vue pour la réunion.

**Réussite à vérifier :** l'information est à jour, son auteur est identifiable et une décision ne peut pas être approuvée par une personne sans mandat.

### B. Faire contribuer un nouvel arrivant

Une personne ayant un accès limité ouvre son Workspace, comprend le but d'un projet et met à jour uniquement l'action qui lui a été confiée.

**Réussite à vérifier :** permissions, compréhension et accessibilité ; aucune donnée d'un autre Workspace ou d'une autre Organization n'est exposée.

### C. Transmettre un dossier

Un responsable prépare un résumé : objectif, état, actions ouvertes, blocages, documents maîtres et relais. Un repreneur indique puis réalise la prochaine action sans recourir systématiquement au responsable sortant.

**Réussite à vérifier :** passation **effective** plutôt que simple dépôt d'une checklist.

### D. Sortir d'une expérimentation

Un administrateur autorisé exporte uniquement les données de son Organization et vérifie leur intelligibilité.

**Réussite à vérifier :** aucune donnée d'un autre tenant, absence de dépendance à un format fermé non documenté.

## 7. Contraintes et frontières

- Une association, un programme, une Team et un Workspace ne sont pas des synonymes.
- Une autorisation liée à un rôle de ProjectHub ne remplace pas le mandat d'une instance de gouvernance.
- Les documents, informations de contact, finances ou systèmes d'automatisation restent sous leur propre gouvernance.
- ProjectHub n'a pas vocation à devenir une comptabilité, une GED complète, un annuaire personnel ou un orchestrateur.
- Les invitations, exports, recherches et agents doivent respecter l'isolation côté serveur.
- La continuité des activités doit être organisée **même si ProjectHub n'est pas livré**.

## 8. Plan d'étude proposé

Avant tout pilote ou import :
1. demander un accord à l'autorité habilitée et définir les données autorisées ;
2. sélectionner avec les utilisateurs un parcours concret et mesurable ;
3. mener des entretiens séparés avec un responsable, un contributeur et une personne susceptible de reprendre ;
4. observer le flux actuel sans supposer les problèmes résolus par un logiciel ;
5. tester un parcours E0 sur données fictives et une permission négative ;
6. vérifier l'accessibilité et la capacité d'export ;
7. décider formellement d'un éventuel pilote E1 après preuves de sécurité et plan de sortie.

**Indicateurs à définir :** temps de préparation d'une revue, complétude des responsables, tâches comprises, autonomie de reprise et incidents d'autorisation. Aucun chiffre de réussite n'est affirmé ici.

## 9. Questions et limites

- Quelle autorité peut valider les besoins et autoriser un essai ?
- Quels processus et données peuvent être étudiés sans contrainte de confidentialité ?
- Quels critères démontrent une passation opérationnelle indépendante du produit ?
- Quelles tâches restent dans les systèmes existants ?
- Quel niveau d'administration est nécessaire pour des membres aux profils variés ?

Les réponses sont **non acquises**. Ce document sera révisé uniquement à partir de données publiables et approuvées.

**Liens :** [personas](00-stakeholders-and-personas.md) - [besoins inter-organisations](03-cross-organization-needs.md) - [workflows](04-current-vs-target-workflows.md) - [politique de publication](../PUBLICATION-POLICY.md).
