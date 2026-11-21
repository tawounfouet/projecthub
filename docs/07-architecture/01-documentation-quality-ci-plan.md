---
id: PH-ENG-DOC-CI-001
title: "ProjectHub - Plan de qualité documentaire et CI GitHub Actions V1.0"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
owner: "ProjectHub Engineering / Documentation - responsable à désigner"
implementation_status: NOT_IMPLEMENTED
validation_status: PROPOSED
related_documents:
  - "docs/PUBLICATION-POLICY.md"
  - "docs/COLLABORATION-BEST-PRACTICES.md"
  - "docs/README.md"
  - "docs/00-context/04-open-questions.md"
  - "docs/05-mvp/01-user-journeys.md"
  - "docs/05-mvp/02-prioritized-backlog.md"
  - "docs/06-validation/01-discovery-baseline-review.md"
---

# ProjectHub - Qualité documentaire automatisée avec GitHub Actions

> **Spécification publique candidate, non approuvée et non implémentée.** Ce document décrit un workflow de contrôle documentaire à construire et à tester. À la date de rédaction, le dépôt `tawounfouet/projecthub` présente des contrôles GitGuardian sur ses PR récentes, mais ne contient pas de workflow documentaire dédié sous `.github/workflows/`. La réussite de GitGuardian ne constitue pas une validation de la documentation, de ses liens ou de ses ID.

**Finalité :** passer d'une revue documentaire manuelle et ponctuelle à des contrôles reproductibles à chaque PR, tout en maintenant une revue humaine de confidentialité, d'exactitude et de décision métier.

**Emplacement public proposé pour la prochaine PR :** `docs/07-architecture/01-documentation-quality-ci-plan.md`. Cette proposition ne modifie pas le dépôt GitHub en l'absence d'un commit distinct.

**Périmètre :** `README.md`, les documents de `docs/`, les illustrations liées, les index, les métadonnées YAML, les registres d'identifiants, puis les liens externes lors d'une phase ultérieure. Ce lot **n'implémente pas** Django, Next.js, ni le MVP E0.

## 1. Situation actuelle et besoin

Les lots PUBLIC-01 à PUBLIC-04 ont permis la publication des **25 éditions publiques** de Discovery Baseline V1.0, complétées par des guides et des documents post-Discovery. Le dépôt a notamment accueilli des images, des index et des documents d'architecture. Leur qualité a été vérifiée de façon ciblée pendant les PR, avec une dépendance importante à la relecture et à des scripts ponctuels.

Principaux risques de régression :

- Un lien Markdown relatif pointe vers un document déplacé, renommé ou absent, ou vers une image oubliée lors du commit.
- Le frontmatter YAML est absent, invalide ou incohérent avec la classification du dépôt public.
- Un identifiant canonique est perdu, dupliqué, renuméroté ou confondu avec une simple référence.
- Un sommaire annonce « en revue » alors que la PR a été fusionnée, ou compte les nouveaux documents comme s'ils faisaient partie des 25 historiques.
- Une édition interne exhaustive est accidentellement ajoutée dans le dépôt public.
- Une réussite de scanner de secrets est interprétée à tort comme une autorisation de publication ou une preuve de validation métier.

**Cas réel à prendre en compte :** la PR #11 contient une baseline exhaustive avec `classification: "INTERNAL - exhaustive working edition"`. Elle nécessite une décision de publication spécifique. Un contrôle strict de classification publique doit la **signaler**, pas la rendre publique par changement automatique d'étiquette. Le contenu d'une branche publique reste déjà accessible avant fusion.

## 2. Objectifs et critères de succès

