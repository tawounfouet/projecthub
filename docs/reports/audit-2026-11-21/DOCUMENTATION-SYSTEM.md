# Architecture - ProjectHub

> Document de référence technique : comment le dépôt est construit et comment les informations circulent. Il décrit le système **tel qu'il est** au 2026-11-21. Les jugements sont dans [`ANALYSE_CRITIQUE.md`](./ANALYSE_CRITIQUE.md) et les faits d'audit dans [`CODEBASE_ANALYSIS.md`](./CODEBASE_ANALYSIS.md).

---

## 1. Vue système

```text
[Archive privée locale resources/internal/**]        [Sources publiques externes]
        |  non suivie : resources/LISEZ-MOI.txt:1      |  exemples : docs/00-context/01-source-register.md:33-49
        |  revue manuelle : docs/PUBLICATION-POLICY.md:22-35
        v
[Éditions publiques docs/00-context .. docs/06-validation]  (25 éditions, statut draft)
        |  docs/README.md:13-25
        +--> [Index et politiques docs/README.md, PUBLICATION-POLICY.md, COLLABORATION-BEST-PRACTICES.md]
        +--> [Registres PH-OPEN / PH-BLG / MVP-UJ / PH-REV] : docs/07-architecture/01-documentation-quality-ci-plan.md:177-185
        v
[Plans post-Discovery docs/07-architecture/] --> [baseline PH-AEB-001 : INTERNAL] : docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:2-13
        |
        v
[GitHub : tawounfouet/projecthub] : docs/PUBLICATION-POLICY.md:57-58
        |  PR Draft -> commentaire mainteneur -> fusion : docs/COLLABORATION-BEST-PRACTICES.md:67-81
        v
[main : 48 fichiers suivis, 41 Markdown, 4 PNG, 2 YAML] : git ls-files
```

**Topologie de déploiement réelle :**

| Composant | Hébergement | Particularité |
|---|---|---|
| Dépôt public | GitHub `tawounfouet/projecthub` (`docs/PUBLICATION-POLICY.md:57-58`) | Aucun service applicatif ; le contenu est des fichiers Markdown, PNG et YAML (`git ls-files`). |
| Espace de travail local | Copie locale avec `resources/` et des modifications non commitées | `resources/` est privé et non suivi (`resources/LISEZ-MOI.txt:15-17`) ; `.gitignore:43` contient la règle `resources/` dans l'arbre de travail (B9). |
| Issues publiques | Templates `.github/ISSUE_TEMPLATE/` | Deux formulaires avec avertissement de confidentialité (`.github/ISSUE_TEMPLATE/bug_report.yml:1-7`, `.github/ISSUE_TEMPLATE/feature_request.yml:1-7`). |
| CI | Aucune | Aucun `.github/workflows/` présent ; le plan est `NOT_IMPLEMENTED` (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`). |

---

## 2. Dépôt documentaire

### 2.1 Organisation

Le dépôt contient trois couches : un index public (`README.md:1-9`, `docs/README.md:1-11`), un corpus de 25 éditions publiques réparties dans sept dossiers (`docs/README.md:13-25`), et des ajouts post-Discovery qui ne comptent pas dans ces 25 (`docs/README.md:80-91`). Les documents substantifs portent un frontmatter `id`, `title`, `version`, `status`, `classification`, `updated_at` (`docs/PUBLICATION-POLICY.md:160-177`) ; les README sont exemptés (`docs/07-architecture/01-documentation-quality-ci-plan.md:103`).

La classification est portée par le frontmatter, pas par le dossier : la baseline de `docs/07-architecture/` reste `INTERNAL - exhaustive working edition` (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:6`), tandis que les plans voisins sont `public` (`docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:6`, `docs/07-architecture/01-documentation-quality-ci-plan.md:6`). C'est la situation B1, documentée comme exception à examiner dans `docs/07-architecture/README.md:13-17`.

### 2.2 Cycle de vie d'une publication

