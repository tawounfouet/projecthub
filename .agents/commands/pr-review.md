---
description: Revue complète de la branche courante avant PR. Use when the user invokes /pr-review or asks to relire une branche entière.
---

Objectif : préparer la phase 4 Review sans ouvrir ni fusionner de PR.

Procédure :

1. Vérifier `git status --short`, `git branch --show-current`, `git log --oneline -5` et `git diff main...HEAD --stat`.
2. Charger le skill `docs-reviewer` et l'agent `ph-audit-reviewer`.
3. Relire tous les commits de la branche par rapport à `main`.
4. Contrôler confidentialité, références, liens, IDs, statuts, classification et cohérence des index.
5. Activer mentalement le mode `security-audit` (`ctrl+s`) pour détecter tout contenu privé.
6. Ne pas pousser, ouvrir de PR ni approuver la publication.

Les arguments transmis par l'utilisateur peuvent restreindre la revue à un chemin ou à un motif.

Sortie attendue : verdict `OK` ou `CORRECTIONS_REQUISES`, puis tableau des findings par gravité.
