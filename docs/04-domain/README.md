# 04 - Domain

**PUBLIC-03 - Modèle conceptuel public, statut draft.** Les contextes et contrats sont des propositions à arbitrer avant conception du schéma de base de données et des API.

| Document | Contenu public |
|---|---|
| [00-ubiquitous-language.md](00-ubiquitous-language.md) | Structure des 145 termes du glossaire et définitions essentielles |
| [01-domain-model.md](01-domain-model.md) | 20 agrégats, 30 relations, 20 commandes et 20 événements |
| [02-domain-boundaries.md](02-domain-boundaries.md) | 13 domaines, propriété canonique et 32 contrats |

## Invariants de conception

- `Organization -> Workspace -> Project -> WorkItem` est une hiérarchie métier candidate, avec contrôles de droits.
- `Client` n'est pas automatiquement `Organization` ; `Team` n'est pas `Workspace`.
- Les portefeuilles, vues et rapports ne doivent pas élargir les permissions.
- La propriété des décisions et des risques demeure une proposition à approuver.
- Les références externes conservent leur système maître et ses autorisations.
- Un projet transmis n'est pas nécessairement repris avec succès.

**13 bounded contexts cibles ne signifient ni 13 microservices ni 13 modules MVP complets.**

Lire les [règles métier](../03-requirements/02-business-rules-and-permissions.md), les [questions ouvertes](../00-context/04-open-questions.md) et la [politique de publication](../PUBLICATION-POLICY.md).
