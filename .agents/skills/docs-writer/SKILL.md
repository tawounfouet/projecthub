---
name: docs-writer
description: Ecrit ou met a jour la documentation ProjectHub a partir de faits verifies. Use when the user asks to write, update, synchronize, or rewrite a doc, README, index, or policy.
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: documentation
---

# Ecriture documentaire ProjectHub

## Source de verite

Dans ce depot, la source de verite n'est pas du code applicatif mais :

1. Les fichiers suivis par Git.
2. Les declarations `fichier:ligne` verifiables.
3. Les decisions `PH-DEC-*`.
4. Les politiques `docs/PUBLICATION-POLICY.md` et `docs/COLLABORATION-BEST-PRACTICES.md`.
5. L'etat reel de `git status`, `git log` et `.gitignore`.

## Regles

- Lire `AGENTS.md` avant toute modification de contenu.
- Lire `docs/PUBLICATION-POLICY.md` avant tout contenu public.
- Ne pas recopier `resources/`, `archives/`, transcripts, credentials ou donnees pilotes.
- Ne pas transformer une proposition en fait accompli.
- Ne pas modifier un statut `approved` sans decision mainteneur.
- Garder les IDs et les index synchronises.
- Prose principale en francais, sauf demande contraire.
- Aucun U+2014.

## Verifications avant de terminer

- Liens relatifs valides.
- Frontmatter present pour les `docs/**/*.md` substantiels.
- Tableaux d'index a jour.
- `git diff --check` passe.
- Statut `draft` et classification `public` coherents.

## Emplacements

| Type | Emplacement |
|---|---|
| Vitrine du depot | `README.md` |
| Regles agent | `AGENTS.md` |
| Carte SDLC | `SDLC.md` |
| Index public | `docs/README.md` |
| Audit historique | `docs/reports/audit-YYYY-MM-DD/` |
| Decisions | `docs/00-context/03-decisions-register.md` |
