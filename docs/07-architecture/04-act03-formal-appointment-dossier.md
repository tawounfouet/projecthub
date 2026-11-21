---
id: PH-ARCH-GOV-ACT03-PACKET-001
title: "ProjectHub - Dossier de décision de gouvernance ACT-03"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
source_issue: "https://github.com/tawounfouet/projecthub/issues/13"
approval_status: PENDING
---

# ACT-03 - Actes de gouvernance à décider

**Ce document est un formulaire de décision, pas une nomination.** Le porteur a approuvé le **principe** de la gouvernance simplifiée dans l'[issue #13](https://github.com/tawounfouet/projecthub/issues/13), mais aucun acte de nomination ou de délégation n'a été fourni. La fusion d'une PR, le compte GitHub du mainteneur et un assistant IA ne suffisent pas à créer un mandat.

## Périmètre strict

Organiser uniquement le suivi technique et les décisions du démonstrateur ProjectHub E0 sur données fictives. Aucun périmètre juridique au nom d'un tiers, aucun rôle DPO présumé, aucun E1 ou accès aux données réelles.

## Proposition soumise au porteur

| Ensemble | Rôles proposés | Limites |
|---|---|---|
| Bloc opérationnel cumulable | GOV-01, GOV-02, GOV-03, GOV-05, GOV-06, GOV-07 et GOV-08 | Chaque délégation doit être décidée et documentée ; les décisions techniques et métier restent distinctes ; toute auto-revue est déclarée |
| Sécurité indépendante | GOV-04 | Nommé séparément, habilité et indépendant de l'auteur du POC ; aucun audit indépendant implicite |
| Protection des données E0 | GOV-09 si applicable | Garantir le caractère fictif des données ; aucun mandat de DPO ni d'autorisation E1 |

## Acte A - Institution du protocole (à compléter par l'autorité compétente)

```yaml
act_id: ACT03-PROTOCOL
decision: PENDING
authority_person_or_instance: null
authority_basis_or_founder_capacity: null
project_scope: "ProjectHub / E0 synthétique seulement"
effective_date: null
expiry_or_review_date: null
approval_rules: null
conflict_management_and_separation: null
signed_or_approved_by_ref: null
approval_evidence_uri: null
approval_timestamp: null
```

Le porteur doit attester explicitement de sa capacité à instituer une gouvernance interne pour le projet. La preuve peut être un acte daté et approuvé, selon le cadre juridique et organisationnel réellement applicable. Ne pas publier de données personnelles ou de signatures sensibles dans le dépôt public ; n'enregistrer qu'une référence autorisée à la preuve.

## Acte B - Attribution des fonctions (un acte par ensemble de mandats cumulés)

```yaml
act_id: ACT03-APPOINTMENT
decision: PENDING
role_ids: []
person_or_instance_ref: null
appointing_authority_ref: null
appointing_authority_basis: null
protocol_act_ref: null
mandate_scope: null
effective_date: null
expiry_or_review_date: null
cumulative_functions_and_reason: null
conflicts_disclosed: null
mitigation_and_separation: null
approved_by_ref: null
approved_at: null
approval_evidence_uri: null
```

Le fait d'être seul porteur justifie **une proposition de cumul**, pas une approbation par défaut. GOV-03 (autorité métier) et GOV-02 (technique) doivent rendre des décisions identifiables séparément sur ADR-0005, même si elles ont le même titulaire.

## Acte C - Revue indépendante de sécurité GOV-04

```yaml
act_id: ACT03-SECURITY-REVIEW
review_status: PENDING
reviewer_ref: null
independence_and_conflicts_confirmed: null
qualification_or_review_scope: null
covered_adrs: [ADR-0004, ADR-0005, ADR-0019]
review_evidence_uri: null
review_date: null
findings_and_residual_risks: null
approval_or_reservations: null
```

L'agent IA, les tests CI et la revue de code par l'auteur ne sont pas des avis indépendants de GOV-04.

## Matrice de décision à ratifier

| Objet | Autorité de décision candidate | Revue requise | État |
|---|---|---|---|
| ADR-0004 / frontières Organization | GOV-02 | GOV-04, GOV-05, GOV-07 | PROPOSED |
| ADR-0005 / memberships, grants, BusinessMandate | GOV-03 sur métier et GOV-02 sur technique, décisions distinctes | GOV-04, GOV-05, GOV-07 | PROPOSED |
| ADR-0019 / RLS | GOV-02 | GOV-04, GOV-05, GOV-07 | PROPOSED |
| GO/NO-GO E0 | GOV-03 et GOV-02 habilités selon protocole | GOV-04 et GOV-07 | NOT_GRANTED |

## Critères de sortie correspondant exactement à l'issue #13

- [ ] Acte A instituant le protocole signé et référencé.
- [ ] Acte B pour tous les rôles applicables, avec titulaires, pouvoir délégant, périmètre, date et conflits.
- [ ] Acte C et reviewer GOV-04 habilité, indépendant et réellement désigné.
- [ ] GOV-09 déclaré applicable ou non applicable et motivé, sans mandat légal présumé.
- [ ] Matrice ADR approuvée et intégrée dans [le registre de mandats](02-architecture-authority-register.md).
- [ ] Les références `PH-OPEN-002/006/016` restent `OPEN` tant que leurs ADR sont non signés ; `ACT-04/05` restent `BLOCKED` jusqu'aux mandats.
- [ ] Approbation du périmètre publiable et vérification du dernier SHA de la PR de mise à jour.

**Statut de clôture : BLOCKED_BY_HUMAN_APPOINTMENTS.** Quand ces preuves existent réellement, mettre à jour les champs `PENDING`, fusionner le registre, cocher l'issue et seulement ensuite la clôturer.
