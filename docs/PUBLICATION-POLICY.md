---
id: PH-DOC-PUB-001
title: "ProjectHub - Politique et processus de publication documentaire"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub maintainer"
created_at: "2026-11-20"
updated_at: "2026-11-20"
related_documents:
  - "docs/README.md"
  - "docs/00-context/00-project-history.md"
  - "docs/00-context/01-source-register.md"
---

# ProjectHub - Politique et processus de publication documentaire

> **Statut : draft.** Ce document formalise le processus proposé de publication des documents de ProjectHub dans le dépôt public. Sa présence dans GitHub ne vaut ni approbation des exigences produit, ni consentement des organisations citées dans les sources, ni autorisation de publier les documents privés.

## 1. Objet et principes

ProjectHub maintient deux éditions documentaires distinctes :

1. **Corpus privé exhaustif** : réflexions, sources, entretiens, analyses spécifiques aux organisations, annexes, arbitrages, constats techniques et documents de travail.
2. **Édition publique autonome** : vision produit, décisions publiables, exigences génériques, modèle conceptuel, MVP candidat, contributions et roadmap, après revue éditoriale et de confidentialité.

La publication publique n'est **jamais une synchronisation automatique** du corpus privé. La version publique doit rester compréhensible sans accès aux sources confidentielles.

Principes :
- **Confidentialité par défaut** : une information non explicitement autorisée reste privée.
- **Minimum nécessaire** : publier la connaissance utile au produit, pas les détails d'exploitation des organisations.
- **Traçabilité** : conserver les identifiants stables des concepts, exigences et décisions lorsque possible.
- **Exactitude** : distinguer les faits vérifiés, hypothèses, propositions, décisions et fonctionnalités réellement livrées.
- **Réversibilité éditoriale** : permettre de corriger un document, sans supposer qu'un contenu déjà rendu public peut être effacé d'Internet.
- **Relecture humaine** : aucun agent IA ne peut valider seul la publication de données tierces ou sensibles.

## 2. Classification et destination

| Classification | Exemples | Destination |
|---|---|---|
| Public | Vision générique, glossaire produit, diagrammes abstraits, API documentées | GitHub, après revue |
| Interne | Notes de cadrage, décisions non arrêtées, discussions d'équipe | Espace privé |
| Confidentiel | Comptes rendus, données associatives ou clients, analyses d'exploitation, entretiens nominatifs | Espace privé avec accès limité |
| Restreint | Secrets, clés, identifiants, détails de vulnérabilités, données personnelles non nécessaires | Systèmes sécurisés dédiés ; jamais dans GitHub ni dans les documents de pilotage |

**Interdit dans les commits, issues, PR et images publics :**
- secrets, jetons, configurations sensibles, adresses internes et chemins locaux révélateurs ;
- comptes rendus privés, verbatims d'entretiens ou données personnelles sans base de publication appropriée ;
- fichiers tiers dont la redistribution n'est pas autorisée ;
- risques ou incidents précis non destinés à la divulgation publique ;
- captures d'écran de systèmes réels montrant des données de clients, membres ou bénévoles.

La simple présence d'un nom d'organisation dans un document source ne prouve ni accord de participation ni permission d'utiliser son nom, sa marque ou ses résultats dans une communication publique.

## 3. Répertoire de travail et arborescence

Le dépôt public est `tawounfouet/projecthub` :
https://github.com/tawounfouet/projecthub

Les documents publics se trouvent dans `docs/`, organisés en :
- `00-context/`
- `01-product/`
- `02-discovery/`
- `03-requirements/`
- `04-domain/`
- `05-mvp/`
- `06-validation/`

Le corpus privé doit vivre **en dehors du clone du dépôt public**, dans un emplacement protégé, avec une politique d'accès et de sauvegarde appropriée. Un `.gitignore` ne constitue pas une frontière de sécurité suffisante.

Les images sélectionnées pour publication peuvent être placées dans `docs/assets/`, avec noms stables, attribution/licence vérifiée et texte alternatif pertinent. La sélection des illustrations se fait au cas par cas.

## 4. Correspondance privé -> public

| Élément | Politique |
|---|---|
| Identifiant documentaire | Réutiliser autant que possible l'ID stable |
| Nom du fichier | Identique si le sujet reste identique ; différent si la portée change fortement |
| Version | Versions privée et publique indépendantes |
| Sources | Remplacer les sources privées par références publiques ou identifiants anonymisés autorisés |
| Données réelles | Généraliser, agréger ou utiliser des exemples synthétiques |
| Statuts | Conserver `draft`, `in-review`, `approved`, `superseded` selon la validation réelle |
| Exigences | Garder les IDs et le statut candidat tant qu'elles ne sont pas approuvées |
| Annexes | Exclure les annexes sensibles ou les remplacer par une synthèse neutre |

