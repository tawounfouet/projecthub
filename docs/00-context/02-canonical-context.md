---
id: PH-CTX-CAN-001
title: "ProjectHub - Contexte canonique public"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-001, PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/00-context/00-project-history.md"
  - "docs/00-context/03-decisions-register.md"
  - "docs/01-product/00-product-vision.md"
---

# ProjectHub - Contexte canonique public

> **Document de référence pour contributeurs - draft, non approuvé formellement.** Il décrit le projet voulu et ses hypothèses, pas une application déjà livrée. Les études de terrain ayant inspiré la vision restent privées.

## 1. Résumé et mission candidate

**ProjectHub** est une initiative de plateforme de gestion de projets et du travail collectif. Elle cherche à relier **objectifs, projets, responsabilités, actions, décisions et mémoire opérationnelle** dans des organisations pouvant utiliser plusieurs outils spécialisés.

**Mission candidate :** aider des équipes à rendre leur travail visible, coordonné et transmissible, tout en conservant des frontières de données claires et la liberté d'utiliser leurs outils d'exécution existants.

Le problème exploré n'est pas seulement la création de tâches : il comprend la dispersion des informations, les changements d'équipe, le suivi des engagements et la difficulté à retrouver le contexte d'une décision.

Cette proposition de valeur n'est pas encore validée auprès d'un marché payant.

## 2. État réel du produit

| Sujet | État au 20 novembre 2026 |
|---|---|
| Dépôt GitHub | Public, initialisé |
| Corpus Discovery privé | 25 documents rédigés en version de travail |
| Approbation de la baseline | En attente, réserves et arbitrages ouverts |
| Architecture Django / Next.js | Orientation de conception, non implémentation démontrée |
| MVP applicatif | Candidat défini sur le papier ; pas de livraison annoncée |
| Pilotes réels | Hypothèses, pas d'accord institutionnel déclaré |
| Community open source | Ambition ; licence non arrêtée |
| SaaS Cloud | Ambition ; pas de service commercial annoncé |

Il faut distinguer **E0** (démonstration avec données fictives) et **E1** (usage pilote de données réelles soumis aux autorisations et contrôles). Cette séparation n'implique pas qu'E0 ou E1 sont déjà opérationnels.

## 3. Concepts fondamentaux

| Terme | Signification candidate | À ne pas confondre avec |
|---|---|---|
| `Organization` | Organisation utilisatrice et frontière d'isolation des données | Client d'une agence |
| `Workspace` | Espace de collaboration appartenant à une Organization | Team, dossier local |
| `Team` | Collectif de membres | Workspace |
| `Project` | Initiative ayant objectifs, responsables et livrables | Repository |
| `WorkItem` | Action ou unité de travail suivie | Décision formelle |
| `Membership` | Lien d'appartenance et d'habilitation dans un périmètre | Simple mention textuelle d'un rôle |
| `Decision` | Arbitrage métier et sa traçabilité | Action d'exécution |
| `Handover` | Processus de transmission et de reprise | Simple changement de nom d'un responsable |
| `Repository` | Dépôt externe ou technique lié à un projet | Projet métier |
| `ExternalResource` | Référence vers un système propriétaire de ses données | Copie automatique des données |

Un projet appartient conceptuellement à un Workspace, qui appartient à une Organization. Les règles d'appartenance, les exceptions et les permissions effectives sont à préciser dans l'architecture.

## 4. Cartographie des domaines cibles

```text
apps/
├── core           # base technique commune
├── identity       # identités, équipes, rôles
├── organizations  # organisations, workspaces
├── portfolios     # portfolios, programs, objectifs stratégiques
├── projects       # projets, objectifs, livrables
├── workitems      # unités de travail, exécution
├── planning       # milestones, releases, iterations
├── views          # table, board, roadmap, calendar
├── collaboration  # activité, commentaires, documents, transmission
├── governance     # décisions, risques, changements, validations
├── integrations   # GitHub, outils et ressources externes
├── automation     # règles, déclencheurs et actions
└── reporting      # indicateurs, rapports et santé projet
```

