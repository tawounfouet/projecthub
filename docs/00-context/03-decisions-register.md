---
id: PH-CTX-DEC-001
title: "ProjectHub - Registre public des décisions et orientations"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-001, PH-CNV-004, PH-GH-001]
related_documents:
  - "docs/00-context/01-source-register.md"
  - "docs/00-context/04-open-questions.md"
---

# ProjectHub - Registre public des décisions

> **Registre de travail, non procès-verbal d'approbation.** Les entrées `PH-DEC-001` à `PH-DEC-018` correspondent aux décisions, orientations et actions enregistrées dans le registre de Discovery. Un ID ou l'expression « décision » ne suffit pas à prouver qu'un choix technique ou commercial est définitivement arrêté.

## 1. Sémantique des statuts

| Statut | Portée |
|---|---|
| `EXECUTED-VERIFIED` | Action observable réalisée ; ne prouve pas que le produit fonctionne |
| `CONFIRMED-PROCESS` | Méthode de travail explicitement adoptée |
| `CONFIRMED-INTENT` | Ambition exprimée, sans décision détaillée |
| `REFERENCE-TARGET` | Cible de conception demandée, encore à modéliser |
| `PROPOSED` | Recommandation non approuvée |
| `OPEN` | Arbitrage toujours nécessaire |

Les engagements opérationnels d'organisations tierces **ne font pas partie de ce registre public**.

## 2. Registre des 18 orientations de référence

| ID | Sujet publiable | Statut retenu | Ce qui n'est pas démontré / décidé |
|---|---|---|---|
| `PH-DEC-001` | Développer une plateforme de gestion de projet interopérable | `CONFIRMED-INTENT` | Étendue exacte des vues et intégrations |
| `PH-DEC-002` | Django/DRF et React/Next.js comme orientation | `REFERENCE-TARGET` | Versions, auth, UI et ADR techniques |
| `PH-DEC-003` | Préserver 13 domaines métier cibles | `REFERENCE-TARGET` | Implémentation de chaque domaine au MVP |
| `PH-DEC-004` | Distinguer Organization, Workspace, Team et Project | `REFERENCE-TARGET` | Permissions et cardinalités détaillées |
| `PH-DEC-005` | Projet d'ingénierie avec pratiques reproductibles | `CONFIRMED-INTENT` | CI, tests et déploiement actuellement opérationnels |
| `PH-DEC-006` | Étudier un usage interne réel | `CONFIRMED-INTENT` | Adoption effective par une équipe |
| `PH-DEC-007` | Viser une distribution open source et un SaaS commercial | `CONFIRMED-INTENT` | Licence, pricing et modèle économique |
| `PH-DEC-008` | Explorer un programme pilote multi-contextes | `CONFIRMED-INTENT` | Accords institutionnels et disponibilité |
| `PH-DEC-009` | Prioriser un cas métier de coordination et continuité | `CONFIRMED-INTENT` | Satisfaction et adoption démontrées |
| `PH-DEC-010` | Analyser les sources et conversations avant de figer les besoins | `CONFIRMED-PROCESS` | Exhaustivité de l'historique |
| `PH-DEC-011` | Construire une Discovery Baseline V1.0 | `CONFIRMED-PROCESS` | Approbation de la baseline |
| `PH-DEC-012` | Utiliser sept dossiers et 25 documents cibles | `CONFIRMED-PROCESS` | Validation métier de chaque document |
| `PH-DEC-013` | Deux éditions documentaires, privée et publique | `CONFIRMED-PROCESS` | Autorisation implicite de publier une source tierce |
| `PH-DEC-014` | Utiliser le dépôt public ProjectHub | `EXECUTED-VERIFIED` | Licence ou produit installable |
| `PH-DEC-015` | Initialiser le dépôt avec la documentation publique | `EXECUTED-VERIFIED` | MVP en production |
| `PH-DEC-016` | Préparer d'abord un contexte détaillé non public | `EXECUTED-VERIFIED` (pour le document privé) | Droit de redistribuer les sources internes |
| `PH-DEC-017` | Consolider les arbitrages avant de préciser l'architecture | `CONFIRMED-PROCESS` | Arbitrages effectivement rendus |
| `PH-DEC-018` | Utiliser Markdown comme mémoire structurée pour humains et agents | `CONFIRMED-INTENT` | Automatisation ou intégration IA implémentée |

**Provenance :** `PH-CNV-001`, `PH-CNV-004` et, pour les faits GitHub, `PH-GH-001` (voir [source register](01-source-register.md)). Les catégories du tableau reflètent la **nature du choix**, pas un vote d'un comité produit.

## 3. Orientations de travail proposées, non validées

| Sujet | Proposition | Statut et dépendance |
|---|---|---|
| Premier parcours utile | Qualifier -> responsabiliser -> suivre -> documenter -> transmettre -> exporter | `PROPOSED` ; tester avec utilisateurs |
| Frontière des données | Organization comme tenant ; Workspaces subordonnés | `REFERENCE-TARGET` pour la distinction, règles exactes ouvertes |
| Modèle de réalisation | Monolithe Django modulaire + API DRF + frontend Next.js | `PROPOSED` ; ADR et prototypes nécessaires |
| Ownership des décisions et risques | `governance` comme propriétaire, `workitems` pour actions | `PROPOSED` ; `PH-OPEN-003` |
| Intégrations | Commencer par les références externes plutôt que synchronisation avancée | `PROPOSED` ; `PH-OPEN-004` |
| Distribution | Cœur commun, Community auto-hébergeable, Cloud managé | `PROPOSED` ; licence, IP et exploitation à définir |
| Priorité sécurité | Tester l'isolation avant données réelles | Principe de sûreté, critères détaillés à approuver |
| Publication | Branche par lot et PR avec relecture humaine | Politique disponible, chaque fusion reste à autoriser |

Ce tableau ne crée pas de nouveaux `PH-DEC`. Un changement de statut nécessite une décision explicite et une preuve conservée.

## 4. Journal des décisions du dépôt public

| Preuve | Action observable |
|---|---|
| [`fb7a000`](https://github.com/tawounfouet/projecthub/commit/fb7a000d7b71b721817e0e768180024994e08025) | Création du premier README |
| [`85c1a59`](https://github.com/tawounfouet/projecthub/commit/85c1a59a1483048f02578c87c58801d9bab96181) | Dossiers, modèles d'issues, premiers documents |
| [`5f45729`](https://github.com/tawounfouet/projecthub/commit/5f45729f19a26e7018556e4f4aa432bb2ecb85c2) | Politique publique de publication et index |

Le lot PUBLIC-01 est préparé **en proposition de pull request**. Une PR ouverte ne constitue pas une fusion ni une approbation du contenu.

## 5. Comment approuver une nouvelle décision

Une décision future doit déclarer :
1. le problème et ses options envisagées ;
2. l'autorité qui décide et la date ;
3. la décision exacte, sa portée et sa justification ;
4. ses conséquences, ses risques et ses tests ;
5. les sources consultables et les sujets restant ouverts ;
6. l'ADR associé si la décision est architecturale.

Ne jamais transformer silencieusement un `PH-OPEN-*` en décision approuvée. Publier uniquement une version neutre des décisions impliquant des tiers.

**Liens :** [questions ouvertes](04-open-questions.md) - [contexte canonique](02-canonical-context.md) - [politique de publication](../PUBLICATION-POLICY.md).
