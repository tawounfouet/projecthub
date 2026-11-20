# Documentation publique de ProjectHub

Bienvenue dans la documentation de conception de **ProjectHub**, une plateforme de pilotage de projets et de travail collectif en phase de Discovery.

> **Statut : draft.** Les documents publics décrivent des intentions, hypothèses et exigences candidates. Ils ne prouvent ni logiciel opérationnel, ni validation utilisateur, ni approbation du MVP.

La [politique de publication documentaire](PUBLICATION-POLICY.md) définit le circuit de revue. Les sources privées et les comptes rendus internes ne sont **pas** publiés dans ce dépôt.

## Discovery Baseline V1.0

| Section | Objet | État public |
|---|---|---|
| [00-context](00-context/) | Historique, sources, contexte, décisions, questions ouvertes | Cinq documents préparés pour revue |
| [01-product](01-product/) | Vision, stratégie, périmètre | Trois documents préparés pour revue |
| [02-discovery](02-discovery/) | Acteurs, besoins et processus | Lot PUBLIC-02 à préparer |
| [03-requirements](03-requirements/) | Exigences et règles | Lot PUBLIC-03 à préparer |
| [04-domain](04-domain/) | Vocabulaire et frontières métier | Lot PUBLIC-03 à préparer |
| [05-mvp](05-mvp/) | Parcours et backlog | Lot PUBLIC-04 à préparer |
| [06-validation](06-validation/) | Protocoles et revue de baseline | Lot PUBLIC-04 à préparer |

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

**Revue humaine requise avant fusion** du lot PUBLIC-01. L'existence de ces fichiers dans une branche de PR ne vaut pas leur approbation.

## Chaîne de traçabilité envisagée

```text
Source -> Observation -> Besoin -> Exigence -> Critère d'acceptation
                                                  -> Backlog et preuve de test
```

Un document `draft` n'est pas une spécification définitivement adoptée. Les identifiants des besoins, décisions et exigences sont maintenus pour permettre les mises à jour sans réécriture de l'historique.

## Conventions documentaires

- Frontmatter YAML avec `id`, `version`, `status`, `classification`, `updated_at`.
- Cycle de vie : `draft`, `in-review`, `approved`, `superseded`.
- Sources publiques ou identifiants de provenance expurgés uniquement.
- Exemples synthétiques ou explicitement autorisés.
- Pas de secrets, dossiers tiers, détails d'incident, données personnelles non nécessaires ni chemins locaux privés.
- Aucun résultat de test ou engagement commercial annoncé sans preuve.

Pour contribuer à la documentation, ouvrir une issue ou une PR **sans ajouter de données privées**. Consulter d'abord la [politique de publication](PUBLICATION-POLICY.md).
