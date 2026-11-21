---
id: PH-ARCH-GOV-ACT03-PROTOCOL-001
title: "ProjectHub - ACT03-PROTOCOL - Modèle public d'institution de gouvernance"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
source_issue: "https://github.com/tawounfouet/projecthub/issues/13"
act_id: ACT03-PROTOCOL
decision: PENDING
approval_status: PENDING_FORMAL_APPROVAL
effective_date: null
approving_authority_ref: null
approval_evidence_uri: null
---

# ACT03-PROTOCOL - Modèle d'acte d'institution (édition publique)

**Statut : DRAFT / NOT APPROVED / NOT EFFECTIVE.** Ce texte est une édition publique autonome et expurgée destinée à la revue. L'original interne et toute pièce nominative, preuve privée ou signature doivent rester hors du dépôt. Sa publication et la fusion de sa PR ne constituent **ni une décision d'institution, ni une nomination, ni un GO E0**.

## 1. Contexte et capacité à confirmer

ProjectHub est présenté par son porteur comme un **projet personnel indépendant**, actuellement porté par une seule personne. Une gouvernance interne du projet peut être proposée, sans mandat pour représenter une société, une association, une organisation tierce ou un client.

| Champ de décision | Valeur |
|---|---|
| Autorité habilitée à instituer son propre protocole | **À attester par le porteur** |
| Qualité et fondement réels | Projet personnel indépendant, capacité et limites à déclarer |
| Périmètre | ProjectHub E0, démonstrateur non productif sur données fictives |
| Date de décision et d'effet | À décider sans rétroactivité présumée |
| Date de réexamen | À fixer |
| Preuve datée d'approbation | Aucune - référence non sensible à renseigner après validation |

Le compte GitHub, un commentaire d'intention, l'assignation d'une issue ou une PR ne remplacent pas une approbation expresse de cet acte.

## 2. Clauses proposées

**P-01 - Institution.** Après adoption expresse, les décisions d'architecture du projet relèveraient d'un protocole documenté avec registre, options, preuves, avis, approbations et réexamens. Tant que le champ `decision` reste `PENDING`, cette clause n'a pas d'effet.

**P-02 - Domaine.** Les décisions candidates concernent ADR-0004 (tenancy), ADR-0005 (permissions et mandats métier), ADR-0019 (PostgreSQL RLS) et un GO/NO-GO E0 séparé. Le POC RLS et SLICE-00 sont des essais sur données synthétiques, pas une autorisation E0 officielle.

**P-03 - Exclusions.** Aucune donnée réelle, production, certification de sécurité, capacité à engager des tiers, autorisation E1 ou DPO institutionnel n'est créée par l'acte.

## 3. Fonctionnement candidat des neuf responsabilités

| Identifiant | Fonction | Limite et traitement |
|---|---|---|
| GOV-01 | Architecture Decision Owner | Registre, versions, preuves, pas approbation par substitution |
| GOV-02 | Architecture Approver | Décisions techniques ADR-0004/0019 et volet technique ADR-0005 |
| GOV-03 | Domain / Product Authority | Décision métier distincte sur ADR-0005 |
| GOV-04 | Security Reviewer | Revue réellement indépendante et habilitée, à nommer séparément |
| GOV-05 | Data Model Owner | Parentages et cohérence Organization / Workspace / Project / WorkItem |
| GOV-06 | Backend POC Lead | POC et essais entièrement synthétiques |
| GOV-07 | QA / Evidence Owner | Preuves et SHA ; auto-revue signalée comme telle |
| GOV-08 | Delivery / CI Maintainer | Contrôles reproductibles, sans approbation automatique |
| GOV-09 | Data Protection Contact | Applicabilité à décider pour les fixtures E0 ; pas de mandat de DPO |

Le **cumul candidat** GOV-01/02/03/05/06/07/08 est possible après nomination explicite. GOV-04 demeure indépendant ; GOV-09 fait l'objet d'une décision distincte. Les avis métier GOV-03 et technique GOV-02 pour ADR-0005 doivent être enregistrés séparément, même si leurs fonctions sont exercées par une même personne.

## 4. Chaîne de décision proposée

1. GOV-01 ouvre une fiche ADR précisant le besoin, les alternatives, les risques et les questions ouvertes.
2. GOV-03 et GOV-02 réalisent leurs analyses métier et technique distinctes ; GOV-05/06 documentent les impacts et le POC.
3. GOV-07 relie les preuves datées, SHA, scénarios positifs et négatifs. `CI success` ne signifie pas `ADR ACCEPTED`.
4. Le reviewer GOV-04, une fois effectivement nommé, émet un avis indépendant, les réserves et les risques résiduels.
5. Le décideur réellement mandaté consigne explicitement l'option retenue, les motifs, les risques acceptés, la date et le réexamen.
6. Le GO/NO-GO officiel E0 est un acte séparé. E1 et les données réelles restent `NO-GO` sans autre autorisation.
7. La publication GitHub ne contient que les éléments autorisés ; la signature originale ou la preuve sensible reste privée.

Un conflit non traité ou une revue GOV-04 requise mais absente bloque l'approbation concernée. Aucune auto-revue ni un agent IA n'est assimilé à une revue indépendante.

## 5. Décision à compléter, sans signature présumée

**Formulation candidate uniquement :** « J'institue pour mon projet personnel ProjectHub, dans les limites E0 synthétiques, le protocole défini au présent acte, sans préjuger de l'attribution de mandats, de l'avis GOV-04, de l'acceptation d'ADR ou du GO E0/E1. »

```yaml
act_id: ACT03-PROTOCOL
decision: PENDING
authority_person_or_instance: null
authority_basis_or_founder_capacity: null
project_scope: "ProjectHub / E0 synthétique seulement"
effective_date: null
expiry_or_review_date: null
approval_rules_ref: "ACT03-PROTOCOL / sections 3-4"
conflict_management_and_separation_ref: "ACT03-PROTOCOL / sections 3-4"
signed_or_approved_by_ref: null
approval_evidence_uri: null
approval_timestamp: null
```

**Conditions de mise en vigueur :** vérifier la qualité du décideur, confirmer ses limites, remplir les champs, examiner le texte, enregistrer une décision explicite et dater l'acte selon un mécanisme d'attestation effectivement retenu. Ne pas exposer de signature personnelle dans le dépôt public.

## 6. Statuts jusqu'à décision expresse

| Élément | Statut |
|---|---|
| ACT03-PROTOCOL et ACT03-APPOINTMENT | `PENDING` |
| Toutes nominations GOV-01..09 | `PENDING` |
| GOV-04 indépendant | `PENDING` |
| ADR-0004 / 0005 / 0019 | `PROPOSED` |
| PH-OPEN-002 / 006 / 016 | `OPEN` |
| ACT-04 / ACT-05 | `BLOCKED` jusqu'aux mandats |
| GO officiel E0 | `NO_GO_PENDING_AUTHORIZATION` |
| E1 et données réelles | `NO-GO` |

**Références :** [issue #13](https://github.com/tawounfouet/projecthub/issues/13), [registre des autorités](02-architecture-authority-register.md), [dossier ACT-03](04-act03-formal-appointment-dossier.md), [ACT03-APPOINTMENT](07-act03-appointment-public-draft.md).