L'anonymisation doit être évaluée sur le **contenu complet**, y compris le croisement avec d'autres informations publiques : retirer un nom ne garantit pas l'absence de réidentification.

## 5. Plan de publication en quatre lots

Le corpus Discovery Baseline V1.0 compte **25 documents principaux rédigés en version privée**. Ils ne sont pas tous approuvés ni publiables en l'état.

### PUBLIC-01 - Context & Product

- Réviser les deux documents déjà présents :
  - `docs/00-context/00-project-history.md`
  - `docs/00-context/01-source-register.md`
- Préparer six nouvelles éditions publiques :
  - `docs/00-context/02-canonical-context.md`
  - `docs/00-context/03-decisions-register.md`
  - `docs/00-context/04-open-questions.md`
  - `docs/01-product/00-product-vision.md`
  - `docs/01-product/01-product-strategy.md`
  - `docs/01-product/02-product-scope.md`
- Contrôler l'index et les avertissements sur les statuts de validation.

### PUBLIC-02 - Discovery

- `docs/02-discovery/00-stakeholders-and-personas.md`
- `docs/02-discovery/01-diversite-alternative-needs.md`
- `docs/02-discovery/02-webtech-solutions-needs.md`
- `docs/02-discovery/03-cross-organization-needs.md`
- `docs/02-discovery/04-current-vs-target-workflows.md`

**Traitement particulier :** les dossiers par organisation ne sont publiables que sous forme générique, anonymisée de manière robuste ou expressément approuvée par les représentants habilités. Le contenu spécifique peut rester entièrement privé ; publier un document public plus court ou un cas fictif si nécessaire.

### PUBLIC-03 - Requirements & Domain

- Les quatre documents de `docs/03-requirements/`
- Les trois documents de `docs/04-domain/`

Publier des exigences candidates, des règles génériques, des modèles conceptuels et des interfaces envisagées. Éviter les détails exploitables d'une infrastructure tierce, les politiques de droits nominatives et toute déclaration de conformité non démontrée.

### PUBLIC-04 - MVP & Validation

- Les trois documents de `docs/05-mvp/`
- Les deux documents de `docs/06-validation/`

Publier la définition candidate du MVP, le backlog expurgé, les parcours et le protocole de validation. La revue publique doit distinguer **complétude documentaire** et **approbation du jalon** ; aucun résultat de test, accord pilote, déploiement E1 ou lancement SaaS ne doit être présenté comme acquis s'il ne l'est pas.

## 6. Cycle de publication d'un lot

1. **Inventorier.** Identifier les versions privées exactes, les propriétaires, leur date et leurs sources.
2. **Qualifier.** Déterminer pour chaque section ce qui est public, à reformuler, à anonymiser ou à exclure.
3. **Rédiger une édition publique autonome.** Préserver les décisions et concepts utiles, sans copier les éléments privés.
4. **Contrôler.** Vérifier confidentialité, droits de publication, cohérence, liens, images, Markdown et historique des modifications.
5. **Proposer une branche et une pull request.** Une PR par lot, avec la liste des fichiers et des contrôles réalisés.
6. **Faire relire.** Le mainteneur examine le diff ; solliciter les responsables habilités de toute organisation concernée si une information qui la concerne doit être publiée.
7. **Approuver et fusionner.** Fusion uniquement après validation explicite du périmètre public et résolution des remarques.
8. **Tracer.** Mettre à jour l'index, la version, le statut documentaire et les décisions de publication.

Branche recommandée pour le premier lot : `docs/discovery-public-01`.

Titre suggéré pour la PR : `docs: publish sanitized Discovery context and product baseline`.

## 7. Contrôles obligatoires avant une PR

- [ ] Aucun secret, identifiant sensible, fichier d'environnement ou chemin de machine personnelle.
- [ ] Aucun document tiers, entretien ou compte rendu privé reproduit sans autorisation.
- [ ] Aucune personne, organisation, image, logo ou donnée réelle identifiable sans justification et accord appropriés.
- [ ] Aucune information de sécurité ou d'infrastructure privée exposée.
- [ ] Aucun engagement commercial, conformité, fonctionnalité, pilote ou test présenté comme validé sans preuve.
- [ ] IDs, liens et références internes cohérents avec les documents déjà publics.
- [ ] Statuts documentaires et hypothèses visibles ; changements de portée justifiés.
- [ ] Markdown lisible et liens relatifs corrects ; exemples et illustrations vérifiés.
- [ ] Diff de la PR vérifié dans son intégralité, y compris les suppressions et les fichiers binaires.
- [ ] Validation humaine obtenue et consignée avant fusion.

