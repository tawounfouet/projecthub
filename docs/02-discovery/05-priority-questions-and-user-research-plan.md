---
id: PH-DISC-EXEC-001
title: "ProjectHub - Plan public de validation des questions prioritaires"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
owner: "Product Discovery - titulaire à confirmer"
related_questions: [PH-OPEN-007, PH-OPEN-001, PH-OPEN-024]
related_journeys: [MVP-UJ-02, MVP-UJ-03, MVP-UJ-06]
publication_status: review_required
---

# Product Discovery - Responsabilités et entretiens utilisateurs

> **Édition publique candidate, non approuvée et non fusionnée.** Ce plan prolonge la Discovery Baseline V1.0. Les trois questions sont `OPEN` dans le registre canonique ; aucun responsable nominatif ni participant n'a été désigné par cette publication, aucun entretien ni exercice E0 n'est prétendu exécuté. Ce texte est une proposition de conduite d'étude et non une validation du MVP.

## 1. Objet et résultats recherchés

Préparer la validation de trois questions prioritaires, avec une démarche en deux temps : **rechercher le problème actuel sans montrer ProjectHub**, puis éprouver des tâches simples à l'aide d'un concept ou d'un scénario E0 synthétique.

| Question | Décision à instruire | Référence de parcours | État |
|---|---|---|---|
| `PH-OPEN-007` | Utilisateur prioritaire et promesse mesurable | `MVP-UJ-02`, `MVP-UJ-03` | `OPEN` |
| `PH-OPEN-001` | Plus petit parcours MVP réellement utile et exclusions | `MVP-UJ-02` puis `03` | `OPEN` |
| `PH-OPEN-024` | Preuve d'autonomie du successeur après une passation | `MVP-UJ-06` | `OPEN` |

Ces décisions n'effacent pas les contraintes transversales d'accès, de tenant, de sécurité et de sortie. La Discovery est rédigée mais reste en attente de validation métier formelle.

## 2. Gouvernance proposée : titulaires à désigner

| Question ou tâche | Rôle attendu | Titulaire | Preuve de nomination |
|---|---|---|---|
| `PH-OPEN-007` | Responsable produit / recherche | À désigner | À fournir |
| `PH-OPEN-001` | Autorité produit | À désigner | À fournir |
| `PH-OPEN-024` | Responsable du parcours de passation | À désigner | À fournir |
| Conduite des entretiens | Research Lead / modérateur | À désigner | À fournir |
| Confidentialité et données | Référent données habilité | À désigner | À fournir |
| Exercice E0 / tests UX | UX / Engineering | À désigner | À fournir |
| Revue des biais | Relecteur distinct si possible | À désigner | À fournir |

Le **mainteneur GitHub** peut approuver la publication documentaire, mais cela ne constitue ni une nomination métier ni un accord d'une organisation tierce. Les rôles peuvent être cumulés lorsque cela est justifié et documenté ; la décision reste attribuée à une autorité compétente.

## 3. Hypothèses à confronter aux pratiques actuelles

### 3.1. `PH-OPEN-007` - Segment et problème

**Hypothèse candidate :** certaines équipes perdent du temps ou du contexte pour retrouver l'état, le responsable, un blocage ou une prochaine action entre plusieurs outils. **Alternative possible :** les outils suffisent et le vrai problème relève des habitudes ou de la gouvernance.

**À observer :** un épisode récent, ses étapes, les outils utilisés, les conséquences et un contre-exemple où le processus fonctionne bien.

### 3.2. `PH-OPEN-001` - Tranche minimale

**Hypothèse candidate :** un Project contextualisé et un WorkItem actionnable constituent une première tranche utile. **Alternative possible :** un outil existant suffit ou un autre élément devient indispensable dès le début.

**À observer :** tâche accomplie, fonctionnalités strictement nécessaires, informations à différer, duplication de saisie et refus liés aux permissions.

### 3.3. `PH-OPEN-024` - Passation

**Hypothèse candidate :** un successeur distinct peut comprendre le contexte et accomplir une prochaine action grâce à une préparation concise. **Alternative possible :** accompagnement humain et autorisations externes sont incontournables.

**À observer :** action réussie ou échouée, aide reçue, sources retrouvées, lacunes et réserves. Une checklist complétée ne prouve pas l'autonomie.

## 4. Profils à inviter, non approuvés comme cible commerciale

