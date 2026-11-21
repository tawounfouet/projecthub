# Project agents, skills and commands

Ce dossier contient les définitions canoniques des agents, skills et commandes utiles à ProjectHub. Elles sont indépendantes de la machine locale : elles vivent dans le dépôt et suivent donc le projet sur un autre poste.

OpenCode ne charge pas automatiquement `.agents/` comme dossier d'agents, de skills ou de commandes. Les adaptateurs réellement chargés sont dans `.opencode/agents/`, `.opencode/skills/` et `.opencode/commands/` ; chacun lit la définition canonique correspondante ici.

- agents : voir le tableau ci-dessous
- skills : voir `.agents/skills/README.md`
- commandes : voir `.agents/commands/README.md`

| Agent | Rôle |
|---|---|
| `ph-docs-guardian` | Vérifie la confidentialité et la politique de publication avant tout contenu public. |
| `ph-audit-reviewer` | Relit un audit ou un livrable documentaire sans le modifier. |
| `ph-sdlc-guide` | Diagnostique la phase SDLC et propose la prochaine commande. |
| `ph-link-checker` | Valide les liens relatifs, les ancres et les références `fichier:ligne`. |
| `ph-commit-planner` | Prépare des commits atomiques conformes aux conventions du dépôt. |

Règles communes :

- Ne jamais recopier le contenu de `resources/` ni d'`archives/` dans un document public.
- Ne jamais présenter un statut `draft` comme approuvé.
- Ne jamais créer de commit, push ou PR sans demande explicite.
- Utiliser des références `fichier:ligne` vérifiables.
- Remplacer tout tiret cadratin par un tiret ASCII `-`.

Après ajout ou modification d'un adaptateur dans `.opencode/agents/`, quitter et redémarrer OpenCode.
