---
name: docs-reviewer
description: Relit un diff ou un document ProjectHub pour exactitude, confidentialite, liens, IDs et coherence de statut. Use when the user asks to review docs, check a PR, or validate an audit deliverable.
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: review
---

# Revue documentaire ProjectHub

## Priorites

1. Confidentialite : aucun secret, transcript, chemin `resources/`, contenu `archives/` ou donnee pilote.
2. Exactitude : chaque fait critique possede une reference `fichier:ligne` existante.
3. Gouvernance : statut `draft` et classification `public` ne sont pas confondus avec une approbation.
4. Coherentiel : IDs `B1`..`B9`, `PH-DEC-*`, `PH-OPEN-*`, `PH-BLG-*`, `MVP-UJ-*`, `PH-REV-*` stables.
5. Navigation : liens relatifs valides, index synchronises.
6. Forme : pas de U+2014, tableaux lisibles, titres coherents.

## Method

1. Lire le diff ou le document en entier.
2. Lire `AGENTS.md`, `docs/PUBLICATION-POLICY.md` et l'index concerne.
3. Verifier les references et les liens en lecture seule.
4. Classer chaque retour : `blocking`, `important`, `nit`.
5. Proposer une correction sans modifier le fichier sauf demande explicite.

## Sortie

```text
## Summary
...

## Issues
### [blocking] titre
Fichier: ...
Probleme: ...
Correction: ...

## Nits
...

## Positives
...
```

Dans ce depot, un probleme de confidentialite ou une publication non approuvee est toujours `blocking`.
