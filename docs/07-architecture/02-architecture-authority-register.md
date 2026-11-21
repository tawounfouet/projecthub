---
id: PH-ARCH-GOV-001
title: "ProjectHub - Registre des autorités et mandats des décisions d'architecture pré-E0"
version: "0.4.0"
status: in-review
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
owner: "Fondateur et porteur indépendant de ProjectHub - référence privée ACT03-APPOINTMENT-2026-11-21-private-v1"
source_baseline: PH-AEB-001
nomination_status: PARTIALLY_APPROVED
protocol_act_ref: "ACT03-PROTOCOL-2026-11-21-private-v1"
appointment_act_ref: "ACT03-APPOINTMENT-2026-11-21-private-v1"
gov09_decision_ref: "GOV-09-2026-11-21-private-v1"
related_adrs: [ADR-0004, ADR-0005, ADR-0019]
related_open_questions: [PH-OPEN-002, PH-OPEN-006, PH-OPEN-016, PH-OPEN-020]
---

# ProjectHub - Registre des autorités d'architecture avant E0

> **Statut : IN_REVIEW / NOMINATIONS OPÉRATIONNELLES APPROUVÉES, GOV-04 PENDING.** Le protocole ACT03-PROTOCOL, l'acte ACT03-APPOINTMENT et la décision GOV-09 ont été approuvés et datés par le porteur le 2026-11-21. Les originaux signés restent hors du dépôt; seules des références non sensibles sont publiées ici. GOV-04 demeure `PENDING` jusqu'à la nomination d'un reviewer indépendant. Un POC PostgreSQL RLS et un sous-ensemble de tests E0 synthétiques ont été exécutés dans la [PR #15](https://github.com/tawounfouet/projecthub/pull/15), avec les workflows post-fusion [E0](https://github.com/tawounfouet/projecthub/actions/runs/44870333128) et [qualité documentaire](https://github.com/tawounfouet/projecthub/actions/runs/44870333226) réussis sur `1095b7e`. Ces preuves n'approuvent aucun ADR et n'accordent pas de GO E0. E1 reste `NO-GO`.

## 1. Objet, portée et état

Ce registre enregistre une gouvernance opérationnelle adaptée à un projet porté par une seule personne. Le cumul des sept fonctions opérationnelles est désormais approuvé par ACT03-APPOINTMENT; GOV-04 reste indépendant et non attribué. Les originaux signés restent privés; seules des références non sensibles sont publiées.

La portée envisagée est limitée à la préparation des décisions `ADR-0004`, `ADR-0005` et `ADR-0019` et aux expérimentations E0 sur des données exclusivement synthétiques. Un POC et des tests synthétiques ont déjà été exécutés dans la PR #15; cela ne vaut ni approbation des résultats par une autorité, ni autorisation de démarrer officiellement E0. Aucune donnée réelle n'est autorisée par ce registre. Toute évolution vers des données réelles ou E1 exige une décision distincte, des autorités institutionnelles compétentes et les gates applicables.

- **Accord de principe consigné :** le 21 novembre 2026, sur l'issue #13; il a autorisé la préparation du modèle.
- **Autorité de nomination et de délégation :** fondateur et porteur indépendant de ProjectHub, attesté dans les actes privés.
- **Décision d'instauration du protocole :** `APPROVED` le 2026-11-21, référence `ACT03-PROTOCOL-2026-11-21-private-v1`.
- **Titularisation :** GOV-01, GOV-02, GOV-03, GOV-05, GOV-06, GOV-07 et GOV-08 sont `APPROVED` le 2026-11-21, référence `ACT03-APPOINTMENT-2026-11-21-private-v1`; GOV-09 est applicable comme contrôle interne limité aux données synthétiques E0, référence `GOV-09-2026-11-21-private-v1`; GOV-04 reste `PENDING`.
- **Questions canoniques :** `PH-OPEN-002`, `PH-OPEN-006` et `PH-OPEN-016` restent `OPEN` jusqu'aux arbitrages compétents signés.
- **Actions dépendantes :** `ACT-04` et `ACT-05` restent `BLOCKED` tant que la revue indépendante GOV-04 et les décisions ADR manquent.