| ID | Objectif candidat | Critère mesurable à confirmer |
|---|---|---|
| `PH-DOC-CI-001` | Détecter les liens locaux invalides | Tout lien relatif cassé provoque un échec explicite avec chemin source |
| `PH-DOC-CI-002` | Valider les métadonnées | Frontmatter requis, valide, champs attendus et formats contrôlés |
| `PH-DOC-CI-003` | Contrôler les IDs canoniques | Absence de trou et de doublon dans quatre registres reconnus |
| `PH-DOC-CI-004` | Éviter les faux positifs | Les plages et références non canoniques ne sont pas prises pour des enregistrements |
| `PH-DOC-CI-005` | Signaler la classification interne | Document `INTERNAL` détecté et soumis à une revue, sans exception silencieuse |
| `PH-DOC-CI-006` | Rendre le contrôle reproductible | Même commande sur Mac, Linux et runner CI avec version de dépendances fixée |
| `PH-DOC-CI-007` | Afficher les erreurs dans la PR | Job GitHub Actions lisible et bloquant après une phase d'observation |
| `PH-DOC-CI-008` | Préserver la confidentialité | Aucun extrait de document confidentiel ni secret affiché dans les logs |
| `PH-DOC-CI-009` | Conserver une approbation humaine | Les décisions produit et les autorisations de publication ne sont jamais auto-approuvées |

Les seuils de bruit acceptables (par exemple 0 faux positif sur les fixtures de référence) sont des **cibles proposées**, non des résultats mesurés.

## 3. Architecture de contrôle proposée

```text
Commit ou Pull Request
        |
        v
.github/workflows/docs-quality.yml
        |
        +-- Job metadata-and-ids
        |      +-- YAML et classification
        |      +-- unicité des IDs documentaires
        |      +-- continuité des registres canoniques
        |
        +-- Job local-links
        |      +-- Markdown et images locales
        |      +-- chemins et cas de nommage
        |
        +-- Job optional-format (phase 2)
        |      +-- markdownlint / conventions éditoriales
        |
        +-- Job external-links (phase 3, planifié)
               +-- HTTP/HTTPS avec cache et exclusions explicites
               +-- résultats non bloquants initialement
```

La politique documentaire demeure la source de vérité sur les classifications et le processus de publication. Le pipeline est un **contrôle technique**, pas une autorité habilitée à divulguer des informations.

## 4. Portée exacte des fichiers

| Zone | Traitement |
|---|---|
| `README.md` (racine) | Liens et images ; frontmatter non obligatoire |
| `docs/README.md` et `docs/**/README.md` | Liens et images ; frontmatter non obligatoire |
| `docs/**/*.md`, sauf `README.md` | Frontmatter, champs requis, IDs documentaires et liens |
| `docs/**/assets/*`, `docs/assets/*` | Existence des cibles d'images et casse des noms |
| `.github/workflows/docs-quality.yml` | Workflow de référence proposé, à créer plus tard |
| `scripts/docs_quality.py` | Validateur proposé, à créer plus tard |
| `docs/quality/requirements.txt` | Dépendances du validateur proposées, à créer plus tard |
| `docs/quality/fixtures/` | Cas attendus et cas invalides proposés |

**Ne pas appliquer** le schéma de frontmatter aux README ni au code, aux images, aux fichiers YAML GitHub et aux sources privées situées hors dépôt.

## 5. Contrat de frontmatter YAML

Le référentiel existant utilise au minimum :

```yaml
---
id: PH-ENG-DOC-CI-001
title: "Titre explicite"
version: "0.1.0"
status: draft
classification: public
updated_at: "2026-11-21"
related_documents: []
---
```

### Champs requis et contrôles

| Champ | Règle candidate |
|---|---|
| `id` | Chaîne non vide, identifiant documentaire unique dans les documents substantiels |
| `title` | Chaîne non vide |
| `version` | Chaîne non vide ; convention de version à homogénéiser progressivement |
| `status` | `draft`, `in-review`, `approved` ou `superseded` pour les éditions publiques |
| `classification` | `public` pour une édition destinée au dépôt public |
| `updated_at` | Date `YYYY-MM-DD`, vérifiée même si PyYAML l'interprète comme `date` |
| `sources` | Optionnel ; tableau de références publiques/expurgées, pas de provenance secrète |
| `related_documents` | Optionnel ; références documentaires à examiner selon leur convention de chemin |
| `owner` | Recommandé ; un rôle à désigner n'est pas une nomination effective |

### Règles d'exception

