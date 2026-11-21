---
description: Archive la session courante dans archives/chats/. Use when the user invokes /archive or asks to save a session summary.
---

Objectif : créer un enregistrement structuré et non commité de la session courante.

Procédure :

1. Charger le skill `session-archive`.
2. Exécuter `date +%Y-%m-%d`, `git status --short`, `git log --oneline -3`, `git diff --name-only` et `git diff --cached --name-only`.
3. Déterminer le rang suivant dans `archives/chats/` pour `projecthub`.
4. Choisir un `topic-slug` minuscule, hyphené, 30 caractères maximum.
5. Rédiger les sections standards : `Intent`, `Outcome`, `Decisions`, `Files Created`, `Files Modified`, `Key Context`, `Commands Run`, `Patterns Established`, `Issues & Workarounds`, `Action Items`, `Related Sessions`, `Full Conversation Summary`.
6. Ne jamais inclure secret, transcript pilote, chemin privé de `resources/` ou contenu de `archives/`.
7. Ajouter un lien dans la session précédente pertinente.
8. Vérifier absence de U+2014 et `git status --short`.

Les arguments transmis par l'utilisateur peuvent imposer le sujet de l'archive.

Sortie attendue : chemin complet de l'archive créée et session précédente mise à jour.
