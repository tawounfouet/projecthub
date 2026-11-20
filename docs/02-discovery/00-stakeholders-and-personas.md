---
id: PH-DISC-STK-001
title: "ProjectHub - Parties prenantes et personas candidats"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources:
  - PH-CNV-004
  - PH-OPS-001
  - PH-OPS-002
related_documents:
  - "docs/01-product/00-product-vision.md"
  - "docs/02-discovery/03-cross-organization-needs.md"
---

# Parties prenantes et personas candidats

> **Discovery - édition publique expurgée.** Ces personas sont des hypothèses de conception dérivées de besoins observés dans différents contextes. Aucun entretien publié ni aucune organisation n'est réputé avoir approuvé ces profils. Les rôles sont illustratifs, sans noms de personnes.

## 1. Objectif de la cartographie

ProjectHub doit permettre de **qualifier, suivre, contextualiser et transmettre** un projet pour des équipes qui ne partagent ni la même organisation ni les mêmes responsabilités. Il est donc nécessaire de distinguer :
- **Acteur métier** : personne accomplissant un travail ou décidant d'un résultat ;
- **Utilisateur du produit** : personne utilisant l'interface ou l'API ;
- **Administrateur** : personne autorisée à gérer un périmètre d'accès ;
- **Sponsor / décideur** : personne qui arbitre la valeur ou le financement ;
- **Personne chargée de la reprise** : personne devant réellement pouvoir poursuivre le travail ;
- **Identité technique** : intégration ou agent disposant de permissions bornées.

Un **persona** est un outil d'analyse. Ce n'est ni une personne réelle, ni un compte, ni un rôle RBAC automatiquement attribué.

## 2. Registre de 13 personas à tester

| ID | Persona candidat | Besoin central à vérifier | Priorité d'étude |
|---|---|---|---|
| `PH-PER-001` | Coordinateur multi-projets | Voir priorités, propriétaires, blocages et états de plusieurs projets | P0 |
| `PH-PER-002` | Lead métier / sponsor de projet | Définir et accepter des résultats, distinguer décision et exécution | P0 |
| `PH-PER-003` | Responsable d'exécution / chef de projet | Organiser actions, responsables, dépendances et échéances | P0 |
| `PH-PER-004` | Contributeur occasionnel ou nouvel arrivant | Comprendre sa première action sans maîtriser tous les outils | P0 |
| `PH-PER-005` | Successeur / repreneur de dossier | Récupérer le contexte, les contacts fonctionnels et les prochaines actions | P0 |
| `PH-PER-006` | Responsable IT / portefeuille technique | Suivre des projets et leur contexte technique sans répliquer Git/CI/CD | P0 |
| `PH-PER-007` | Relais fonctionnel / référent recette | Vérifier qu'un livrable répond au besoin métier | P1 |
| `PH-PER-008` | Administrateur d'Organization / Workspace | Gérer membres et permissions sans accéder implicitement à tout | P0 |
| `PH-PER-009` | Responsable de gouvernance | Retrouver les arbitrages légitimes et leurs responsables | P1 |
| `PH-PER-010` | Lecteur / observateur | Comprendre un état sans pouvoir le modifier | P1 |
| `PH-PER-011` | Utilisateur ou testeur d'accessibilité | Naviguer et agir sans obstacle évitable | P0 transversal |
| `PH-PER-012` | Acheteur / sponsor économique Cloud | Évaluer coût, fiabilité, sécurité, exploitation et réversibilité | P1 commercial |
| `PH-PER-013` | Mainteneur Community / intégrateur | Installer, mettre à jour, documenter et étendre la solution | P2 |

La priorité d'étude ne constitue pas une priorité de développement adoptée. `PH-PER-011` est une **perspective de test transversale**, et non une catégorie humaine homogène.

## 3. Rôles, accès et pouvoirs de décision

| Situation | Distinction indispensable | Conséquence produit candidate |
|---|---|---|
| Une personne gère un projet | `ProjectLead` ≠ `OrgAdmin` | Les droits de modification restent contextualisés |
| Une personne décide du résultat | `Approver` ≠ `Assignee` | L'acceptation doit être autorisée |
| Un membre quitte une équipe | Responsabilité métier ≠ appartenance technique | La révocation préserve l'historique sans conserver l'accès |
| Une personne rejoint deux organisations | Identité globale ≠ données partagées | Vérifier chaque contexte d'Organization |
| Un observateur lit un rapport | Lecture ≠ export massif | Les permissions d'export restent contrôlées |
| Un agent automatise une action | Identité technique ≠ délégation universelle | Permissions minimales, journaux, validation sensible |

