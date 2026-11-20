---
id: PH-CTX-HIST-001
title: "ProjectHub - Historique public du projet"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-18"
updated_at: "2026-11-20"
sources: [PH-CNV-001, PH-CNV-002, PH-CNV-003, PH-CNV-004, PH-GH-001]
related_documents:
  - "docs/00-context/01-source-register.md"
  - "docs/00-context/02-canonical-context.md"
---

# ProjectHub - Historique du projet

> **Édition publique expurgée - draft.** Ce document retrace des choix de conception, des intentions et quelques opérations vérifiables. Ce n'est ni un journal de déploiement, ni la preuve que le logiciel est déjà développé. Les échanges anciens ne sont disponibles qu'en extraits.

## 1. Évolution de la réflexion

| Période | Étape | État de preuve | Apport |
|---|---|---|---|
| 30 juin 2026 | Idéation d'une plateforme de gestion de projet avec backlog, labels, milestones, GitHub Projects, vues Table/Board/Roadmap et commandes CLI reproductibles | Extraits de discussion | Intention technique et fonctionnelle initiale |
| 11 septembre 2026 | Présentation structurée en huit axes : vision, problème, solution, architecture, utilisateurs, fonctionnalités, roadmap, valeur | Extraits de discussion | Passage à un discours de produit |
| Novembre 2026 | Examen des usages internes, de la diffusion open source et d'un SaaS managé | Intentions exprimées | Ambitions compatibles, modalités non décidées |
| Novembre 2026 | Analyse privée de besoins provenant d'organisations aux contextes différents | Sources privées, non publiées | Hypothèses de coordination, suivi et continuité |
| 18-20 novembre 2026 | Définition de Discovery Baseline V1.0 : 25 documents en sept sections | Processus documentaire | Formalisation des sources, besoins, exigences et MVP candidat |
| 18 novembre 2026 | Initialisation du dépôt public GitHub | Commits vérifiés | Première fondation documentaire, sans code applicatif |
| 20 novembre 2026 | Politique de publication publique/privée ajoutée | Commit vérifié | Cadre de confidentialité, de revue et de diffusion |
| 20 novembre 2026 | Préparation du lot PUBLIC-01 | Travail de publication en cours | Huit documents Context & Product proposés pour revue |

Les dates de l'apparition d'un **besoin chez une organisation** et de sa **prise en compte dans ProjectHub** sont distinctes. Les analyses de terrain ne doivent pas être présentées comme des versions déjà livrées de ProjectHub.

## 2. Les étapes de conception

### 2.1. De l'outil de projet à la plateforme de pilotage

L'idée initiale portait sur les notions classiques de projet, backlog, milestone et vue. Les réflexions ultérieures mettent davantage l'accent sur le lien entre objectifs, responsabilités, actions, décisions, contexte opérationnel et transmission.

### 2.2. De l'équipe technique à l'organisation

La plateforme doit prendre en compte des structures distinctes :
- `Organization` : périmètre propriétaire de données et frontière d'isolation candidate ;
- `Workspace` : espace de collaboration au sein d'une Organization ;
- `Team` : collectif de personnes, distinct d'un Workspace ;
- `Project` : initiative métier, distincte d'un dépôt technique ;
- `WorkItem` : unité de travail suivie.

Le détail des rôles, permissions et relations reste à arbitrer. Un répertoire informatique ou un client commercial n'est pas automatiquement un Workspace ou un tenant.

### 2.3. De la démonstration technique à la stratégie produit

Quatre trajectoires sont envisagées : **Engineering** (qualité de réalisation), **Internal** (usage réel), **Community** (distribution auto-hébergeable après choix d'une licence), et **Cloud** (SaaS managé si la viabilité est démontrée). Une proposition Enterprise pourrait suivre, sans être un objectif initial.

### 2.4. De la réflexion orale à la documentation vérifiable

Le chantier Discovery Baseline V1.0 s'organise en sept sections : Context, Product, Discovery, Requirements, Domain, MVP et Validation. Le corpus privé comprend 25 documents rédigés. **Rédigé ne signifie pas approuvé** : les entretiens, arbitrages et preuves d'utilisation restent nécessaires.

## 3. Architecture cible évoquée

L'orientation proposée est **Django / Django REST Framework**, **React / Next.js** et une persistance relationnelle telle que **PostgreSQL**, dans une architecture modulaire.

Les **13 domaines cibles** sont :
```text
core             identity         organizations    portfolios
projects         workitems        planning         views
collaboration    governance       integrations     automation
reporting
```

Ce découpage est une **carte métier cible**. Il n'impose ni 13 microservices ni 13 fonctionnalités complètes au MVP. Les frontières litigieuses, par exemple entre `workitems` et `governance`, ne sont pas arbitrées.

## 4. Faits vérifiables du dépôt

Dépôt : [tawounfouet/projecthub](https://github.com/tawounfouet/projecthub).

| Commit | Action |
|---|---|
| [`fb7a000`](https://github.com/tawounfouet/projecthub/commit/fb7a000d7b71b721817e0e768180024994e08025) | Initialisation de `README.md` |
| [`85c1a59`](https://github.com/tawounfouet/projecthub/commit/85c1a59a1483048f02578c87c58801d9bab96181) | Structure documentaire et premières sources publiques |
| [`5f45729`](https://github.com/tawounfouet/projecthub/commit/5f45729f19a26e7018556e4f4aa432bb2ecb85c2) | Politique de publication documentaire |

Ces commits n'attestent pas d'un MVP exécuté ni de la disponibilité d'un service Cloud.

## 5. Décisions encore ouvertes

- Périmètre définitif et ordre des parcours MVP.
- Règles RBAC, héritage des accès et conception multi-tenant.
- Modèle canonique des décisions, risques, passations et référentiels techniques.
- Première intégration externe et niveau de synchronisation.
- Licence, propriété intellectuelle, contributions et conditions de distribution.
- Marché payeur, tarifs, calendrier Cloud et capacité d'exploitation.
- Accord formel des organisations et critères de validation des pilotes.

Voir [décisions](03-decisions-register.md) et [questions ouvertes](04-open-questions.md).

## 6. Limites et maintenance

Les conversations du 30 juin et du 11 septembre ne sont pas encore archivées intégralement dans le corpus actuel. Les sources privées des organisations sont exploitées pour **des besoins candidats**, pas pour annoncer leur approbation ou divulguer leurs opérations.

Toute modification de l'histoire doit distinguer **date de l'événement**, **date d'observation**, **preuve**, **statut de la décision** et **autorité**. Le présent document peut évoluer sans réécrire rétroactivement l'historique.

**Documents associés :** [registre public des sources](01-source-register.md), [contexte canonique](02-canonical-context.md), [vision produit](../01-product/00-product-vision.md).