- L'absence de frontmatter sur un README **n'est pas une erreur**.
- Les documents historiques ne doivent pas être réécrits arbitrairement pour satisfaire une nouvelle préférence de format.
- Une `classification: INTERNAL` dans `docs/` constitue une **anomalie de diffusion** à traiter humainement. Ne pas modifier sa classification automatiquement ni ajouter un passe-droit général.
- Des valeurs historiques de `status` autres que celles du cycle public doivent être inventoriées avant le passage en mode bloquant.
- Pour toute exception indispensable, exiger un dossier de décision signé et une règle limitée à un chemin et une date de révision. Le fait d'être sur une branche n'est pas une protection de confidentialité.

### Ce que le validateur ne peut pas garantir

Le frontmatter cohérent ne prouve ni la conformité juridique, ni la propriété intellectuelle, ni le consentement d'un tiers, ni l'exactitude d'une affirmation.

## 6. Vérification des liens Markdown

### Liens à couvrir dès la phase 1

- `[Doc](01-product/00-product-vision.md)` et `[Index](../README.md)` ;
- `[Image](assets/00-product-vision.png)` et `![Texte alternatif](assets/01-product-strategy.png)` ;
- liens rédigés dans les documents Markdown, hors blocs de code ;
- chemins avec espaces ou caractères URL encodés, sous réserve du comportement du vérificateur choisi ;
- noms sensibles à la casse, même si le Mac possède un système de fichiers qui ne l'est pas.