| Persona candidat | Raison de l'étudier |
|---|---|
| `PH-PER-001` - Coordinateur multi-projets | Priorités, statuts et responsables |
| `PH-PER-002` - Sponsor métier | Résultats attendus et décisions |
| `PH-PER-003` - Responsable d'exécution | Suivi d'action et blocage |
| `PH-PER-004` - Contributeur occasionnel | Compréhension d'une première tâche |
| `PH-PER-005` - Repreneur | Transmission effective |
| `PH-PER-006` - Responsable IT / portefeuille | Besoins sans double saisie de Git / CI/CD |
| `PH-PER-011` - Perspective d'accessibilité | Obstacles à la compréhension et à l'usage |

Les personas sont des **hypothèses**, pas des personnes ou des rôles RBAC. Il faut varier l'ancienneté, la fréquence d'usage, les contextes et les avis favorables ou critiques.

**Taille indicative à discuter :** une première vague exploratoire de 9 à 12 entretiens de 35 à 45 minutes, si les autorisations et le recrutement le permettent. Ce nombre est une proposition d'organisation **non préapprouvée**, pas un seuil de preuve, ni une étude statistiquement représentative.

## 5. Préconditions avant collecte

- [ ] Responsables et autorités désignés avec mandat explicite.
- [ ] Objectifs, hypothèses, critères d'analyse et méthode approuvés **avant** les entretiens.
- [ ] Participants volontaires, suffisamment informés, avec possibilité de refus et de retrait.
- [ ] Autorisations organisationnelles requises obtenues lorsque les situations en dépendent.
- [ ] Canaux de recrutement et stockage privé autorisés ; confidentialité et rétention définies.
- [ ] Pas de secrets ni de données réelles non autorisées dans les notes, captures ou dépôts publics.
- [ ] Enregistrement audio non présumé ; conditions distinctes à déterminer si nécessaire.
- [ ] Format d'entretien accessible et adapté aux personnes volontaires.
- [ ] Exemples et éventuels tests E0 fondés sur des données **synthétiques**.

## 6. Conduite d'un entretien de 35 à 45 minutes

### Introduction

Indiquer que la recherche porte sur les méthodes actuelles, n'évalue pas la personne et ne promet aucune fonctionnalité. Demander une situation récente sans détails confidentiels.

### Questions sur le contexte et le problème

1. Quelle est votre responsabilité sur les projets suivis récemment ?
2. Quel épisode récent illustre la recherche d'un responsable, d'un statut ou d'une action ?
3. Quels outils avez-vous utilisés, dans quel ordre ?
4. Où avez-vous perdu du temps, du contexte ou de la confiance ? Quelles conséquences avez-vous réellement observées ?
5. Dans quel cas le même travail s'est-il bien passé, et pourquoi ?
6. Quelle solution existante suffit aujourd'hui ?

### Questions sur le plus petit parcours

7. Quelles informations sont indispensables pour créer et suivre une initiative ?
8. Qu'est-ce qui peut être ajouté plus tard sans bloquer une action ?
9. Comment une action change-t-elle de responsable, de priorité ou de statut aujourd'hui ?
10. Qu'est-ce qui ferait d'un outil supplémentaire une charge inutile ?

### Questions sur la reprise

11. Racontez une transition récente de responsabilité.
12. Quelle était la première action du successeur ?
13. De quelle aide humaine, référence ou permission avait-il besoin ?
14. Comment avez-vous observé que la reprise était vraiment réussie ou bloquée ?

### Clôture

15. Quel contre-exemple ou obstacle n'avons-nous pas évoqué ?
16. Quelle question vous paraît mal posée ?

**Ne pas commencer par montrer ProjectHub** et ne pas assimiler l'intention d'utiliser le produit à une preuve d'adoption.

## 7. Exercices E0 proposés, distincts des entretiens

| Exercice candidat | Tâche fictive | Réussite à définir avant exécution | Contrôle de sûreté |
|---|---|---|---|
| `PH-OPEN-007` | Retrouver un Project, son responsable et une action | Informations correctes, source et aide connue | Aucun objet de `Demo-Org-B` visible dans A |
| `PH-OPEN-001` | Créer un Project et suivre un WorkItem | Action suivie, résultat et champs indispensables identifiés | Parentage et autorisations contrôlés |
| `PH-OPEN-024` | Faire reprendre une action par un autre acteur | Action réalisée, niveau d'aide et réserves consignés | Droit du successeur réellement vérifié |

