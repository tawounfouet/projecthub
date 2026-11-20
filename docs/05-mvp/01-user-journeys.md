---
id: PH-MVP-UJ-001
title: "ProjectHub - Parcours utilisateurs MVP candidats (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / UX / Engineering - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/05-mvp/00-mvp-definition.md"
  - "docs/05-mvp/02-prioritized-backlog.md"
  - "docs/06-validation/00-pilot-validation-plan.md"
---

# ProjectHub - Parcours utilisateurs du MVP

> **Édition publique expurgée - draft.** Les dix parcours `MVP-UJ-01..10` et les **62 critères `UJxx-ACnn`** du corpus privé servent de référence de conception. Les fiches qui suivent en proposent une synthèse publique et des exemples de critères, sans publier des données d'organisations ni prétendre que les essais ont été exécutés.

## 1. Objectif de l'évaluation

Le MVP doit démontrer qu'une équipe peut **qualifier une initiative, désigner un responsable, suivre le travail, consulter le contexte, préparer une passation et exporter ses données**, tout en préservant ses droits d'accès.

Une page chargée, un clic réussi ou un test rédigé n'est **pas** une preuve suffisante de réussite utilisateur. Les résultats doivent provenir d'un exercice daté sur une version identifiable du produit.

## 2. Jeu de données de démonstration E0

Utiliser exclusivement des données synthétiques :
- `Demo-Org-A` et `Demo-Org-B`, Organizations fictives sans relation d'accès ;
- au moins un Workspace par tenant ;
- Projects fictifs, WorkItems, dates, blocages et références factices ;
- un membre du tenant A, un membre du tenant B, une personne autorisée sur A et B, et un utilisateur sans droits ;
- profils distincts d'administrateur technique, ProjectLead, contributeur, approbateur potentiel et successeur.

Les tests doivent pouvoir être rejoués avec un jeu déterministe. Aucun compte, document ou incident d'une organisation réelle ne doit être inséré dans E0.

## 3. Les dix parcours de référence

| ID | Intention du parcours | Slice candidate | Vérification centrale |
|---|---|---|---|
| `MVP-UJ-01` | Se connecter et choisir un contexte | `SLICE-00` | Session et permissions effectivement limitées au tenant |
| `MVP-UJ-02` | Créer une initiative traçable | `SLICE-01` | Project relié au bon Workspace |
| `MVP-UJ-03` | Suivre une action et son blocage | `SLICE-01/02` | Auteur, responsable, état, échéance et historique |
| `MVP-UJ-04` | Préparer une réunion sans reporting fictif | `SLICE-02` | Sources et fraîcheur des informations |
| `MVP-UJ-05` | Référencer un document sans le copier | `SLICE-03` | Accès à la référence sans transfert de droits tiers |
| `MVP-UJ-06` | Préparer, recevoir et vérifier une passation | `SLICE-04` | Autonomie d'une personne distincte |
| `MVP-UJ-07` | Révoquer sans effacer l'histoire | `SLICE-00/04` | Accès bloqué, historique préservé |
| `MVP-UJ-08` | Exporter et sortir sans verrouillage | `SLICE-05` | Export lisible hors plateforme et sans fuite |
| `MVP-UJ-09` | Refuser une approbation sans mandat | `SLICE-00/02` | Pas de décision institutionnelle par un simple admin |
| `MVP-UJ-10` | Séparer relations clients et Organizations | `SLICE-00/01` | ClientReference n'ouvre aucun accès inter-tenant |

La planification reste à arbitrer ; une référence de slice ne constitue ni une release livrée, ni un ticket réalisé.

## 4. Fiches synthétiques des parcours

### MVP-UJ-01 - Contexte actif

**Acteur :** personne ayant plusieurs affiliations.  
**Déclencheur :** connexion et sélection d'un Workspace.

**Nominal candidat :** identifier la session, lister uniquement les Organizations autorisées, choisir un Workspace, afficher le contexte actif et ouvrir la liste des Projects accessibles.

**Alternatives à tester :** invitation non activée, affiliation révoquée, Workspace inexistant, réutilisation d'une session ancienne.

**Refus obligatoire :** un compte de A ne peut retrouver les données de B ni en modifiant un ID API, ni par recherche ou export.

**Preuve :** logs de tests sans secrets, permissions évaluées côté serveur et contexte affiché.

### MVP-UJ-02 - Création d'initiative

**Acteur :** ProjectLead ou créateur habilité.  
**Nominal :** sélectionner le Workspace, créer le Project, préciser objectif, responsable, éventuel livrable et prochaine action.

**Alternatives :** projet sans responsable à compléter, nom déjà utilisé, date invalide, Workspace archivé.

**Refus :** création dans un Workspace d'une autre Organization.

**Preuve :** Project nouvellement créé dans le bon parent, avec historique initial et validation des champs.

### MVP-UJ-03 - Travail actionnable

**Acteur :** contributeur habilité.  
**Nominal :** créer ou retrouver un WorkItem, l'assigner, définir priorité et échéance éventuelle, déclarer un blocage, puis changer l'état.

**Alternatives :** assignee absent ou non éligible, échéance absente, blocage non résolu, changement concurrent.

**Refus :** assignation ou modification hors scope.

**Preuve :** état, auteur, horodatage et blocage interprétables, sans validation fictive.

### MVP-UJ-04 - Revue factuelle

**Acteur :** coordinateur ayant accès à plusieurs projets.  
**Nominal :** filtrer une Table, repérer les projets bloqués, afficher les dernières mises à jour et distinguer état déclaré, vérifié et inconnu.

**Alternatives :** projets sans mise à jour récente, résultat vide, KPI impossible à calculer.

**Refus :** inclure les Projects d'une autre Organization dans un total ou une vue.