## 2. Fonctions attribuées et cumul

| ID | Fonction | Périmètre du mandat | Cumul approuvé | Titulaire / statut |
|---|---|---|---|---|
| GOV-01 | Architecture Decision Owner | Tenir le registre ADR, relier décisions, options, risques et preuves; ne se substitue pas aux approbateurs | Bloc opérationnel approuvé | Porteur indépendant / `APPROVED` |
| GOV-02 | Architecture Approver | Décision technique sur `ADR-0004` et `ADR-0019`, et sur le mécanisme technique de `ADR-0005` | Bloc opérationnel approuvé; avis technique distinct à tracer | Porteur indépendant / `APPROVED` |
| GOV-03 | Domain / Product Authority | Sémantique métier et mandat produit de `ADR-0005` dans le périmètre explicitement délégué | Bloc opérationnel approuvé; décision métier distincte de GOV-02 | Porteur indépendant / `APPROVED` |
| GOV-04 | Security Reviewer | Examiner menaces, risques inter-tenant, cas de refus, révocation, contournements et risques résiduels | **Revue indépendante**; expressément exclue du cumul | Évaluateur habilité à désigner / `PENDING` |
| GOV-05 | Data Model Owner | Cohérence du modèle Organization / Workspace / Project / WorkItem et de leurs relations | Bloc opérationnel approuvé | Porteur indépendant / `APPROVED` |
| GOV-06 | Backend POC Lead | Encadrer les POC isolés, dont le POC déjà exécuté dans la PR #15, et leurs suites éventuelles sur données exclusivement synthétiques | Bloc opérationnel approuvé | Porteur indépendant / `APPROVED` |
| GOV-07 | QA / Evidence Owner | Définir les critères avant exécution; tracer scénario, résultat, environnement, date et SHA, y compris les résultats de la PR #15 | Bloc opérationnel approuvé; auto-évaluation déclarée | Porteur indépendant / `APPROVED` |
| GOV-08 | Delivery / CI Maintainer | Maintenir les contrôles de PR et vérifier leur reproductibilité sur le SHA concerné | Bloc opérationnel approuvé; checks non assimilés à une approbation métier | Porteur indépendant / `APPROVED` |
| GOV-09 | Data Protection Contact | Pour E0 seulement, vérifier que les fixtures, exemples et preuves restent synthétiques et excluent les données réelles | Contrôle interne applicable aux seules données synthétiques E0; aucun mandat de DPO | Porteur indépendant / `APPROVED` |

Le **bloc opérationnel attribué** comprend GOV-01, GOV-02, GOV-03, GOV-05, GOV-06, GOV-07 et GOV-08. Le cumul est approuvé par ACT03-APPOINTMENT, avec déclaration des conflits et mesures de séparation. Pour `ADR-0005`, l'avis technique GOV-02 et la décision de sémantique GOV-03 restent deux actes distincts, même en cas de cumul.

GOV-04 doit être exercé par un évaluateur habilité distinct de l'auteur des travaux évalués et du responsable du POC. Tant qu'aucun reviewer n'est désigné, aucun avis indépendant de sécurité n'est acquis et une approbation qui en dépend ne peut pas être déclarée complète. GOV-09 a fait l'objet d'une décision distincte limitée aux données synthétiques E0; il ne confère pas de rôle de DPO ni d'autorisation de traiter des données réelles.

