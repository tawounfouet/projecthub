# Documentation publique de ProjectHub

Bienvenue dans la documentation de conception de **ProjectHub**, une plateforme de pilotage de projets et de travail collectif en phase de Discovery.

> **Statut : draft.** Les documents publics décrivent des intentions, hypothèses et exigences candidates. Ils ne prouvent ni logiciel opérationnel, ni validation utilisateur, ni approbation du MVP.

La [politique de publication documentaire](PUBLICATION-POLICY.md) définit le circuit de revue. Les sources privées et les comptes rendus internes ne sont **pas** publiés dans ce dépôt.

**Collaboration et contributions :** lire le [guide GitHub / GitLab / Azure DevOps](COLLABORATION-BEST-PRACTICES.md) pour les Issues, PR/MR, reviews, approbations, contrôles et travail avec des agents IA.

**Bilan post-publication :** consulter le [retour d'expérience sur Discovery Baseline V1.0](reports/2026-11-21-discovery-baseline-publication-bilan.md) pour le résultat, les preuves GitHub, les limites et les prochaines étapes.

**Exécution du lot P0 post-PR #12 :** voir le [bilan des correctifs, du run CI et des nominations en attente](reports/2026-11-21-p0-remediation-execution.md).

**Expérimentation P1 uniquement synthétique :** consulter le [runbook E0](../E0.md), le [rapport d'exécution](reports/2026-11-21-p1-e0-rls-execution.md), le [rapport GitGuardian](reports/2026-11-21-p1-secret-remediation.md) et le [dossier ADR-0019](07-architecture/03-adr-0019-rls-poc-decision.md). Les tests réussis dans la PR #15 ne constituent ni approbation des ADR ni GO E0.

## Discovery Baseline V1.0

| Section | Objet | État public |
|---|---|---|
| [00-context](00-context/) | Historique, sources, contexte, décisions, questions ouvertes | Cinq documents publics sur main, statut draft |
| [01-product](01-product/) | Vision, stratégie, périmètre | Trois documents publics sur main, statut draft |
| [02-discovery](02-discovery/) | Acteurs, besoins et processus | Cinq éditions publiques sur main, statut draft |
| [03-requirements](03-requirements/) | Exigences et règles | Quatre éditions publiques sur main, statut draft |
| [04-domain](04-domain/) | Vocabulaire et frontières métier | Trois éditions publiques sur main, statut draft |
| [05-mvp](05-mvp/) | Parcours et backlog | Trois éditions publiques sur main, statut draft |
| [06-validation](06-validation/) | Protocoles et revue de baseline | Deux éditions publiques sur main, statut draft |

**25 documents privés ont été rédigés en interne**, mais pas encore formellement approuvés et non publiables tels quels. Le présent dépôt contient **des éditions publiques réécrites**, dont la progression est indépendante du corpus privé.

## PUBLIC-01 - Context & Product

| Document | Description |
|---|---|
| [Historique](00-context/00-project-history.md) | Chronologie et provenance des choix |
| [Registre public des sources](00-context/01-source-register.md) | Niveaux de preuve, références génériques et lacunes |
| [Contexte canonique](00-context/02-canonical-context.md) | Synthèse réutilisable de la vision et des concepts |
| [Décisions et orientations](00-context/03-decisions-register.md) | 18 entrées de référence avec leurs statuts |
| [Questions ouvertes](00-context/04-open-questions.md) | 30 arbitrages candidats conservant leurs IDs |
| [Vision produit](01-product/00-product-vision.md) | Problèmes, utilisateurs et valeur attendue |
| [Stratégie produit](01-product/01-product-strategy.md) | Segments, apprentissage, Community et Cloud |
| [Périmètre produit](01-product/02-product-scope.md) | 25 capacités candidates et exclusions du MVP |

**PUBLIC-01 a été fusionné sur main.** Les documents gardent le statut métier `draft` : la fusion n'approuve ni le MVP ni les exigences.

## PUBLIC-02 - Product Discovery

| Document | Description |
|---|---|
| [Parties prenantes et personas](02-discovery/00-stakeholders-and-personas.md) | 13 personas candidats, acteurs et protocole d'étude |
| [Étude générique de coordination associative](02-discovery/01-diversite-alternative-needs.md) | Besoins et parcours associatifs abstraits, sans données d'organisation |
| [Étude générique de portefeuille technique](02-discovery/02-webtech-solutions-needs.md) | Pilotage multi-projets, maintenance et limites des outils spécialisés |
| [Besoins inter-organisations](02-discovery/03-cross-organization-needs.md) | 29 familles transversales, divergences et socle candidat |
| [Processus As-Is / To-Be](02-discovery/04-current-vs-target-workflows.md) | 32 parcours de référence généralisés et preuves attendues |

**Attention :** les deux documents dont le nom de fichier reflète l'index historique sont **des éditions publiques génériques**, pas des expressions de besoins officielles de ces organisations. Les sources et états internes restent privés, conformément à la [politique de publication](PUBLICATION-POLICY.md).

## PUBLIC-03 - Requirements & Domain

| Document | Contenu |
|---|---|
| [Exigences fonctionnelles](03-requirements/00-functional-requirements.md) | 130 FR candidates, 13 domaines, priorités et exemples vérifiables |
| [Exigences non fonctionnelles](03-requirements/01-non-functional-requirements.md) | 113 NFR candidates, douze familles de qualité et contrôles E0/E1 |
| [Règles métier et permissions](03-requirements/02-business-rules-and-permissions.md) | 111 règles, modèle RBAC candidat et scénarios de refus |
| [Matrice de traçabilité](03-requirements/03-requirements-traceability.md) | Liens génériques entre 29 familles de besoins, exigences et preuves |
| [Langage ubiquitaire](04-domain/00-ubiquitous-language.md) | Index de 145 termes et définitions publiques essentielles |
| [Modèle de domaine](04-domain/01-domain-model.md) | 20 agrégats, 30 relations, 20 commandes et 20 événements candidats |
| [Frontières et contrats](04-domain/02-domain-boundaries.md) | Treize domaines, propriété canonique et 32 contrats candidats |

**PUBLIC-03 est fusionné sur main.** Les sept éditions sont expurgées, condensées et restent en statut `draft` : leur publication ne valide ni les spécifications ni leur implémentation.

## PUBLIC-04 - MVP & Validation

| Document | Contenu |
|---|---|
| [Définition du MVP](05-mvp/00-mvp-definition.md) | Treize capacités candidates, sept slices, conditions E0/E1 |
| [Parcours utilisateurs](05-mvp/01-user-journeys.md) | Dix parcours `MVP-UJ-01..10` et critères de démonstration |
| [Backlog priorisé](05-mvp/02-prioritized-backlog.md) | Sept Epics, 45 items `PH-BLG-001..045` non créés en Issues |
| [Plan de validation](06-validation/00-pilot-validation-plan.md) | Huit expériences MVP et huit gates avant E1 |
| [Revue de baseline](06-validation/01-discovery-baseline-review.md) | 25 documents privés rédigés, 20 réserves et verdict de revue |

**PUBLIC-04 est fusionné sur main.** Les cinq éditions publiques de ce lot restent des propositions expurgées. Les 25 documents de Discovery sont **publiés**, mais **ni le périmètre MVP ni la baseline ne sont officiellement approuvés**. Aucune expérience E0 ou gate E1 n'est présentée comme réussie.

## Plans complémentaires après Discovery Baseline V1.0

La baseline Discovery historique reste composée de **25 documents**. Les documents ci-dessous sont des ajouts **postérieurs** pour préparer les validations produit et les arbitrages techniques. Un POC et des tests E0 synthétiques ont été intégrés sur `main` via la PR #15, avec preuves CI sur le commit de fusion `1095b7e`; ils ne constituent ni approbation d'ADR ni GO E0.

| Document | Objet | Statut |
|---|---|---|
| [Plan de recherche utilisateurs](02-discovery/05-priority-questions-and-user-research-plan.md) | `PH-OPEN-007`, `PH-OPEN-001`, `PH-OPEN-024`, rôles à désigner et entretiens | Draft public |
| [Plan ADR, tenancy et permissions avant E0](07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md) | `ADR-0004`, `ADR-0005`, `ADR-0019`, tests fictifs A/B | Draft public |
| [Architecture & Engineering Baseline V1.0 exhaustive](07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md) | Document source **intégral**, non expurgé, publication acceptée par `PH-DEC-019` | **Classification publique ; statut `DRAFT / PROPOSED - NOT APPROVED` inchangé** |
| [Plan de CI documentaire](07-architecture/01-documentation-quality-ci-plan.md) | Liens Markdown, frontmatter, continuité des IDs et workflow GitHub Actions | **Draft public - CI fusionnée sur `main` via la PR #14; run post-fusion réussi** |
| [Registre des autorités d'architecture pré-E0](07-architecture/02-architecture-authority-register.md) | Cumul opérationnel proposé, actes de nomination à formaliser, revue indépendante GOV-04 `PENDING` et données synthétiques E0 | **Draft public - toutes les nominations `PENDING`; issue #13 ouverte** |
| [POC et tests E0 synthétiques](https://github.com/tawounfouet/projecthub/pull/15) | Comparaison RLS, tests Django/DRF et smoke tests | **PR #15 fusionnée, CI post-fusion réussie sur `1095b7e`; ADR et GO E0 en attente** |
| [Bilan technique P1](reports/2026-11-21-p1-e0-rls-execution.md) | Protocole, scénarios A/B, résultats et limites du POC | **Preuves CI sur données synthétiques, aucune décision institutionnelle** |
| [ADR-0019 - décision candidate](07-architecture/03-adr-0019-rls-poc-decision.md) | R-0/R-1/R-2 et arbitrage GOV-02/GOV-04 | **PROPOSED - issue #16 ouverte** |
| [Audit documentaire 2026-11-21](reports/audit-2026-11-21/INDEX.md) | Faits, verdict, recommandations, système documentaire et navigation produits par l'audit du dépôt | **Livrables d'audit - état observé au 2026-11-21** |

Lire l'[index Architecture](07-architecture/README.md) et la [politique de publication](PUBLICATION-POLICY.md). Les décisions ADR, la validation métier et les gates E1 restent en attente.

## Chaîne de traçabilité envisagée

```text
Source -> Observation -> Besoin -> Exigence -> Critère d'acceptation
                                                  -> Backlog et preuve de test
```

Un document `draft` n'est pas une spécification définitivement adoptée. Les identifiants des besoins, décisions et exigences sont maintenus pour permettre les mises à jour sans réécriture de l'historique.

## Prochain jalon recommandé

La suite utile est de tester les hypothèses prioritaires, pas d'étendre les catalogues. À partir des questions `PH-OPEN-007` (utilisateur et promesse), `PH-OPEN-001` (plus petit MVP utile) et `PH-OPEN-024` (preuve de passation) :

1. choisir les parcours et profils à confronter à des utilisateurs, avec les autorisations nécessaires ;
2. comparer chaque tâche à la méthode actuelle et définir avant le test les mesures et critères de décision ;
3. exécuter les scénarios E0 sur des données synthétiques, puis consigner aussi les échecs et résultats non concluants ;
4. mettre à jour le périmètre MVP, le backlog et les décisions selon les preuves obtenues.

Le [foyer de validation proposé](05-mvp/00-mvp-definition.md#foyer-de-validation-recommandé) privilégie trois questions et des parcours précis ; il ne valide pas le MVP. Les grands catalogues d'exigences, de capacités et de backlog restent des références candidates, pas le périmètre à livrer d'un seul coup. Le [registre des questions ouvertes](00-context/04-open-questions.md#arbitrages-à-préparer-en-premier) indique les preuves attendues et les responsables encore à désigner. Le [protocole de validation](06-validation/00-pilot-validation-plan.md#11-protocole-dobservation-et-de-mesure) détaille les informations à fixer et à consigner. Aucun propriétaire de décision, seuil, résultat utilisateur ou accord de pilote n'est présumé ; E1 reste No-Go tant que les autorisations et les huit gates ne sont pas prouvées.

## Conventions documentaires

- Frontmatter YAML avec `id`, `version`, `status`, `classification`, `updated_at`.
- Cycle de vie : `draft`, `in-review`, `approved`, `superseded`.
- Sources publiques ou identifiants de provenance expurgés uniquement.
- Exemples synthétiques ou explicitement autorisés.
- Pas de secrets, dossiers tiers, détails d'incident, données personnelles non nécessaires ni chemins locaux privés.
- Aucun résultat de test ou engagement commercial annoncé sans preuve.

Pour contribuer à la documentation, ouvrir une issue ou une PR **sans ajouter de données privées**. Consulter d'abord la [politique de publication](PUBLICATION-POLICY.md).