Les tests E0 ne sont **pas déclarés implémentés ou exécutés**. Un test de passation dans une maquette doit être présenté comme tel, pas comme une preuve technique de permission.

## 8. Mesure, statut et décision

Avant les sessions, approuver au minimum : hypothèse, population, tâche, mesure, méthode de relevé, comparaison au processus actuel, critère de réussite, conditions d'arrêt, autorité habilitée et traitement des données manquantes.

| Niveau | Statuts documentés ou candidats | Règle |
|---|---|---|
| Entretien | `NOT_RUN`, puis session effectivement réalisée ou annulée | Compte rendu interne privé requis |
| Expérience | `NOT_RUN`, `PASS`, `FAIL`, `INCONCLUSIVE`, `NOT_ASSESSED` | Résultats bornés à l'exercice et au critère préapprouvé |
| Question canonique | `OPEN`, `DECIDED`, `SUPERSEDED` | Seul un acte habilité et tracé change le statut |
| Pilote E1 | `NO-GO` en l'absence d'accord et de preuves | Huit gates E1 restent à évaluer |

### Matrice publique de résultats (à compléter après revue)

| ID | Preuve favorable agrégée | Contre-preuve agrégée | Limites | Verdict actuel |
|---|---|---|---|---|
| `PH-OPEN-007` | À collecter | À collecter | Pas d'entretiens attestés | `OPEN` |
| `PH-OPEN-001` | À collecter | À collecter | Pas de test E0 attesté | `OPEN` |
| `PH-OPEN-024` | À collecter | À collecter | Pas de passation attestée | `OPEN` |

## 9. Livrables et séquence proposée

1. Désigner les trois autorités et l'équipe de recherche ; faire confirmer les mandats.
2. Approuver le protocole, les critères de preuve et la confidentialité.
3. Recruter des volontaires de profils variés ; enregistrer les accords hors GitHub.
4. Conduire les entretiens, rechercher les contre-exemples et préserver les notes privées.
5. Établir une synthèse agrégée des frictions et méthodes actuelles.
6. Si un prototype E0 est disponible, exécuter les exercices fictifs et enregistrer les résultats.
7. Préparer trois dossiers de décision, avec options, preuves contradictoires, limitations et conséquences.
8. Si les autorités approuvent, synchroniser `04-open-questions.md`, `03-decisions-register.md`, MVP et backlog ; sinon conserver le statut `OPEN` avec motif.

Aucune date, session, estimation ferme ni décision n'est revendiquée.

## 10. Modèle public de dossier de décision

```yaml
question_id: PH-OPEN-007
accountable_role: "Responsable produit / recherche"
accountable_person: null
appointment_ref: null
status: PENDING
options: []
sanitized_evidence_for: []
sanitized_evidence_against: []
limitations: []
choice: null
rationale: null
decision_ref: null
approved_at: null
```

Le registre canonique des questions ouvertes reste la **source de vérité**. Une PR fusionnée ne change pas automatiquement leur statut.

## 11. Politique de publication et limites

Conserver **hors du dépôt public** les identités, coordonnées, consentements, notes brutes, enregistrements, plannings nominatifs, données d'organisation, preuves réidentifiantes et accords confidentiels. Seules des synthèses expurgées et autorisées peuvent être publiées. La revue doit documenter les limitations de l'échantillonnage et les résultats contraires.

## 12. Références ProjectHub

- [Questions ouvertes et règles de clôture](../00-context/04-open-questions.md)
- [Personas et protocole initial](00-stakeholders-and-personas.md)
- [Besoins transversaux](03-cross-organization-needs.md)
- [Workflows As-Is / To-Be](04-current-vs-target-workflows.md)
- [MVP candidat et foyer de validation](../05-mvp/00-mvp-definition.md)
- [Parcours de référence](../05-mvp/01-user-journeys.md)
- [Plan de validation, §11.1](../06-validation/00-pilot-validation-plan.md#111-recherche-utilisateur-avant-prototype)
- [Revue et réserves Discovery](../06-validation/01-discovery-baseline-review.md)
- [Politique de publication](../PUBLICATION-POLICY.md)

**Fin - Édition publique candidate.** Aucune modification GitHub ou approbation n'est réalisée par la création de ce fichier.
