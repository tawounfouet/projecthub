# 03 - Requirements

**PUBLIC-03 - Éditions publiques expurgées, statut draft.** Les documents décrivent des exigences de conception candidates. Ils ne constituent ni des spécifications officiellement approuvées, ni la preuve de tests ou d'une application opérationnelle.

| Document | Contenu public |
|---|---|
| [00-functional-requirements.md](00-functional-requirements.md) | 130 exigences fonctionnelles candidates, réparties sur 13 domaines |
| [01-non-functional-requirements.md](01-non-functional-requirements.md) | 113 exigences qualité, douze familles et méthodes de vérification |
| [02-business-rules-and-permissions.md](02-business-rules-and-permissions.md) | 111 règles, rôles, grants, mandats et refus inter-tenant |
| [03-requirements-traceability.md](03-requirements-traceability.md) | Matrice de couverture documentaire et exemples de chaînes de preuve |

## Principes de maintenance

- Conserver les identifiants `PH-REQ`, `PH-NFR` et `PH-BR` stables.
- Distinguer priorité candidate, validation métier, implémentation et preuve d'essai.
- Aucun `Organization` ne donne accès aux données d'un autre tenant par défaut.
- Les seuils de sécurité, performance et accessibilité sont à décider et démontrer, non à inventer.
- Les états et données de sources tierces restent privés sauf publication autorisée.
- Les relations de traçabilité publiques ne révèlent pas les identifiants internes des organisations.

Voir [Discovery](../02-discovery/README.md), [Domain](../04-domain/README.md), [Product Scope](../01-product/02-product-scope.md) et [Publication Policy](../PUBLICATION-POLICY.md).
