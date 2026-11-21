---
name: sdlc-orchestrator
description: Guide le projet ProjectHub dans les 7 phases SDLC et recommande la prochaine commande. Use when the user runs /sdlc, asks what to do next, or discusses the development lifecycle.
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: sdlc
---

# Orchestration SDLC ProjectHub

Ce skill utilise `SDLC.md` comme carte courante. Il tient compte du fait que le depot ne livre pas d'application executable.

## Diagnostic

Toujours verifier :

```bash
git status --short
git diff --cached --stat
git log --oneline -5
git diff --check
```

Ne pas proposer `npm run test`, `pytest`, `ruff`, `npm run lint` ou deploy applicatif sauf si un runner apparait reellement dans le depot.

## Phases

| Phase | Etat type dans ProjectHub | Outils utiles |
|---|---|---|
| 1 Plan | Audit, decisions, specifications | `architect` (`ctrl+a`), agent `plan`, skill `docs-writer` |
| 2 Build | Corrections documentaires, commits | skill `git-hygiene`, agent `ph-commit-planner` |
| 3 Test | Souvent non applicable | `git diff --check`, link checker inline |
| 4 Review | Branche prete, PR a ouvrir | `/pr-review`, `/review`, `ph-audit-reviewer`, `ctrl+s` |
| 5 Release | PR relue, resume des changements | `diff-summary`, `/release` si demande |
| 6 Deploy | Push, PR, merge par mainteneur | `git push`, `gh pr create`, `ph-commit-planner` |
| 7 Maintain | Documentation et dette | `/docs`, `ph-link-checker`, `find-todos` |

## Sortie attendue

```text
Phase courante: N - nom
Preuves: ...
Outils disponibles: ...
Prochaine commande: ...
```

Ne jamais pousser, creer de PR ou approuver une publication sans demande explicite.
