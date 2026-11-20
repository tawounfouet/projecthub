---
id: PH-PILOT-VAL-001
title: "ProjectHub - Plan candidat de validation et de pilotes (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Pilot Governance - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/05-mvp/00-mvp-definition.md"
  - "docs/05-mvp/01-user-journeys.md"
  - "docs/05-mvp/02-prioritized-backlog.md"
  - "docs/06-validation/01-discovery-baseline-review.md"
---

# ProjectHub - Plan de validation du MVP et des pilotes

> **Édition publique expurgée - draft.** Ce document est un protocole **proposé**, non un accord de participation, un rapport de test exécuté ou une autorisation de traiter des données réelles. Les sources internes sur les organisations susceptibles d'être concernées, leurs projets et leurs interlocuteurs ne sont pas publiées.

## 1. Objectif et politique de preuve

Le programme vise à vérifier trois choses distinctes :

1. **Validité du problème** : les difficultés de coordination, de visibilité et de transmission existent-elles dans les tâches observées ?
2. **Utilité du produit** : ProjectHub permet-il d'accomplir un parcours sans créer une charge de gestion disproportionnée ?
3. **Sûreté et exploitabilité** : données, droits, secrets, sauvegardes, incidents, accessibilité et sortie sont-ils maîtrisés ?

Une déclaration d'intérêt ou un commentaire positif ne remplace pas une observation. Une démonstration E0 ne permet pas de conclure à l'aptitude à traiter les données d'une organisation réelle.

## 2. Deux programmes, deux types de décision

| Programme | Environnement | Autorisation | Type de preuve |
|---|---|---|---|
| **E0** - démonstration | Tenants, utilisateurs et Projects fictifs | Décision de travail interne sur le prototype fictif | Tests fonctionnels, API négatifs, scénarios UX |
| **E1** - pilote réel limité | Jeux de données minimisés et explicitement autorisés | Accord d'une instance compétente **par organisation** + huit gates validées | Évaluations de valeur et exploitation datées |

**Règle :** le passage E0 -> E1 est bloqué par défaut. Aucune participation tierce ne peut être déduite d'un rôle du concepteur dans cette organisation.

## 3. Terrains d'étude génériques

Le programme compare des contextes d'usage différents, sans révéler leurs données :
- coordination d'initiatives au sein d'une équipe associative ;
- visibilité de plusieurs projets et activités d'une équipe technique ;
- activités partagées par un réseau de membres ;
- tests d'accessibilité par des utilisateurs volontaires et compétents.

Ces terrains sont des **hypothèses de recrutement**, pas une liste de partenariats conclus. Un sponsor habilité doit définir l'objectif, les participants, les données, la durée, le support et la possibilité de retrait avant E1.

## 4. Gouvernance de l'essai

| Rôle | Fonction candidate | Peut décider |
|---|---|---|
| Product Owner ProjectHub | Question d'apprentissage, backlog et décisions produit | Scope du prototype selon gouvernance ProjectHub |
| Sponsor organisationnel habilité | Autoriser ou refuser un essai de son organisation | Périmètre institutionnel et arrêt |
| Référent données | Catégories de données, conservation et sortie | Recommandation et contrôle selon mandat |
| Responsable technique / sécurité | Évaluer les tests, accès, restauration et risques | Verdict technique dans son périmètre |
| Opérateur du pilote | Déploiement, incidents, sauvegardes, continuité | Mise en oeuvre technique autorisée |
| Référent accessibilité | Protocole, obstacles, corrections et retests | Avis spécialisé sur parcours |
| Participant volontaire | Réaliser une tâche et signaler les problèmes | Consentement à l'étude dans le cadre applicable |
| Evaluateur indépendant, si possible | Observer les usages et documenter sans biais | Rapport, pas approbation institutionnelle |

Une même personne peut cumuler des rôles, mais les conflits d'intérêts et l'absence de revue indépendante doivent être déclarés, non masqués.

## 5. Jeu E0 et conditions d'observation

