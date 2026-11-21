# SDLC - ProjectHub

Ce fichier est une carte de navigation du cycle de vie du dépôt. Il décrit l'état observé le 2026-11-21 et les outils disponibles dans ce dépôt documentation-only. Ce n'est ni une preuve d'implémentation ni une approbation produit.

---

## Diagnostic du jour

| Contrôle | Résultat |
|---|---|
| `git status --short` | Propre |
| `git diff --cached --stat` | Aucun fichier staged |
| Tests | Non applicables : aucun runner, manifeste ou workflow détecté |
| Preflight | `git diff --check` passe ; validateur de liens inline : 0 erreur |
| Branche | `docs/fix-audit-bugs-b2-b9`, 6 commits locaux, non poussée |
| PR | Aucune PR ouverte |

Le dépôt ne contient pas d'application exécutable. Les contrôles disponibles sont donc documentaires : whitespace, liens relatifs, références `fichier:ligne`, cohérence des IDs et relecture humaine.

---

## Cycle complet

```text
[1 PLAN] ----> [2 BUILD] ----> [3 TEST] ----> [4 REVIEW] ----> [5 RELEASE] ----> [6 DEPLOY] ----> [7 MAINTAIN]
  TERMINE       TERMINE        N/A            ICI             SUIVANT         APRES           CONTINU
  audit +      B1..B9         pas de         PR Draft        relecture       push + merge   docs + dette
  PH-DEC-019   corriges        runner        a ouvrir        finale          si approuve    documentaire
  commits                     preflight      a relire        decision        pas de         validateur
  atomiques                   doc OK         par un pair     mainteneur      serveur        a implementer
```

---

## Phase courante : 4 - Review

Le travail de correction est terminé et committé sur une branche dédiée. Il reste à le rendre visible pour relecture, puis à demander une revue.

### Outils disponibles pour cette phase

| Outil | Usage |
|---|---|
| `/pr-review` | Revue de la branche entière par rapport à `main` |
| `/review` | Revue ciblée d'un fichier ou d'un diff |
| `@code-reviewer` | Revue structurée : sécurité, exactitude, performance, maintenabilité |
| `security-audit` (`ctrl+s`) | Recherche de fuites de secrets ou de contenu privé |
| `debug` (`ctrl+d`) | Investigation d'un problème détecté en revue |
| `git diff --check` | Contrôle whitespace disponible localement |

### Prochaines commandes

```bash
git push -u origin docs/fix-audit-bugs-b2-b9
gh pr create --draft --base main --head docs/fix-audit-bugs-b2-b9
```

Après ouverture de la PR Draft :

1. Lancer `/pr-review`.
2. Demander une relecture humaine explicite.
3. Passer la PR en Ready uniquement après correction des retours.
4. Ne pas fusionner tant que la relecture mainteneur n'est pas enregistrée.

---

## Détail des phases

| Phase | État dans ce dépôt | Preuve ou limite |
|---|---|---|
| 1 - Planification | Terminée pour l'audit | 5 livrables dans `docs/reports/audit-2026-11-21/`, décision `PH-DEC-019` |
| 2 - Développement | Terminé pour ce lot | 6 commits : B9, B2-B8, B1, déplacement audit, README, AGENTS |
| 3 - Testing | Non applicable | Aucun code, test, lint, typecheck ou CI configuré |
| 4 - Review | Courante | Branche locale prête, pas encore poussée ni relue |
| 5 - Release | À venir | Pas de tag applicatif prévu ; préparer le changelog de la PR si demandé |
| 6 - Deploy | À venir | Push, PR, puis merge par le mainteneur ; aucun serveur applicatif |
| 7 - Maintenance | Continue | Implémenter le validateur documentaire et traiter la dette listée dans l'audit |

---

## Phase 5 - Release

Déclenchement : après revue favorable.

Actions possibles :

- Résumer les 6 commits dans la description de PR.
- Vérifier que `README.md`, `AGENTS.md` et `docs/README.md` pointent vers les bons chemins.
- Ne pas créer de tag de version applicatif : ce dépôt ne livre pas de logiciel exécutable.
- Enregistrer toute décision de publication dans `docs/00-context/03-decisions-register.md`.

Outils : `/release`, `@release-prep`, `diff-summary`.

---

## Phase 6 - Deploy

Déclenchement : après relecture mainteneur.

Commandes possibles :

```bash
git push -u origin docs/fix-audit-bugs-b2-b9
gh pr ready
```

La fusion doit être décidée par le mainteneur. Aucun déploiement d'application n'est concerné.

Outils : `/commit`, skill `git-hygiene`, plugin `env-protection`.

---

## Phase 7 - Maintenance

Dette documentaire connue :

- Implémenter le validateur minimal proposé dans `docs/reports/audit-2026-11-21/RECOMMANDATIONS.md`.
- Brancher le contrôle des liens relatifs en mode hors réseau.
- Surveiller la dérive des statuts `draft`, des registres d'IDs et des classifications.
- Garder `archives/` et `resources/` ignorés par Git.
- Mettre à jour `docs/README.md` et `README.md` après chaque livrable ajouté.

Outils : `/docs`, `@docs-writer`, `find-todos`, skill `git-hygiene`.

---

## Liens utiles

- [Audit complet](docs/reports/audit-2026-11-21/INDEX.md)
- [Recommandations](docs/reports/audit-2026-11-21/RECOMMANDATIONS.md)
- [Décision `PH-DEC-019`](docs/00-context/03-decisions-register.md)
- [Politique de publication](docs/PUBLICATION-POLICY.md)
- [Bonnes pratiques de collaboration](docs/COLLABORATION-BEST-PRACTICES.md)
- [Instructions agent](AGENTS.md)

---

*Dernière mise à jour : 2026-11-21 - carte générée après le diagnostic SDLC de la branche `docs/fix-audit-bugs-b2-b9`.*
