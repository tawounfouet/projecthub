---
id: PH-CTX-SRC-001
title: "ProjectHub - Registre public des sources"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-18"
updated_at: "2026-11-20"
baseline: "ProjectHub Discovery Baseline V1.0"
related_documents:
  - "docs/00-context/00-project-history.md"
  - "docs/00-context/02-canonical-context.md"
  - "docs/PUBLICATION-POLICY.md"
---

# ProjectHub - Registre public des sources

> **Édition publique expurgée.** Ce registre décrit des classes de sources et leur niveau de preuve. Il ne publie ni comptes rendus internes, ni chemins locaux, ni données personnelles, ni constats de sécurité spécifiques. Une source privée mentionnée ici n'est ni accessible au public ni autorisée à être reproduite.

## 1. Règles de preuve

| Marqueur | Interprétation |
|---|---|
| `DIRECT` | Fait constatable directement, par exemple un commit GitHub ou une déclaration explicite |
| `EXCERPT` | Extrait ou résumé d'un échange ancien, sans transcription intégrale |
| `PRIVATE-REVIEWED` | Document métier examiné dans un espace privé, non redistribuable |
| `DERIVED` | Synthèse secondaire, utile à la compréhension mais pas preuve indépendante |
| `PROPOSAL` | Analyse ou recommandation, non adoptée |
| `PENDING` | Pièce ou validation manquante |

**Important :** un fichier rédigé ne prouve pas qu'une exigence est validée, qu'une fonctionnalité existe ou qu'une action historique reste ouverte à la date du jour.

## 2. Sources publiques ou publiquement référencées

| ID | Date / période | Catégorie | Accès | Apport et limite |
|---|---|---|---|---|
| `PH-CNV-001` | 2026-06-30 | Idéation ProjectHub, GitHub Projects et CLI | `EXCERPT` | Intentions initiales ; transcript complet à récupérer |
| `PH-CNV-002` | 2026-09-11 | Présentation générale du projet | `EXCERPT` | Narration produit initiale |
| `PH-CNV-003` | 2026-09-11 | Présentation du produit en huit axes | `EXCERPT` | Vision, problème, solution, architecture, utilisateurs, fonctions, roadmap, valeur |
| `PH-CNV-004` | Novembre 2026 | Échanges de conception ProjectHub | `DIRECT` pour les intentions exprimées | Stratégie, organisation, Discovery et publication ; conversation non ouverte au public |
| `PH-GH-001` | Novembre 2026 | [Dépôt GitHub ProjectHub](https://github.com/tawounfouet/projecthub) | `DIRECT` | Faits de dépôt, branche et commits ; ne prouve aucune fonctionnalité livrée |
| `PH-OPS-001` | 2026 | Source privée de coordination associative | `PRIVATE-REVIEWED` | Suivi, responsabilités, transmission ; aucune donnée source publiée |
| `PH-OPS-002` | 2026 | Sources privées de portefeuille technique | `PRIVATE-REVIEWED` | Coordination multi-projets, maintenance, documentation |
| `PH-OPS-003` | 2026 | Inventaire privé d'un écosystème technique | `PRIVATE-REVIEWED` | Distinction entre projets, dépôts, composants et infrastructure |
| `PH-DER-001` | 2026-11 | Synthèse stratégique interne | `DERIVED` | Orientation produit, non preuve primaire |
| `PH-DER-002` | 2026-11 | Audit historique interne | `DERIVED` | Contrôle des sources et lacunes |
| `PH-DER-003` | 2026-11 | Contexte canonique interne | `DERIVED` | Consolidation privée, non publiable telle quelle |

Les identifiants `PH-OPS-*` sont des **références publiques génériques**. Ils ne permettent pas de reconstruire les pièces d'origine ni d'en déduire les autorisations de diffusion.

## 3. Provenance des principales affirmations

| Affirmation publique | Références | Statut |
|---|---|---|
| Vision d'une plateforme interopérable de suivi de projets et de travail | `PH-CNV-001`, `PH-CNV-004` | Intention |
| Orientation Django/DRF + React/Next.js | `PH-CNV-001`, `PH-CNV-004` | Cible technique, non ADR |
| Cartographie de 13 domaines fonctionnels | `PH-CNV-001`, `PH-CNV-004` | Cible, non implémentation |
| Distinction Organization / Workspace / Team / Project | `PH-CNV-004` | Contrainte conceptuelle de conception |
| Ambition Community + Cloud | `PH-CNV-004` | Intention commerciale, sans licence ou prix approuvés |
| Pilotage, traçabilité, continuité comme problèmes candidats | `PH-OPS-001`, `PH-OPS-002` | Observations privées généralisées, validation utilisateur en attente |
| Existence du dépôt public et du socle documentaire | `PH-GH-001` | Vérifiable par commits |
| Deux éditions documentaires avec revue avant fusion | `PH-CNV-004`, `PH-GH-001` | Processus formalisé, voir la politique |

## 4. Lacunes connues

| ID | Manque | Traitement prévu |
|---|---|---|
| `PH-GAP-001` | Transcriptions complètes des échanges initiaux | Intégrer au registre privé après récupération |
| `PH-GAP-002` | Entretiens métier et accord sur les besoins | Conduire les validations avec participants habilités |
| `PH-GAP-003` | Actualisation des constats historiques | Vérifier dans les espaces autorisés, sans publier le détail |
| `PH-GAP-004` | Choix final MVP, licence, gouvernance SaaS | Formaliser les décisions avec preuve et responsable |
| `PH-GAP-005` | Autorisations de diffusion de sources tierces | Demander avant toute citation ou cas nominatif |
| `PH-GAP-006` | Test fonctionnel, sécurité et exploitation de ProjectHub | Développer puis tester ; aucun résultat ne peut être anticipé |

## 5. Politique d'ajout d'une source

1. Enregistrer dans le **registre privé** sa provenance complète, sa date, sa classification, son autorité et ses éventuelles restrictions.
2. Définir si une description générique suffit dans le registre public.
3. Conserver un identifiant stable sans divulguer le contenu, les personnes, les chemins ou les caractéristiques techniques sensibles.
4. Relier toute affirmation produit à un niveau de preuve (`DIRECT`, `EXCERPT`, `DERIVED` ou `PROPOSAL`).
5. Soumettre toute source nouvelle au processus [PUBLICATION-POLICY.md](../PUBLICATION-POLICY.md).
6. Mettre à jour les lacunes et la date de revue ; ne jamais transformer silencieusement une proposition en décision.

## 6. Lecture du registre

La source privée complète n'est pas nécessaire pour comprendre la documentation publique. Les besoins et exemples diffusés doivent être **génériques, synthétiques ou autorisés**.

- [Historique](00-project-history.md)
- [Contexte canonique](02-canonical-context.md)
- [Vision produit](../01-product/00-product-vision.md)
