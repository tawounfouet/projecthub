# Analyse de la codebase - ProjectHub

> Analyse réalisée le 2026-11-21. Périmètre : 48 fichiers suivis, la confidentialité documentaire, l'intégrité des registres d'IDs et la dette de vérification. Aucun secret n'est reproduit dans ce document.

<!-- Document FACTUEL : chaque affirmation vérifiable est accompagnée d'une référence `fichier:ligne`. Le jugement est dans ./ANALYSE_CRITIQUE.md. Les bugs B1..B9 sont réutilisés à l'identique dans tous les livrables. -->

---

## 1. Vue d'ensemble

ProjectHub est un dépôt de recherche documentaire en phase Discovery, et non une application fonctionnelle : l'avertissement officiel figure en `README.md:5` et dans `docs/README.md:5`. Les choix Django/DRF, Next.js/React/TypeScript et PostgreSQL sont des cibles proposées, pas du code livré (`README.md:23-31`, `docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:91-93`).

| Package | Stack | LOC | Rôle |
|---|---|---:|---|
| `README.md` (racine) | Markdown + badges GitHub | 72 | Positionnement produit et avertissement de statut (`README.md:1`, `README.md:5`) |
| `docs/` racine et `docs/00-context` à `docs/06-validation` | Markdown, PNG locaux | 6 371 | 25 éditions publiques de Discovery, index et politiques (`docs/README.md:13-25`, `docs/README.md:113-120`) |
| `docs/07-architecture` | Markdown | 2 740 | Plans ADR/CI et baseline exhaustive non approuvée (`docs/07-architecture/README.md:7-11`) |
| `docs/reports` | Markdown | 157 | Bilan de publication et limites de preuve (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:19`) |
| `resources/` | Markdown et PNG locaux | hors LOC suivies | Archive privée non suivie par Git (`resources/LISEZ-MOI.txt:1`, `resources/LISEZ-MOI.txt:15-17`) |

Les LOC sont mesurées par `git ls-files '*.md' | xargs wc -l` : 8 111 lignes Markdown suivies au total. Le relevé `git ls-files` donne 48 fichiers suivis, dont 41 `.md`, 4 `.png`, 2 `.yml` et 1 fichier sans extension. Le dossier local `resources/` contient 73 fichiers, dont 46 `.md` et 24 `.png`, alors que `resources/INVENTAIRE.json:2-5` déclare 32 documents Markdown et 20 images ; l'écart est vérifiable par `find resources -type f`.

**Caractéristiques générales :**

- Aucun manifeste de package, workspace, lockfile, serveur, test, lint ou build n'est détecté parmi les fichiers suivis ; le plan de CI documentaire précise que ses scripts sont à créer (`docs/07-architecture/01-documentation-quality-ci-plan.md:98-100`, `:226`).
- Aucun workflow GitHub Actions n'est présent sous `.github/workflows/` ; `.github/` ne contient que deux templates d'issue (`.github/ISSUE_TEMPLATE/bug_report.yml:1`, `.github/ISSUE_TEMPLATE/feature_request.yml:1`). La politique constate qu'aucun pipeline n'est présumé configuré (`docs/PUBLICATION-POLICY.md:158`).
- Le dépôt est donc un dépôt de documentation, pas un monorepo applicatif. Les seules « données » suivies sont Markdown, PNG et YAML de templates d'issue (`git ls-files`).
- L'état local avant audit comporte `.gitignore` et `README.md` modifiés, plus `AGENTS.md` non suivi ; cet audit décrit cet état de travail, pas un commit immutable (`git status --short`).
- L'historique local contient 28 commits, dont cinq fusions à deux parents pour les PR #7 à #11 ; les lots PUBLIC-01 à PUBLIC-04 ont été fusionnés sous forme de commits à parent unique (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:37-44`, `git log --pretty='%h %p %s' --reverse`).

---

## 2. Architecture

```text
[Corpus privé local resources/internal/**]  (non suivi)
        |  réécriture manuelle et revue humaine : docs/PUBLICATION-POLICY.md:22-35
        v
[Éditions publiques docs/00-context/ .. docs/06-validation/]  (25 documents, statut draft)
        |------------------------------> [docs/README.md : index public] : docs/README.md:13-25
        |------------------------------> [registres PH-OPEN / PH-BLG / MVP-UJ / PH-REV] : docs/07-architecture/01-documentation-quality-ci-plan.md:177-186
        v
[Plans post-Discovery docs/07-architecture/] ----> [baseline PH-AEB-001, classification INTERNAL] : docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:2-13
        |
        v
[PR Draft -> relecture mainteneur -> décision humaine -> main] : docs/COLLABORATION-BEST-PRACTICES.md:67-81
```

