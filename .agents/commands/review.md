---
description: Revue documentaire en lecture seule d'un fichier, d'un livrable ou d'un diff. Use when the user invokes /review, asks to relire un document, or asks to check a PR.
---

Objectif : relire sans modifier, en priorisant confidentialité, exactitude et gouvernance.

Procédure :

1. Charger le skill `docs-reviewer` et l'agent `ph-audit-reviewer`.
2. Lire le fichier ou le diff cible en entier.
3. Lire `AGENTS.md`, `docs/PUBLICATION-POLICY.md` et l'index concerné.
4. Vérifier références `fichier:ligne`, liens relatifs, IDs stables, statuts et classification.
5. Signaler tout secret, transcript, chemin `resources/` ou contenu `archives/` comme `blocking`.
6. Classer les retours : `blocking`, `important`, `nit`.
7. Ne pas éditer les fichiers.

Les arguments transmis par l'utilisateur désignent la cible de la revue.

Sortie attendue : `Summary`, `Issues`, `Nits`, `Positives`.
