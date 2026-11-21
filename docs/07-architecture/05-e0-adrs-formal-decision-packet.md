---
id: PH-ARCH-ADR-E0-DECISION-PACKET-001
title: "ProjectHub - Dossier d'arbitrage ADR-0004, ADR-0005, ADR-0019 et GO E0"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
source_issue: "https://github.com/tawounfouet/projecthub/issues/16"
decision_status: PROPOSED_AWAITING_APPROVALS
e0_gate: NO_GO_PENDING_AUTHORIZATION
---

# Décisions E0 - Dossier prêt pour arbitrage

**Aucune décision n'est ici approuvée.** Ce dossier complète la [comparaison RLS](03-adr-0019-rls-poc-decision.md) ; il ne remplace pas les [mandats](02-architecture-authority-register.md) ni le [protocole ACT-03](04-act03-formal-appointment-dossier.md).

## Éléments techniques reproductibles

La [PR #15](https://github.com/tawounfouet/projecthub/pull/15) a intégré un démonstrateur fictif Django/DRF, Next.js et PostgreSQL. Le [run post-fusion sur main #44870888636](https://github.com/tawounfouet/projecthub/actions/runs/44870888636) est `success`, associé au SHA `092bf2ac2f892f8898df24db276c960aebe95429`. Les scripts [POC RLS](../../poc/rls/README.md), 20 tests Django (sur ce SHA), les refus inter-tenant et le smoke HTTP ont été exécutés. Ce sont des preuves d'essais **synthétiques**, pas une attestation d'audit sécurité ni de performance. La stabilité du démarrage a un [suivi #19](https://github.com/tawounfouet/projecthub/issues/19).

## Décisions précédentes à obtenir

| ADR | Objet technique | Éléments à vérifier | Responsable requis |
|---|---|---|---|
| ADR-0004 | Organization comme frontière ; clés composites ; refus A/B | Parentage, contexte, export, fuite d'ID, intégrité DB | GOV-02 avec avis GOV-04/GOV-05/GOV-07 |
| ADR-0005 | Membership, WorkspaceGrant, BusinessMandate séparés | Révocation immédiate, privilèges, cas négatifs, sémantique métier | GOV-03 métier + GOV-02 technique, avec avis GOV-04 |
| ADR-0019 | Défense en profondeur PostgreSQL RLS | R-0, R-1, R-2, risques résiduels, migrations, pooling, tâches | GOV-02 avec avis GOV-04/GOV-05/GOV-07 |

Aucune adoption de RLS sur les tables métier Django n'est prétendue dans le prototype E0 ; le POC R-1 reste isolé.

## Options RLS à arbitrer

| Option | Avantage | Risque à accepter explicitement |
|---|---|---|
| R-0 | Isolation applicative seule, modèle moins complexe | Une requête SQL non filtrée peut exposer plusieurs Organizations |
| R-1 | RLS sur les tables tenant-scoped, défense additionnelle | Contexte transactionnel/pooling/jobs, ownership, migrations et tests à étendre |
| R-2 - RECOMMANDÉE POUR EXAMEN | POC isolé, isolation Django et contraintes composites E0 ; décision R-1 différée | Les tables Django ne bénéficient pas encore de RLS ; les risques d'accès SQL non filtré persistent |

**R-2 est une recommandation technique et non une décision prise.** Avant tout GO, le décideur habilité doit dater et motiver le choix, signer l'acceptation des risques résiduels et prévoir une échéance de réexamen.

## Fiche de décision par ADR (copier pour chaque ADR)

```yaml
adr_id: null  # ADR-0004, ADR-0005 ou ADR-0019
status: PROPOSED
scope: "ProjectHub E0, données synthétiques uniquement"
decision_option: null
alternatives_and_reasons: null
consequences_and_accepted_residual_risks: null
mandatory_tests_and_evidence_sha: null
architecture_approver_GOV02_ref: null
product_authority_GOV03_ref: null
security_review_GOV04_evidence_uri: null
other_reviews_GOV05_GOV07_refs: null
effective_date: null
reassessment_date: null
formal_approval_uri: null
```

Pour ADR-0005, les décisions métier (GOV-03) et technique (GOV-02) doivent être distinctement explicites. Pour ADR-0019, l'avis GOV-04 doit couvrir les chemins de contournement, le SQL non filtré et les limites du POC.

## Acte de GO/NO-GO E0 à compléter séparément

```yaml
gate_id: G-E0-START
decision: NO_GO_PENDING_AUTHORIZATION
scope: "E0 synthétique, démonstrateur non-production"
governing_protocol_ref: null
appointments_GOV02_GOV03: null
GOV04_security_review_uri: null
ADR0004_approved_ref: null
ADR0005_approved_ref: null
ADR0019_approved_ref: null
QA_evidence_sha_and_run: null
risk_acceptance_and_contingencies: null
approvers_refs: []
decision_date: null
approval_evidence_uri: null
```

Le GO E0 ne découle ni de la fusion de la PR #15 ni des contrôles CI. **E1 reste NO-GO** et toutes les données réelles demeurent interdites dans cette expérimentation.

## Critères de clôture de l'issue #16

- [ ] Issue #13 effectivement clôturée après nomination documentée de GOV-02/GOV-03/GOV-04 et mandats applicables.
- [ ] Revue de sécurité indépendante GOV-04 reçue et reliée aux preuves.
- [ ] ADR-0004 et ADR-0005 formellement approuvés dans leurs périmètres respectifs.
- [ ] Option R-0/R-1/R-2 décidée, motivée, signée et datée pour ADR-0019 ; risques et réexamen consignés.
- [ ] Scénarios de refus A/B, révocation, parentage, export et reproduction SQL validés avec SHA/environnement exacts.
- [ ] Acte GO/NO-GO E0 signé par les autorités mandatées et lié au registre.
- [ ] Aucune prétention à E1 GO ou à l'utilisation de données réelles.

**Statut de clôture : BLOCKED_BY_GOVERNANCE_AND_SECURITY_REVIEW.** Les documents peuvent être publiés comme propositions, mais l'issue ne doit pas être fermée avant ces décisions réelles.