### 2.1 Publication documentaire

Le circuit repose sur deux éditions distinctes : corpus privé exhaustif et édition publique autonome (`docs/PUBLICATION-POLICY.md:22-25`). La publication n'est jamais une synchronisation automatique (`docs/PUBLICATION-POLICY.md:27`) et aucun agent IA ne peut valider seul une donnée tierce ou sensible (`docs/PUBLICATION-POLICY.md:35`). Les contrôles obligatoires sont une checklist humaine, dont l'absence de secret, de document tiers non autorisé et de statut présenté comme validé sans preuve (`docs/PUBLICATION-POLICY.md:145-156`).

### 2.2 Registres et traçabilité

Quatre registres canoniques sont identifiés comme vérifiables : `PH-OPEN-001..030`, `PH-BLG-001..045`, `MVP-UJ-01..10` et `PH-REV-001..020` (`docs/07-architecture/01-documentation-quality-ci-plan.md:177-185`). Le même document avertit qu'une plage comme `PH-REQ-001..130` ne crée pas 130 enregistrements publics (`docs/07-architecture/01-documentation-quality-ci-plan.md:186`, `:199`). Les conventions de frontmatter et de cycle de statut sont décrites en `docs/README.md:113-120`.

### 2.3 Topologie de déploiement réelle

Aucun composant applicatif déployable n'est présent : pas de Dockerfile, de configuration Vercel/Netlify, de service ou de script de démarrage dans les fichiers suivis (`git ls-files`). Le plan de CI documentaire propose un workflow futur `.github/workflows/docs-quality.yml` et un validateur `scripts/docs_quality.py`, tous deux absents et marqués `NOT_IMPLEMENTED` (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`, `:98-100`).

---

## 3. Inventaire des surfaces de publication

Il n'existe aucune route HTTP ni endpoint applicatif. Le tableau ci-dessous est une adaptation obligatoire du template aux surfaces réelles du dépôt : fichiers par lesquels une information devient publique ou est présentée comme décisionnaire. La colonne « Contrôle » décrit l'état vérifié, pas une garantie.

| Surface | Contenu notable | Contrôle réel |
|---|---|---|
| `README.md:5`, `README.md:23-31` | Statut Discovery et pile cible | Avertissement textuel ; aucune validation automatique (`docs/PUBLICATION-POLICY.md:158`) |
| `docs/README.md:13-25`, `:80-91` | Index des 25 éditions et ajouts post-Discovery | Statuts maintenus manuellement ; B7 concerne des actions déjà réalisées (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:136`, `:139`) |
| `docs/PUBLICATION-POLICY.md:145-158` | Checklist de publication | Relecture humaine requise ; aucun pipeline configuré (`:158`) |
| `docs/00-context/04-open-questions.md:28-43`, `:119-126` | Ordre des arbitrages | Deux classements divergents : B8 |
| `docs/03-requirements/01-non-functional-requirements.md:39`, `:58-65`, `:122` | Famille d'isolation et tests proposés | `PH-NFR-010` sans scénario dédié : B5 |
| `docs/05-mvp/02-prioritized-backlog.md:141-148` | Huit items Gate | Correspondance non bijective avec les huit gates : B6 |
| `docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:5-13` | Baseline exhaustive | Classification `INTERNAL` et fichier suivi : B1 |
| `.github/ISSUE_TEMPLATE/bug_report.yml:7`, `.github/ISSUE_TEMPLATE/feature_request.yml:7` | Avertissements de confidentialité | Consignes textuelles seulement |

En gras : surfaces posant problème (voir §4 et §5).

---

## 4. Sécurité - vulnérabilités

### 🔴 Critiques

- **Aucune vulnérabilité critique confirmée dans ce dépôt de documentation.** Il n'y a ni endpoint exécutable ni application déployée (`README.md:5`, `git ls-files`) et aucun secret avec valeur n'a été identifié dans les fichiers analysés. Les exemples de configuration de la baseline utilisent des placeholders `${...:?required}` (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:1240-1253`). Cette absence constatée ne dispense pas de la revue humaine prescrite en `docs/PUBLICATION-POLICY.md:145-156`.

### 🟠 Élevées

