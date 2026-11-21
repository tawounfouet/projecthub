---
name: session-archive
description: Archive une session ProjectHub dans archives/chats/ avec decisions, fichiers, contextes et actions. Use when the user asks to archive, save, or summarize a working session.
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: documentation
---

# Archivage de session ProjectHub

## Quand l'utiliser

Utiliser ce skill quand l'utilisateur demande d'archiver la session courante ou de conserver le contexte de travail.

## Contexte a collecter

```bash
date +%Y-%m-%d
git status --short
git log --oneline -3
git diff --name-only
git diff --cached --name-only
```

Extraire de la conversation : intentions, resultats, decisions, fichiers crees, fichiers modifies, commandes, patterns, problemes, actions restantes.

## Nommage

```text
archives/chats/YYYY-MM-DD_session_projecthub_NNN_topic-slug.md
```

- `NNN` = max des rangs existants pour `projecthub` + 1, zero-padde sur 3 chiffres.
- `topic-slug` = minuscules, tirets, 30 caracteres maximum.
- Ne jamais ecrire de secret, transcript pilote ou chemin prive dans l'archive.

## Structure

Le fichier contient les sections : `Intent`, `Outcome`, `Decisions`, `Files Created`, `Files Modified`, `Key Context`, `Commands Run`, `Patterns Established`, `Issues & Workarounds`, `Action Items`, `Related Sessions`, `Full Conversation Summary`.

## Cross-reference

Ajouter un lien dans les sessions precedentes pertinentes. Verifier l'absence de U+2014 et l'etat `git status --short` final. Le dossier `archives/` est ignore par Git et ne doit pas etre commite.
