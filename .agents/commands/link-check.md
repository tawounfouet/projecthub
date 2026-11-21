---
description: Valide les liens relatifs, ancres et références fichier:ligne. Use when the user invokes /link-check or asks to check documentation links.
---

Objectif : contrôle en lecture seule de la navigation documentaire.

Procédure :

1. Charger l'agent `ph-link-checker`.
2. Parcourir les fichiers Markdown ciblés.
3. Vérifier que chaque lien relatif existe depuis le dossier du document source.
4. Vérifier que chaque référence `fichier:ligne` pointe vers un fichier existant et une ligne valide.
5. Signaler les liens vers `resources/`, `archives/` ou tout chemin privé depuis un document public.
6. Signaler les caractères U+2014.
7. Ne pas modifier les fichiers.

Les arguments transmis par l'utilisateur désignent le fichier ou le dossier à contrôler. Par défaut, contrôler `README.md`, `AGENTS.md`, `SDLC.md`, `docs/` et `.agents/`.

Sortie attendue : `LIENS_OK`, `LIENS_CASSES`, `REF_OK`, `REF_INVALIDES`, `PRIVATE_TARGETS`, `EMDASH`, puis tableau des problèmes.