```text
Sources privées ou publiques
  -> qualifier ce qui est public, à reformuler, à anonymiser ou à exclure
  -> rédiger une édition publique autonome
  -> contrôler confidentialité, droits, cohérence, liens, images et diff
  -> proposer une branche et une PR
  -> relecture du mainteneur
  -> approbation et fusion
  -> mettre à jour index, version, statut et décisions
```
Étapes vérifiées en `docs/PUBLICATION-POLICY.md:130-139`. Le circuit effectif utilisé pour les lots PUBLIC-01 à PUBLIC-04 est décrit en `docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:72-87` : PR Draft, relecture, commentaire d'accord, réponse dans la discussion, `squash merge`, vérification de `main`. Pour les PR #7 à #11, l'historique local montre cinq commits de fusion à deux parents (`git log --merges --pretty='%h %p %s'`).

### 2.3 Flux métier clés

**Flux A - d'une source privée à une édition publique**

```text
[resources/**]
   |  ⚠️ franchissement de la frontière de confidentialité
   |  aucune synchronisation automatique : docs/PUBLICATION-POLICY.md:27
   v
[édition publique réécrite] -> [frontmatter public] -> [index] -> [PR]
```
Les sources privées ne sont pas reproducibles telles quelles ; les références `PH-OPS-*` sont génériques (`docs/00-context/01-source-register.md:18`, `:49`). Un agent IA ne peut pas valider seul une publication sensible (`docs/PUBLICATION-POLICY.md:35`).

**Flux B - mise à jour d'un registre d'IDs**

```text
[table canonique] -> [lecture de la première colonne] -> [contrôle de continuité]
```
La règle est définie en `docs/07-architecture/01-documentation-quality-ci-plan.md:169-199` : les quatre registres sont `PH-OPEN-001..030`, `PH-BLG-001..045`, `MVP-UJ-01..10`, `PH-REV-001..020` (`:177-185`). Les plages et les citations répétées ne sont pas des enregistrements (`:186`, `:199`). Les bugs B5, B6 et B8 montrent des écarts dans ce flux.

**Flux C - préparation E0**

```text
[ADR PROPOSED : docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:60-85]
   |  décisions à prendre ; POC NOT_RUN : :11-12
   v
[E0 avec deux Organizations fictives : docs/05-mvp/00-mvp-definition.md:35-40]
   |  ⚠️ aucune donnée réelle
   v
[huit gates NOT_ASSESSED avant E1 : docs/06-validation/00-pilot-validation-plan.md:111-124]
```
E1 reste `No-Go` tant que les accords et les gates ne sont pas prouvés (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:1648`).

---

## 3. Modèle de données

Il n'existe ni base de données ni ORM dans le dépôt : les seules données persistantes sont des fichiers suivis par Git (`git ls-files`). Le « modèle » est donc documentaire.

```text
Source (privée ou publique)
   +--< Édition publique (id, title, version, status, classification, updated_at)
          +--< Index (docs/README.md et READMEs de dossiers)
          +--< Registre (PH-OPEN, PH-BLG, MVP-UJ, PH-REV)
          +--< Asset local (PNG référencé)
          +--< Plan ou rapport post-Discovery
```

| Objet | Attributs vérifiés | Référence |
|---|---|---|
| Édition publique | `id`, `title`, `version`, `status`, `classification`, `updated_at` ; `sources` et `related_documents` optionnels | `docs/PUBLICATION-POLICY.md:160-177` |
| Cycle de statut | `draft`, `in-review`, `approved`, `superseded` | `docs/README.md:113-120` |
| Registre canonique | Préfixe, largeur, plage, fichier propriétaire et section | `docs/07-architecture/01-documentation-quality-ci-plan.md:177-185` |
| Gate E1 | Identifiant `G-*`, preuve attendue, état `NOT_ASSESSED` | `docs/06-validation/00-pilot-validation-plan.md:111-124` |
| Archive privée | 73 fichiers locaux, non suivis, contenant notamment des sources et dossiers internes | `resources/LISEZ-MOI.txt:1`, `:15-17` ; `find resources -type f` |

Les données métier décrites dans les documents (Organization, Workspace, Project, WorkItem, memberships, grants, mandats) sont des propositions conceptuelles, pas des tables persistées : le modèle de domaine est présenté comme candidat (`docs/04-domain/01-domain-model.md:19`) et la baseline indique que les 13 domaines ne doivent pas nécessairement devenir 13 modules (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:193`).

