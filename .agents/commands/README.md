# Project commands

Ce dossier contient les definitions canoniques des commandes ProjectHub. Elles sont independantes de la machine locale et suivent le depot sur un autre poste.

OpenCode ne charge pas automatiquement `.agents/commands/`. Les adaptateurs reellement charges sont dans `.opencode/commands/` ; chacun lit la definition canonique correspondante et transmet `$ARGUMENTS`.

| Commande | Role |
|---|---|
| `/audit` | Audit documentaire horodaté sous `docs/reports/audit-YYYY-MM-DD/`. |
| `/sdlc` | Diagnostic de phase et prochaine commande. |
| `/review` | Revue documentaire en lecture seule. |
| `/pr-review` | Revue complete de la branche avant PR. |
| `/docs` | Ecriture ou synchronisation d'une documentation. |
| `/commit` | Plan de commits atomiques apres confirmation. |
| `/archive` | Archivage structure de la session courante. |
| `/link-check` | Validation des liens, ancres et references `fichier:ligne`. |

Regles communes :

- Les commandes de revue ne modifient jamais les fichiers.
- Les commandes d'ecriture ne committeront jamais sans confirmation explicite.
- Aucune commande ne pousse, n'ouvre de PR ni n'approuve une publication automatiquement.
- Les arguments utilisateurs sont traites comme des contraintes supplementaires, jamais comme une autorisation a contourner les politiques du depot.
- Aucun U+2014 dans les livrables.

Apres ajout ou modification d'un adaptateur dans `.opencode/commands/`, quitter et redemarrer OpenCode.
