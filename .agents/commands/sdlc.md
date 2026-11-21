---
description: Diagnostique la phase SDLC courante de ProjectHub. Use when the user invokes /sdlc, asks what to do next, or discusses the development lifecycle.
---

Objectif : situer le dépôt dans `SDLC.md` et proposer la prochaine commande exacte.

Procédure :

1. Charger le skill `sdlc-orchestrator` ou l'agent `ph-sdlc-guide`.
2. Lire `SDLC.md` et `AGENTS.md`.
3. Exécuter `git status --short`, `git diff --cached --stat`, `git log --oneline -5` et `git diff --check`.
4. Vérifier l'absence de manifestes, tests, lint, typecheck et workflows avant toute recommandation.
5. Ne pas proposer de commande npm, pytest, ruff ou déploiement applicatif sauf preuve réelle dans le dépôt.
6. Ne pas pousser ni ouvrir de PR sans demande explicite.

Les arguments transmis par l'utilisateur peuvent forcer une phase particulière : `plan`, `build`, `test`, `review`, `release`, `deploy`, `maintain`.

Sortie attendue : phase courante, preuves, outils disponibles, prochaine commande.
