---
id: PH-PROD-SCP-001
title: "ProjectHub - Périmètre produit public"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-001, PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/01-product/00-product-vision.md"
  - "docs/01-product/01-product-strategy.md"
  - "docs/00-context/04-open-questions.md"
---

# ProjectHub - Périmètre produit

> **Frontière candidate - non approuvée.** Ce document distingue le produit cible, le premier MVP démontrable, les préconditions d'un pilote réel et les extensions reportées. Il ne signifie pas que les fonctionnalités sont développées.

## 1. Définition positive et non-objectifs

ProjectHub vise une couche de **pilotage des projets et responsabilités**, reliant les engagements, les actions, les informations de suivi, les décisions et le contexte nécessaire à la transmission.

Il n'a pas vocation à remplacer les outils spécialisés de gestion des dépôts Git, de stockage documentaire, de communication, de comptabilité, de CRM ou d'orchestration de workflows.

**Principe d'intégration :** référencer les ressources externes, préserver leur propriétaire et n'étendre l'interopérabilité qu'avec des cas validés. Une référence vers une ressource externe ne transfère ni sa propriété ni ses permissions à ProjectHub.

## 2. Quatre niveaux à distinguer

1. **Vision de long terme** : les 13 domaines fonctionnels cibles et les fonctionnalités évolutives.
2. **MVP candidat** : le parcours transversal minimal et ses fonctions de soutien.
3. **E0 démontrable** : implémentation testable sur données fictives, sans accord de pilote réel.
4. **E1 pilotable** : usage de données réelles uniquement après accords, sécurité, opérations, réversibilité et contrôles.

Une fonctionnalité présente dans la **vision** n'est pas nécessairement incluse dans le **MVP**, et une fonction du MVP ne sera considérée comme **livrée** qu'après tests et preuve.

## 3. Modèle et domaines cibles

```text
Organization (frontière de données candidate)
  └── Workspace (collaboration)
        └── Project (objectif, livrables, responsabilité)
              └── WorkItem (travail et suivi)
```

Les Teams, permissions, objectifs, décisions, risques, documents, périodes de planning et ressources externes sont des préoccupations transversales selon leurs propriétaires canoniques.

| Domaine cible | Responsabilité candidate |
|---|---|
| `core` | Invariants et services techniques communs |
| `identity` | Utilisateurs, équipes, affiliations et autorisations |
| `organizations` | Organizations, Workspaces et structure |
| `portfolios` | Portfolios, programmes, thèmes stratégiques |
| `projects` | Projects, objectifs et livrables |
| `workitems` | Travail, affectations, suivi |
| `planning` | Jalons, releases, itérations |
| `views` | Table, Board, Roadmap, Calendar |
| `collaboration` | Commentaires, activité et documents de référence |
| `governance` | Décisions, risques, changements et validations |
| `integrations` | Connecteurs et ressources externes |
| `automation` | Règles et déclencheurs |
| `reporting` | Indicateurs et santé des projets |

**Attention :** 13 domaines cibles ne signifie pas 13 modules complets au MVP. La propriété des décisions et risques entre `workitems` et `governance` fait encore partie des décisions ouvertes (`PH-OPEN-003`).

## 4. Catalogue de périmètre PH-SCP

Les IDs `PH-SCP-001` à `PH-SCP-025` correspondent aux capacités candidates du document de scope privé. Les priorités publiques sont conservées **comme propositions**, pas comme engagements.

| ID | Capacité candidate | Priorité de travail | Limite du premier incrément |
|---|---|---|---|
| `PH-SCP-001` | Accès sécurisé et séparation des organisations | P0-C | Pas de SSO Enterprise |
| `PH-SCP-002` | Organizations et Workspaces | P0-C | Pas de structure organisationnelle avancée |
| `PH-SCP-003` | Gestion de membres et invitations | P0-C | Pas de fédération d'identité |
| `PH-SCP-004` | Rôles de base | P0-C | Pas de moteur RBAC arbitrairement personnalisable |
| `PH-SCP-005` | Créer et actualiser un Project | P0-C | Pas de templates métier complexes |
| `PH-SCP-006` | Responsable principal et relais | P0-C | Pas de matrice RACI complète |
| `PH-SCP-007` | WorkItems simples | P0-C | Pas de taxonomie universelle |
| `PH-SCP-008` | États, priorités, échéances et assignations | P0-C | Pas d'automatisation générale des transitions |
| `PH-SCP-009` | Vue Table ou Board | P0-C | Pas de toutes les vues simultanément |
| `PH-SCP-010` | Références documentaires externes | P0-C | Pas de GED complète |
| `PH-SCP-011` | Historique pertinent | P0-C | Pas d'event sourcing imposé |
| `PH-SCP-012` | Passation simple de Project | P0-C | Pas de transfert d'accès aux systèmes tiers |
| `PH-SCP-013` | Export minimal autorisé | P0-C | Pas de migration universelle |
| `PH-SCP-014` | Milestones simples | P1-C | Pas de Gantt et planification avancés |
| `PH-SCP-015` | Commentaires et notes de suivi | P1-C | Pas de messagerie temps réel |
| `PH-SCP-016` | Décisions et risques simples | P1-C / OPEN | Ownership à arbitrer |
| `PH-SCP-017` | Vue synthétique et indicateurs | P1-C | Pas de BI prédictive |
| `PH-SCP-018` | Référence à un dépôt Git | P1-C | Pas de synchronisation PR/issues |
| `PH-SCP-019` | Recherche et navigation interprojets | P1-C | Pas de recherche documentaire globale |
| `PH-SCP-020` | Catalogue d'actifs techniques | P2-C | Pas de CMDB générale |
| `PH-SCP-021` | Import Markdown/CSV | P1-C / OPEN | Pas d'import de données non contrôlées |
| `PH-SCP-022` | Synchronisation GitHub avancée | P2-C | Pas de sync automatique au MVP |
| `PH-SCP-023` | Automatisations et triggers | P2-C | Pas de moteur généraliste |
| `PH-SCP-024` | Agent IA de connaissance | P2-C | Pas d'accès implicite à un corpus privé |
| `PH-SCP-025` | Facturation SaaS | Hors MVP | Conditionnée à un produit Cloud futur |