Des outils comme `markdownlint`, `gitleaks` et un vérificateur de liens peuvent renforcer les contrôles, mais **aucun pipeline n'est présumé configuré actuellement**. Le succès d'un scanner ne remplace pas la revue humaine.

## 8. Métadonnées minimales des éditions publiques

Chaque document substantiel doit déclarer un en-tête YAML :

```yaml
---
id: PH-DOC-EXAMPLE-001
title: "Titre du document"
version: "0.1.0"
status: draft
classification: public
updated_at: "YYYY-MM-DD"
sources: []
related_documents: []
---
```

Les documents publics n'exposent ni chemins vers les archives privées ni identifiants sensibles. Lorsqu'une source privée justifie une exigence, un identifiant de provenance expurgé peut suffire ; cela ne confère pas au public un droit d'accès à cette source.

## 9. Workflow GitHub reproductible

Les commandes suivantes sont des **exemples de procédure**, pas des actions déjà exécutées pour les lots PUBLIC-01 à PUBLIC-04.

```bash
git clone https://github.com/tawounfouet/projecthub.git
cd projecthub
git switch main
git pull --ff-only
git switch -c docs/discovery-public-01

# Ajouter uniquement les documents publics après revue locale.
git status --short
git diff --check
git diff --stat
git diff --cached --check

# Examiner précisément les modifications avant commit.
git add docs/
git diff --cached --stat
git diff --cached

git commit -m "docs: publish sanitized Discovery context and product baseline"
git push -u origin docs/discovery-public-01

# Après installation et authentification GitHub CLI :
gh pr create --base main --head docs/discovery-public-01   --title "docs: publish sanitized Discovery context and product baseline"   --body "Publication expurgée du lot PUBLIC-01 ; revue humaine requise."
```

**Attention :** l'exemple `git add docs/` n'est sûr que si tous les nouveaux fichiers de `docs/` ont été relus et sont publiables. Pour davantage de sûreté, ajouter les fichiers un par un. Aucun fichier privé ne doit être présent dans le clone public.

Les changements de processus, tels que la présente politique, peuvent faire l'objet d'un commit de maintenance distinct des lots documentaires.

## 10. Conditions de décision et responsabilités

| Rôle | Responsabilité |
|---|---|
| Auteur / agent assistant | Prépare et vérifie une proposition, signale les incertitudes |
| Mainteneur ProjectHub | Décide du contenu à proposer, relit la PR et autorise la fusion |
| Référent métier | Confirme l'exactitude des formulations métier si elles concernent son périmètre |
| Responsable habilité d'une organisation tierce | Autorise ou refuse la publication de ses informations, selon les règles applicables |
| Relecteur sécurité / confidentialité, si désigné | Examine les risques de divulgation et les données personnelles |

Toute demande d'agent IA de publier une source interne doit être soumise à l'approbation humaine pertinente. Le mainteneur de ProjectHub ne peut pas, du seul fait de son rôle, autoriser la divulgation de données appartenant à une autre organisation.

## 11. Réaction à une divulgation accidentelle

1. Interrompre la diffusion et avertir le mainteneur.
2. Évaluer immédiatement la nature du contenu exposé, les personnes ou organisations concernées et les mesures de protection nécessaires.
3. Révoquer/renouveler sans délai les secrets compromis ; ne pas attendre un simple retrait du fichier.
4. Corriger le dépôt et étudier le traitement de l'historique Git avec les responsables compétents.
5. Informer les parties concernées et appliquer les procédures d'incident et obligations éventuelles.
6. Conserver un rapport d'incident dans un espace privé.

**Supprimer un fichier ou réécrire l'historique Git ne garantit pas la disparition des copies, forks, caches ou clones déjà créés.**

## 12. Politique de licence et de communication

À la date de cette première politique, le choix de licence open source est **à arbitrer**. Rendre un dépôt public ne signifie pas que son contenu est automatiquement placé sous une licence open source.

Ne pas annoncer la disponibilité d'un produit stable, un niveau de sécurité certifié, des engagements de service ou une adhésion officielle des pilotes sans éléments probants et validation.

## 13. Critères de fin du lot PUBLIC-01

Le lot PUBLIC-01 est terminé seulement si :
- les deux documents publics existants ont été revus ;
- les six nouvelles éditions publiques ont été rédigées et relues ;
- l'index documentaire est mis à jour ;
- la revue de confidentialité, d'exactitude et de droits de publication est consignée ;
- la PR est fusionnée sur `main` par décision du mainteneur.

**L'ajout de cette politique ne lance ni ne valide à lui seul PUBLIC-01.**

---

**Historique des modifications**
- 2026-11-20 - `0.1.0` : première édition du processus de publication documentaire, issue de la préparation de ProjectHub Discovery Baseline V1.0.
