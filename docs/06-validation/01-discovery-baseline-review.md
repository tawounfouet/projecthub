---
id: PH-VAL-REVIEW-001
title: "ProjectHub - Revue de Discovery Baseline V1.0 (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Product / Discovery Review - approbation formelle à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-GH-001, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/00-context/03-decisions-register.md"
  - "docs/00-context/04-open-questions.md"
  - "docs/05-mvp/00-mvp-definition.md"
  - "docs/05-mvp/02-prioritized-backlog.md"
  - "docs/06-validation/00-pilot-validation-plan.md"
---

# ProjectHub - Revue publique de la Discovery Baseline V1.0

> **Revue documentaire expurgée - draft, approbation en attente.** La revue privée a examiné 24 documents de travail avant la création du 25e document de revue, puis constaté un **corpus rédigé de 25/25**. Ce résultat n'est ni une preuve de validation par les utilisateurs, ni une qualification de sécurité, ni un accord de pilote, ni une validation du MVP. Les observations propres aux organisations étudiées et leurs pièces internes ne sont pas publiées.

## 1. Résumé de décision

| Question de revue | Conclusion documentaire proposée | Conséquence |
|---|---|---|
| Les 25 documents de Discovery sont-ils rédigés ? | **Oui : 25/25**, tous initialement en `draft` | La rédaction est terminée |
| La Discovery est-elle officiellement approuvée ? | **Non : approbation en attente** | Réserves et décisions à traiter |
| Peut-on préparer l'architecture et une démonstration fictive E0 ? | **Oui, sous réserves explicites** | ADR, prototypes et tests sur données synthétiques |
| Peut-on piloter des données réelles en E1 ? | **No-Go à ce stade** | Accords et huit gates non prouvés |
| Peut-on publier le corpus privé tel quel ? | **Non** | Édition publique distincte et expurgée |
| Un SaaS Cloud commercial peut-il être annoncé comme opérationnel ? | **Non** | Exploitation, tests, IP, marché et contrats non démontrés |

**Formulation conseillée :** « Discovery Baseline V1.0 - dossier documentaire complet, approbation formelle en attente ».

L'accord d'un mainteneur sur la publication de documents est **une approbation éditoriale**, pas l'approbation métier de la baseline.

## 2. Périmètre et niveau de preuve

La revue privée contrôlait la présence des fichiers, leurs en-têtes, leur cohérence, les liens d'identifiants et les décisions ouvertes. Elle ne réalisait pas :
- d'entretiens utilisateurs complets ni d'étude commerciale représentative ;
- de vérification actuelle des systèmes d'organisations tierces ;
- de tests d'intrusion, restauration ou fonctionnement en production ;
- de validation juridique des pilotes, de la licence ou de la tarification ;
- d'essais de valeur d'usage sur un MVP opérationnel.

| Niveau | Preuve | Ce qu'il permet de conclure |
|---|---|---|
| `S0` | Intention du porteur | Direction de conception |
| `S1` | Document métier daté | Observation historique, pas statut actuel |
| `S2` | Analyse dérivée | Hypothèse à tester |
| `S3` | Critère ou spécification | Résultat attendu, non démontré |
| `S4` | Test exécuté | Résultat borné au scénario, commit et données |
| `S5` | Approbation habilitée | Autorisation dans un périmètre défini |

À la date de la revue source, les matériaux relus couvraient principalement **S0 à S3**. Les validations **S4 et S5** nécessaires à E1 manquaient.

## 3. Inventaire de la baseline documentaire

| Section | Dossier | Documents privés de travail | Éditions publiques attendues |
|---|---|---:|---:|
| Context | `00-context` | 5 | 5 |
| Product | `01-product` | 3 | 3 |
| Discovery | `02-discovery` | 5 | 5 |
| Requirements | `03-requirements` | 4 | 4 |
| Domain | `04-domain` | 3 | 3 |
| MVP | `05-mvp` | 3 | 3 |
| Validation | `06-validation` | 2 | 2 |
| **Total** | **7 dossiers** | **25** | **25** |

Les éditions publiques sont **condensées**, non des copies anonymisées ligne par ligne. Elles reprennent les concepts utiles au produit et les IDs de traçabilité sans publier les pièces privées.

## 4. Acquis conceptuels de la Discovery

1. **Vision cohérente à vérifier** : qualifier, responsabiliser, suivre, documenter, transmettre, exporter.
2. **Deux contextes métier différents étudiés** : besoins de coordination collective et pilotage multi-projets techniques, sans présumer leur représentativité.
3. **Modèle conceptuel** : `Organization -> Workspace -> Project -> WorkItem`, avec `Team`, `ClientReference` et `Repository` distincts.
4. **Frontières des outils** : ProjectHub référence les systèmes spécialisés plutôt que de les remplacer automatiquement.
5. **MVP borné** : 13 capacités `PH-SCP-001..013`, 10 parcours, 7 slices et 45 items candidats.
6. **Séparation E0/E1** : aucun essai sur données réelles sans autorisation et preuves de sûreté.

Ces acquis représentent une **cohérence documentaire**. Leurs hypothèses doivent être réfutables et confrontées aux utilisateurs.