Les frontières exactes du RBAC ne sont pas arbitrées. Elles doivent être démontrées par des **tests de refus côté serveur**, et non seulement par des menus masqués.

## 4. Huit scénarios d'observation

Les scénarios `SCN-STK-01` à `SCN-STK-08` sont issus de la cartographie privée ; leurs formulations publiques sont génériques.

| Scénario | Acteur principal | Question de recherche |
|---|---|---|
| `SCN-STK-01` - Point d'avancement multi-projets | Coordinateur | Trouve-t-il les initiatives prioritaires et leur état ? |
| `SCN-STK-02` - Reprendre un projet | Successeur | Peut-il expliquer et exécuter la prochaine étape ? |
| `SCN-STK-03` - Première contribution | Nouveau membre | Comprend-il la tâche, le contexte et les autorisations ? |
| `SCN-STK-04` - Suivi technique | Responsable IT | Une référence externe évite-t-elle la double saisie ? |
| `SCN-STK-05` - Déléguer l'administration | Administrateur | Les droits octroyés sont-ils appropriés et révocables ? |
| `SCN-STK-06` - Préparer une décision | Sponsor | Peut-il distinguer faits, propositions et validations ? |
| `SCN-STK-07` - Parcours inclusif | Utilisateur testeur | Peut-il naviguer au clavier et comprendre les erreurs ? |
| `SCN-STK-08` - Évaluer l'offre Cloud | Acheteur potentiel | La valeur managée justifie-t-elle un budget ? |

**Aucun de ces scénarios n'est déclaré exécuté** : il s'agit d'un plan d'observation.

## 5. Jobs to Be Done candidats

- **Coordination** : « Quand plusieurs initiatives avancent simultanément, je veux voir l'état, le responsable et les prochains points de décision pour conduire une revue utile. »
- **Contribution** : « Quand j'arrive sur un projet, je veux comprendre le but et la prochaine action sans dépendre d'une explication orale permanente. »
- **Passation** : « Quand une responsabilité change, je veux disposer d'un contexte vérifiable et d'un relais capable d'agir. »
- **Gouvernance** : « Quand un arbitrage est demandé, je veux distinguer l'autorité compétente des personnes exécutant le travail. »
- **Gestion des accès** : « Quand un membre change de périmètre, je veux qu'il conserve uniquement les permissions justifiées. »
- **Adoption** : « Quand j'évalue un produit managé, je veux mesurer le coût total et la possibilité de quitter le service. »

## 6. Risques de biais

1. **Biais du concepteur** : son expertise technique et son contexte ne représentent pas l'ensemble des utilisateurs.
2. **Biais des responsables** : leur vision du portefeuille peut différer de celle des contributeurs.
3. **Biais de fréquence** : un utilisateur occasionnel peut avoir plus besoin d'une interface explicite qu'un utilisateur quotidien.
4. **Biais d'automatisation** : une fonctionnalité IA peut masquer un problème de qualité de la source.
5. **Biais de décision** : être administrateur n'accorde aucune compétence métier statutaire.
6. **Biais de disponibilité** : l'intention de participer n'est pas un accord d'organisation.

Les recherches doivent inclure des personnes autres que le porteur initial et privilégier des situations concrètes plutôt que des avis abstraits.

## 7. Protocole de validation proposé

Pour chaque persona candidat :
1. obtenir une participation volontaire et une autorisation appropriée ;
2. réaliser un entretien structuré (environ 35 à 45 minutes, durée indicative) ;
3. demander un exemple récent de travail, de blocage ou de transmission ;
4. observer le processus actuel avec des données de démonstration ou autorisées ;
5. tester une maquette ou un parcours E0 ;
6. enregistrer des constats anonymisés, sans publier de verbatim nominatif ;
7. qualifier l'hypothèse : confirmée, infirmée ou insuffisamment documentée.

**Mesures candidates** : temps pour retrouver une action, taux de reprise autonome, erreurs de permission, étapes inutiles, satisfaction contextualisée, besoin réel de double saisie. Seuls des tests permettront de choisir des seuils.

## 8. Hypothèses et décisions ouvertes

- Qui sont les utilisateurs prioritaires du premier MVP ? `PH-OPEN-007`.
- Comment distinguer responsables, relais et personnes autorisées ? `PH-OPEN-002`.
- Quel parcours démontre une reprise réelle ? `PH-OPEN-024`.
- Quelles validations organisationnelles sont nécessaires ? `PH-OPEN-009`.
- Quel rôle pour les identités techniques et agents IA ? `PH-OPEN-028`.

**Liens :** [vision](../01-product/00-product-vision.md), [contexte](../00-context/02-canonical-context.md), [besoins transversaux](03-cross-organization-needs.md), [workflows](04-current-vs-target-workflows.md).
