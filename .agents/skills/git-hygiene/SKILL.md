---
name: git-hygiene
description: Prepare des commits atomiques en conventional commits pour ProjectHub. Use when the user asks to commit, prepare a PR, split changes, or clean git history.
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: git
---

# Hygiene Git ProjectHub

## Regle principale

Ne jamais lancer `git add`, `git commit`, `git push` ou `gh pr create` sans demande explicite de l'utilisateur.

## Workflow

1. Inspecter :

```bash
git status --short
git diff --stat
git diff --cached --stat
```

2. Regrouper par intention unique : ignore rules, contenu, decision, deplacement, README, AGENTS, configuration agent.
3. Formater le message : `type(scope): description`.
4. Utiliser des types coherents avec le depot : `fix`, `docs`, `chore`, `refactor`.
5. Ne pas mettre de point final, garder la description en minuscules et sous 72 caracteres.
6. Verifier le diff stage avant tout commit.
7. Verifier apres coup avec `git log --oneline -5`.

## Exemples deja utilises dans ce depot

```text
fix(B9): versionner les regles d'ignore de resources/ et archives/
fix(B1): formaliser la publication de la baseline exhaustive
docs(audit): deplacer les livrables sous docs/reports/audit-2026-11-21
docs(agents): aligner les regles avec l'audit traite
```

## Cas particuliers

- Ne pas committer `resources/`, `archives/` ou tout secret.
- Ne pas presenter un commentaire de conversation comme une revue GitHub approuvee.
- Sur un depot documentation-only, le preflight est `git diff --check` et la verification des liens.
