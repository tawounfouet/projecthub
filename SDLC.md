# SDLC - ProjectHub

Ce document est une carte de navigation du cycle de vie ProjectHub. Il distingue la **publication documentaire** de la construction logicielle E0 et des autorisations E1. Les états ci-dessous décrivent les preuves GitHub, non une application fonctionnelle.

## 1. État de référence vérifié (21 novembre 2026)

| Élément | Situation observée | Suite |
|---|---|---|
| Discovery Baseline V1.0 | 25 éditions publiques, `draft` | Revue métier toujours requise |
| Audit documentaire B1..B9 | Correctifs intégrés via [PR #12](https://github.com/tawounfouet/projecthub/pull/12), fusionnée le 21 novembre 2026 | Ne pas rouvrir des constats historiques sans preuve nouvelle |
| Architecture exhaustive `PH-AEB-001` | Publiée sous `PH-DEC-019` avec classification `public` | `DRAFT / PROPOSED - NOT APPROVED` ; aucun ADR accepté automatiquement |
| Agents OpenCode | Définitions versionnées dans `.agents/` et adaptateurs `.opencode/` | Tests d'intégration à réaliser avant revendication d'exécution |
| CI de qualité documentaire | **Fusionnée sur `main`** via [PR #14](https://github.com/tawounfouet/projecthub/pull/14), commit `547c684b` | [Run GitHub après fusion réussi](https://github.com/tawounfouet/projecthub/actions/runs/44860486972) |
| Décision d'architecture pré-E0 | Autorités à nommer ; `ADR-0004/0005/0019` proposés | [Issue ACT-03 #13](https://github.com/tawounfouet/projecthub/issues/13) et [registre de mandat](docs/07-architecture/02-architecture-authority-register.md) |
| Application E0 | [PR #15](https://github.com/tawounfouet/projecthub/pull/15) propose Django/DRF + Next.js + PostgreSQL et un POC RLS sur données fictives | [CI E0 #44862176849](https://github.com/tawounfouet/projecthub/actions/runs/44862176849) réussie sur `ae3aa6f` (20 tests Django et 2 smoke HTTP) ; ADR et GO E0 non approuvés |
| Pilote E1 | `NO-GO` | Autorisations et huit gates à démontrer séparément |

**Référence Git P0 :** [commit de fusion de PR #14](https://github.com/tawounfouet/projecthub/commit/547c684b1d52f4913c01a0adf91acdb5a87431a7). La branche P1 est distincte et ne remplace pas les décisions humaines d'architecture.

## 2. Carte SDLC et état des étapes

```text
PLAN       -> BUILD          -> TEST             -> REVIEW         -> RELEASE
Audit P0      Correction P0      Fixtures CI        PR + approbation   Fusion décidée
                  |                 |                  |
                  +-----------------+------------------+
                                                     |
                   MAINTAIN <------------------------+---> DEPLOY
                   Docs, CI, ADR                         Aucun service E0
```

Les PR #12 et #14 sont **fusionnées**. Le chantier P1 dans [PR #15](https://github.com/tawounfouet/projecthub/pull/15) apporte du code de démonstration et doit passer migrations, tests API, build Next.js, SQL RLS et smoke HTTP. `DEPLOY` dans le cadre E0 signifie seulement démarrage d'une stack locale synthétique, jamais une mise en production.

## 3. Remédiation post-PR #12

| Action | Livrable | État dans le lot en cours | Critère de clôture |
|---|---|---|---|
| `ACT-01` : cohérence des statuts | Ce SDLC, plan ADR, index | Terminé sur `main` via PR #14 | Rester synchronisé sur l'évolution P1 |
| `ACT-02` : CI documentaire | `.github/workflows/docs-quality.yml`, `scripts/docs_quality.py`, tests synthétiques | Fusionnée via PR #14, validée sur `main` | Vérifier le statut des contrôles sur chaque PR |
| `ACT-03` : autorités d'architecture | Registre versionné et [issue #13](https://github.com/tawounfouet/projecthub/issues/13) | Coordination ouverte, nominations `PENDING` | Mandats, titulaires, délégations et décision signés |
| `ACT-04` et `ACT-05` | Arbitrages et POC tenant/RBAC/RLS | `BLOCKED` avant nominations et preuves | ADR approuvés et tests réels sur données fictives |

`ACT-01` et `ACT-02` sont vérifiés après fusion P0. `ACT-03` reste bloqué par les nominations. Le POC RLS P1 ne vaut pas décision officielle `ADR-0019` ; un résultat CI vert ne signe pas une décision d'architecture.

## 4. Commandes de vérification

Pour le candidat E0, suivre le [runbook local](E0.md) et la [CI d'intégration](.github/workflows/e0-foundation.yml) ; aucune donnée réelle n'est permise. Les checks E0 supplémentaires portent sur POC PostgreSQL RLS, migrations, API Django, Next.js et HTTP smoke.

À la racine du clone, après installation des dépendances Python du lot CI :

```bash
git status --short
git diff --check
python -m pip install -r docs/quality/requirements.txt
python -m unittest discover -s tests -p 'test_docs_quality.py' -v
python scripts/docs_quality.py --strict
```

Ces commandes vérifient les fichiers publics, les métadonnées, les quatre registres canoniques et les liens locaux. Aucun appel réseau vers des URL contenues dans les documents n'est effectué par le validateur. Voir [la procédure qualité](docs/quality/README.md).

## 5. Revue, publication et conservation des preuves

1. Décrire le périmètre et les tests de la PR, y compris les exceptions historiques.
2. Faire relire le diff complet, notamment les changements dans les fichiers de gouvernance.
3. Contrôler les checks GitHub Actions sur le SHA de la branche.
4. Obtenir la décision explicite du mainteneur, puis fusionner selon la [politique de publication](docs/PUBLICATION-POLICY.md).
5. Vérifier `main` après fusion et seulement alors mettre à jour les statuts de preuve.

La revue de publication ne vaut ni validation des exigences, ni acceptation des ADR, ni accord pour les données réelles E1.

## 6. Sources de vérité

- [Index documentaire](docs/README.md)
- [Architecture et décisions](docs/07-architecture/README.md)
- [Registre des mandats pré-E0](docs/07-architecture/02-architecture-authority-register.md)
- [Publication et confidentialité](docs/PUBLICATION-POLICY.md)
- [Bonnes pratiques de collaboration](docs/COLLABORATION-BEST-PRACTICES.md)
- [Audit historique du 21 novembre 2026](docs/reports/audit-2026-11-21/INDEX.md)

*Document de suivi actualisé le 21 novembre 2026. Toute nouvelle PR doit être suivie par ses propres références et preuves, sans réécrire l'historique de la PR #12.*
