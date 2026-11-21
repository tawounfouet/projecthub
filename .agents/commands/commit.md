---
description: Prépare des commits atomiques conformes aux conventions du dépôt. Use when the user invokes /commit, asks to commit, or asks to split changes.
---

Objectif : produire un plan de commits relisible, sans action Git surprise.

Procédure :

1. Charger le skill `git-hygiene` et l'agent `ph-commit-planner`.
2. Exécuter `git status --short`, `git diff --stat`, `git diff --cached --stat` et `git log --oneline -5`.
3. Regrouper par intention unique : ignore rules, contenu, décision, déplacement, README, AGENTS, configuration locale.
4. Proposer des messages `type(scope): description` en minuscules, sans point final.
5. Vérifier qu'aucun secret, fichier `resources/`, fichier `archives/` ou fichier non intentionnel n'est inclus.
6. Présenter le plan et attendre confirmation avant `git add` et `git commit`.
7. Après exécution, vérifier `git log --oneline -5` et `git diff --check`.

Les arguments transmis par l'utilisateur peuvent préciser le périmètre ou le message souhaité.

Sortie attendue : plan de commits avec fichiers et messages, puis résultat après confirmation.