**Outil candidat :** [Lychee](https://github.com/lycheeverse/lychee), lancé en mode **hors réseau** pour les liens locaux lors des PR. Commencer par les liens de fichiers et d'images. L'analyse des ancres `#section` peut être activée après validation de la correspondance avec les ancres générées par GitHub, pour éviter les faux positifs liés aux caractères accentués.

Les liens comme `https://github.com/...` ne doivent pas rendre chaque PR instable à cause d'une limite de débit, d'une indisponibilité distante ou d'une authentification externe. Les contrôler dans une tâche séparée et moins fréquente.

### Politique de liens externes

- Vérification hebdomadaire candidate, avec timeout, retry et cache.
- Exclusions documentées, motivées, datées et limitées, sans masquer tous les échecs.
- Pas d'accès à des adresses privées, localhost ou réseaux internes depuis l'analyse automatique.
- Pas de jetons d'accès ajoutés dans des URLs documentaires ni affichés dans les sorties.
- Une réponse 403 ou 429 est un événement à qualifier, pas nécessairement la preuve d'un lien cassé.

## 7. Continuité des IDs - règle la plus importante

Tous les ID qui figurent dans un fichier **ne sont pas des enregistrements à compter**. Il faut distinguer :

1. une **ligne canonique** dans le tableau qui détient l'entité ;
2. une **référence** dans une autre section ou un autre document ;
3. une **plage** comme `PH-REQ-001..130`, qui résume une source privée et ne crée pas 130 lignes publiques.

### Registres canoniques vérifiables aujourd'hui

| Registre | Fichier propriétaire | Format | Plage attendue | Méthode |
|---|---|---|---|---|
| Questions ouvertes | `docs/00-context/04-open-questions.md` | `PH-OPEN-NNN` | `001..030` | Première colonne des tableaux des sections 2 à 5 |
| Backlog | `docs/05-mvp/02-prioritized-backlog.md` | `PH-BLG-NNN` | `001..045` | Première colonne du catalogue section 4 |
| Parcours MVP | `docs/05-mvp/01-user-journeys.md` | `MVP-UJ-NN` | `01..10` | Première colonne du tableau section 3 |
| Réserves de revue | `docs/06-validation/01-discovery-baseline-review.md` | `PH-REV-NNN` | `001..020` | Première colonne du registre section 6 |

**Ne pas exiger** l'existence de 130 lignes `PH-REQ`, 113 lignes `PH-NFR`, 111 lignes `PH-BR` ou 145 définitions de glossaire dans les éditions publiques : celles-ci présentent des **synthèses**, pas les registres privés exhaustifs.

### Algorithme attendu

Pour chaque registre, le script doit :

1. Lire **uniquement** le fichier propriétaire et les sections de référence appropriées.
2. Extraire les ID en **première colonne** des tableaux canoniques, pas toutes les mentions du texte.
3. Vérifier le format (`NN` ou `NNN`), l'absence de doublons et de trous.
4. Comparer à l'ensemble attendu, en affichant les numéros manquants et supplémentaires.
5. En cas de changement de nombre, exiger une décision explicite et une adaptation du contrat de validation.
6. Préserver les IDs stables : un item obsolète doit suivre une politique de dépréciation plutôt que provoquer une renumérotation silencieuse.

**Exemple :** deux citations de `PH-OPEN-007` dans un paragraphe ne sont **pas** deux questions. Une plage `PH-REQ-001..009` n'est pas neuf enregistrements individuels. C'est une erreur d'utiliser `len(re.findall(...))` sur tout le fichier pour prouver la continuité.

## 8. Esquisse d'arborescence de mise en oeuvre

```text
projecthub/
├── .github/
│   └── workflows/
│       └── docs-quality.yml              # à créer
├── scripts/
│   └── docs_quality.py              # à créer
├── docs/
│   ├── quality/
│   │   ├── requirements.txt          # à créer
│   │   ├── id-registries.yml         # optionnel en phase 2
│   │   └── fixtures/                 # à créer
│   ├── 00-context/
│   ├── 01-product/
│   ├── 02-discovery/
│   ├── 03-requirements/
│   ├── 04-domain/
│   ├── 05-mvp/
│   ├── 06-validation/
│   └── 07-architecture/              # présent sur la PR #11, pas encore sur main
└── README.md
```

Les chemins `docs/quality/` et `scripts/docs_quality.py` sont **proposés**, pas présents ou déjà opérationnels.

## 9. Modèle de workflow GitHub Actions

> **Exemple de conception**, à enregistrer en `.github/workflows/docs-quality.yml` lors d'une PR d'implémentation distincte. La validation des versions des actions, de leur épinglage SHA et du comportement de Lychee sur le dépôt doit précéder l'activation obligatoire.

```yaml
name: Documentation Quality

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: docs-quality-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  metadata-and-ids:
    name: docs-metadata-and-ids
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install doc validator dependencies
        run: python -m pip install -r docs/quality/requirements.txt
      - name: Verify metadata and canonical IDs
        run: python scripts/docs_quality.py --strict

  local-links:
    name: docs-local-links
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Check local Markdown links and images
        uses: lycheeverse/lychee-action@v2
        with:
          args: >-
            --offline --no-progress --include-fragments=none
            README.md 'docs/**/*.md'
          fail: true
```

### Choix de sécurité du modèle

- Aucun `pull_request_target` pour exécuter des scripts provenant d'une PR non fiable.
- `GITHUB_TOKEN` limité à `contents: read` ; aucun secret de déploiement ni PAT.
- Pas de push automatique, correction automatique ou commentaire par robot exigeant un jeton d'écriture.
- Passer les actions tierces à des **SHA complets vérifiés** avant l'adoption comme contrôle de branche obligatoire. Les versions ci-dessus sont des repères lisibles, **pas des SHA épinglés**.
- Installer des dépendances depuis un `requirements.txt` à versions fixées et contrôlées ; ne pas installer une dépendance à partir d'une branche arbitraire.
- Le workflow est volontairement **sans filtre `paths`** pour éviter qu'un contrôle déclaré obligatoire soit laissé « Pending » sur une PR hors documentation. Les jobs peuvent être optimisés plus tard sans rendre le check requis impossible à satisfaire.
- Toujours faire tourner les vérifications sur le contenu proposé dans la PR, sans exposer des informations d'un environnement de production.

**Note :** l'absence de filtre `paths` est un choix de sûreté de la protection de branche, pas une obligation GitHub universelle. La stratégie sera réévaluée avec la politique des checks requis.

## 10. Implémentation proposée du validateur Python

Le fragment ci-dessous constitue une **base exécutable à adapter et à tester**, pas un script installé sur le dépôt. Il suppose `PyYAML` disponible dans les dépendances épinglées. Il valide des **lignes de tableau** propriétaires et évite de compter les références répétées ailleurs.

```python
#!/usr/bin/env python3
"""Contrôles initiaux de frontmatter et continuité des registres canoniques."""
from __future__ import annotations

import argparse
from datetime import date, datetime
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQUIRED = ("id", "title", "version", "status", "classification", "updated_at")
PUBLIC_STATES = {"draft", "in-review", "approved", "superseded"}

# Les bornes des sections proviennent de la structure des documents actuels.
REGISTRIES = [
    ("docs/00-context/04-open-questions.md", "PH-OPEN", 3, 30, 2, 6),
    ("docs/05-mvp/02-prioritized-backlog.md", "PH-BLG", 3, 45, 4, 5),
    ("docs/05-mvp/01-user-journeys.md", "MVP-UJ", 2, 10, 3, 4),
    ("docs/06-validation/01-discovery-baseline-review.md", "PH-REV", 3, 20, 6, 7),
]


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise ValueError("frontmatter YAML absent ou mal délimité")
    value = yaml.safe_load(match.group(1))
    if not isinstance(value, dict):
        raise ValueError("frontmatter YAML non associatif")
    return value


def check_metadata() -> list[str]:
    errors = []
    seen = {}
    for path in sorted(DOCS.rglob("*.md")):
        if path.name == "README.md":
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            data = parse_frontmatter(path)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{rel}: {exc}")
            continue
        for field in REQUIRED:
            if field not in data or data[field] in (None, ""):
                errors.append(f"{rel}: champ manquant ou vide: {field}")
        doc_id = data.get("id")
        if not isinstance(doc_id, str) or not doc_id.strip():
            errors.append(f"{rel}: id documentaire invalide")
        elif doc_id in seen:
            errors.append(f"{rel}: id dupliqué {doc_id} (déjà dans {seen[doc_id]})")
        else:
            seen[doc_id] = rel
        if data.get("classification") != "public":
            errors.append(f"{rel}: classification non publique, revue humaine requise")
        if data.get("status") not in PUBLIC_STATES:
            errors.append(f"{rel}: statut documentaire inconnu ou non approuvé")
        val = data.get("updated_at")
        if isinstance(val, datetime):
            errors.append(f"{rel}: updated_at doit être une date sans heure")
        elif isinstance(val, date):
            pass  # PyYAML convertit parfois la date YAML en objet date.
        elif isinstance(val, str):
            try:
                if date.fromisoformat(val).isoformat() != val:
                    raise ValueError("format non canonique")
            except ValueError:
                errors.append(f"{rel}: updated_at non conforme à YYYY-MM-DD")
        else:
            errors.append(f"{rel}: updated_at absent ou non daté")
    return errors


def check_registry(path_str, prefix, width, count, begin, end):
    path = ROOT / path_str
    if not path.exists():
        return [f"{path_str}: registre absent"]
    text = path.read_text(encoding="utf-8")
    section = 0
    observed = []
    row = re.compile(r"^\|\s*`" + re.escape(prefix) +
                     r"-(\d{" + str(width) + r"})`\s*\|")
    for line in text.splitlines():
        header = re.match(r"^##\s+(\d+)\.\s", line)
        if header:
            section = int(header.group(1))
        if begin <= section < end:
            match = row.match(line)
            if match:
                observed.append(int(match.group(1)))
    required = set(range(1, count + 1))
    unique = set(observed)
    missing = sorted(required - unique)
    unexpected = sorted(unique - required)
    duplicates = sorted(n for n in unique if observed.count(n) > 1)
    issues = []
    if missing or unexpected or duplicates:
        issues.append(
            f"{path_str}: {prefix}: manquants={missing}, "
            f"hors-plage={unexpected}, doublons={duplicates}"
        )
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    if not DOCS.exists():
        print("Dossier docs absent", file=sys.stderr)
        return 2
    errors = check_metadata()
    for row in REGISTRIES:
        errors.extend(check_registry(*row))
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    print(f"Document quality: {len(errors)} erreur(s) détectée(s)")
    return 1 if errors and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### Limites à compléter avant production

