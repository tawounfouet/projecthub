# INDEX - Documentation du projet

Point d'entrée de toute la documentation d'audit. Ce dossier contient **5 livrables d'audit** ; avec `README.md` et `AGENTS.md` à la racine, l'ensemble compte **7 documents Markdown**. Cette page sert de sommaire et de guide de navigation. Les bugs B1 et B9 décrits ci-dessous ont été traités après la rédaction de l'audit ; ce document conserve l'état observé au 2026-11-21.

---

## 1. Les documents

| Document | Rôle | Contenu en une ligne | À lire quand… |
|---|---|---|---|
| [`CODEBASE_ANALYSIS.md`](./CODEBASE_ANALYSIS.md) | Faits | État réel du dépôt, surfaces de publication, vulnérabilités et bugs B1..B9 avec `fichier:ligne`. | Il faut une référence factuelle vérifiable avant de modifier un document. |
| [`ANALYSE_CRITIQUE.md`](./ANALYSE_CRITIQUE.md) | Jugement | Verdicts /10, pattern systémique de dérive des garde-fous et option réparer ou réécrire. | Il faut comprendre pourquoi les neuf bugs se reproduisent. |
| [`RECOMMANDATIONS.md`](./RECOMMANDATIONS.md) | Action | Phases 0 à 5, correctifs B1..B9, validateur minimal et critères d'acceptation. | Il faut appliquer les correctifs sans réanalyser le dépôt. |
| [`DOCUMENTATION-SYSTEM.md`](./DOCUMENTATION-SYSTEM.md) | Référence | Système tel qu'il est : flux de publication, registres, modèle documentaire et conventions. | Il faut comprendre comment les fichiers et les IDs sont reliés. |
| [`INDEX.md`](./INDEX.md) | Navigation | Cette page : sommaire, navigation par tâche et repères chiffrés. | On ne sait pas par où commencer. |
| [`README.md`](../../../README.md) | Vitrine | Positionnement produit, statut Discovery et liens vers les livrables d'audit. | On arrive dans le dépôt ou on cherche son statut officiel. |
| [`AGENTS.md`](../../../AGENTS.md) | Instructions agent | Règles de confidentialité, conventions documentaires et workflow vérifié. | Un agent ou un contributeur va modifier le dépôt. |

**Ordre de lecture suggéré** : `README.md` -> `INDEX.md` -> `CODEBASE_ANALYSIS.md` -> `ANALYSE_CRITIQUE.md` -> `DOCUMENTATION-SYSTEM.md` -> `RECOMMANDATIONS.md` -> `AGENTS.md`.

---

## 2. Navigation par tâche

