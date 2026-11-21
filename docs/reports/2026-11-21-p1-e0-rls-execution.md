---
id: PH-REP-P1-E0-001
title: "ProjectHub - Bilan technique P1, POC PostgreSQL RLS et SLICE-00 synthétique"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
implementation_status: VERIFIED_IN_PR_CI
delivery_status: PR_OPEN_AWAITING_REVIEW
architecture_decision_status: PROPOSED_AWAITING_AUTHORITY
source_pr: "https://github.com/tawounfouet/projecthub/pull/15"
proof_run: "https://github.com/tawounfouet/projecthub/actions/runs/44862176849"
source_sha: "ae3aa6f321d032366ea50a3008ee2e5aa7609a62"
---

# ProjectHub - Rapport d'exécution P1 et preuves E0

**Périmètre :** POC PostgreSQL RLS, bootstrap Django/DRF + Next.js + PostgreSQL, implémentation expérimentale de `SLICE-00`. **Données exclusivement fictives** ; aucun résultat de pilote réel ni validation métier n'est implicite. La PR publique reste soumise à revue et le GO/NO-GO E0 est distinct des tests.

## 1. Références vérifiées

- PR : [#15, lot P1](https://github.com/tawounfouet/projecthub/pull/15).
- Run GitHub Actions sur PostgreSQL 16.15 : [#44862176849](https://github.com/tawounfouet/projecthub/actions/runs/44862176849), statut `success` au SHA `ae3aa6f321d032366ea50a3008ee2e5aa7609a62`.
- Deux jobs de ce run : `E0 PostgreSQL / DRF / Next / RLS` et `E0 Docker Compose integration`, tous les deux `success`.
- Run qualité documentaire sur la même révision : [#44862176842](https://github.com/tawounfouet/projecthub/actions/runs/44862176842), `success`.
- Une validation exécutée sur une révision antérieure ne certifie pas automatiquement les commits ultérieurs. Toujours consulter le dernier SHA et ses checks.

## 2. Résultats reproductibles

| Essai | Preuve attendue | Résultat observé dans les logs du run |
|---|---|---|
| PostgreSQL 16 / rôle applicatif | Rôle sans superuser ni `BYPASSRLS` | Contrôle SQL terminé avec `success` |
| R-0 (sans RLS) | Requête non filtrée retourne les deux lignes synthétiques A+B | Assertion passée : 2 |
| R-1 (RLS forcée) | Avec contexte transactionnel A, même requête ne retourne que A | Assertion passée : 1 |
| Contexte SQL absent | Aucune ligne visible sous RLS | Assertion passée : 0 |
| SQL brut sur B depuis A | INSERT interdit, UPDATE affecte 0 ligne | Assertions passées |
| Transaction suivante | Un contexte A ne contamine pas la session sous B | Assertions passées |
| Owner sans bypass sous `FORCE ROW LEVEL SECURITY` | Le propriétaire voit aussi une seule ligne A | Assertion passée |
| Django | `makemigrations --check --dry-run` et migrations réelles | Jobs réussis |
| API Django/DRF | Refus A/B, permission, révocation, export, parentage DB | `Ran 20 tests` et `OK` |
| Node / Next.js | `npm ci`, typage TS, build | Jobs réussis après verrouillage des dépendances |
| HTTP via Next -> Django | Connexion, contexte A, lecture B refusée, mandat refusé, export A | `E0_HTTP_SMOKE_PASSED` |
| Docker Compose | Construction, démarrage local, migrations/seed, smoke et nettoyage | `E0_HTTP_SMOKE_PASSED` dans le second job |

Le POC est **une comparaison fonctionnelle**, pas une étude de performance représentative, une preuve exhaustive de conformité ou un audit externe.

## 3. Lecture des P1

| Chantier | Sortie technique | Décision restante |
|---|---|---|
| **P1 RLS / ADR-0019** | R-0 et R-1 comparés sur une vraie instance PostgreSQL en CI, protocole SQL versionné | **R-2 recommandé, non accepté** : validation GOV-02 et avis GOV-04 via [issue #16](https://github.com/tawounfouet/projecthub/issues/16) |
| **P1 bootstrap E0** | Backend Django/DRF, frontend Next.js, Postgres, Docker Compose, rôles SQL séparés, migrations et CI | Revue PR, approbation d'architecture et sécurité pour tout GO E0 formel |
| **P1 SLICE-00** | Deux Organizations fictives, memberships/grants, sélection du contexte, invitation en attente, révocation, audit, approbation sans mandat refusée, export tenant | Validation métier et permission d'utiliser un éventuel environnement de démonstration, jamais de données E1 |

Les modèles Project et WorkItem ne représentent que des **sentinelles techniques de périmètre** ; les Epics et capacités de `SLICE-01` ne sont pas déclarés livrés.

## 4. Risques et limitations résiduelles

1. **Autorités architecture encore non nommées :** [issue ACT-03 #13](https://github.com/tawounfouet/projecthub/issues/13) ; pas d'ADR `ACCEPTED`, pas de GO officiel `G-ARCH` ou `G-E0-START`.
2. **RLS uniquement dans le POC SQL :** les tables métier Django ne portent aucune policy RLS dans cette version E0. Isolation obtenue par contrôles Django et contraintes PostgreSQL composites. Une adoption de R-1 requiert approbation.
3. **Environnement non production :** comptes et mot de passe publics uniquement fictifs, `DEBUG=1` dans Compose, aucune authentification institutionnelle, aucun throttling de production, sauvegardes ou système d'exploitation E1.
4. **Exemples limités :** uniquement A/B et un petit sous-ensemble de scénarios. Les caches, jobs asynchrones, stockage documentaire, conformité et sécurité de déploiement restent hors lot.
5. **Versionnage npm :** `frontend/package-lock.json` conserve les résolutions transverses et `npm ci` exige leur cohérence avec `package.json`. Les images de base Docker sont taggées ; leur immutabilité par digest et une politique de mises à jour restent à organiser.

## 5. Démarrage local et contrôle

Voir le [runbook E0](../../E0.md) et le [README du POC RLS](../../poc/rls/README.md). Les commandes sont adaptées à un clone local et à des secrets fictifs remplacés dans un fichier `.env` non versionné. Le workflow CI est `.github/workflows/e0-foundation.yml`.

## 6. Gates documentaires et décisionnelles

| Gate | État |
|---|---|
| Tests RLS de comparaison et refus | `VERIFIED_IN_PR_CI` sur SHA documenté |
| Tests Django/DRF tenant/revocation et HTTP | `VERIFIED_IN_PR_CI` sur SHA documenté |
| Bootstrap Docker Compose synthétique | `VERIFIED_IN_PR_CI` sur SHA documenté |
| Revue humaine et fusion de la PR #15 | `PENDING` |
| Nominations GOV-01..09 applicables | `PENDING` - issue #13 |
| Approbation ADR-0004 / ADR-0005 | `PROPOSED` |
| Arbitrage officiel ADR-0019 | `PROPOSED` - issue #16 |
| GO de démarrage E0 au nom du projet | `NOT_GRANTED` |
| E1 avec données réelles | **NO-GO**, huit gates et accords requis |

**Décision d'ingénierie proposée :** poursuivre l'étude technique en bac à sable synthétique avec un schéma partagé contrôlé par l'API et les clés composites ; **différer l'adoption de RLS dans les tables Django** (option R-2), uniquement si l'autorité architecture approuve cette décision avec les risques résiduels et conditions de réexamen.

Toute décision humaine signée doit être tracée dans le registre compétent et ne peut pas être simulée par un agent IA.