- Ajouter des tests unitaires sur le parseur et les formats YAML déjà présents.
- La validation des liens est déléguée à Lychee, et non au parseur Python ci-dessus.
- Le format des tables peut évoluer ; la CI doit être modifiée avec la documentation plutôt que la bloquer sans diagnostic.
- Les frontières de sections `## N.` proviennent des fichiers actuels : elles sont un **contrat de structure**, à versionner et à tester.
- Les plages attendues doivent être changées uniquement avec une décision documentaire explicite.
- Évaluer les faux positifs existants avant d'activer `--strict` sur la branche protégée.
- Limiter les logs à des chemins et erreurs de règle ; ne pas imprimer des paragraphes entiers provenant de documents qui pourraient être mal classifiés.

## 11. Dépendances et versionnement

Exemple de `docs/quality/requirements.txt` **à créer et à épingler** :

```text
# Exemple de dépendance : fixer la version approuvée avant merge.
PyYAML==6.0.3
```

L'outil Lychee doit lui aussi être associé à une version testée ; privilégier le SHA complet de l'action GitHub après validation. Les dépendances et versions mentionnées sont des **choix de mise en oeuvre proposés**, pas des outils déjà présents dans ProjectHub.

## 12. Fixtures et tests négatifs indispensables

| Cas | Exemple | Comportement attendu |
|---|---|---|
| `T-DOC-001` | Document public avec frontmatter valide | PASS |
| `T-DOC-002` | `README.md` sans frontmatter | PASS |
| `T-DOC-003` | Document substantiel sans `id` | FAIL |
| `T-DOC-004` | Deux documents avec même `id` | FAIL |
| `T-DOC-005` | Date `updated_at` invalide | FAIL |
| `T-DOC-006` | `classification: INTERNAL` dans un document public | FAIL et alerte de publication |
| `T-DOC-007` | Référence Markdown relative vers un fichier absent | FAIL |
| `T-DOC-008` | PNG présent sur Mac mais non suivi par Git | FAIL en CI |
| `T-DOC-009` | 45 lignes canoniques `PH-BLG-001..045` | PASS |
| `T-DOC-010` | Omission de `PH-BLG-017` dans le tableau | FAIL |
| `T-DOC-011` | Même `PH-OPEN-007` cité dans deux paragraphes | PASS (une seule ligne canonique) |
| `T-DOC-012` | Plage `PH-REQ-001..130` sans 130 lignes | PASS |
| `T-DOC-013` | Deux lignes `MVP-UJ-06` dans le tableau | FAIL |
| `T-DOC-014` | Nouveau document post-Discovery dans `docs/07-architecture` | PASS sans augmenter artificiellement le total historique de 25 |
| `T-DOC-015` | Lien externe inaccessible temporairement | Ne bloque pas la PR en phase initiale |
| `T-DOC-016` | Changement d'une section canonique sans mise à jour du parseur | FAIL explicite ; revue de compatibilité requise |