| Je veux… | Aller à |
|---|---|
| Vérifier s'il y a une application à lancer | [`CODEBASE_ANALYSIS.md` §1](./CODEBASE_ANALYSIS.md#1-vue-densemble) et [`README.md`](../../../README.md) (`README.md:5`) |
| Configurer un environnement ou des variables | [`DOCUMENTATION-SYSTEM.md` §5](./DOCUMENTATION-SYSTEM.md#5-conventions-transverses-à-connaître) : seuls des placeholders sont présents (`CODEBASE_ANALYSIS.md` §6.3) |
| Comprendre le flux privé vers public | [`DOCUMENTATION-SYSTEM.md` §2.3, flux A](./DOCUMENTATION-SYSTEM.md#23-flux-métier-clés) |
| Retrouver un bug précis | [`CODEBASE_ANALYSIS.md` §5](./CODEBASE_ANALYSIS.md#5-bugs-confirmés), registre B1..B9 |
| Connaître les failles de sécurité | [`CODEBASE_ANALYSIS.md` §4](./CODEBASE_ANALYSIS.md#4-sécurité---vulnérabilités) : B1 et B9 en 🟠, aucun 🔴 confirmé |
| Commencer à corriger | [`RECOMMANDATIONS.md` Phase 0](./RECOMMANDATIONS.md#phase-0---urgence-immédiate), puis Phase 2 pour B2..B8 |
| Écrire les contrôles de remplacement des tests | [`RECOMMANDATIONS.md`, filet de sécurité](./RECOMMANDATIONS.md#filet-de-sécurité--suite-de-contrôles-minimale) |
| Moderniser la vérification documentaire | [`RECOMMANDATIONS.md` Phase 5](./RECOMMANDATIONS.md#phase-5---modernisation) |
| Publier une mise à jour | [`docs/PUBLICATION-POLICY.md`](../../PUBLICATION-POLICY.md) et [`DOCUMENTATION-SYSTEM.md` §2.2](./DOCUMENTATION-SYSTEM.md#22-cycle-de-vie-dune-publication) |
| Décider si E1 peut démarrer | [`DOCUMENTATION-SYSTEM.md` §2.3, flux C](./DOCUMENTATION-SYSTEM.md#23-flux-métier-clés) : E1 reste `No-Go` |
| Comprendre pourquoi la baseline est un risque | [`ANALYSE_CRITIQUE.md` §3.1](./ANALYSE_CRITIQUE.md#31-le-modèle-à-deux-éditions-est-défendable-mais-son-exception-nest-pas-opérationnelle) |
| Savoir quelles règles un agent doit respecter | [`AGENTS.md`](../../../AGENTS.md) |

---

## 3. Carte rapide du code source

Le dépôt n'a pas de code applicatif ; la « carte du code » est une carte des sources de vérité documentaires (`README.md:5`, `git ls-files`).

| Domaine | Point d'entrée | Cœur du système |
|---|---|---|
| Documentation publique | [`README.md`](../../../README.md) (`README.md:5`) | [`docs/README.md`](../../README.md) (`docs/README.md:13-25`) |
| Politique de publication | [`docs/PUBLICATION-POLICY.md`](../../PUBLICATION-POLICY.md) (`docs/PUBLICATION-POLICY.md:22`) | Checklist et avant-PR (`docs/PUBLICATION-POLICY.md:145-158`) |
| Registres d'IDs | [`docs/00-context/04-open-questions.md`](../../00-context/04-open-questions.md) (`docs/00-context/04-open-questions.md:28`) | Contrat des quatre registres (`docs/07-architecture/01-documentation-quality-ci-plan.md:177-199`) |
| Architecture | [`docs/07-architecture/README.md`](../../07-architecture/README.md) (`docs/07-architecture/README.md:7`) | Baseline `PH-AEB-001` (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:2-13`) |
| Bilan de lot | [`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md`](../2026-11-21-discovery-baseline-publication-bilan.md) (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:19`) | Workflow réellement utilisé (`:72-87`) |
| Archive privée | `resources/LISEZ-MOI.txt` (`resources/LISEZ-MOI.txt:1`) | Non suivie par Git ; ne jamais lier depuis un document public |

Fichiers à connaître absolument avant toute modification :

- `docs/PUBLICATION-POLICY.md` : publication manuelle et relecture humaine (`:22-35`, `:145-158`).
- `docs/07-architecture/README.md` : décision `PH-DEC-019` de publication de la baseline (`:13-17`).
- `docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md` : statut `DRAFT / PROPOSED`, 1 815 lignes (`:5`, `:38`).
- `docs/07-architecture/01-documentation-quality-ci-plan.md` : plan `NOT_IMPLEMENTED` et registres canoniques (`:10-11`, `:177-199`).
- `docs/reports/2026-11-21-discovery-baseline-publication-bilan.md` : état réel des lots et limites de preuve (`:26-44`, `:100-106`).
- `AGENTS.md` : garde-fous pour les sessions suivantes.

---

## 4. Repères chiffrés

- 48 fichiers suivis par Git ; 41 Markdown, 4 PNG, 2 YAML et 1 fichier sans extension (`git ls-files`).
- 8 111 lignes Markdown suivies (`git ls-files '*.md' | xargs wc -l`) ; la baseline exhaustive représente 1 815 lignes (`docs/07-architecture/README.md:10`).
- 25 éditions publiques de Discovery Baseline V1.0 (`docs/README.md:25`), plus des ajouts post-Discovery non comptés dans ce total (`docs/README.md:80-91`).
- 9 bugs confirmés B1..B9 (`CODEBASE_ANALYSIS.md` §5).
- 0 vulnérabilité 🔴 confirmée, 2 🟠 (B1, B9) et 2 🟡 (`CODEBASE_ANALYSIS.md` §4).
- 0 workflow GitHub Actions, 0 script de test, 0 manifeste de dépendances (`CODEBASE_ANALYSIS.md` §1 et §2.3).
- 243 liens Markdown relatifs analysés, aucun ne pointant vers une cible manquante au moment de l'audit (`CODEBASE_ANALYSIS.md` §7).
- 73 fichiers dans l'archive locale `resources/`, non suivis par Git (`find resources -type f`, `resources/LISEZ-MOI.txt:15-17`).

---

*Dernière mise à jour : 2026-11-21 - documents générés lors d'un audit complet du dépôt.*