## 5. Couverture et limites des catalogues

| Inventaire | Volume | Signification |
|---|---:|---|
| Besoins normalisés | 29 familles | Hypothèses transversales documentées |
| Personas candidats | 13 | Profils de recherche à valider |
| Workflows candidats | 32 | Scénarios génériques à examiner |
| Exigences fonctionnelles | 130 | 16 P0-G, 29 P0-C, 50 P1, 35 P2 |
| Exigences non fonctionnelles | 113 | 69 P0-G, 22 P0-C, 14 P1, 8 P2 |
| Règles métier | 111 | Invariants et permissions candidats |
| Langage ubiquitaire | 145 termes | Définitions à confirmer |
| Domain model | 20 agrégats, 30 relations | Proposition, non ORM |
| Domain boundaries | 32 contrats | Proposition, non API |
| MVP | 10 parcours, 45 backlog items | Tests et planification non exécutés |
| Validation | 8 expériences MVP, 8 gates E1 | Non exécutées ou non évaluées |

Un inventaire plus détaillé n'est pas synonyme de maturité fonctionnelle supérieure.

## 6. Vingt réserves de revue, éditions publiques

Les IDs `PH-REV-001..020` sont préservés. Les formulations ci-dessous sont **génériques**, et les statuts reproduisent le **point de départ de la revue privée au 20/11/2026**. Un changement ultérieur sur GitHub ne les résout pas automatiquement : il faut un nouveau constat et une preuve.

| ID | Réserve rendue publiable | Gravité source | État source |
|---|---|---|---|
| `PH-REV-001` | Compléter la provenance historique du dépôt public | Moyenne | `OPEN` |
| `PH-REV-002` | Récupérer les transcriptions anciennes accessibles seulement par extraits | Moyenne | `OPEN` |
| `PH-REV-003` | Réconcilier des inventaires historiques hétérogènes avant tout pilote | Moyenne | `OPEN` |
| `PH-REV-004` | Valider personas et parcours avec utilisateurs indépendants | Haute | `OPEN` |
| `PH-REV-005` | Faire approuver le périmètre et les exclusions MVP | Haute | `OPEN` |
| `PH-REV-006` | Trancher rôles, héritages et révocation RBAC | Haute | `OPEN` |
| `PH-REV-007` | Arrêter le propriétaire canonique Decision/Risk | Haute | `OPEN` |
| `PH-REV-008` | Préciser ClientReference, Organization et associations | Haute | `OPEN` |
| `PH-REV-009` | Fixer la preuve de reprise d'une passation | Haute | `OPEN` |
| `PH-REV-010` | Définir seuils NFR et procédures de preuve | Haute | `OPEN` |
| `PH-REV-011` | Compléter certaines liaisons NFR / workflows | Haute | `OPEN` |
| `PH-REV-012` | Obtenir des accords institutionnels distincts avant les pilotes E1 | Critique E1 | `OPEN` |
| `PH-REV-013` | Exécuter et évaluer les huit gates E1 | Critique E1 | `OPEN` |
| `PH-REV-014` | Actualiser les constats historiques hors produit, indépendamment de ProjectHub | Haute | `OPEN` |
| `PH-REV-015` | Encadrer les éditions publiques par une procédure et une revue de droits | Moyenne | `OPEN` |
| `PH-REV-016` | Clarifier propriété intellectuelle, licence et opérateur SaaS | Haute selon échéance | `OPEN` |
| `PH-REV-017` | Éviter qu'un grand corpus donne l'impression d'un MVP figé | Moyenne | `MITIGATION-PROPOSED` |
| `PH-REV-018` | Distinguer ID d'exemple et question ouverte active | Faible | `MITIGATION-PROPOSED` |
| `PH-REV-019` | Vérifier les namespaces de workflows dans les contrôles automatiques | Faible | `MITIGATION-PROPOSED` |
| `PH-REV-020` | Assurer la synchronisation sémantique privé / public | Moyenne | `OPEN` |

**Note sur `PH-REV-015` :** depuis la revue source, une [politique de publication](../PUBLICATION-POLICY.md) a bien été ajoutée au dépôt public. C'est un **progrès vérifiable**, mais la clôture de la réserve exige encore de confirmer son application effective et l'approbation des versions concernées.

Les réserves `PH-REV-012` et `013` sont **bloquantes pour E1**. On ne doit pas les lever par simple arbitrage éditorial.

## 7. Décisions à formaliser avant l'architecture détaillée

| Sujet | Questions ouvertes source | Livrable de décision attendu |
|---|---|---|
| Valeur et segment prioritaire | `PH-OPEN-007`, `012` | Synthèse d'entretiens et choix produit |
| MVP et exclusions | `PH-OPEN-001`, `023` | Scope approuvé et parcours démonstratif |
| Tenant / RBAC / grants | `PH-OPEN-002`, `006`, `020` | Modèle d'accès et tests négatifs |
| Propriété des décisions | `PH-OPEN-003` | ADR sur Decision/Risk |
| Client / Workspace / Team | `PH-OPEN-016`, `029` | Glossaire et relations décidées |
| Passation | `PH-OPEN-024` | Critère de réussite du repreneur |
| Qualité et exploitation | `PH-OPEN-021`, `026`, `027` | NFR, seuils et protocole de test |
| Données des pilotes | `PH-OPEN-009`, `018`, `030` | Accords de chaque autorité habilitée |
| Distribution / licence / IP | `PH-OPEN-005`, `014` | Décision juridique et de gouvernance |