**Tests avant activation :** exécuter les fixtures localement, puis le workflow en PR Draft ; produire un compte rendu daté des réussites, échecs et faux positifs. Aucune de ces fixtures n'est déclarée exécutée par le présent document.

## 13. Exécution locale proposée sur Mac

Depuis un clone synchronisé de `projecthub` après création des scripts et dépendances :

```bash
cd "$(git rev-parse --show-toplevel)"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r docs/quality/requirements.txt
python scripts/docs_quality.py --strict

git diff --check
git status --short
```

Pour les liens, installer Lychee depuis une source officielle ou utiliser une installation documentée et épinglée ; éviter de masquer les erreurs avec `|| true` pour le job de vérification locale obligatoire.

## 14. Stratégie de mise en service progressive

| Étape | Travail | Porte de passage |
|---|---|---|
| `CI-DOC-0` - Audit | Inventorier les formats réels, les anomalies et exceptions, y compris la PR #11 | Rapport de compatibilité et classification revue |
| `CI-DOC-1` - Scripts | Implémenter frontmatter, unicité d'ID, registres canoniques et liens locaux | Tests positifs/négatifs reproductibles |
| `CI-DOC-2` - PR pilote | Déployer le workflow sur une branche dédiée, sans le rendre immédiatement obligatoire | Trois PR ou simulations étudiées, bruit corrigé |
| `CI-DOC-3` - Protection | Ajouter les jobs de documentation comme checks requis si la gouvernance l'autorise | Checks stables, procédure de dépannage publiée |
| `CI-DOC-4` - Externe | Planifier les liens HTTP/HTTPS et, si pertinent, le lint Markdown | Rapport régulier exploitable, faible taux de fausses alertes |

