---
id: PH-REQ-TRACE-001
title: "ProjectHub - Traçabilité publique des besoins et exigences"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Requirements Engineering - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/02-discovery/03-cross-organization-needs.md"
  - "docs/02-discovery/04-current-vs-target-workflows.md"
  - "docs/03-requirements/00-functional-requirements.md"
  - "docs/03-requirements/01-non-functional-requirements.md"
  - "docs/03-requirements/02-business-rules-and-permissions.md"
---

# ProjectHub - Traçabilité des besoins, exigences et preuves

> **Édition publique expurgée - draft.** La matrice interne vérifie une chaîne documentaire, pas une validation métier ou technique. Les références individuelles aux constats opérationnels, fichiers internes et identifiants d'organisations sont volontairement exclues de la version publique.

## 1. Chaîne de traçabilité

```text
Catégorie de source autorisée
  -> besoin normalisé PH-XNEED
  -> exigence fonctionnelle PH-REQ / qualité PH-NFR
  -> règle PH-BR / workflow PH-WF
  -> capacité de périmètre PH-SCP
  -> scénario d'acceptation
  -> backlog candidat
  -> preuve de test réellement exécuté
```

**Ne pas confondre :**
- existence d'un ID = **couverture documentaire** ;
- exigence candidate = **proposition à valider** ;
- ticket de backlog = **intention d'implémentation** ;
- preuve de test = **résultat observé** ;
- accord pilote = **autorisation institutionnelle distincte**.

## 2. Résultats de couverture documentaire

| Catalogue public ou source de travail | Quantité | Interprétation |
|---|---:|---|
| Familles normalisées `PH-XNEED-001..029` | 29 | Besoins synthétisés sur plusieurs contextes |
| Workflows candidats `PH-WF-C01..C10`, `DA01..DA10`, `WEB01..WEB12` | 32 | Parcours illustratifs, pas résultats de terrain |
| Exigences fonctionnelles `PH-REQ-001..130` | 130 | Catalogue candidat, 13 domaines |
| NFR `PH-NFR-001..113` | 113 | 12 familles de qualité |
| Règles `PH-BR-001..111` | 111 | Permissions et invariants candidats |
| Termes `PH-TERM-001..145` | 145 | Vocabulaire partagé à valider |
| Capacités `PH-SCP-001..025` | 25 | Scope candidat |
| Agrégats `PH-DM-AGG-001..020` | 20 | Modèle conceptuel |
| Contrats `PH-BC-001..032` | 32 | Interactions inter-domaines proposées |

Ces totaux concernent le **corpus de conception**, et non des exigences validées ou implémentées. Plusieurs éléments se recoupent, donc leurs chiffres ne sont pas additionnables.

## 3. Couverture par familles de besoins

La matrice ci-dessous reprend **les nombres de liens explicites aux exigences fonctionnelles et workflows** calculés dans le registre privé. Les colonnes individuelles des sources internes sont exclues. Les comptages peuvent se chevaucher.

| Famille | Sujet générique | FR liés | WF liés | Statut |
|---|---|---:|---:|---|
| `PH-XNEED-001` | Accès et contexte organisationnel | 21 | 2 | À valider |
| `PH-XNEED-002` | Inventaire des projets et états | 5 | 4 | À valider |
| `PH-XNEED-003` | Responsables et relais | 5 | 3 | À valider |
| `PH-XNEED-004` | Objectifs, livrables, acceptation | 8 | 5 | À valider |
| `PH-XNEED-005` | Actions, priorité et échéances | 9 | 5 | À valider |
| `PH-XNEED-006` | Blocages et arbitrages | 5 | 3 | À valider |
| `PH-XNEED-007` | Historique et provenance | 8 | 4 | À valider |
| `PH-XNEED-008` | Références et documents | 6 | 3 | À valider |
| `PH-XNEED-009` | Vues et indicateurs | 15 | 3 | À valider |
| `PH-XNEED-010` | Export et sortie | 2 | 1 | À valider |
| `PH-XNEED-011` | Décisions et risques | 4 | 2 | À valider |
| `PH-XNEED-012` | Dépôts Git et références externes | 5 | 2 | À valider |
| `PH-XNEED-013` | Échéances critiques | 5 | 1 | À valider |
| `PH-XNEED-014` | Versions et releases | 4 | 2 | À valider |
| `PH-XNEED-015` | Onboarding | 3 | 1 | À valider |
| `PH-XNEED-016` | Transmission et autonomie | 5 | 5 | À valider |
| `PH-XNEED-017` | Dépendances et impacts | 3 | 0 | À valider |
| `PH-XNEED-018` | Fiabilité des statuts | 16 | 5 | À valider |
| `PH-XNEED-019` | Accessibilité | 1 | 1 | À valider |
| `PH-XNEED-020` | Collaboration asynchrone | 2 | 0 | À valider |
| `PH-XNEED-021` | Référentiels spécialisés | 1 | 2 | À valider |
| `PH-XNEED-022` | IA et services techniques | 7 | 2 | À valider |
| `PH-XNEED-023` | Environnements | 2 | 1 | À valider |
| `PH-XNEED-024` | Correctifs et incidents | 3 | 2 | À valider |
| `PH-XNEED-025` | Packages partagés | 1 | 1 | À valider |
| `PH-XNEED-026` | Intégrations et jobs | 2 | 1 | À valider |
| `PH-XNEED-027` | Exploration et R&D | 4 | 1 | À valider |
| `PH-XNEED-028` | Import contrôlé | 2 | 2 | À valider |
| `PH-XNEED-029` | Client distinct du tenant | 11 | 3 | À valider |