Le choix d'une technologie ne doit pas servir à éviter un arbitrage métier ou de permissions.

## 8. Huit portes E1 : aucun verdict prouvé

| Gate | Preuve à obtenir |
|---|---|
| `G-LEGAL-DATA` | Autorisation et données minimisées |
| `G-ACCESS` | Tests d'autorisation et isolation |
| `G-SECRETS` | Revue de protection des secrets |
| `G-BACKUP` | Restauration démontrée |
| `G-OPERATE` | Support, runbooks et incidents |
| `G-DATA-EXIT` | Export, rétention et sortie |
| `G-ACCESSIBILITY` | Tests d'accessibilité pertinents |
| `G-CHANGE` | CI, migrations et rollback exercés |

**Verdict de référence : `NOT_ASSESSED` pour chacune.** La revue documentaire n'a pas testé l'application ni délivré d'autorisation de pilote.

## 9. Plan de levée des réserves

### Horizon A - Clôture de Discovery

- Nommer explicitement l'autorité de revue.
- Affecter les 20 réserves à des responsables habilités.
- Arbitrer le plus petit parcours MVP et documenter les exclusions.
- Organiser des entretiens et tests utilisateurs sur un protocole approuvé.
- Requalifier les réserves à partir de preuves, pas seulement de discussions.

### Horizon B - Architecture & Engineering Baseline

- Préparer des ADR sur RBAC, tenant, ownership et contrats.
- Définir modèles, migrations et API avant les cas de données réelles.
- Prévoir tests d'accès, sauvegarde/restauration, observabilité et réversibilité.
- Conserver une frontière claire entre Community auto-hébergeable et Cloud éventuel.

### Horizon C - Démonstration E0

- Implémenter les slices nécessaires sur données fictives.
- Exécuter les dix parcours et les huit expériences concernées.
- Enregistrer les défauts, tests négatifs, résultats et versions testées.
- Revoir la valeur plutôt que seulement le nombre de tickets clôturés.

### Horizon D - Pilotes E1

- Obtenir les autorisations de chaque organisation concernée.
- Démontrer les huit gates applicables et signer les responsabilités.
- Mesurer les usages dans un périmètre limité, avec arrêt et export possibles.

### Horizon E - Distribution et commercialisation

- Clarifier IP, licence, contributions et responsabilité d'exploitation.
- Préparer installation indépendante et documentation pour Community.
- Ne considérer une offre Cloud commerciale qu'après validation de l'exploitation, des accords et de la valeur payante.

Ces horizons sont **des séquences conditionnelles**, pas une promesse de calendrier.

## 10. Décision de revue à compléter

```yaml
baseline: "ProjectHub Discovery Baseline V1.0"
review_document: PH-VAL-REVIEW-001
decision_date: null
decision_authority: null
decision: PENDING
# Valeurs futures possibles : APPROVED, APPROVED_WITH_RESERVATIONS, RETURN_FOR_REWORK
blocking_reservations:
  - PH-REV-012
  - PH-REV-013
evidence_links: []
pilot_e1_authorized: false
notes: "Revue documentaire complète ; approbation formelle non enregistrée."
```

La date et l'autorité doivent être renseignées par le décideur réel. Une PR fusionnée sur GitHub ne complète pas ce procès-verbal.

## 11. Politique de double édition

- Le **corpus privé** conserve la provenance détaillée, les constats internes et les annexes sensibles, avec accès limité.
- L'**édition publique** résume les décisions, hypothèses et IDs utiles au produit.
- Les différences sont assumées et versionnées ; une correction dans l'édition publique ne modifie pas silencieusement la pièce source.
- Les liens privés n'apparaissent pas dans les issues, PR ni captures publiques.
- L'alignement des identifiants et des statuts doit faire l'objet d'un contrôle régulier.

La [politique de publication](../PUBLICATION-POLICY.md) et le [guide de collaboration](../COLLABORATION-BEST-PRACTICES.md) encadrent cette démarche.

## 12. Verdict et prochaine porte

**Décision recommandée : autoriser la préparation exploratoire de l'architecture et du prototype E0, tout en maintenant l'approbation formelle de la Discovery en attente et l'usage de données réelles en No-Go.**

Ce verdict résulte de la **revue du contenu documentaire**. Il ne s'étend pas à des garanties sur le logiciel, à des accords de pilotes ni à une certification.

**Documents :** [MVP](../05-mvp/00-mvp-definition.md), [parcours](../05-mvp/01-user-journeys.md), [backlog](../05-mvp/02-prioritized-backlog.md), [plan de validation](00-pilot-validation-plan.md), [questions ouvertes](../00-context/04-open-questions.md).
