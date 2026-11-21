# Project skills

Ce dossier contient les definitions canoniques des skills utiles a ProjectHub. Elles sont independantes de la machine locale et suivent le depot sur un autre poste.

OpenCode ne charge pas automatiquement `.agents/skills/` comme dossier de skills. Les adaptateurs reellement charges sont dans `.opencode/skills/<name>/SKILL.md` ; chacun lit la definition canonique correspondante ici.

| Skill | Rôle |
|---|---|
| `repo-audit` | Audit documentaire sous `docs/reports/audit-YYYY-MM-DD/` avec references verifiables. |
| `sdlc-orchestrator` | Diagnostic SDLC adapte a un depot documentation-only. |
| `git-hygiene` | Commits atomiques en conventional commits, sans action Git automatique. |
| `session-archive` | Archivage structure dans `archives/chats/` avec rang incremente. |
| `docs-writer` | Ecriture et synchronisation documentaire a partir de faits verifies. |
| `docs-reviewer` | Revue documentaire : confidentialite, exactitude, liens, IDs et statuts. |

Regles communes :

- Ne jamais recopier de contenu prive de `resources/` ou `archives/`.
- Ne jamais faire d'action Git ou de publication sans demande explicite.
- Verifier les references `fichier:ligne` et les liens relatifs.
- Eviter le U+2014 dans tous les livrables.

Apres ajout ou modification d'un adaptateur dans `.opencode/skills/`, quitter et redemarrer OpenCode.
