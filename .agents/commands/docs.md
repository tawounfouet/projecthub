---
description: Écrit ou met à jour une documentation ProjectHub. Use when the user invokes /docs, asks to write a README, update an index, or synchronize a doc.
---

Objectif : produire une documentation vérifiable et conforme aux politiques du dépôt.

Procédure :

1. Charger le skill `docs-writer`.
2. Lire `AGENTS.md`, `docs/PUBLICATION-POLICY.md` et `docs/COLLABORATION-BEST-PRACTICES.md`.
3. Identifier la source de vérité : fichiers suivis, `fichier:ligne`, décisions `PH-DEC-*`, état Git réel.
4. Ne jamais recopier `resources/`, `archives/`, transcript, credential ou donnée pilote.
5. Ne pas transformer un statut `draft` en approbation.
6. Ajouter le frontmatter requis pour les fichiers `docs/**/*.md` substantiels.
7. Mettre à jour les index concernés.
8. Vérifier liens relatifs, IDs, absence de U+2014 et `git diff --check`.
9. Ne pas committer sauf demande explicite séparée.

Les arguments transmis par l'utilisateur désignent le fichier cible et l'intention.

Sortie attendue : fichiers modifiés, changements apportés, vérifications finales.