---

## 4. Interface

L'interface est le rendu Markdown sur GitHub et les deux formulaires d'issue. Le README racine affiche une illustration et des badges de pile cible (`README.md:7-9`, `:25-35`) ; l'index public organise les documents par lots (`docs/README.md:13-25`, `:27-91`) ; les formulaires d'issue imposent des champs et affichent un avertissement de confidentialité (`.github/ISSUE_TEMPLATE/bug_report.yml:3-7`, `.github/ISSUE_TEMPLATE/feature_request.yml:3-7`).

Il n'y a pas de state management client, de `localStorage`, de cookie applicatif ni de route frontend (`git ls-files`, `README.md:5`). Les liens relatifs sont la primitive de navigation : 243 liens locaux ont été analysés pendant l'audit sans cible manquante, et le plan recommande un contrôle hors réseau avec Lychee (`docs/07-architecture/01-documentation-quality-ci-plan.md:149-159`). La casse des noms de fichiers doit être vérifiée malgré un système macOS non sensible à la casse (`:151-155`).

---

## 5. Conventions transverses à connaître

| Sujet | Convention |
|---|---|
| Frontmatter | Champs `id`, `title`, `version`, `status`, `classification`, `updated_at` sur les documents substantifs ; README exemptés (`docs/PUBLICATION-POLICY.md:160-177`, `docs/07-architecture/01-documentation-quality-ci-plan.md:103`). |
| Statuts | `draft`, `in-review`, `approved`, `superseded` ; la publication GitHub ne change pas le statut (`docs/README.md:113-120`, `:66`, `:78`). |
| IDs canoniques | `PH-OPEN-001..030`, `PH-BLG-001..045`, `MVP-UJ-01..10`, `PH-REV-001..020` ; compter la première colonne des tableaux propriétaires (`docs/07-architecture/01-documentation-quality-ci-plan.md:177-199`). |
| Confidentialité | Réécriture manuelle, minimum nécessaire, relecture humaine ; aucun agent ne valide seul une donnée tierce (`docs/PUBLICATION-POLICY.md:22-35`). |
| Chemins privés | Aucun chemin d'archive privée dans les éditions publiques (`docs/PUBLICATION-POLICY.md:177`) ; l'ignore local est `resources/` (`.gitignore:43`, B9). |
| Liens | Liens relatifs privilégiés ; liens externes vérifiés dans une tâche séparée, avec exclusions datées (`docs/07-architecture/01-documentation-quality-ci-plan.md:146-167`). |
| Fusion | Lots PUBLIC-01 à PUBLIC-04 fusionnés en `squash merge` (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:29`, `:83`) ; PR #7 à #11 visibles comme fusions à deux parents dans `git log`. |
| Configuration d'exemple | Variables requises écrites en placeholders `${...:?required}`, sans valeur réelle (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:1240-1253`). |
| ADR et preuves | Statut `PROPOSED`, POC `NOT_RUN`, preuves `NOT_RUN` ; aucune exécution n'est attestée par la publication (`docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:9-12`, `:196-209`). |

---

## 6. Limites structurelles - résumé

Ces choix sont détaillés et argumentés dans [`ANALYSE_CRITIQUE.md`](./ANALYSE_CRITIQUE.md) :

1. La baseline `INTERNAL` est suivie dans le dépôt public sans décision de publication consignée (B1).
2. La protection de l'archive privée n'est pas versionnée (B9).
3. Plusieurs documents décrivent un état antérieur à la fusion effective (B2, B3, B7).
4. Une formulation laisse croire que des éditions `draft` sont validées (B4).
5. Les correspondances NFR/tests et backlog/gates ne sont pas bijectives (B5, B6).
6. Deux ordres de priorité coexistent pour les `PH-OPEN` (B8).
7. Aucun contrôle automatisé ne vérifie la classification, les IDs ou les liens (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`, `docs/PUBLICATION-POLICY.md:158`).

Les correctifs correspondants sont dans [`RECOMMANDATIONS.md`](./RECOMMANDATIONS.md).
