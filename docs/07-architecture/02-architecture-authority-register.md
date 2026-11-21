---
id: PH-ARCH-GOV-001
title: "ProjectHub - Registre des autorités et mandats des décisions d'architecture pré-E0"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
owner: "Architecture Decision Owner - titulaire à désigner"
source_baseline: PH-AEB-001
nomination_status: PENDING_FORMAL_APPROVAL
related_adrs: [ADR-0004, ADR-0005, ADR-0019]
related_open_questions: [PH-OPEN-002, PH-OPEN-006, PH-OPEN-016, PH-OPEN-020]
---

# ProjectHub - Registre des autorités d'architecture avant E0

> **Statut : DRAFT / AUCUNE NOMINATION APPROUVÉE.** Ce registre rend les mandats et les décisions à obtenir explicites. La publication d'une PR, l'assignation d'une issue GitHub ou le rôle de mainteneur du dépôt ne constituent pas la désignation d'une autorité architecture, sécurité, métier ou juridique. Aucun ADR n'est `ACCEPTED`. Aucun POC E0 n'est attesté.

## 1. Coordination de la nomination

- **Point de suivi GitHub :** [issue #13 - ACT-03](https://github.com/tawounfouet/projecthub/issues/13).
- **Coordination de suivi proposée :** le mainteneur GitHub `@tawounfouet` est l'assigné de l'issue **uniquement pour solliciter et enregistrer les nominations**. Cela ne lui attribue pas automatiquement un mandat d'approbation métier ou de sécurité.
- **Autorité de nomination :** à identifier formellement.
- **Décision d'institution du protocole :** `PENDING`, à consigner avec auteur, date, périmètre, preuve et conflit d'intérêts.
- **Données autorisées pour l'étude E0 :** jeux strictement synthétiques. E1 conserve `NO-GO`.

## 2. Fonctions à attribuer nominativement

| ID | Fonction | Responsabilité et portée du mandat candidat | Titulaire | Statut |
|---|---|---|---|---|
| GOV-01 | Architecture Decision Owner | Tenir le registre, relier décisions, scénarios et preuves ; ne signe pas à la place de l'approbateur | `UNASSIGNED` | `PENDING` |
| GOV-02 | Architecture Approver | Approuver `ADR-0004` et `ADR-0019` pour une portée E0 explicite | `UNASSIGNED` | `PENDING` |
| GOV-03 | Domain / Product Authority | Approuver les règles métier et mandats de `ADR-0005` | `UNASSIGNED` | `PENDING` |
| GOV-04 | Security Reviewer | Évaluer les risques inter-tenant, les refus, la révocation et les alternatives RLS | `UNASSIGNED` | `PENDING` |
| GOV-05 | Data Model Owner | Définir la cohérence Organization / Workspace / Project / WorkItem | `UNASSIGNED` | `PENDING` |
| GOV-06 | Backend PoC Lead | Prototyper les options avec données fictives uniquement | `UNASSIGNED` | `PENDING` |
| GOV-07 | QA / Evidence Owner | Définir les tests avant exécution et conserver SHA, environnement et résultats | `UNASSIGNED` | `PENDING` |
| GOV-08 | Delivery / CI Maintainer | Garantir les contrôles documentaires et la traçabilité des PR | `UNASSIGNED` | `PENDING` |
| GOV-09 | Data Protection Contact | Examiner la minimisation et l'interdiction de données réelles en E0 | `UNASSIGNED` | `PENDING` |

Une même personne peut cumuler des fonctions **seulement si** la séparation des responsabilités et les éventuels conflits sont évalués et consignés. La revue de sécurité indépendante est préférée lorsque possible.

## 3. Carte des approbations requises

| Décision | Préparation | Avis attendu | Approbation compétente | Statut |
|---|---|---|---|---|
| `ADR-0004` : tenant, parentage, isolation | GOV-01 / GOV-05 / GOV-06 | GOV-04 et GOV-07 | GOV-02 | `PROPOSED` |
| `ADR-0005` : RBAC, scopes, BusinessMandate | GOV-01 / GOV-03 / GOV-06 | GOV-04 et GOV-07 | GOV-03 pour le métier ; GOV-02 pour le mécanisme technique | `PROPOSED` |
| `ADR-0019` : couche PostgreSQL RLS | GOV-01 / GOV-06 | GOV-04 / GOV-05 / GOV-07 | GOV-02 | `PROPOSED` |
| Démarrer `SLICE-00` sur données fictives | GOV-01 / GOV-06 | GOV-04 / GOV-07 | GOV-02 (technique) et GOV-03 (périmètre produit), décisions distinctes | `NO_GO` |
| Pilote E1 et données réelles | Hors E0 ; autorités organisationnelles à nommer séparément | Sécurité, données, exploitation | Autorisation institutionnelle spécifique et huit gates E1 | `NO_GO` |

Les approbations distinctes pour `ADR-0005` et E0 ne sont pas deux signatures interchangeables. Elles doivent posséder leur propre périmètre et leur propre preuve.

## 4. Registre de nomination à compléter par l'autorité

Le dossier de chaque fonction doit inclure :

```yaml
role_id: GOV-02
person_or_instance_ref: null
appointing_authority_ref: null
mandate_scope: null
delegation_basis: null
effective_at: null
expires_at: null
approval_evidence_url: null
conflict_of_interest_disclosure: null
status: PENDING
```

**Critère ACT-03 :** aucun rôle `GOV-01..09` requis ne reste sans titulaire, pouvoir et preuve adaptés au périmètre ; protocole institué par décision datée ; chaîne ADR vers approbateur sans ambiguïté. Tant que ces conditions manquent, l'action demeure `IN_REVIEW / BLOCKED_ON_NOMINATION`, et `ACT-04` / `ACT-05` ne peuvent pas être déclarées achevées.

## 5. Références

- [Plan public ADR avant E0](00-adr-tenancy-permissions-pre-e0-plan.md)
- [Baseline technique exhaustive publique, non approuvée](ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md)
- [Questions canoniques encore ouvertes](../00-context/04-open-questions.md)
- [Politique de publication](../PUBLICATION-POLICY.md)
