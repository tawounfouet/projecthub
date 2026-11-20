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

> **Portefeuille de questions candidates.** Les identifiants `PH-OPEN-001` à `PH-OPEN-030` sont conservés depuis le registre privé, mais les formulations sont expurgées. Toutes sont indiquées `OPEN` tant qu'aucune décision explicite, traçable et autorisée n'est intervenue. L'absence de réponse n'est pas un accord implicite.

## 1. Priorité et portes de décision

- **P0** : nécessaire pour figer le parcours MVP, les frontières d'accès, la revue ou la sécurité de données réelles.
- **P1** : nécessaire pour une évolution ciblée, un pilote opérationnel ou une distribution Community.
- **P2** : peut être différé à une phase Cloud, commerciale ou avancée.
- **Externe** : décision relevant d'une organisation tierce, non du mainteneur ProjectHub.

La priorité décrit le **moment où décider**, pas l'obligation de développer la fonctionnalité.

## 2. Questions Product / MVP

| ID | Question | Priorité candidate | Pour résoudre |
|---|---|---|---|
| `PH-OPEN-001` | Quel parcours constitue le plus petit MVP utile ? | P0 | Valider scénario, exclusions et critères de recette |
| `PH-OPEN-007` | Quel utilisateur prioritaire et quelle promesse mesurable ? | P0 | Entretiens avec utilisateurs et décideurs |
| `PH-OPEN-012` | Quels indicateurs prouvent un bénéfice réel ? | P1 | Baseline, définition et protocole de mesure |
| `PH-OPEN-017` | Comment représenter objectifs, livrables et responsables ? | P0 | Scénarios et vocabulaire approuvés |
| `PH-OPEN-020` | Quel premier mode de déploiement : démonstration isolée ou multi-tenant ? | P0 | Plan E0/E1 et exigences d'isolation |
| `PH-OPEN-023` | Table, Board, Roadmap : quelles vues réellement utiles au MVP ? | P1 | Test d'usage comparatif |
| `PH-OPEN-024` | Comment démontrer la reprise d'un projet ? | P0 | Scénario de passation et vérification de l'autonomie |

## 3. Domaine / permissions / données

| ID | Question | Priorité candidate | Pour résoudre |
|---|---|---|---|
| `PH-OPEN-002` | Quels rôles, memberships, délégations et droits effectifs ? | P0 | Matrice RBAC, tests de refus et révocation |
| `PH-OPEN-003` | Quel domaine possède décisions, risques et actions ? | P0 | Propriété canonique, événements et invariants |
| `PH-OPEN-006` | Comment garantir l'isolation multi-tenant et l'évolution Cloud ? | P0 sécurité / P1 détail Cloud | Modèle de données, tests et preuve |
| `PH-OPEN-016` | Comment séparer Client, Organization, Workspace et Team ? | P0 | Glossaire et cas inter-organisation |
| `PH-OPEN-021` | Quel minimum non fonctionnel avant données réelles ? | P0 | Contrôles observables et seuils approuvés |
| `PH-OPEN-026` | Comment gérer export, rétention, suppression et réversibilité ? | P0 E1 | Protocole de sortie et tests |
| `PH-OPEN-027` | Quel niveau d'accessibilité et comment le vérifier ? | P1 avant pilote spécialisé | Parcours, référentiel et tests |
| `PH-OPEN-029` | Comment représenter dépôt, environnement, service et composant ? | P1 | Modèle des références techniques sans mélange avec Project |

## 4. Intégrations, documentation, IA

| ID | Question | Priorité candidate | Pour résoudre |
|---|---|---|---|
| `PH-OPEN-004` | Quelle première intégration et quel niveau de synchronisation ? | P1 | Cas concret, coûts de permission et conflits de données |
| `PH-OPEN-011` | Quelles bibliothèques externes/internes seraient réutilisables ? | P2 | Audit de code, licence et qualité |
| `PH-OPEN-013` | Quelles sources peut exploiter une éventuelle IA ? | P2 | Autorisations, modèle de données et tests de fuite |
| `PH-OPEN-022` | Où conserver la documentation et son historique ? | P1 | Source de vérité, liens et droits |
| `PH-OPEN-025` | Comment importer le travail existant sans double saisie ? | P1 | Mapping, nettoyage et réversibilité |
| `PH-OPEN-028` | Quel rôle pour les agents IA, et quels droits ? | P2 ; P0 si action réelle | Identités techniques, audit et approbation humaine |

## 5. Pilotes, gouvernance et distribution

| ID | Question | Priorité candidate | Pour résoudre |
|---|---|---|---|
| `PH-OPEN-005` | Quelle licence et quelle gouvernance de contribution ? | P1 avant distribution du code | Droits IP, compatibilité et politique |
| `PH-OPEN-008` | Quel tarif et quelle unité de facturation Cloud ? | P2 | Entretiens acheteurs, coûts d'exploitation |
| `PH-OPEN-009` | Quelles autorisations institutionnelles et données de pilote ? | P0 externe avant E1 | Accords, rôles et périmètre documentés |
| `PH-OPEN-010` | Comment sécuriser une transmission opérationnelle indépendante du logiciel ? | P0 externe | Plan de passation porté par l'organisation concernée |
| `PH-OPEN-014` | Qui détient les droits et qui peut opérer commercialement ProjectHub ? | P1 | Arbitrage juridique et de gouvernance |
| `PH-OPEN-015` | Qui relit et approuve les éditions publiques ? | P0 publication | Politique désormais écrite ; relecteur effectif à désigner |
| `PH-OPEN-018` | Quels niveaux d'assistance et d'exploitation pendant les pilotes ? | P1 | Engagements proportionnés et autorisés |
| `PH-OPEN-019` | Quel état actuel des travaux issus des analyses historiques ? | P0 externe | Vérification auprès des responsables autorisés |
| `PH-OPEN-030` | Qui approuve la baseline Discovery et ses réserves ? | P0 | Décision écrite du responsable compétent |

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

## 7. Ordre d'arbitrage recommandé

1. **Discovery** : `001`, `007`, `016`, `017`, `024`, `030`.
2. **Conception de l'accès et de l'isolation** : `002`, `003`, `006`, `020`, `021`, `026`.
3. **Publication et communauté** : `015`, `005`, `014`.
4. **Pilotes E1** : `009`, `012`, `018`, `027` et contrôles opérationnels.
5. **Extensions** : `004`, `011`, `013`, `025`, `028`, `029`.
6. **Commercial** : `008` après preuves de valeur.

La [stratégie produit](../01-product/01-product-strategy.md) ne peut pas présenter les questions ici comme résolues. Les décisions prises ultérieurement doivent être synchronisées avec le [registre des décisions](03-decisions-register.md).