**Ne pas** faire de `docs-quality` un contrôle requis avant que le workflow existe dans `main` et fonctionne sur les PR concernées. L'approbation de l'architecture et du modèle RBAC est indépendante de l'approbation de cette CI.

## 15. Matrice de responsabilités à désigner

| Rôle candidat | Responsabilité | Désignation |
|---|---|---|
| Mainteneur ProjectHub | Accepter les règles de qualité et la stratégie de fusion | À confirmer |
| Référent documentation | Maintenir les schémas de frontmatter et les registres | À désigner |
| Référent Engineering | Implémenter et maintenir scripts et workflow | À désigner |
| Référent sécurité / confidentialité | Vérifier les exceptions de classification et risques de divulgation | À désigner |
| Référent produit | Valider les changements de plage et de signification des IDs | À désigner |
| Contributeur | Corriger les échecs et fournir les preuves dans la PR | Selon chaque PR |

## 16. Critères de validation du document et de la future CI

### Critères de validation de cette spécification

- [ ] Relecture de la politique documentaire et des documents canoniques.
- [ ] Décision sur l'inclusion des documents d'architecture non encore fusionnés.
- [ ] Décision explicite sur la baseline marquée `INTERNAL`, sans conversion automatique.
- [ ] Accord du mainteneur sur les registres, les seuils et le comportement des échecs.
- [ ] Accord sur les responsabilités de maintenance et la fréquence de vérification.

### Définition de terminé pour l'implémentation future

- [ ] Workflow et scripts commitées sur une branche dédiée.
- [ ] Tests unitaires de parseur et des quatre registres exécutés avec résultats conservés.
- [ ] Liens locaux et images contrôlés avec diagnostic exploitable.
- [ ] Pinning des actions externes et des dépendances approuvé.
- [ ] Permissions du `GITHUB_TOKEN` limitées au besoin réel.
- [ ] PR de démonstration exécutée avec au moins une anomalie volontaire correctement détectée.
- [ ] Aucun document privé ou secret ajouté aux tests et aux logs.
- [ ] Revue humaine et squash merge selon la politique ProjectHub.
- [ ] Check GitHub Actions confirmé opérationnel sur `main`.
- [ ] Décision distincte sur son éventuel caractère obligatoire dans la protection de branche.

## 17. Backlog technique candidat

| ID | Tâche candidate | Priorité | Livrable |
|---|---|---|---|
| `DOC-QA-001` | Inventorier les frontmatter publics et exceptions | P0 | Rapport d'audit |
| `DOC-QA-002` | Figurer les règles de champs YAML et IDs documentaires | P0 | Contrat de schéma |
| `DOC-QA-003` | Implémenter le parseur YAML sûr | P0 | `scripts/docs_quality.py` |
| `DOC-QA-004` | Contrôler l'unicité des IDs documentaires | P0 | Tests et diagnostic |
| `DOC-QA-005` | Contrôler quatre registres canoniques | P0 | Validations et fixtures |
| `DOC-QA-006` | Ajouter Lychee en contrôle local hors réseau | P0 | Job liens |
| `DOC-QA-007` | Configurer GitHub Actions avec permissions minimales | P0 | Workflow |
| `DOC-QA-008` | Vérifier la compatibilité Mac et Linux | P1 | Guide reproductible |
| `DOC-QA-009` | Ajouter la stratégie de classification et de publication | P0 | Alertes et décision humaine |
| `DOC-QA-010` | Préparer les scénarios d'échec/rollback des checks | P1 | Runbook CI |
| `DOC-QA-011` | Évaluer le lint Markdown sans reformatage massif | P2 | Proposition de règles |
| `DOC-QA-012` | Ajouter une vérification planifiée des liens externes | P2 | Workflow séparé et rapport |
| `DOC-QA-013` | Mettre à jour le guide de contribution | P1 | Documentation mainteneur |
| `DOC-QA-014` | Décider si les jobs deviennent des checks requis | P1 | Décision de gouvernance |

Ces références sont **des tâches de conception** ; elles ne correspondent pas à des GitHub Issues déjà créées.

## 18. Risques, limites et décisions ouvertes

