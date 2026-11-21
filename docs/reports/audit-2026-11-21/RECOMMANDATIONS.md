# Recommandations - ProjectHub

> Document d'**action** : il traduit les faits de [`CODEBASE_ANALYSIS.md`](./CODEBASE_ANALYSIS.md) et le verdict de [`ANALYSE_CRITIQUE.md`](./ANALYSE_CRITIQUE.md) en plan de remédiation. Les IDs B1..B9 gardent exactement le même sens que dans l'analyse factuelle.

**Lecture rapide :** Phase 0 = aujourd'hui · Phase 1 = confidentialité bloquante · Phase 2 = bugs documentaires · Phase 3 = intégrité des correspondances · Phase 4 = robustesse · Phase 5 = modernisation.

---

## Phase 0 - Urgence immédiate

| # | Action | Détail |
|---|---|---|
| B9 | Versionner la protection de l'archive privée | Conserver la ligne `resources/` de `.gitignore:43` dans un commit dédié, puis vérifier `git check-ignore -v resources/INVENTAIRE.json` et `git ls-files resources` (doit être vide). Ne pas ajouter le contenu de `resources/` à un commit. |
| B1 | Obtenir une décision mainteneur sur la baseline `INTERNAL` | La baseline porte `classification: "INTERNAL - exhaustive working edition"` (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:6`) et l'index exige une confirmation explicite (`docs/07-architecture/README.md:15-17`). Deux sorties possibles : déplacer le fichier hors du dépôt public, ou enregistrer une exception datée avec périmètre et révision. Ne pas remplacer l'étiquette par `public` pour faire passer un contrôle. |
| B1 | Gel des changements de publication tant que la décision n'est pas consignée | La politique exige qu'une information non autorisée reste privée (`docs/PUBLICATION-POLICY.md:30`) et interdit la publication automatique (`:27`). Ce gel concerne les ajouts dans `docs/`, pas la correction des autres bugs. |

**Critère de sortie de la phase 0 :** `git show HEAD:.gitignore` contient `resources/` ; `git ls-files resources` est vide ; la décision B1 est écrite dans un fichier versionné avec date, décideur et portée, ou le fichier `INTERNAL` n'est plus suivi.

---

## Phase 1 - Sécurité bloquante

### 1.1 Contrôle minimal de classification

Le plan complet n'est pas implémenté (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`) ; un contrôle local minimal peut toutefois être introduit immédiatement. Il doit signaler une classification non publique sans la corriger automatiquement, conformément à `docs/07-architecture/01-documentation-quality-ci-plan.md:135-141`.

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"draft", "in-review", "approved", "superseded"}
REQUIRED = ("id", "title", "version", "status", "classification", "updated_at")


def tracked_markdown():
    out = subprocess.check_output(
        ["git", "ls-files", "docs", "README.md"], cwd=ROOT, text=True
    )
    return [ROOT / name for name in out.splitlines() if name.endswith(".md")]


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}
    values = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            values[key.strip()] = value.strip().strip("\"'")
    return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    errors = []
    for path in sorted(tracked_markdown()):
        if path.name == "README.md":
            continue
        rel = path.relative_to(ROOT).as_posix()
        values = frontmatter(path)
        for field in REQUIRED:
            if not values.get(field):
                errors.append(f"{rel}: champ absent {field}")
        if values.get("classification") != "public":
            errors.append(
                f"{rel}: classification {values.get('classification')!r} - decision humaine requise"
            )
        if values.get("status") not in ALLOWED:
            errors.append(f"{rel}: statut hors cycle public {values.get('status')!r}")
        if "resources/" in path.read_text(encoding="utf-8"):
            errors.append(f"{rel}: reference a l'archive privee")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    print(f"docs quality: {len(errors)} erreur(s)")
    return 1 if errors and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