- `Demo-Org-A`, `Demo-Org-B`, plusieurs Workspaces et Projects fictifs ;
- rôles distincts : membre A, membre B, multi-appartenance, administrateur, contributeur, successeur et observateur ;
- WorkItems, blocages, références documentaires fictives et événements datés ;
- jeu de test déterministe, réinitialisable et sans secrets véritables ;
- outils externes simulés ou autorisés ; aucun scrape ni import implicite ;
- évaluation des refus sur interface **et API** (listes, détail par ID, recherche, export).

Le but est d'observer un **résultat métier**, pas seulement de valider des écrans. Les participants et leurs données d'évaluation sont collectés selon un protocole approprié.

## 6. Huit expériences MVP à préparer

Les identifiants ci-dessous sont **`MVP:EXP-01..08`**, pour les distinguer du programme stratégique **`PH-EXP-01..08`**. Même numéro ne signifie **pas** même protocole, mesure ou responsabilité.

| ID de l'expérience MVP | Question | Tâche observée | Preuve proposée |
|---|---|---|---|
| `MVP:EXP-01` | Retrouver un Project est-il simple ? | Identifier l'état et le responsable d'une initiative | Résultat correct et temps **mesuré**, sans chiffre présumé |
| `MVP:EXP-02` | Une action reste-t-elle compréhensible ? | Modifier un WorkItem et son blocage | Statut et historique consultables |
| `MVP:EXP-03` | Une revue peut-elle s'appuyer sur des faits ? | Préparer une revue multi-projets | Source, fraîcheur et décisions en attente identifiées |
| `MVP:EXP-04` | La passation est-elle effective ? | Faire accomplir une action par un successeur | Autonomie observée, réserves documentées |
| `MVP:EXP-05` | Deux Organizations restent-elles isolées ? | Essais directs et indirects A/B | Refus serveur, pas de fuite API, recherche ou export |
| `MVP:EXP-06` | Retrouve-t-on le document maître ? | Suivre une référence externe autorisée | Source et permissions préservées |
| `MVP:EXP-07` | La sortie est-elle réalisable ? | Exporter et lire hors produit | Archive intelligible et contrôlée par tenant |
| `MVP:EXP-08` | Le langage est-il compris ? | Interpréter Project, Workspace, Client et état | Erreurs de compréhension identifiées |

**Statut de toutes les expériences : `NOT_RUN`.** Aucun résultat favorable ne peut être inscrit sans une session de test réelle, datée et reproductible.

## 7. Correspondance avec les dix parcours

| Parcours | Expériences MVP utiles | Contrôle |
|---|---|---|
| `MVP-UJ-01` | `MVP:EXP-05`, `08` | Contexte explicite |
| `MVP-UJ-02` | `MVP:EXP-01`, `08` | Parentage du Project |
| `MVP-UJ-03` | `MVP:EXP-02` | Transition et historique |
| `MVP-UJ-04` | `MVP:EXP-03` | Synthèse fondée sur faits |
| `MVP-UJ-05` | `MVP:EXP-06` | Liens et provenance |
| `MVP-UJ-06` | `MVP:EXP-04` | Reprise autonome |
| `MVP-UJ-07` | `MVP:EXP-05` | Révocation |
| `MVP-UJ-08` | `MVP:EXP-07` | Export et sortie |
| `MVP-UJ-09` | `MVP:EXP-05` | Mandat d'approbation |
| `MVP-UJ-10` | `MVP:EXP-05`, `08` | Client différent du tenant |

La couverture est **documentaire**. Elle ne constitue pas une matrice de tests exécutés.

## 8. Huit gates obligatoires avant E1

