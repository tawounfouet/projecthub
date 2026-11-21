---
id: PH-ARCH-GOV-001
title: "ProjectHub - Registre des autorités et mandats des décisions d'architecture pré-E0"
version: "0.3.0"
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

> **Statut : DRAFT / PROPOSITION DE GOUVERNANCE, AUCUNE NOMINATION APPROUVÉE.** Le commentaire du mainteneur sur l'[issue ACT-03 #13](https://github.com/tawounfouet/projecthub/issues/13#issuecomment-7056931493) autorise la préparation d'un modèle simplifié, pas la nomination d'une personne ni l'approbation d'un ADR. Les identités GitHub, l'assignation d'une issue, une review de PR et une fusion documentaire ne constituent pas un mandat. Un POC PostgreSQL RLS et un sous-ensemble de tests E0 synthétiques ont été exécutés dans la [PR #15](https://github.com/tawounfouet/projecthub/pull/15), avec les workflows [E0](https://github.com/tawounfouet/projecthub/actions/runs/44862485190) et [qualité documentaire](https://github.com/tawounfouet/projecthub/actions/runs/44862485329) réussis sur `cd9e285`. La PR reste ouverte en attente de revue; ces preuves n'approuvent aucun ADR et n'accordent pas de GO E0. E1 reste `NO-GO`.

## 1. Objet, portée et état

Ce registre propose une gouvernance opérationnelle adaptée à un projet actuellement porté par une seule personne. Le cumul de plusieurs fonctions opérationnelles est possible **après délégation explicite**, mais la présente proposition ne désigne aucun titulaire et ne présume ni l'autorité de nomination ni l'étendue de ses pouvoirs.

La portée envisagée est limitée à la préparation des décisions `ADR-0004`, `ADR-0005` et `ADR-0019` et aux expérimentations E0 sur des données exclusivement synthétiques. Un POC et des tests synthétiques ont déjà été exécutés dans la PR #15; cela ne vaut ni approbation des résultats par une autorité, ni autorisation de démarrer officiellement E0. Aucune donnée réelle n'est autorisée par ce registre. Toute évolution vers des données réelles ou E1 exige une décision distincte, des autorités institutionnelles compétentes et les gates applicables.

- **Accord de principe consigné :** le 21 novembre 2026, sur l'issue #13; il autorise la préparation du modèle uniquement.
- **Autorité de nomination et de délégation :** à identifier et à consigner dans un acte formel.
- **Décision d'instauration du protocole :** `PENDING`.
- **Titularisation des fonctions GOV-01 à GOV-09 :** `PENDING`.
- **Questions canoniques :** `PH-OPEN-002`, `PH-OPEN-006` et `PH-OPEN-016` restent `OPEN` jusqu'aux arbitrages compétents signés.
- **Actions dépendantes :** `ACT-04` et `ACT-05` restent `BLOCKED` tant que les mandats et approbations requis manquent.

## 2. Fonctions proposées et cumul

| ID | Fonction | Périmètre du mandat à confirmer | Cumul proposé | Titulaire / statut |
|---|---|---|---|---|
| GOV-01 | Architecture Decision Owner | Tenir le registre ADR, relier décisions, options, risques et preuves; ne se substitue pas aux approbateurs | Bloc opérationnel candidat | À désigner par acte / `PENDING` |
| GOV-02 | Architecture Approver | Décision technique sur `ADR-0004` et `ADR-0019`, et sur le mécanisme technique de `ADR-0005` | Bloc opérationnel candidat; avis distinct à tracer | À désigner par acte / `PENDING` |
| GOV-03 | Domain / Product Authority | Sémantique métier et mandat produit de `ADR-0005` dans le périmètre explicitement délégué | Bloc opérationnel candidat; décision distincte de GOV-02 | À désigner par acte / `PENDING` |
| GOV-04 | Security Reviewer | Examiner menaces, risques inter-tenant, cas de refus, révocation, contournements et risques résiduels | **Revue indépendante**; ne fait pas partie du bloc opérationnel candidat | Évaluateur habilité à désigner / `PENDING` |
| GOV-05 | Data Model Owner | Cohérence du modèle Organization / Workspace / Project / WorkItem et de leurs relations | Bloc opérationnel candidat | À désigner par acte / `PENDING` |
| GOV-06 | Backend POC Lead | Encadrer les POC isolés, dont le POC déjà exécuté dans la PR #15, et leurs suites éventuelles sur données exclusivement synthétiques | Bloc opérationnel candidat | À désigner par acte / `PENDING` |
| GOV-07 | QA / Evidence Owner | Définir les critères avant exécution; tracer scénario, résultat, environnement, date et SHA, y compris les résultats de la PR #15 | Bloc opérationnel candidat; une auto-vérification ne vaut pas revue indépendante | À désigner par acte / `PENDING` |
| GOV-08 | Delivery / CI Maintainer | Maintenir les contrôles de PR et vérifier leur reproductibilité sur le SHA concerné | Bloc opérationnel candidat; ne peut pas déclarer ses propres checks comme approbation métier | À désigner par acte / `PENDING` |
| GOV-09 | Data Protection Contact | Pour E0 seulement, vérifier que les fixtures, exemples et preuves restent synthétiques et excluent les données réelles | Périmètre initial limité aux données synthétiques E0; aucun mandat juridique général n'est présumé | Applicabilité et titulaire à confirmer par acte / `PENDING` |

