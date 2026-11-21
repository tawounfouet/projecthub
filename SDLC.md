# SDLC - ProjectHub

Ce document est une carte de navigation du cycle de vie ProjectHub. Il distingue la **publication documentaire** de la construction logicielle E0 et des autorisations E1. Les états ci-dessous décrivent les preuves GitHub, non une application fonctionnelle.

## 1. État de référence vérifié (21 novembre 2026)

| Élément | Situation observée | Suite |
|---|---|---|
| Discovery Baseline V1.0 | 25 éditions publiques, `draft` | Revue métier toujours requise |
| Audit documentaire B1..B9 | Correctifs intégrés via [PR #12](https://github.com/tawounfouet/projecthub/pull/12), fusionnée le 21 novembre 2026 | Ne pas rouvrir des constats historiques sans preuve nouvelle |
| Architecture exhaustive `PH-AEB-001` | Publiée sous `PH-DEC-019` avec classification `public` | `DRAFT / PROPOSED - NOT APPROVED` ; aucun ADR accepté automatiquement |
| Agents OpenCode | Définitions versionnées dans `.agents/` et adaptateurs `.opencode/` | Tests d'intégration à réaliser avant revendication d'exécution |
| CI de qualité documentaire | Absente du commit `main` de référence `f20ab25` | Nouveau workflow et tests soumis dans la [PR #14](https://github.com/tawounfouet/projecthub/pull/14) ; [premier run réussi](https://github.com/tawounfouet/projecthub/actions/runs/44859773975) sur le SHA `4ec0b4c` |
| Décision d'architecture pré-E0 | Autorités à nommer ; `ADR-0004/0005/0019` proposés | [Issue ACT-03 #13](https://github.com/tawounfouet/projecthub/issues/13) et [registre de mandat](docs/07-architecture/02-architecture-authority-register.md) |
| Application E0 | Aucun backend/frontend/DB migrée démontrés | Bootstrap après décisions structurantes |
| Pilote E1 | `NO-GO` | Autorisations et huit gates à démontrer séparément |

**Référence Git :** [commit de `main` après PR #12](https://github.com/tawounfouet/projecthub/commit/f20ab25f27c4f7e5d91def4319e9cf66bbdccdde). Ce SHA est un **repère historique**, pas l'affirmation que `main` ne changera plus.

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

La PR #12 est déjà **fusionnée**. Le travail P0 du présent cycle constitue **une autre contribution**, qui suit son propre enchaînement de vérification et de validation. Le mot `DEPLOY` signifie ici uniquement intégration documentaire : aucun serveur, conteneur ou SaaS n'est déployé.

## 3. Remédiation post-PR #12

| Action | Livrable | État dans le lot en cours | Critère de clôture |
|---|---|---|---|
| `ACT-01` : cohérence des statuts | Ce SDLC, plan ADR, index | Proposé en branche P0 | Revue et fusion, aucune contradiction connue |
| `ACT-02` : CI documentaire | `.github/workflows/docs-quality.yml`, `scripts/docs_quality.py`, tests synthétiques | Validé par le premier run GitHub en PR #14 ; fusion et revue encore en attente | Run lié au SHA, tests valides/invalides passants |
| `ACT-03` : autorités d'architecture | Registre versionné et [issue #13](https://github.com/tawounfouet/projecthub/issues/13) | Coordination ouverte, nominations `PENDING` | Mandats, titulaires, délégations et décision signés |
| `ACT-04` et `ACT-05` | Arbitrages et POC tenant/RBAC/RLS | `BLOCKED` avant nominations et preuves | ADR approuvés et tests réels sur données fictives |

`ACT-01` et `ACT-02` ne doivent pas être marqués `DONE_VERIFIED` avant les validations et la vérification de `main`. Un résultat CI vert ne signe pas une décision d'architecture.

## 4. Commandes de vérification

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