| Risque | Impact | Mesure candidate |
|---|---|---|
| Faux positifs liés aux plages d'IDs | Blocage injustifié de PR | Compter uniquement les tableaux canoniques |
| Divergence entre ancres GitHub et outil de liens | Alerte non fiable | Désactiver le contrôle d'ancres en phase initiale |
| Document interne commité sur une branche publique | Exposition irréversible potentielle | Relecture préalable, alerte bloquante, procédure d'incident |
| Actions ou dépendances non épinglées | Risque de supply chain | SHA complet et contrôle des mises à jour |
| Liens externes éphémères | CI instable | Contrôle séparé, retries et exclusions documentées |
| Pipeline trop lent | Friction contributive | Job rapide local en PR, contrôles réseau programmés |
| CI interprétée comme preuve métier | Fausse déclaration de maturité | Mention explicite : qualité documentaire seulement |
| Logs riches en contenu privé | Diffusion supplémentaire de données | Logs minimaux, aucune copie intégrale du contenu suspect |

## 19. Feuille de route de réalisation proposée

**Lot A - Contrat** : audit du dépôt, définition des sections propriétaires, fixtures, stratégie de classification et de dates.

**Lot B - Validateur** : parseur YAML, contrôle des IDs et diagnostics avec retours d'erreur sûrs.

**Lot C - Workflow** : job PR/`main`, vérification Lychee hors réseau, versions d'actions épinglées, exécution en mode pilote.

**Lot D - Gouvernance** : relecture, correction des faux positifs, choix des checks requis et guide contributeur.

**Lot E - Extensions** : liens externes programmés, lint Markdown, statistiques de qualité et politique de maintenance.

Aucune date fixe ni budget n'est engagé par ce plan. Le passage entre lots dépend des preuves et décisions consignées.

## 20. Décision demandée

Approuver ou amender le périmètre du **contrôle documentaire V1.0**, désigner les responsables et autoriser une **PR d'implémentation séparée**. Cette PR devra livrer de vrais fichiers `.github/workflows/docs-quality.yml`, `scripts/docs_quality.py`, les fixtures et les dépendances, puis prouver les résultats sur le dépôt.

**Le présent document n'atteste ni la création de ce workflow, ni sa réussite dans GitHub Actions.** Il décrit les conditions pour le faire sans confusion avec GitGuardian ou avec l'approbation métier de ProjectHub.

## 21. Références

### Références ProjectHub examinées sur GitHub

- [Index public](https://github.com/tawounfouet/projecthub/blob/main/docs/README.md)
- [Politique documentaire](https://github.com/tawounfouet/projecthub/blob/main/docs/PUBLICATION-POLICY.md)
- [Guide de collaboration](https://github.com/tawounfouet/projecthub/blob/main/docs/COLLABORATION-BEST-PRACTICES.md)
- [Questions ouvertes](https://github.com/tawounfouet/projecthub/blob/main/docs/00-context/04-open-questions.md)
- [Backlog MVP](https://github.com/tawounfouet/projecthub/blob/main/docs/05-mvp/02-prioritized-backlog.md)
- [Parcours MVP](https://github.com/tawounfouet/projecthub/blob/main/docs/05-mvp/01-user-journeys.md)
- [Revue Discovery](https://github.com/tawounfouet/projecthub/blob/main/docs/06-validation/01-discovery-baseline-review.md)
- [PR #11, ajouts Discovery et Architecture](https://github.com/tawounfouet/projecthub/pull/11)

### Références techniques officielles ou projets éditeurs

- [GitHub - Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [GitHub - Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
- [GitHub - Use GITHUB_TOKEN for authentication](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token)
- [GitHub - Managing Actions settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)
- [Lychee - link checker](https://github.com/lycheeverse/lychee)
- [Lychee - GitHub Action](https://github.com/lycheeverse/lychee-action)
- [PyYAML - documentation](https://github.com/yaml/pyyaml.org/blob/master/wiki/PyYAMLDocumentation.md)

---

**Historique** : `0.1.0` (2026-11-21), première proposition de qualité documentaire continue pour ProjectHub. Les valeurs, scripts et workflows fournis ici sont des modèles à valider avant mise en production.
