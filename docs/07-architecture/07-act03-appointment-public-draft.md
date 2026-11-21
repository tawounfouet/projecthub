---
id: PH-ARCH-GOV-ACT03-APPOINTMENT-001
title: "ProjectHub - ACT03-APPOINTMENT - Modèle public de nomination opérationnelle"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
source_issue: "https://github.com/tawounfouet/projecthub/issues/13"
act_id: ACT03-APPOINTMENT
decision: PENDING
nomination_status: PENDING_FORMAL_APPROVAL
person_or_instance_ref: null
appointing_authority_ref: null
approval_evidence_uri: null
---

# ACT03-APPOINTMENT - Modèle d'acte d'attribution cumulée (édition publique)

**Statut : DRAFT / NO NOMINATION / NOT EFFECTIVE.** Cette édition publique autonome n'identifie aucun titulaire réel et ne contient aucune attestation. Elle ne devient applicable qu'après approbation effective du [protocole ACT03-PROTOCOL](06-act03-protocol-public-draft.md), décision de nomination explicite, dates et preuves.

## 1. Conditions préalables

| Condition | Situation actuelle |
|---|---|
| Protocole interne ACT03-PROTOCOL | `PENDING` ; référence à renseigner après approbation effective |
| Auteur et fondement de la nomination | `PENDING` ; qualité réelle de porteur indépendant à attester |
| Titulaire nommé | `PENDING` ; aucune identité inférée du compte GitHub |
| Périmètre / dates / revue | `PENDING` ; non rétroactifs par défaut |
| Conflits d'intérêts | Déclaration personnelle à établir, pas préremplie |
| Preuve datée | `PENDING` ; référence publique non sensible à fournir |

## 2. Cumul proposé, non encore attribué

**Rôles candidats :** GOV-01, GOV-02, GOV-03, GOV-05, GOV-06, GOV-07 et GOV-08. Ce cumul se justifierait par la gestion individuelle d'un projet personnel et le périmètre E0 entièrement synthétique ; cette justification doit elle-même être attestée.

| Rôle | Mission candidate | Restriction |
|---|---|---|
| GOV-01 | Registre ADR et traçabilité | Ne remplace pas l'approbateur |
| GOV-02 | Arbitrage technique | Séparer la décision technique de GOV-03 |
| GOV-03 | Arbitrage métier | Volet métier ADR-0005 distinct |
| GOV-05 | Modèle de données / parentage | Documenter les impacts et exceptions |
| GOV-06 | POC backend synthétique | Aucune donnée réelle |
| GOV-07 | QA, tests et preuves | Déclarer toute auto-évaluation |
| GOV-08 | Delivery, CI et publication | Aucun check vert ne vaut approbation ADR |

Pour ADR-0005, une personne cumulant GOV-02 et GOV-03 doit produire **deux décisions identifiables**. Le fait d'avoir testé ou développé un composant n'établit pas la qualité de reviewer indépendant.

## 3. Fonctions hors de cette attribution

**GOV-04 : PENDING_INDEPENDENT_REVIEWER.** Un acte distinct doit nommer une personne compétente, indépendante de l'auteur des travaux examinés, en indiquant le périmètre ADR-0004/0005/0019, les conflits, la date et la preuve de nomination. Ni Copilot, ni OpenCode, ni les tests CI, ni une auto-revue n'équivalent à son avis.

**GOV-09 : APPLICABILITY_PENDING.** Le porteur doit décider séparément si un point de contact pour la vérification de données fictives est nécessaire, et préciser ses missions et son titulaire si applicable. Ce rôle interne éventuel ne constitue pas une nomination juridique de DPO.

## 4. Cumul, séparation, risques

- Le mandat est limité à la gouvernance **interne** de ProjectHub sur un E0 non productif à données exclusivement fictives.
- Le titulaire déclarera lui-même ses intérêts, conflits potentiels et mesures d'atténuation, sans présomption de « aucun conflit ».
- Les décisions techniques, décisions métier, auto-évaluations et avis indépendants devront rester distincts et traçables.
- Toute approbation qui nécessite GOV-04 reste bloquée jusqu'à une revue réellement reçue.
- L'acte n'autorise aucune représentation d'un tiers, production, donnée réelle, ADR accepté de façon tacite ou GO E0/E1.

## 5. Acte de nomination à compléter après protocole effectif

```yaml
act_id: ACT03-APPOINTMENT
decision: PENDING
role_ids:
  - GOV-01
  - GOV-02
  - GOV-03
  - GOV-05
  - GOV-06
  - GOV-07
  - GOV-08
person_or_instance_ref: null
appointing_authority_ref: null
appointing_authority_basis: null
protocol_act_ref: null
mandate_scope: "Proposé : ProjectHub / E0 synthétique seulement"
effective_date: null
expiry_or_review_date: null
cumulative_functions_and_reason: null
conflicts_disclosed: null
mitigation_and_separation: null
approved_by_ref: null
approved_at: null
approval_evidence_uri: null
status: PENDING_FORMAL_APPROVAL
```

**Clause candidate à accepter ou refuser par le porteur après approbation du protocole :** « En ma qualité expressément attestée de porteur de mon projet personnel ProjectHub, j'attribue les fonctions opérationnelles énumérées à la personne explicitement identifiée, pour E0 synthétique seulement, sous réserve des règles de séparation, de transparence et de revue indépendante. »

Avant effet, vérifier l'identité, l'autorité, le fondement, le protocole approuvé, le périmètre, les conflits, les dates et l'approbation explicite. Conserver la version approuvée et les pièces sensibles dans un espace privé ; consigner une référence non sensible au registre.

## 6. Suite opératoire dans l'issue #13

1. Faire instituer **ACT03-PROTOCOL** par une décision expresse, datée et documentée.
2. Faire approuver **ACT03-APPOINTMENT** avec titulaire, périmètre, dates, conflits et preuves authentiques.
3. Désigner indépendamment GOV-04 et trancher l'applicabilité GOV-09 par actes séparés.
4. Après preuve, mettre à jour le [registre officiel](02-architecture-authority-register.md), la matrice ADR et cocher uniquement les responsabilités attribuées.
5. Laisser ADR-0004/0005/0019 `PROPOSED` jusqu'aux revues et décisions réellement approuvées ; ne pas accorder de GO E0 ni E1.

| Élément | État avant approbation |
|---|---|
| Cumul GOV-01/02/03/05/06/07/08 | `PENDING_FORMAL_APPROVAL` |
| GOV-04 | `PENDING_INDEPENDENT_REVIEWER` |
| GOV-09 | `APPLICABILITY_PENDING` |
| GO E0 | `NO_GO_PENDING_AUTHORIZATION` |
| E1 / données réelles | `NO-GO` |

**Références :** [issue #13](https://github.com/tawounfouet/projecthub/issues/13), [dossier ACT-03](04-act03-formal-appointment-dossier.md), [protocole](06-act03-protocol-public-draft.md).