| Gate | Objet | Preuve de passage à fournir | État |
|---|---|---|---|
| `G-LEGAL-DATA` | Autorisation institutionnelle et périmètre légal | Décision habilitée, données, participants, finalité, durée et retrait | `NOT_ASSESSED` |
| `G-ACCESS` | Permissions et isolation multi-tenant | Tests négatifs A/B, memberships, API, recherche, exports, révocation | `NOT_ASSESSED` |
| `G-SECRETS` | Gestion des secrets | Revue des configurations, journaux, dépendances et fixtures | `NOT_ASSESSED` |
| `G-BACKUP` | Sauvegardes et restauration | Exercice réussi sur périmètre isolé, intégrité vérifiée | `NOT_ASSESSED` |
| `G-OPERATE` | Exploitation et incidents | Runbook, responsables, canal d'alerte et exercice | `NOT_ASSESSED` |
| `G-DATA-EXIT` | Export, conservation, suppression et retrait | Réversibilité vérifiée, politique d'effacement et de restitution | `NOT_ASSESSED` |
| `G-ACCESSIBILITY` | Accessibilité du parcours | Tests pertinents, rapport de barrières et corrections | `NOT_ASSESSED` |
| `G-CHANGE` | Maîtrise des changements | CI, migrations, non-régression et rollback exercé | `NOT_ASSESSED` |

Les 8 gates couvrent des ensembles de preuves. Elles ne remplacent pas les **69 NFR `P0-G`** et les **16 FR `P0-G`** qu'il faudra relier explicitement aux tests.

## 9. Conditions d'arrêt immédiat

Le pilote doit être suspendu et les autorités concernées consultées en cas :
- d'accès inter-tenant non autorisé, de fuite de données ou de secrets ;
- de perte de données ou d'impossibilité de restaurer une sauvegarde ;
- de défaillance grave des permissions ou de la révocation ;
- d'exposition de données non couvertes par l'accord ;
- d'absence de procédure d'incident ou de sortie opérationnelle ;
- de problème de sécurité, confidentialité ou accessibilité jugé bloquant.

Une anomalie peut conduire à un **No-Go**, même si une démonstration visuelle semble réussir.

## 10. Décision Go / No-Go / Go sous réserves

| Verdict | Conditions | Conséquence |
|---|---|---|
| `GO-E0` | Parcours fictifs démontrés et défauts bloquants traités | Continuer la validation E0, pas les données réelles |
| `NO-GO-E0` | Comportement fondamental ou isolation non démontrés | Corriger avant nouvelle démo |
| `GO-E1` | Accord habilité, huit gates satisfaites, périmètre approuvé | Pilote limité, surveillé, réversible |
| `NO-GO-E1` | Une condition bloquante ou une autorisation manque | Pas de données réelles |
| `GO-WITH-RESERVATIONS` | Réserves non bloquantes, acceptées par autorités responsables | Périmètre restreint, suivi et arrêt possible |

Aucune réserve de confidentialité, de légalité ou d'isolation ne peut être requalifiée arbitrairement en « mineure » par l'équipe produit.

## 11. Protocole d'observation et de mesure

Pour chaque expérience :
1. poser une question de recherche et une hypothèse réfutable ;
2. désigner les participants et les autorisations pertinentes ;
3. choisir une tâche concrète et un jeu de données approprié ;
4. enregistrer le **point de départ** et les outils alternatifs ;
5. observer un résultat réel (trouvé, mis à jour, transmis, refusé, exporté) ;
6. mesurer uniquement les données réellement collectées ;
7. noter erreurs, temps, hésitations, commentaires et possibilités de correction sans surveiller la performance personnelle ;
8. consigner une version de logiciel, des anomalies et un verdict ;
9. comparer aux méthodes existantes avant de décider de poursuivre.

### 11.1 Critères à fixer avant une session

Avant de recueillir des résultats, consigner pour chaque expérience :
- l'hypothèse, la tâche, le profil participant (sans identité personnelle) et le jeu de données autorisé ;
- la méthode actuelle servant de comparaison, ou la raison pour laquelle aucune comparaison n'est possible ;
- la mesure, son unité et ses bornes (début/fin) ; pour un taux, le numérateur et le dénominateur ;
- le critère de décision, sa justification et la personne habilitée à l'approuver ;
- les conditions d'arrêt et les anomalies qui imposent un `No-Go`.