- **B1 - Exposition d'une édition exhaustive classée `INTERNAL`.** La baseline porte `classification: "INTERNAL - exhaustive working edition"` et `status: "DRAFT / PROPOSED - NOT APPROVED"` (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:5-6`), alors que l'index du dossier exige une relecture intégrale et une confirmation explicite du mainteneur avant publication (`docs/07-architecture/README.md:15-17`). Le fichier est suivi par Git et l'index principal le décrit comme « non expurgé, à examiner spécialement » (`docs/README.md:88`). Effet concret : une version de travail non sanctionnée est lisible dans un dépôt public, et la politique « confidentialité par défaut » (`docs/PUBLICATION-POLICY.md:30`) n'est plus opposable par la seule classification du fichier.
- **B9 - Règle d'ignore de l'archive privée non versionnée.** `.gitignore:43` contient `resources/` dans l'arbre de travail, mais `git show HEAD:.gitignore` ne contient aucune entrée `resources/`. L'archive est décrite comme privée et non publiable telle quelle (`resources/LISEZ-MOI.txt:15-17`) et contient 73 fichiers localement (`find resources -type f`). Effet concret : un clone de `HEAD` n'hérite pas de cette protection ; un `git add -A` peut indexer des sources confidentielles.

### 🟡 Moyennes

- **B4 - Statut de validation suggéré par une formulation ambiguë.** `docs/00-context/02-canonical-context.md:142` appelle le dépôt « source de vérité des éditions publiques validées », alors que le même document est `status: draft` en `:5` et que le risque d'approbation implicite est explicite en `docs/01-product/README.md:29`. Effet concret : un lecteur ou un agent peut traiter des brouillons comme des exigences approuvées.
- **Absence de filet automatisé de confidentialité.** Le plan documentaire indique `implementation_status: NOT_IMPLEMENTED` et `validation_status: PROPOSED` (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`) ; la politique rappelle qu'un scanner éventuel ne remplace pas la revue humaine (`docs/PUBLICATION-POLICY.md:158`). Effet concret : B1, B2, B3, B7 et B8 ne sont détectés que par relecture.

---

## 5. Bugs confirmés

Les bugs de ce dépôt sont des défauts documentaires vérifiables par lecture, pas des erreurs d'exécution applicative. Leur effet est décrit en termes de décision ou de vérification concrète.

| # | Fichier:ligne | Bug |
|---|---|---|
| B1 | `docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:5-6` ; `docs/07-architecture/README.md:15-17` ; `docs/README.md:88` | Baseline `INTERNAL` suivie dans le dépôt public sans confirmation de publication consignée dans ces fichiers : l'édition exhaustive non expurgée reste accessible et le garde-fou de classification est contourné. |
| B2 | `docs/07-architecture/01-documentation-quality-ci-plan.md:222` ; `git ls-files docs/07-architecture/` | Le plan affirme que `07-architecture/` est « présent sur la PR #11, pas encore sur main », alors que ses quatre fichiers sont suivis : la carte des fichiers du validateur est périmée et peut faire échouer ou mal interpréter une future CI. |
| B3 | `docs/00-context/03-decisions-register.md:80` ; `docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:37-44` ; `docs/README.md:66`, `:78` | Le registre affirme que PUBLIC-01 est seulement « en proposition de pull request » alors que les lots PUBLIC-01 à PUBLIC-04 sont fusionnés : l'état affiché du jalon est faux et invite à republier un lot terminé. |
| B4 | `docs/00-context/02-canonical-context.md:142` ; `:5` ; `docs/01-product/README.md:29` | L'expression « éditions publiques validées » coexiste avec des statuts `draft` et un avertissement explicite : le document peut être lu comme une approbation métier jamais enregistrée. |
| B5 | `docs/03-requirements/01-non-functional-requirements.md:39` ; `:58-65` ; `:122` | `PH-NFR-010` appartient à la famille `001..010` mais n'a ni épreuve dans le tableau de tests proposés ni ligne dans la fiche de vérification `001..009` : une exigence `P0-G` d'isolation peut être déclarée couverte sans scénario ni critère préétabli. |
| B6 | `docs/05-mvp/02-prioritized-backlog.md:141-148` ; `docs/06-validation/00-pilot-validation-plan.md:115-122` | Les huit items `PH-BLG-038..045` ne correspondent pas un à un aux huit gates : `PH-BLG-039` regroupe `G-ACCESS` et `G-SECRETS`, et `PH-BLG-045` est la décision Go/No-Go. Un suivi « 8/8 items faits » ne prouve donc pas les huit gates séparément. |
| B7 | `docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:136`, `:139` ; `docs/README.md:11`, `:78`, `:88` | Le bilan recommande encore de corriger l'index pour référencer le bilan et de préparer la baseline, alors que les deux sont déjà présents : appliquer ces actions à la lettre duplique le travail et peut relancer la publication d'un document `INTERNAL`. |
| B8 | `docs/00-context/04-open-questions.md:34-41` ; `:121-124` | `PH-OPEN-021` et `PH-OPEN-009` figurent dans les « arbitrages à préparer en premier » puis sont classés respectivement aux groupes 2 et 4 : deux lecteurs peuvent choisir des priorités différentes pour les mêmes questions. |
| B9 | `.gitignore:43` ; `git show HEAD:.gitignore` ; `resources/LISEZ-MOI.txt:15-17` | La protection `resources/` n'existe que dans l'arbre de travail, pas dans `HEAD` : après un clone, l'archive privée n'est pas ignorée et peut être ajoutée par erreur. |

---

## 6. Dette technique et risques environnementaux

### 6.1 Code

Aucun code applicatif n'est présent ; la dette est documentaire. Les états périmés se concentrent dans `docs/07-architecture/01-documentation-quality-ci-plan.md:222` (B2), `docs/00-context/03-decisions-register.md:80` (B3) et `docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:136-139` (B7). Les registres d'IDs ne sont pas encore validés par un script, alors que le contrat de validation existe déjà (`docs/07-architecture/01-documentation-quality-ci-plan.md:169-199`).

### 6.2 Obsolescence

Aucun manifeste ni dépendance installée n'est détectable (`git ls-files`), donc aucune version EOL mesurable. La baseline indique que les versions des composants cibles doivent être épinglées par ADR et que la matrice correspondante n'est pas figée (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:660-667`). Le plan CI donne des versions d'exemple non épinglées et exige un SHA complet avant adoption (`docs/07-architecture/01-documentation-quality-ci-plan.md:282-288`).