Les essais déjà exécutés sont un sous-ensemble technique sur données fictives: comparaison RLS R-0/R-1, tests Django/DRF et smoke tests. Ils sont consignés dans la [PR #15](https://github.com/tawounfouet/projecthub/pull/15) et ses runs CI réussis, notamment sur le SHA `1095b7e`. Les mandats GOV-06 et GOV-07 résultent de l'acte de nomination, non de ces essais; ceux-ci ne constituent ni une revue de sécurité GOV-04, ni une validation exhaustive des scénarios candidats.

## 3. Matrice proposée des décideurs et reviewers

Les rôles indiqués ci-dessous sont désormais rattachés à des mandats attribués pour le bloc opérationnel et le contrôle GOV-09; GOV-04 reste à nommer. Les trois ADR restent `PROPOSED` et leurs approbations `PENDING`.

| ADR | Préparation proposée | Décideur(s) requis | Reviewers / contrôles requis | État |
|---|---|---|---|---|
| `ADR-0004` - tenancy, parentage et isolation | GOV-01, GOV-05, GOV-06 | GOV-02 pour la décision technique | GOV-04 pour la sécurité; GOV-07 pour les critères et preuves; GOV-03 si une sémantique produit est affectée | `PROPOSED`; décision et reviews `PENDING` |
| `ADR-0005` - RBAC, scopes et BusinessMandate | GOV-01, GOV-03, GOV-05, GOV-06 | GOV-03 pour le sens métier; GOV-02 pour le mécanisme technique; les deux décisions doivent être consignées séparément | GOV-04 pour les risques et refus; GOV-07 pour la vérifiabilité; GOV-05 pour la cohérence du modèle | `PROPOSED`; décisions et reviews `PENDING` |
| `ADR-0019` - PostgreSQL RLS | GOV-01, GOV-05, GOV-06 | GOV-02 pour la décision technique | GOV-04 pour les risques et possibilités de contournement; GOV-07 pour les scénarios et résultats; GOV-05 pour les conséquences sur le modèle | `PROPOSED`; décision et reviews `PENDING` |

Une review GitHub, un résultat CI vert ou la fusion d'un ADR ne constitue pas l'acte de décision. Chaque ADR devra enregistrer ses options, conséquences, périmètre, décideur mandaté, avis reçus, réserves, décision explicite et preuve datée. Aucune entrée ne devient `ACCEPTED` sans cette preuve et les approbations distinctes exigées ci-dessus.

Le démarrage d'un POC ou de `SLICE-00` ne découle pas de l'approbation de cette matrice. Une autorisation E0 séparée doit confirmer les mandats, la revue de sécurité requise, les critères QA et l'usage exclusif de données synthétiques. E1 et toute donnée réelle restent `NO-GO`.

## 4. Décision d'instauration du protocole

Le protocole a été institué par décision expresse du fondateur et porteur indépendant le 2026-11-21. Le commentaire de principe du 21 novembre 2026 ne suffisait pas; l'acte privé approuvé apporte la preuve.

```yaml
decision_type: institute_architecture_approval_protocol
appointing_authority_ref: "Fondateur et porteur indépendant de ProjectHub"
authority_basis: "Acte privé ACT03-PROTOCOL-2026-11-21-private-v1"
scope: "ProjectHub / E0 synthétique seulement"
effective_date: "2026-11-21"
separation_and_conflict_controls: "ACT03-PROTOCOL sections 3-4; GOV-04 exclu du cumul; GOV-02 et GOV-03 distincts"
decision: APPROVED
approval_evidence_url: "ACT03-PROTOCOL-2026-11-21-private-v1 (référence non sensible, original hors dépôt)"
approved_by_ref: "Fondateur et porteur indépendant"
approved_at: "2026-11-21"
```

La preuve est un acte privé daté, conservé hors dépôt. La publication de cette référence ne remplace pas l'original et n'ajoute aucun pouvoir de représentation de tiers.

## 5. Modèle d'acte de nomination

Le modèle ci-dessous enregistre l'acte de nomination effectivement approuvé pour le bloc opérationnel. GOV-09 est consigné séparément dans la section 1 avec sa propre référence.

```yaml
role_ids: [GOV-01, GOV-02, GOV-03, GOV-05, GOV-06, GOV-07, GOV-08]
person_ref_or_instance: "Porteur indépendant de ProjectHub - référence privée ACT03-APPOINTMENT-2026-11-21-private-v1"
appointing_authority_ref: "Fondateur et porteur indépendant de ProjectHub"
appointing_authority_basis: "Acte privé ACT03-PROTOCOL-2026-11-21-private-v1"
delegation_reference: "ACT03-APPOINTMENT-2026-11-21-private-v1"
mandate_scope: "ProjectHub / E0 synthétique seulement"
effective_date: "2026-11-21"
expiry_or_review_date: "2027-05-21"
cumulative_roles: [GOV-01, GOV-02, GOV-03, GOV-05, GOV-06, GOV-07, GOV-08]
conflict_of_interest_disclosure: "Cumul des mandats opérationnels; auteur des travaux E0; responsable POC GOV-06; auto-vérification GOV-07"
separation_of_duties_and_mitigations: "Décisions GOV-02 et GOV-03 séparées; GOV-04 externe à désigner; preuves datées; checks CI non assimilés à une approbation ADR"
approval_evidence_url: "ACT03-APPOINTMENT-2026-11-21-private-v1 (référence non sensible, original hors dépôt)"
approved_by_ref: "Fondateur et porteur indépendant"
approved_at: "2026-11-21"
status: APPROVED
```

Pour qu'une fonction soit marquée comme attribuée, l'autorité de nomination, son fondement, le titulaire, le périmètre, la délégation, la date d'effet, les conflits/cumul et la preuve d'approbation doivent être renseignés et vérifiables. Une identité GitHub ou le rôle `OrgAdmin` ne prouve aucun de ces éléments.

## 6. Validations humaines : état

1. [x] Identifier et documenter l'autorité compétente pour instituer le protocole et déléguer les mandats.
2. [x] Approuver le protocole au moyen du modèle de la §4, avec portée, date et preuve conservée hors dépôt.
3. [x] Décider du bloc opérationnel GOV-01/02/03/05/06/07/08 et nommer son titulaire par acte, sans confondre cumul proposé et nomination effective.
4. [ ] Désigner un reviewer de sécurité GOV-04 habilité et suffisamment indépendant; définir comment les conflits et éventuelles réserves sont traités.
5. [x] Confirmer l'applicabilité de GOV-09 au seul périmètre des données synthétiques E0; toute extension vers des données réelles exige un nouveau mandat.
6. [ ] Formaliser les décideurs et approbations distinctes des ADR-0004, ADR-0005 et ADR-0019 selon la matrice de la §3.
7. [ ] Après attribution, recueillir les décisions ADR et leurs preuves.
8. [ ] Faire compléter, revoir indépendamment et accepter formellement les preuves QA/POC déjà exécutées dans la PR #15; définir et exécuter les scénarios restants sur données synthétiques seulement.

Les validations 1, 2, 3 et 5 sont réalisées par actes privés datés. GOV-04 et les décisions ADR restent `PENDING`; les `PH-OPEN-002/006/016` restent `OPEN`, `ACT-04` et `ACT-05` restent `BLOCKED`, les ADR restent `PROPOSED`, E0 n'est pas `GO` et E1 reste `NO-GO`. L'issue #13 demeure ouverte jusqu'à vérification humaine de ses critères de clôture.

Les [modèles publics ACT03-PROTOCOL](06-act03-protocol-public-draft.md) et [ACT03-APPOINTMENT](07-act03-appointment-public-draft.md) restent des éditions de référence DRAFT. L'institution et la nomination résultent des actes privés approuvés, non de leur publication. Les originaux signés ne sont pas publiés.

## 7. Références

- [Issue ACT-03 #13 et accord de principe](https://github.com/tawounfouet/projecthub/issues/13)
- [POC et tests synthétiques E0 dans la PR #15](https://github.com/tawounfouet/projecthub/pull/15)
- [Plan public ADR avant E0](00-adr-tenancy-permissions-pre-e0-plan.md)
- [Baseline technique exhaustive publique, non approuvée](ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md)
- [Questions canoniques encore ouvertes](../00-context/04-open-questions.md)
- [Politique de publication](../PUBLICATION-POLICY.md)
- [Guide de collaboration et de revue](../COLLABORATION-BEST-PRACTICES.md)