**Preuve :** l'utilisateur explique la source et la fraîcheur d'une information et identifie les décisions encore à prendre.

### MVP-UJ-05 - Références documentaires

**Acteur :** membre autorisé d'un Project.  
**Nominal :** rattacher une référence externe avec titre, type, source et visibilité ; retrouver ensuite cette référence depuis le Project.

**Alternatives :** lien inaccessible, document déplacé, référence expirée ou non vérifiée.

**Refus :** révéler l'URL ou ses métadonnées à un utilisateur non autorisé ; reproduire un token ou document interne.

**Preuve :** lien stocké et consultable selon les droits ProjectHub ; droits du système externe inchangés.

### MVP-UJ-06 - Passation réelle

**Acteurs :** responsable sortant, successeur et observateur habilité.  
**Nominal :** préparer objectif, état, historique, actions ouvertes et références, proposer le relais, vérifier les droits puis faire accomplir une prochaine action par le successeur.

**Alternatives :** documents absents, successeur non habilité, exercice échoué, réserves restantes.

**Refus :** marquer le Handover « validé » sur simple remise d'un dossier ou par un acteur sans mandat.

**Preuve :** action effectivement accomplie, date, résultat et réserves, sans divulguer de données réelles.

### MVP-UJ-07 - Révocation sûre

**Acteur :** administrateur autorisé du tenant.  
**Nominal :** désactiver un membership, vérifier qu'il ne peut plus lire ou modifier les ressources, maintenir les événements historiques attribuables.

**Alternatives :** propriétaire unique, session ancienne, job déjà planifié, ressource partagée.

**Refus :** une session révoquée accède par URL directe, API, recherche ou export.

**Preuve :** tests de refus exécutés après révocation, conservation de l'historique et absence de fuite de secrets.

### MVP-UJ-08 - Portabilité et sortie

**Acteur :** responsable des données habilité.  
**Nominal :** demander un export du périmètre autorisé, obtenir un fichier structuré, l'ouvrir hors ProjectHub et vérifier les références.

**Alternatives :** export volumineux, fichier incomplet, droit retiré pendant la génération, suppression réglementée.

**Refus :** intégrer des données du tenant B à l'export de A ou permettre le téléchargement par un acteur non autorisé.

**Preuve :** inspection indépendante du format et du contenu ; la suppression reste une opération distincte à autoriser.

### MVP-UJ-09 - Approbation sous mandat

**Acteur :** administrateur technique ou contributeur sans autorité métier.  
**Nominal :** consulter le résultat d'un travail et identifier qui doit décider de son acceptation.

**Refus attendu :** une requête d'approbation non mandatée est rejetée côté serveur, même si l'acteur peut administrer le Workspace.

**Preuve :** test négatif et absence de changement d'état. Il n'est **pas nécessaire d'implémenter tout un système de décisions** pour prouver ce refus au socle candidat.

### MVP-UJ-10 - Client distinct du tenant

**Acteur :** responsable de Project dans une équipe multi-clients.  
**Nominal :** rattacher une référence client synthétique à un Project du tenant A et la consulter selon les droits de A.

**Alternatives :** client homonyme, plusieurs contrats ou acteurs, modification de la relation.

**Refus :** déduire du nom de client un droit d'accès à une autre Organization, ses Projects ou son historique.

**Preuve :** séparation testée entre `ClientReference`, `Organization`, `Workspace` et `Team`.

## 5. Trois démonstrations de bout en bout candidates

| Démo | Enchaînement de parcours | Ce qu'elle pourrait démontrer |
|---|---|---|
| `DEMO-D1` - Coordination et passation | 02 -> 03 -> 04 -> 05 -> 06 | Travail compréhensible et reprise autonome sur données fictives |
| `DEMO-D2` - Suivi d'une livraison technique | 10 -> 02 -> 03 -> 05 -> 04 | Références vers le bon outil sans remplacement de Git |
| `DEMO-D3` - Isolation entre tenants | 01 -> 07 -> 08 -> 09 -> 10 | Refus par scope, révocation, export et mandat |

Les trois scénarios sont **des plans de démonstration**, pas des tests effectués ni des témoignages de pilotes.

## 6. Accepter ou rejeter un parcours

Pour chaque parcours :
1. préciser `scenario_id`, actor, Organization, Workspace et data classification ;
2. enregistrer le commit SHA et l'environnement E0 ;
3. exécuter le nominal, une alternative et un refus direct API si pertinent ;
4. enregistrer le résultat observé, la durée seulement si mesurée, les anomalies et les preuves ;
5. tester l'accessibilité des actions essentielles : clavier, focus, messages, zoom ;
6. consigner un verdict par un évaluateur distinct de l'auteur lorsque possible ;
7. revalider après correction et distinguer `passed`, `failed`, `blocked`, `not-run`.

Les **62 `UJxx-ACnn` du corpus privé** ne sont pas tous publiés ici ; ils restent des références de conception et devront être repris uniquement dans les tests publiables appropriés.

## 7. Ordre, risques et réserves

`MVP-UJ-01` et ses refus précèdent les autres scénarios. `MVP-UJ-02` est nécessaire pour `03` et `05`, qui rendent la passation `06` significative. La révocation `07` doit être retestée après chaque changement de politique d'accès. La sortie `08` peut précéder `06` si cela protège les données.

**Toujours en suspens :** rôles et héritage, autorité métier, preuve de reprise, UX Table/Board, qualité des statuts et seuils d'acceptation.

Voir [définition du MVP](00-mvp-definition.md), [backlog](02-prioritized-backlog.md), [plan de validation](../06-validation/00-pilot-validation-plan.md) et [règles métier](../03-requirements/02-business-rules-and-permissions.md).