### 6.3 Configuration bloquante

Les seules vérifications disponibles sont `git diff --check` et `git status --short`, conformément à la procédure de contrôle local (`docs/COLLABORATION-BEST-PRACTICES.md:320-329`) et à la section d'exécution locale du plan (`docs/07-architecture/01-documentation-quality-ci-plan.md:473-486`). Le plan de vérification des liens recommande un mode hors réseau pour les PR et traite les liens externes dans une tâche séparée (`docs/07-architecture/01-documentation-quality-ci-plan.md:149-167`). Aucun serveur de développement, variable d'environnement requise ni service externe n'est nécessaire pour ce dépôt de documentation (`README.md:5`, `git ls-files`).

---

## 7. Points forts

- La séparation entre corpus privé et éditions publiques est explicitement documentée et impose une relecture humaine (`docs/PUBLICATION-POLICY.md:22-35`).
- Le statut `draft` est maintenu malgré la fusion des lots, ce qui évite de présenter des spécifications candidates comme approuvées (`docs/README.md:66`, `:78`).
- Les registres canoniques et la règle de comptage des IDs sont définis avant l'automatisation (`docs/07-architecture/01-documentation-quality-ci-plan.md:177-199`).
- Les limites de preuve sont répétées dans les documents de synthèse : publication ne vaut pas validation (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:19`, `:33`).
- Le contrôle des liens relatifs effectué pendant l'audit ne trouve aucune cible manquante parmi 243 liens locaux analysés hors blocs de code (`python` inline, lecture seule).

---

## 8. Recommandations priorisées

1. **P0 -** versionner la règle `resources/` et obtenir une décision mainteneur documentée sur la baseline `INTERNAL` (B1, B9).
2. **P1 -** corriger les états périmés et la formulation de validation (B2, B3, B4, B7).
3. **P2 -** combler le trou de vérification `PH-NFR-010` et aligner backlog/gates (B5, B6).
4. **P3 -** unifier les deux classements de priorités `PH-OPEN` (B8).
5. **P4 -** mettre en oeuvre le validateur documentaire décrit mais non implémenté, sans le confondre avec une validation métier (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`, `:490-500`).

Le plan détaillé, les correctifs et les critères d'acceptation sont dans `./RECOMMANDATIONS.md`.

---

*Méthodologie : lecture intégrale de la racine, des politiques, des 25 éditions Discovery, des ajouts post-Discovery et de la baseline de 1 815 lignes ; vérification croisée des fichiers suivis, du `.gitignore`, de l'historique Git, des liens relatifs et des registres d'IDs. Chaque bug du §5 est justifié par une ligne de fichier précise. Le jugement associé est dans `./ANALYSE_CRITIQUE.md`.*