Le **bloc opérationnel candidat** comprend GOV-01, GOV-02, GOV-03, GOV-05, GOV-06, GOV-07 et GOV-08. Un même titulaire peut recevoir plusieurs de ces délégations, mais chaque responsabilité, décision, conflit d'intérêts et mesure de séparation doit être explicite dans l'acte. Pour `ADR-0005`, l'avis technique GOV-02 et la décision de sémantique GOV-03 sont deux actes distincts, même en cas de cumul.

GOV-04 doit être exercé par un évaluateur habilité distinct de l'auteur des travaux évalués et du responsable du POC. Tant qu'aucun reviewer n'est désigné, aucun avis indépendant de sécurité n'est acquis et une approbation qui en dépend ne peut pas être déclarée complète. GOV-09 ne confère pas un rôle de DPO ni une autorisation de traiter des données réelles; tout changement de périmètre impose une nouvelle décision et une personne compétente à désigner.

Les essais déjà exécutés sont un sous-ensemble technique sur données fictives: comparaison RLS R-0/R-1, tests Django/DRF et smoke tests. Ils sont consignés dans la [PR #15](https://github.com/tawounfouet/projecthub/pull/15) et ses runs CI réussis, notamment sur le SHA `cd9e285`. Cela ne constitue ni une nomination GOV-06/GOV-07, ni une revue de sécurité GOV-04, ni une validation exhaustive des scénarios candidats.

## 3. Matrice proposée des décideurs et reviewers

Les rôles indiqués ci-dessous sont des responsabilités cibles, non des personnes déjà mandatées. Les trois ADR restent `PROPOSED` et leurs approbations `PENDING`.

| ADR | Préparation proposée | Décideur(s) requis | Reviewers / contrôles requis | État |
|---|---|---|---|---|
| `ADR-0004` - tenancy, parentage et isolation | GOV-01, GOV-05, GOV-06 | GOV-02 pour la décision technique | GOV-04 pour la sécurité; GOV-07 pour les critères et preuves; GOV-03 si une sémantique produit est affectée | `PROPOSED`; décision et reviews `PENDING` |
| `ADR-0005` - RBAC, scopes et BusinessMandate | GOV-01, GOV-03, GOV-05, GOV-06 | GOV-03 pour le sens métier; GOV-02 pour le mécanisme technique; les deux décisions doivent être consignées séparément | GOV-04 pour les risques et refus; GOV-07 pour la vérifiabilité; GOV-05 pour la cohérence du modèle | `PROPOSED`; décisions et reviews `PENDING` |
| `ADR-0019` - PostgreSQL RLS | GOV-01, GOV-05, GOV-06 | GOV-02 pour la décision technique | GOV-04 pour les risques et possibilités de contournement; GOV-07 pour les scénarios et résultats; GOV-05 pour les conséquences sur le modèle | `PROPOSED`; décision et reviews `PENDING` |

Une review GitHub, un résultat CI vert ou la fusion d'un ADR ne constitue pas l'acte de décision. Chaque ADR devra enregistrer ses options, conséquences, périmètre, décideur mandaté, avis reçus, réserves, décision explicite et preuve datée. Aucune entrée ne devient `ACCEPTED` sans cette preuve et les approbations distinctes exigées ci-dessus.

Le démarrage d'un POC ou de `SLICE-00` ne découle pas de l'approbation de cette matrice. Une autorisation E0 séparée doit confirmer les mandats, la revue de sécurité requise, les critères QA et l'usage exclusif de données synthétiques. E1 et toute donnée réelle restent `NO-GO`.

## 4. Modèle de décision d'instauration du protocole

Le protocole ne prendra effet qu'après une décision explicite de l'autorité compétente. Le commentaire de principe du 21 novembre 2026 ne remplit pas ce modèle.

```yaml
decision_type: institute_architecture_approval_protocol
appointing_authority_ref: null
authority_basis: null
scope: null
effective_date: null
separation_and_conflict_controls: null
decision: PENDING
approval_evidence_url: null
approved_by_ref: null
approved_at: null
```

La preuve doit être un acte accessible et vérifiable. Une discussion, une assignation, un nom de compte ou une fusion de PR ne suffit pas à démontrer l'autorité, la délégation ou l'approbation.

## 5. Modèle d'acte de nomination

Compléter un acte par fonction ou par groupe de fonctions explicitement cumulées. Les champs inconnus restent vides jusqu'à validation; aucun nom, date, délégation ou lien de preuve n'est à déduire.

```yaml
role_ids: []
person_ref_or_instance: null
appointing_authority_ref: null
appointing_authority_basis: null
delegation_reference: null
mandate_scope: null
effective_date: null
expiry_or_review_date: null
cumulative_roles: []
conflict_of_interest_disclosure: null
separation_of_duties_and_mitigations: null
approval_evidence_url: null
approved_by_ref: null
approved_at: null
status: PENDING
```

Pour qu'une fonction soit marquée comme attribuée, l'autorité de nomination, son fondement, le titulaire ou l'instance, le périmètre, la délégation, la date d'effet, les conflits/cumul et la preuve d'approbation doivent être renseignés et vérifiables. Une identité GitHub ou le rôle `OrgAdmin` ne prouve aucun de ces éléments.

## 6. Validations humaines restant à obtenir

1. Identifier et documenter l'autorité compétente pour instituer le protocole et déléguer les mandats.
2. Approuver le protocole au moyen du modèle de la §4, avec portée, date et preuve consultable.
3. Décider si le bloc opérationnel GOV-01/02/03/05/06/07/08 est approprié, puis nommer son ou ses titulaires par acte, sans confondre cumul proposé et nomination effective.
4. Désigner un reviewer de sécurité GOV-04 habilité et suffisamment indépendant; définir comment les conflits et éventuelles réserves sont traités.
5. Confirmer l'applicabilité et désigner GOV-09 pour le seul périmètre initial des données synthétiques E0; toute extension vers des données réelles exige un nouveau mandat.
6. Formaliser les décideurs et approbations distinctes des ADR-0004, ADR-0005 et ADR-0019 selon la matrice de la §3.
7. Après attribution, recueillir les décisions ADR et leurs preuves; elles ne sont pas incluses dans cette proposition.
8. Faire compléter, revoir indépendamment et accepter formellement les preuves QA/POC déjà exécutées dans la PR #15; définir et exécuter les scénarios restants sur données synthétiques seulement. Les résultats techniques de la PR ne valent ni approbation d'architecture ni GO E0.

Jusqu'à ces validations, les nominations et l'instauration du protocole sont `PENDING`, les `PH-OPEN-002/006/016` restent `OPEN`, `ACT-04` et `ACT-05` restent `BLOCKED`, les ADR restent `PROPOSED`, E0 n'est pas `GO` et E1 reste `NO-GO`. L'issue #13 demeure ouverte jusqu'à vérification humaine de ses critères de clôture.

## 7. Références

- [Issue ACT-03 #13 et accord de principe](https://github.com/tawounfouet/projecthub/issues/13)
- [POC et tests synthétiques E0 dans la PR #15](https://github.com/tawounfouet/projecthub/pull/15)
- [Plan public ADR avant E0](00-adr-tenancy-permissions-pre-e0-plan.md)
- [Baseline technique exhaustive publique, non approuvée](ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md)
- [Questions canoniques encore ouvertes](../00-context/04-open-questions.md)
- [Politique de publication](../PUBLICATION-POLICY.md)
- [Guide de collaboration et de revue](../COLLABORATION-BEST-PRACTICES.md)