Les critères quantitatifs ne sont pas présumés : ils doivent être convenus en fonction de l'usage attendu avant le test, jamais ajustés après observation pour transformer un résultat en succès. Pour une expérience qualitative, définir un comportement observable et une règle d'interprétation plutôt qu'un chiffre artificiel. Si le critère ou la comparaison manque, inscrire `NOT_ASSESSED` ou `INCONCLUSIVE` selon le cas ; ne pas conclure à une validation.

Pour les contrôles d'accès, toute divulgation non autorisée constitue un échec et déclenche l'arrêt prévu. L'absence de fuite dans les scénarios exécutés ne prouve que ces scénarios, pas l'absence générale de vulnérabilité ni l'aptitude à E1.

Utiliser `NOT_RUN` avant toute session, `PASS` ou `FAIL` selon le critère fixé à l'avance, `INCONCLUSIVE` si les observations ne permettent pas de trancher et `NOT_ASSESSED` si le protocole ou les preuves sont insuffisants. Ces statuts décrivent une expérience, pas l'approbation globale du MVP ou d'un pilote.

### 11.2 Lecture des résultats

Les mesures candidates incluent le temps de recherche d'un Project, la complétude d'une mise à jour, l'effort de préparation d'une revue, l'autonomie de reprise et la lisibilité d'un export. Pour éviter les interprétations ambiguës, préciser avant la session comment chaque mesure sera relevée ; par exemple, pour une passation, indiquer l'action attendue et si l'aide du facilitateur est permise. Les résultats restent bornés au scénario, aux participants, aux données et à la version testés. Un résultat positif isolé ne vaut ni validation générale du besoin, ni approbation du MVP.

## 12. Organisation des phases et horizon indicatif

Une **séquence conditionnelle** peut suivre :
- préparation du protocole, jeux E0 et personnes référentes ;
- exécution E0, correction des anomalies, nouvelle démonstration ;
- accords et dossier des huit gates E1 ;
- démarrage restreint si les gates et autorisations sont satisfaites ;
- revues périodiques, observations et éventuelle sortie.

Le plan source évoque un **programme pilote conditionnel d'environ 90 jours** comme support de planification, pas une date de démarrage ou une obligation contractualisée. Les capacités des équipes et l'accord des organisations restent à établir.

## 13. Format minimal des preuves

```yaml
id: MVP:EXP-05
status: NOT_RUN
hypothesis: null
environment: null
commit_sha: null
data_classification: synthetic
participant_profile: null
tenant_scope: null
scenario: "refus de lecture cross-tenant"
baseline: null
measure_and_unit: null
decision_criterion: null
criterion_rationale: null
criterion_approved_by: null
expected: "accès interdit"
observed: null
anomalies: []
executed_at: null
evidence_url: null
reviewer: null
decision: null
```

Les `null` sont intentionnels : ne pas ajouter de preuves fictives pour « compléter » un rapport. Les profils et références de preuve ne doivent pas révéler d'identité ni de données personnelles ; conserver les pièces sensibles dans un espace autorisé, hors de la PR publique.

## 14. Risques, responsabilités et suites

Risques prioritaires : confusion entre auteur du produit et autorité de l'organisation, problème historique supposé actuel, biais du pilote, double saisie, permissions sous-spécifiées, passation de façade, export non testé, données d'accessibilité traitées comme une démonstration marketing.

**Actions de réduction proposées :** séparation des décisions produit et organisationnelles, entretiens avec acteurs distincts, jeux synthétiques, politiques d'arrêt, registres de décisions et de preuves, tests négatifs, accès limités, suivi des réserves.

**État actuel :** plan rédigé, organisations non engagées par cette publication, expériences non exécutées et gates E1 non évaluées.

Voir [parcours](../05-mvp/01-user-journeys.md), [backlog](../05-mvp/02-prioritized-backlog.md), [revue Discovery](01-discovery-baseline-review.md), [NFR](../03-requirements/01-non-functional-requirements.md).