**13 domaines cibles ne signifie pas 13 modules à implémenter dans le MVP.** Les concepts `Decision` et `Risk` figurent historiquement dans `workitems` et `governance` ; leur propriété canonique reste ouverte.

## 5. Architecture et exigences de qualité envisagées

- Backend : Django + Django REST Framework ; frontend : React / Next.js / TypeScript.
- Persistance relationnelle envisagée : PostgreSQL.
- Monolithe modulaire comme **point de départ candidat**, à confirmer par ADR.
- Contrôle d'accès **côté serveur**, aucune confiance accordée à une restriction uniquement visible dans l'interface.
- Isolation des Organizations, y compris dans les requêtes, exports, tâches et intégrations.
- Tests automatiques, migrations reproductibles, journalisation appropriée, sauvegardes restaurables et documentation.
- Accessibilité des parcours principaux, export et portabilité.
- Pas de dépendance automatique aux packages internes d'une autre organisation.

Le choix exact des frameworks complémentaires, de l'hébergement et des détails de l'authentification n'est pas acté.

## 6. MVP candidat : parcours de valeur

```text
Qualifier un projet
  -> identifier un responsable et un relais
  -> suivre les WorkItems et blocages
  -> conserver des références et un historique
  -> transmettre le contexte à une autre personne
  -> exporter ses données autorisées
```

La proposition initiale comprend :
- contexte Organization / Workspace ;
- membres et permissions essentielles ;
- projets et tâches simples ;
- statuts, priorités, affectations, échéances ;
- vue Table ou Board, à confirmer ;
- liens vers documents externes sans stockage redondant systématique ;
- historique des changements utiles ;
- transmission et export.

Sont **différés dans le premier MVP candidat** : synchronisation GitHub avancée, agents IA autonomes, orchestrateur généraliste, catalogue d'infrastructure complet et facturation SaaS.

## 7. Stratégie de distribution envisagée

| Dimension | Finalité | Statut |
|---|---|---|
| Engineering | Qualité, tests, conventions, CI et architecture | Direction de travail |
| Internal | Validation d'usages réels | Objectif d'apprentissage |
| Community | Distribution installable et auto-hébergeable sous future licence | Projet, non disponible |
| Cloud | Service managé, maintenance et support | Projet, non disponible |
| Enterprise | Services ou conditions particulières | Hypothèse ultérieure |

Une version auto-hébergée utile et une offre Cloud managée sont des voies compatibles, sous réserve de propriété intellectuelle, financement et capacité opérationnelle.

## 8. État des validations et gouvernance

- Les personnes jouant un rôle d'éditeur de documents, de Product Owner et d'autorité d'approbation doivent être explicitement désignées.
- Les données issues de tiers ne peuvent être publiées ni utilisées dans des pilotes sans cadre approprié.
- Les tests de sécurité et de permissions doivent précéder toute utilisation de données réelles.
- Les choix controversés restent dans les [questions ouvertes](04-open-questions.md), sans décision implicite.

Les besoins de terrain reflètent **des environnements différents** ; la convergence observée ne signifie pas des processus identiques ni un accord de participation.

## 9. Source de vérité et documents liés

Le dépôt GitHub est la **source de vérité des éditions publiques sous statut `draft`** et de l'historique des publications. La présence d'un document dans `main` ne vaut pas approbation métier. Il ne contient pas les sources métier privées et ne remplace pas leur espace d'archivage.

Lire aussi :
- [Historique](00-project-history.md) et [registre des sources](01-source-register.md)
- [Registre des décisions](03-decisions-register.md)
- [Vision](../01-product/00-product-vision.md), [stratégie](../01-product/01-product-strategy.md) et [périmètre](../01-product/02-product-scope.md)
- [Politique de publication](../PUBLICATION-POLICY.md)

**Mise à jour :** le contexte canonique public doit refléter toute nouvelle décision officielle, sans effacer ses anciennes versions de l'historique Git.
