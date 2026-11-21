# ADR-0019 - POC PostgreSQL Row-Level Security

Prototype SQL **indépendant de l'application E0** et limité à des organisations fictives. Il compare sur les mêmes lignes :

- `R-0` : une table accessible au rôle applicatif sans RLS ; un `SELECT` sans filtre renvoie A et B (contrôle négatif volontaire).
- `R-1` : une table avec `ENABLE/FORCE ROW LEVEL SECURITY`, une politique `USING/WITH CHECK` et un `set_config(..., true)` local à la transaction ; la même requête renvoie uniquement le tenant autorisé.
- `R-2` : **option recommandée pour décision formelle**, garder RLS isolée au POC avant adoption dans les tables Django, car l'architecture finale et les mandats sont en attente.

## Reproduction

Avec PostgreSQL 16 et un utilisateur d'administration sur une instance jetable :

```bash
psql -X -v ON_ERROR_STOP=1 -d postgres -f poc/rls/01_setup.sql
psql -X -v ON_ERROR_STOP=1 -d postgres -f poc/rls/02_assertions.sql
```

La commande finale doit afficher `RLS_POC_ASSERTIONS_PASSED`. La CI exécute ces commandes sous PostgreSQL 16 avec des données inventées et fait échouer la PR si une assertion échoue.

## Portée des preuves

Contrôles : rôle non superuser, `NOBYPASSRLS`, propriétaire distinct, `FORCE`, contexte absent (0 lignes), lecture sans WHERE sous contexte A, refus INSERT/UPDATE B, bascule A/B en transactions successives, transaction locale nettoyée et propriétaire contraint.

**Limites :** aucune comparaison de latence crédible sur deux lignes, pas de pooling PgBouncer réel, pas de politique RLS sur les tables métier Django, pas de protection contre un client SQL capable d'usurper `app.organization_id`. RLS ne remplace jamais membership, grants, mandats, accès DB ni protections API. Les contraintes de références peuvent révéler des informations par leurs erreurs et doivent être conçues séparément.

Le POC ne vaut pas adoption `ADR-0019` : la décision est `PROPOSED / R-2 RECOMMENDED` jusqu'à une signature GOV-02 documentée dans [le registre pré-E0](../../docs/07-architecture/02-architecture-authority-register.md).
