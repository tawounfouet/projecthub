---
id: PH-CTX-OPEN-001
title: "ProjectHub - Questions ouvertes publiques"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-001, PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/00-context/03-decisions-register.md"
  - "docs/01-product/02-product-scope.md"
---

# ProjectHub - Questions ouvertes et arbitrages

> **Registre canonique de questions candidates.** Les identifiants `PH-OPEN-001` à `PH-OPEN-030` sont conservés depuis le registre privé, mais les formulations sont expurgées. Les 30 questions sont actuellement `OPEN` : aucune décision explicite, traçable et autorisée n'est consignée ici. Une référence à un ID dans un autre document ne change pas son statut ; l'absence de réponse n'est pas un accord implicite.

## 1. Priorité et portes de décision

- **P0** : nécessaire pour figer le parcours MVP, les frontières d'accès, la revue ou la sécurité de données réelles.
- **P1** : nécessaire pour une évolution ciblée, un pilote opérationnel ou une distribution Community.
- **P2** : peut être différé à une phase Cloud, commerciale ou avancée.
- **Externe** : décision relevant d'une organisation tierce, non du mainteneur ProjectHub.

La priorité décrit le **moment où décider**, pas l'obligation de développer la fonctionnalité.

### Arbitrages à préparer en premier

Cette vue donne un ordre de travail et les preuves minimales attendues. Les personnes responsables ne sont pas encore désignées ; les rôles indiqués doivent être attribués avant le jalon correspondant. Les horizons sont des portes de décision, pas des dates promises.

| ID | Décideur / responsable à désigner | Jalon | Preuve ou sortie minimale |
|---|---|---|---|
| `PH-OPEN-007` | Responsable produit / recherche | Avant de retenir un segment utilisateur | Entretiens autorisés sur des situations récentes, solutions actuelles, effets et contre-exemples |
| `PH-OPEN-001` | Autorité produit | Après la synthèse de découverte, avant de figer le MVP | Petit nombre de parcours, exclusions et critères observables reliés aux preuves |
| `PH-OPEN-024` | Responsable du parcours de passation | Avant de retenir la passation dans le MVP | Exercice où un successeur distinct réalise une action définie ; aide reçue et réserves consignées |
| `PH-OPEN-016` | Responsable du modèle de domaine | Avant de figer le modèle métier | Scénarios comparés pour Client, Organization, Workspace et Team, répercutés dans le glossaire et le modèle |
| `PH-OPEN-002` | Responsable produit / accès | Avant de figer les permissions E0 | Matrice acteur-action-ressource, révocation et scénarios négatifs |
| `PH-OPEN-006` | Responsable architecture / sécurité | Avant toute implémentation multi-tenant à évaluer en E0 | Frontière canonique, modèle d'isolation et tests négatifs planifiés |
| `PH-OPEN-021` | Responsable qualité / risque | Avant toute décision E1 | Scénarios, mesures, seuils justifiés et autorité d'approbation pour les NFR applicables |
| `PH-OPEN-009` | Autorité habilitée de chaque organisation concernée | Avant toute donnée réelle en E1 | Autorisation institutionnelle et périmètre de données explicites ; aucun rôle n'est présumé |

La première tâche de gouvernance est de désigner ces responsables et d'enregistrer leurs décisions. Ne pas inventer de noms, de dates, d'accords ou de preuves pour remplir le tableau.

## 2. Questions Product / MVP

| ID | Question | Priorité candidate | Pour résoudre | Statut / décision liée |
|---|---|---|---|---|
| `PH-OPEN-001` | Quel parcours constitue le plus petit MVP utile ? | P0 | Valider scénario, exclusions et critères de recette | `OPEN` |
| `PH-OPEN-007` | Quel utilisateur prioritaire et quelle promesse mesurable ? | P0 | Entretiens avec utilisateurs et décideurs | `OPEN` |
| `PH-OPEN-012` | Quels indicateurs prouvent un bénéfice réel ? | P1 | Baseline, définition et protocole de mesure | `OPEN` |
| `PH-OPEN-017` | Comment représenter objectifs, livrables et responsables ? | P0 | Scénarios et vocabulaire approuvés | `OPEN` |
| `PH-OPEN-020` | Quel premier mode de déploiement : démonstration isolée ou multi-tenant ? | P0 | Plan E0/E1 et exigences d'isolation | `OPEN` |
| `PH-OPEN-023` | Table, Board, Roadmap : quelles vues réellement utiles au MVP ? | P1 | Test d'usage comparatif | `OPEN` |
| `PH-OPEN-024` | Comment démontrer la reprise d'un projet ? | P0 | Scénario de passation et vérification de l'autonomie | `OPEN` |

## 3. Domaine / permissions / données

| ID | Question | Priorité candidate | Pour résoudre | Statut / décision liée |
|---|---|---|---|---|
| `PH-OPEN-002` | Quels rôles, memberships, délégations et droits effectifs ? | P0 | Matrice RBAC, tests de refus et révocation | `OPEN` |
| `PH-OPEN-003` | Quel domaine possède décisions, risques et actions ? | P0 | Propriété canonique, événements et invariants | `OPEN` |
| `PH-OPEN-006` | Comment garantir l'isolation multi-tenant et l'évolution Cloud ? | P0 sécurité / P1 détail Cloud | Modèle de données, tests et preuve | `OPEN` |
| `PH-OPEN-016` | Comment séparer Client, Organization, Workspace et Team ? | P0 | Glossaire et cas inter-organisation | `OPEN` |
| `PH-OPEN-021` | Quel minimum non fonctionnel avant données réelles ? | P0 | Contrôles observables et seuils approuvés | `OPEN` |
| `PH-OPEN-026` | Comment gérer export, rétention, suppression et réversibilité ? | P0 E1 | Protocole de sortie et tests | `OPEN` |
| `PH-OPEN-027` | Quel niveau d'accessibilité et comment le vérifier ? | P1 avant pilote spécialisé | Parcours, référentiel et tests | `OPEN` |
| `PH-OPEN-029` | Comment représenter dépôt, environnement, service et composant ? | P1 | Modèle des références techniques sans mélange avec Project | `OPEN` |