| Surface | État actuel | Correctif |
|---|---|---|
| Baseline `PH-AEB-001` | `INTERNAL` et suivie (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:6`) | Appliquer la décision B1 ; le validateur doit continuer à signaler l'anomalie tant qu'aucune exception n'est formellement enregistrée. |
| `resources/` | Règle d'ignore absente de `HEAD` (B9) | Commit de la règle et vérification par `git check-ignore`. |
| Issues publiques | Avertissements textuels (`.github/ISSUE_TEMPLATE/bug_report.yml:7`, `.github/ISSUE_TEMPLATE/feature_request.yml:7`) | Conserver les avertissements et rappeler le canal privé dans la documentation de contribution ; aucun secret ne doit être collé dans une issue. |
| Statuts publics | Formulation « validées » ambiguë (B4) | Remplacer par « éditions publiées sous statut `draft` ». |

### 1.2 Durcissement transversal

Ne pas activer le contrôle comme check obligatoire tant que la baseline `INTERNAL` n'est pas traitée : le plan prévoit explicitement une phase d'observation (`docs/07-architecture/01-documentation-quality-ci-plan.md:490-500`). Avant activation, épingler les actions tierces par SHA complet et limiter `GITHUB_TOKEN` à `contents: read` (`:282-288`).

---

## Phase 2 - Bugs documentaires

| Bug | Fichier:ligne | Correctif |
|---|---|---|
| B2 | `docs/07-architecture/01-documentation-quality-ci-plan.md:222` | Remplacer « présent sur la PR #11, pas encore sur main » par « présent sur `main` ; contrat de structure à tester ». Vérifier avec `git ls-files docs/07-architecture/`. |
| B3 | `docs/00-context/03-decisions-register.md:80` | Remplacer « préparé en proposition de pull request » par « fusionné sur `main` ; voir le bilan de publication, section 2 », avec un lien relatif vers `docs/reports/2026-11-21-discovery-baseline-publication-bilan.md` depuis la racine, ou `../reports/2026-11-21-discovery-baseline-publication-bilan.md` depuis `docs/00-context/`. |
| B4 | `docs/00-context/02-canonical-context.md:142` | Remplacer « éditions publiques validées » par « éditions publiques sous statut `draft` » ; conserver l'avertissement de `:18`. |
| B5 | `docs/03-requirements/01-non-functional-requirements.md:39`, `:58-65`, `:122` | Ajouter une ligne `PH-NFR-010` dans le tableau de tests proposés et étendre la fiche `PH-NFR-001..009` en `PH-NFR-001..010` avec mesure et condition de décision. |
| B6 | `docs/05-mvp/02-prioritized-backlog.md:141-148` ; `docs/06-validation/00-pilot-validation-plan.md:115-122` | Ajouter une colonne « Gate couvert » : `038` -> `G-LEGAL-DATA`, `039` -> `G-ACCESS` + `G-SECRETS`, `040` -> `G-BACKUP`, `041` -> `G-OPERATE`, `042` -> `G-ACCESSIBILITY`, `043` -> `G-CHANGE`, `044` -> `G-DATA-EXIT`, `045` -> « décision Go/No-Go, non une gate ». Ne pas renuméroter les `PH-BLG`. |
| B7 | `docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:136`, `:139` | Remplacer les actions 1 et 4 par « vérifier que l'index et la baseline restent synchronisés » et lier `docs/README.md:11`, `:88` depuis la racine. |
| B8 | `docs/00-context/04-open-questions.md:34-41`, `:121-124` | Choisir un seul ordre canonique. Conserver l'ordre de `:121-126` comme référence et modifier le tableau d'introduction pour qu'il contienne les mêmes IDs dans le même ordre, ou inversement. |
| B9 | `.gitignore:43` | Action de la phase 0 ; aucune autre correction de contenu. |
| B1 | Baseline et index architecture | Action de la phase 0 ; ne pas traiter comme une simple coquille rédactionnelle. |

**Critère de sortie de la phase 2 :** les neuf IDs B1..B9 ont un correctif appliqué ou une décision consignée ; `git diff --check` passe ; les liens relatifs ajoutés sont vérifiés.

---

## Phase 3 - Intégrité des correspondances

Les règles suivantes doivent devenir explicites dans `docs/README.md:113-120` et `docs/07-architecture/01-documentation-quality-ci-plan.md:169-199` :

- Ne jamais compter un ID cité dans un paragraphe comme un enregistrement canonique (B8).
- Ne jamais faire correspondre un item `PH-BLG` à une gate sans identifier exactement le `G-*` (B6).
- Toute famille NFR déclarée doit posséder un scénario, une mesure et une condition de décision avant le test (B5).
- Les plages `PH-OPEN-001..030`, `PH-BLG-001..045`, `MVP-UJ-01..10` et `PH-REV-001..020` ne changent que par décision documentée (`docs/07-architecture/01-documentation-quality-ci-plan.md:177-186`, `:193-199`).

---

## Phase 4 - Robustesse et qualité

- Exécuter localement `python scripts/docs_quality.py --strict`, `git diff --check` et `git status --short` avant chaque PR, comme le propose `docs/07-architecture/01-documentation-quality-ci-plan.md:473-486`.
- Vérifier les liens relatifs en mode hors réseau ; le plan recommande Lychee avec `--offline` et `--include-fragments=none` (`docs/07-architecture/01-documentation-quality-ci-plan.md:149-159`, `:266-280`).
- Traiter les liens externes dans une tâche séparée et peu fréquente, sans faire échouer chaque PR pour un 403 ou 429 (`docs/07-architecture/01-documentation-quality-ci-plan.md:161-167`).
- Ne pas ajouter de dépendance applicative : le dépôt n'a aucun manifeste et n'en a pas besoin pour cette phase (`git ls-files`).

---

## Phase 5 - Modernisation

| Sujet | Migration | Bénéfice |
|---|---|---|
| Validateur documentaire | Passer du script minimal au contrat complet du plan : frontmatter YAML, IDs canoniques, fixtures et diagnostics (`docs/07-architecture/01-documentation-quality-ci-plan.md:298-448`) | Détection automatique de B2, B3, B4, B5, B6 et B8, sans remplacer la revue humaine. |
| Workflow GitHub Actions | Créer `.github/workflows/docs-quality.yml` avec `contents: read`, sans `pull_request_target` et avec actions épinglées (`docs/07-architecture/01-documentation-quality-ci-plan.md:228-292`) | Contrôle reproductible sur Mac, Linux et CI (`docs/07-architecture/01-documentation-quality-ci-plan.md:56`). |
| Gouvernance ADR | Nommer les autorités d'ADR et les responsables de gates (`docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:48-56`) | Rend possible une décision datée au lieu d'un statut `PROPOSED` permanent. |
| E0 futur | Garder deux Organizations synthétiques et des tests négatifs avant toute donnée réelle (`docs/05-mvp/00-mvp-definition.md:35-40`, `docs/06-validation/00-pilot-validation-plan.md:34-39`) | Évite de confondre démonstration et pilote E1. |

---

## Filet de sécurité : suite de contrôles minimale

```text
scripts/docs_quality.py
docs/quality/requirements.txt
docs/quality/fixtures/valid_public.md
docs/quality/fixtures/internal_classification.md
docs/quality/fixtures/missing_id.md
```

Commande locale vérifiable :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r docs/quality/requirements.txt
python scripts/docs_quality.py --strict
git diff --check
git status --short
```

**Critère d'acceptation global :** zéro erreur sur les fixtures valides, erreurs explicites attendues sur les fixtures `INTERNAL` et sans `id`, aucun lien relatif cassé, `git ls-files resources` vide et décision B1 consignée. Le plan prévoit 16 cas de fixtures et rappelle qu'aucun n'a été exécuté à ce jour (`docs/07-architecture/01-documentation-quality-ci-plan.md:450-471`).

---

## Récapitulatif de la roadmap

| Phase | Contenu | Effort | Jalons de sortie |
|---|---|---|---|
| Phase 0 | B9 et B1, gel de publication | 0,5 à 1 jour | Règle `resources/` dans `HEAD` ; décision baseline écrite ou fichier retiré. |
| Phase 1 | Contrôle minimal de classification | 0,5 à 1 jour | Script exécutable ; anomalie `INTERNAL` signalée sans relabel ; aucun check requis. |
| Phase 2 | B2 à B8 | 0,5 à 1 jour | Neuf bugs traités ; liens relatifs vérifiés ; `git diff --check` vert. |
| Phase 3 | Correspondances NFR, gates, IDs | 0,5 jour | `PH-NFR-010` couvert ; table 8 gates sans ambiguïté ; un seul ordre `PH-OPEN`. |
| Phase 4 | Exécution locale des contrôles | 0,5 jour | Commandes locales documentées et exécutées ; liens locaux sans casse. |
| Phase 5 | CI, ADR et préparation E0 | 2 à 5 jours | Workflow épinglé en PR pilote ; responsables nommés ; E1 toujours `No-Go`. |

> **Principe directeur** : corriger l'état déclaré sans jamais transformer une hypothèse en décision, ni une classification interne en publication implicite.

Le suivi détaillé des bugs est dans [`CODEBASE_ANALYSIS.md`](./CODEBASE_ANALYSIS.md) ; l'argumentation stratégique est dans [`ANALYSE_CRITIQUE.md`](./ANALYSE_CRITIQUE.md).
