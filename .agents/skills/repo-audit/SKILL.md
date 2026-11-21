---
name: repo-audit
description: Audit documentaire complet de ProjectHub sous docs/reports/audit-YYYY-MM-DD/. Use when the user asks to auditer ce repo, générer les docs d'audit, analyser la documentation, or invokes /audit.
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: audit
---

# Audit documentaire ProjectHub

Ce skill est adapté à un dépôt documentation-only. Il ne suppose ni code applicatif, ni test, ni build, ni CI.

## Regles non negociables

1. Tout fait doit etre verifie par lecture directe, avec reference `fichier:ligne`. Si ce n'est pas verifiable, ne pas l'ecrire.
2. Ne jamais recopier de secret, transcript pilote, nom de client, chemin de `resources/` ou contenu de `archives/`.
3. Garder les IDs `B1`..`B9` stables quand l'audit porte sur le bilan du 2026-11-21.
4. Ne pas transformer un statut `draft` en approbation.
5. Ne pas publier, committer, pousser ou ouvrir de PR sans demande explicite.

## Phase A - Investigation avant redaction

Lire, dans cet ordre :

1. Racine : `README.md`, `AGENTS.md`, `SDLC.md`, `.gitignore`, `.github/`.
2. Etat Git : `git status --short`, `git log --oneline -10`, `git branch --show-current`.
3. Politiques : `docs/PUBLICATION-POLICY.md` et `docs/COLLABORATION-BEST-PRACTICES.md`.
4. Index : `docs/README.md` et `docs/reports/audit-2026-11-21/INDEX.md`.
5. Registres : `PH-DEC-*`, `PH-OPEN-*`, `PH-BLG-*`, `MVP-UJ-*`, `PH-REV-*`.
6. Liens relatifs et references `fichier:ligne`.
7. Absence de manifestes, tests, lint, typecheck et workflows applicatifs.

Aucun livrable n'est ecrit avant la fin de cette phase.

## Phase B - Redaction

Si un nouvel audit est demande, creer `docs/reports/audit-YYYY-MM-DD/`. Ne pas ecraser l'audit historique du 2026-11-21.

Livrables, dans cet ordre :

| Ordre | Fichier | Nature |
|---|---|---|
| 1 | `CODEBASE_ANALYSIS.md` | Faits verifies et bugs identifies. |
| 2 | `ANALYSE_CRITIQUE.md` | Jugement, notation et these centrale. |
| 3 | `RECOMMANDATIONS.md` | Actions priorisees et criteres d'acceptation. |
| 4 | `DOCUMENTATION-SYSTEM.md` | Systeme documentaire reel, pas architecture applicative. |
| 5 | `INDEX.md` | Navigation et sources de verite. |
| 6 | `README.md` | Mise a jour ciblee si necessaire. |
| 7 | `AGENTS.md` | Amelioration ciblee seulement. |

Chaque document substantiel sous `docs/**` utilise le frontmatter `id`, `title`, `version`, `status`, `classification`, `updated_at`.

## Phase C - Verifications

- [ ] References `fichier:ligne` existantes.
- [ ] Liens relatifs valides.
- [ ] IDs stables et comptes coherents.
- [ ] Aucun secret ni contenu prive recopie.
- [ ] Aucun U+2014.
- [ ] `git diff --check` passe.
- [ ] Statuts et classification cohens.

Terminer par la liste des fichiers crees ou modifies et le top 3 des constats.
