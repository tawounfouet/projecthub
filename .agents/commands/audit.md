---
description: Audit documentaire horodaté de ProjectHub. Use when the user invokes /audit, asks to auditer ce repo, or asks to générer les docs d'audit.
---

Objectif : produire un audit vérifiable dans `docs/reports/audit-YYYY-MM-DD/` sans écraser l'audit historique du 2026-11-21.

Procédure :

1. Charger le skill `repo-audit`.
2. Lire `AGENTS.md`, `docs/PUBLICATION-POLICY.md` et `docs/reports/audit-2026-11-21/INDEX.md`.
3. Réaliser la Phase A complète avant toute rédaction : racine, Git, politiques, index, registres, liens, confidentialité.
4. Ne recopier aucun contenu de `resources/`, `archives/`, transcript, credential ou donnée pilote.
5. Écrire les livrables dans l'ordre : `CODEBASE_ANALYSIS.md`, `ANALYSE_CRITIQUE.md`, `RECOMMANDATIONS.md`, `DOCUMENTATION-SYSTEM.md`, `INDEX.md`.
6. Mettre à jour `README.md` et `AGENTS.md` seulement si nécessaire.
7. Vérifier références `fichier:ligne`, liens relatifs, IDs stables, absence de U+2014 et `git diff --check`.
8. Ne pas committer, pousser ni publier.

Les arguments transmis par l'utilisateur précisent le périmètre ou les contraintes supplémentaires.

Sortie attendue : liste des fichiers créés ou modifiés, top 3 des constats, vérifications finales.
