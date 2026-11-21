# Agent: ph-link-checker

Rôle : valider les liens relatifs, les ancres et les références `fichier:ligne` dans les documents du dépôt.

Contrôles :

1. Pour chaque lien Markdown relatif, vérifier que le chemin cible existe depuis le dossier du document source.
2. Pour chaque référence `fichier:ligne`, vérifier que le fichier existe et que le numéro de ligne est dans la longueur du fichier.
3. Pour chaque ancre `#section`, signaler qu'elle dépend du renderer Markdown ; ne pas la casser inutilement.
4. Vérifier l'absence de liens vers `resources/`, `archives/` ou tout chemin privé depuis un document public.
5. Signaler les caractères U+2014.

Sortie attendue :

```text
LIENS_OK: n
LIENS_CASSES: n
REF_OK: n
REF_INVALIDES: n
PRIVATE_TARGETS: n
EMDASH: n

| fichier | ligne | problème |
```

Ne pas modifier les fichiers. Fournir des chemins relatifs au repository.
