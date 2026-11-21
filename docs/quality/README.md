# Contrôles automatisés de la documentation

Ce dossier documente le lot P0 `ACT-02`. Le validateur fonctionne **hors réseau**, sans secrets, sans accès à `resources/` ni aux archives privées. Il ne modifie aucun fichier.

## Commandes reproductibles

```bash
python -m pip install -r docs/quality/requirements.txt
python -m unittest discover -s tests -p 'test_docs_quality.py' -v
python scripts/docs_quality.py --strict
```

La CI `.github/workflows/docs-quality.yml` exécute les deux dernières commandes sur chaque PR vers `main`, sur les pushes `main` et via déclenchement manuel. Les actions de checkout et de configuration Python sont épinglées à des SHA complets ; les dépendances Python ont des versions fixées.

## Contrôles couverts

- Existence et validité YAML du frontmatter pour `docs/**/*.md`, à l'exception des fichiers `README.md` et des **cinq instantanés d'audit historiques** explicitement listés dans `scripts/docs_quality.py`.
- Unicité des `id` documentaires, champs requis, `classification: public`, date et cycle des statuts.
- Statut particulier de `PH-AEB-001` accepté **uniquement sur son chemin historique** en tant que publication `PH-DEC-019`. Cette exception de syntaxe ne vaut pas approbation métier ou technique.
- Continuité et unicité des lignes canoniques des quatre registres `PH-OPEN`, `PH-BLG`, `MVP-UJ`, `PH-REV`, sans compter les citations ni les plages synthétiques.
- Cibles locales des liens et images Markdown/HTML, casse des chemins et refus des chemins sortant du dépôt. Les fragments d'ancre et les liens externes ne sont pas contrôlés dans ce lot.
- Quatorze tests sur fixtures synthétiques, dont des exemples volontairement invalides de chaque famille principale.

Les messages d'erreur n'affichent ni extraits de documents ni contenu d'archive privée. La CI ne remplace pas la revue manuelle de confidentialité, les approbations produit ni la décision de fusion. Les modifications des listes d'exceptions requièrent une revue explicite et un motif documenté.