**P0-C** = candidat cœur du MVP ; **P1-C** = évolution à évaluer ; **P2-C** = extension future ; **OPEN** = arbitrage nécessaire.

## 5. Parcours vertical du MVP

```text
Un membre habilité entre dans une Organization / Workspace
  -> qualifie un Project et un responsable
  -> suit des WorkItems, échéances et blocages
  -> consulte des références et un historique utile
  -> réattribue et transmet un Project
  -> vérifie la compréhension de la personne repreneuse
  -> exporte les données accessibles de son périmètre
```

Le parcours doit pouvoir être testé **sans outil propriétaire obligatoire**, avec deux organisations fictives distinctes et des droits différents pour les tests négatifs.

## 6. Préconditions qualité et exploitation

Pour E0 :
- authentification et permissions de base testées ;
- isolation entre organisations vérifiée ;
- parcours principaux fonctionnels sur données fictives ;
- export limité au périmètre autorisé ;
- erreurs, états et historiques compréhensibles.

Pour E1, il faut **en plus**, avant toute donnée réelle :
- autorisation institutionnelle et cadre de traitement des données ;
- contrôle d'accès et isolation côté serveur, avec tests négatifs ;
- protection des secrets et environnement exploité de manière sûre ;
- sauvegarde ET restauration démontrée ;
- journalisation, surveillance, support et procédure d'incident ;
- export, rétention, suppression et plan de sortie ;
- accessibilité des parcours essentiels ;
- contrôle des changements et procédure de retour arrière.

Ce sont des conditions à prouver, et non des certifications ou garanties déjà obtenues.

## 7. Exclusions volontaires

Ne font pas partie du premier noyau :
- remplacer la gestion du code, les revues Git ou la CI/CD ;
- stocker automatiquement toutes les archives et documents d'une organisation ;
- migrer ou synchroniser à l'aveugle les outils existants ;
- réaliser une suite ERP/CRM/finance complète ;
- lancer un orchestrateur universel ou un agent IA autonome ;
- facturer un abonnement, gérer des SLA Enterprise ou annoncer une disponibilité commerciale ;
- développer toute la cartographie des 13 domaines avant de tester la valeur ;
- traiter les accords pilotes ou les passations réelles comme accomplis du seul fait qu'une interface les représente.

## 8. Maîtrise de la dérive de périmètre

Toute nouvelle fonctionnalité candidate doit répondre à cinq questions :
1. **Quel utilisateur et quel besoin source ?**
2. **Quel résultat observable et quel parcours d'acceptation ?**
3. **Quelle priorité par rapport au noyau ?**
4. **Quels droits, risques, dépendances et coûts d'exploitation ?**
5. **Quel arbitrage approuvé permet son entrée dans le lot ?**

Les demandes spécifiques à une organisation ne deviennent pas automatiquement des composants génériques. Les exceptions justifiées par la sécurité peuvent être requises avant tout pilote réel même si elles ne sont pas visibles à l'utilisateur.

## 9. Scénarios de validation

| Scénario | Résultat attendu |
|---|---|
| Suivi interprojets | Trouver le responsable, les actions et l'état courant |
| Passation | Une autre personne peut identifier et poursuivre le travail |
| Contexte technique | Relier un projet à ses ressources sans dupliquer le système maître |
| Contribution non technique | Comprendre et réaliser une tâche sans expertise de développeur |
| Isolation négative | Un utilisateur d'une autre Organization ne récupère aucune donnée non autorisée |
| Réversibilité | Une Organization peut exporter son périmètre autorisé |

Ces critères sont des **tests candidats non exécutés**. Ils soutiennent la discussion du MVP, pas son acceptation automatique.

## 10. État de la décision

Le catalogue fait l'objet d'une **proposition de scope V0.1.0**. Il doit être revu avec les utilisateurs, le Product Owner et l'ingénierie avant d'être traité comme un engagement de réalisation.

Références : [vision](00-product-vision.md), [stratégie](01-product-strategy.md), [questions ouvertes](../00-context/04-open-questions.md), [politique de publication](../PUBLICATION-POLICY.md).