**Lecture :** `0 WF lié` indique l'absence d'un lien explicite dans le registre, et non l'inutilité d'un scénario. Les totaux des colonnes ne représentent pas des objets distincts car les liens sont plusieurs-à-plusieurs.

## 4. Exemples concrets de chaînes publiques

| Besoin normalisé | Exigence liée dans le registre source | Scope | Critère candidat |
|---|---|---|---|
| `PH-XNEED-001` - Isolation | `PH-REQ-001` - contexte autorisé | `PH-SCP-001` | Rejeter une opération sans tenant valide |
| `PH-XNEED-001` - Collaboration sûre | `PH-REQ-010` - invitation contrôlée | `PH-SCP-003/004` | Invitation sans accès étranger |
| `PH-XNEED-002` - Projet suivi | `PH-REQ-038` - fiche Project | `PH-SCP-005` | Fiche dans le bon Workspace |
| `PH-XNEED-003` - Responsable | `PH-REQ-040` - ProjectLead | `PH-SCP-005/006` | Changement de responsable historisé |
| `PH-XNEED-005` - Travail | `PH-REQ-050` - WorkItem | `PH-SCP-007/008` | Action visible uniquement au bon projet |
| `PH-XNEED-006` - Blocage | `PH-REQ-055` - motif / prochaine action | `PH-SCP-008` | Blocage compris et suivi |
| `PH-XNEED-008` - Documents | `PH-REQ-080` - référence externe | `PH-SCP-010` | Aucun transfert de droit du système source |
| `PH-XNEED-016` - Passation | `PH-REQ-082` - dossier de reprise | `PH-SCP-012` | Repreneur consulte actions et lacunes |
| `PH-XNEED-001` - Mandat | `PH-REQ-094` - refus d'approbation | `PH-SCP-001` | Un contributeur ne valide pas sans mandat |
| `PH-XNEED-012` - Dépôt | `PH-REQ-104` - lien GitHub | `PH-SCP-018` | Référence sans synchronisation |
| `PH-XNEED-009` - Synthèse | `PH-REQ-123` - reporting | `PH-SCP-009` | Totaux limités au scope et date annoncée |

Ces correspondances sont issues des fiches candidates. Les tests restent à créer puis à exécuter.

## 5. Une fiche de preuve par test

```yaml
requirement_id: PH-REQ-001
scenario_id: DEMO-AUTH-001
environment: "à renseigner"
commit_sha: "à renseigner"
data_classification: synthetic
actor_role: "à renseigner"
expected_result: "refus inter-tenant"
observed_result: null
evidence_location: null
executed_at: null
approved_by: null
status: not-run
```

La valeur `null` est intentionnelle : **aucune preuve n'est encore enregistrée**.

## 6. Gouvernance des liens

1. Un ID existant n'est pas réutilisé pour un autre besoin.
2. Toute nouvelle exigence référence au moins une motivation et un critère vérifiable.
3. Une décision modifiant le scope déclenche une revue des FR, NFR, BR, termes, contrats et scénarios touchés.
4. Les corrections d'une synthèse ne réécrivent pas les pièces sources privées.
5. Toute donnée ou référence vers un tiers doit respecter la politique de publication.
6. Une revue formelle doit distinguer couverture des IDs, approbation métier et preuves de tests.
7. Le propriétaire d'un document ou d'un ticket n'est pas automatiquement habilité à approuver une action dans une Organization.

## 7. Réserves majeures

La Discovery est **rédigée mais non formellement approuvée**. Les entretiens, le périmètre MVP final, le modèle RBAC, les décisions de Domain Ownership et les contrôles des pilotes E1 restent ouverts. Les documents publics sont des **éditions de travail**, distinctes des sources confidentielles.

Voir [besoins transversaux](../02-discovery/03-cross-organization-needs.md), [FR](00-functional-requirements.md), [NFR](01-non-functional-requirements.md), [BR](02-business-rules-and-permissions.md) et [glossaire](../04-domain/00-ubiquitous-language.md).