## 4. Intégrations, documentation, IA

| ID | Question | Priorité candidate | Pour résoudre | Statut / décision liée |
|---|---|---|---|---|
| `PH-OPEN-004` | Quelle première intégration et quel niveau de synchronisation ? | P1 | Cas concret, coûts de permission et conflits de données | `OPEN` |
| `PH-OPEN-011` | Quelles bibliothèques externes/internes seraient réutilisables ? | P2 | Audit de code, licence et qualité | `OPEN` |
| `PH-OPEN-013` | Quelles sources peut exploiter une éventuelle IA ? | P2 | Autorisations, modèle de données et tests de fuite | `OPEN` |
| `PH-OPEN-022` | Où conserver la documentation et son historique ? | P1 | Source de vérité, liens et droits | `OPEN` |
| `PH-OPEN-025` | Comment importer le travail existant sans double saisie ? | P1 | Mapping, nettoyage et réversibilité | `OPEN` |
| `PH-OPEN-028` | Quel rôle pour les agents IA, et quels droits ? | P2 ; P0 si action réelle | Identités techniques, audit et approbation humaine | `OPEN` |

## 5. Pilotes, gouvernance et distribution

| ID | Question | Priorité candidate | Pour résoudre | Statut / décision liée |
|---|---|---|---|---|
| `PH-OPEN-005` | Quelle licence et quelle gouvernance de contribution ? | P1 avant distribution du code | Droits IP, compatibilité et politique | `OPEN` |
| `PH-OPEN-008` | Quel tarif et quelle unité de facturation Cloud ? | P2 | Entretiens acheteurs, coûts d'exploitation | `OPEN` |
| `PH-OPEN-009` | Quelles autorisations institutionnelles et données de pilote ? | P0 externe avant E1 | Accords, rôles et périmètre documentés | `OPEN` |
| `PH-OPEN-010` | Comment sécuriser une transmission opérationnelle indépendante du logiciel ? | P0 externe | Plan de passation porté par l'organisation concernée | `OPEN` |
| `PH-OPEN-014` | Qui détient les droits et qui peut opérer commercialement ProjectHub ? | P1 | Arbitrage juridique et de gouvernance | `OPEN` |
| `PH-OPEN-015` | Qui relit et approuve les éditions publiques ? | P0 publication | Politique désormais écrite ; relecteur effectif à désigner | `OPEN` |
| `PH-OPEN-018` | Quels niveaux d'assistance et d'exploitation pendant les pilotes ? | P1 | Engagements proportionnés et autorisés | `OPEN` |
| `PH-OPEN-019` | Quel état actuel des travaux issus des analyses historiques ? | P0 externe | Vérification auprès des responsables autorisés | `OPEN` |
| `PH-OPEN-030` | Qui approuve la baseline Discovery et ses réserves ? | P0 | Décision écrite du responsable compétent | `OPEN` |

Le classement ne doit pas être lu comme une validation de l'importance de chaque besoin auprès d'un utilisateur réel.

## 6. Dossier de décision minimal

Pour fermer une question, documenter :
- son ID stable, son décideur et la date ;
- au moins deux options ou une justification du choix unique ;
- les preuves collectées et les hypothèses ;
- la décision et ses effets sur les besoins, le MVP et le backlog ;
- les scénarios de validation et les risques résiduels ;
- le lien vers `03-decisions-register.md` et, le cas échéant, un ADR.

Certaines décisions peuvent être clôturées **pour E0** tout en restant ouvertes pour E1 ou Cloud.

## 7. Cycle de vie et statut des IDs

Le tableau des questions de ce document est la source de vérité de leur statut. Un ID cité dans un parcours, une exigence ou une proposition ne constitue ni une question supplémentaire ni une mise à jour de statut.

- `OPEN` : question non résolue ; toutes les 30 entrées sont actuellement dans cet état.
- `DECIDED` : décision prise par une autorité compétente ; garder la ligne et indiquer le `PH-DEC-*` correspondant, sa portée et sa date.
- `SUPERSEDED` : question remplacée ; garder la ligne et indiquer le `PH-OPEN-*` qui lui succède.

Ne pas supprimer un ID résolu ou le réutiliser. Un exemple fictif doit être marqué `EXAMPLE` et ne doit pas emprunter un ID `PH-OPEN-*`. Une PR fusionnée ou un ticket terminé ne change pas à lui seul le statut d'une question.

## 8. Ordre d'arbitrage recommandé

> L'ordre ci-dessous est la référence unique ; le tableau de la §1 donne le même ordre sous forme détaillée.

1. **Discovery** : `001`, `007`, `016`, `017`, `024`, `030`.
2. **Conception de l'accès et de l'isolation** : `002`, `003`, `006`, `020`, `021`, `026`.
3. **Publication et communauté** : `015`, `005`, `014`.
4. **Pilotes E1** : `009`, `012`, `018`, `027` et contrôles opérationnels.
5. **Extensions** : `004`, `011`, `013`, `025`, `028`, `029`.
6. **Commercial** : `008` après preuves de valeur.

La [stratégie produit](../01-product/01-product-strategy.md) ne peut pas présenter les questions ici comme résolues. Les décisions prises ultérieurement doivent être synchronisées avec le [registre des décisions](03-decisions-register.md).
