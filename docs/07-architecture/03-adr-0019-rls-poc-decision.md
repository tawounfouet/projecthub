---
id: PH-ADR-0019-POC-001
title: "ProjectHub - ADR-0019, preuve POC RLS et option recommandée avant E0"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
related_adrs: [ADR-0004, ADR-0005, ADR-0019]
decision_status: PROPOSED_AWAITING_AUTHORITY
recommended_option: R-2
proof_status: CI_VERIFIED_PR15
approver: GOV-02_UNASSIGNED
---

# ADR-0019 - PostgreSQL Row-Level Security

> **Proposition à arbitrer, pas un ADR ACCEPTED.** L'issue [ACT-03 #13](https://github.com/tawounfouet/projecthub/issues/13) ne contient pas de nominations techniques formelles au moment de la préparation du lot P1. La publication de ce rapport et l'exécution d'un POC ne substituent pas une signature de l'autorité GOV-02.

## Contexte et hypothèse de recherche

L'[architecture candidate](00-adr-tenancy-permissions-pre-e0-plan.md) distingue la frontière Organization de Workspace et demande de comparer le schéma partagé avec contrôle applicatif et l'option de défense en profondeur PostgreSQL RLS. La question n'est **pas** de considérer RLS comme source des droits métier : memberships, grants, contexte actif et mandats restent sous contrôle serveur.

## Options à présenter à l'autorité

| Option | Mécanisme | Bénéfice | Risque et coût |
|---|---|---|---|
| R-0 | Filtre tenant et parentage applicatifs, sans RLS | Simplicité opérationnelle du premier bootstrap | Une requête SQL non filtrée peut lire A et B si le rôle a SELECT sur les deux |
| R-1 | RLS sur chaque table tenant-scoped, rôle non owner, FORCE, contexte transaction-local | Défense sur SQL non filtré ou accès ORM brut | Tenant GUC, pooling, migrations, policies, vues, FK et jobs doivent être systématiquement maîtrisés |
| R-2 | POC RLS isolé, adoption dans le schéma Django reportée et conditionnée | Prouve le fonctionnement SQL sans engager une stratégie non approuvée | Pas de défense RLS sur l'application E0 tant que l'ADR n'est pas accepté |

## Protocole reproductible

Les fichiers [POC SQL](../../poc/rls/README.md) exécutent dans PostgreSQL 16 :

1. Deux jeux A/B identiques dans `r0_rows` (sans politique) et `r1_rows` (ENABLE/FORCE RLS).
2. Test avec rôle `ph_poc_app` `NOSUPERUSER NOBYPASSRLS`, différent du propriétaire des tables.
3. Sans contexte `app.organization_id` : zéro ligne visible dans `r1_rows`.
4. Avec `set_config('app.organization_id', A, true)` **dans une transaction** : R-0 affiche A+B, R-1 seulement A.
5. Les écritures sous tenant B depuis contexte A sont refusées, même si la requête est SQL brute.
6. Les contextes se réinitialisent après COMMIT et la bascule A vers B n'hérite pas de A.
7. FORCE RLS est exercé contre le rôle propriétaire non superuser.

Le fichier de tests SQL s'arrête sur toute assertion incorrecte. Le [run GitHub Actions #44862176849](https://github.com/tawounfouet/projecthub/actions/runs/44862176849) a retourné `RLS_POC_ASSERTIONS_PASSED` sur SHA `ae3aa6f321d032366ea50a3008ee2e5aa7609a62`. Les deux jobs E0/Compose sont `success`, avec 20 tests Django et deux smoke tests HTTP passés. Voir le [bilan d'exécution P1](../reports/2026-11-21-p1-e0-rls-execution.md). La présence de preuves CI ne transforme pas cette proposition en ADR approuvé.

## Proposition d'arbitrage technique

**Option recommandée : R-2 pour le démonstrateur synthétique E0**, puis revisiter R-1 avec GOV-02/GOV-04 lorsque les conditions suivantes sont remplies :

- POC exécuté sur PostgreSQL 16 ; rôle d'application sans privilèges de migration et sans BYPASSRLS.
- Preuves de tenancy et permissions applicatives, y compris accès directs, parentage, révocation, export et contexte multi-org.
- Prototype de context management transactionnel Django avec pooling et tâches async testé avant activation RLS sur tables métier.
- Politique de migration/ownership distincte, tests de vues, FOREIGN KEY, erreur d'unicité et absence de fuite d'informations.
- Comparaison de charge sur un jeu représentatif, car deux lignes ne mesurent aucune performance exploitable.
- Gouvernance : mandat, auteur et date de la décision, avis sécurité et conditions de réexamen enregistrés.

Cette proposition reste **un choix d'ingénierie à confirmer** et ne donne pas l'autorisation de démarrer E0 officiellement.

## Décision et preuve humaine à compléter

L'[issue d'arbitrage #16](https://github.com/tawounfouet/projecthub/issues/16) contient les options et les preuves à faire examiner par GOV-02/GOV-04 après nomination officielle. La recommandation R-2 ne vaut pas `ACCEPTED`.

| Élément | État |
|---|---|
| Responsable du POC GOV-06 | UNASSIGNED |
| Security Reviewer GOV-04 | UNASSIGNED |
| Architecture Approver GOV-02 | UNASSIGNED |
| Avis sécurité documenté | PENDING |
| Option acceptée | NOT_APPROVED |
| Date de décision | null |
| Lien du compte rendu d'approbation | null |
| Statut décisionnel ADR-0019 | PROPOSED |

**E1 : NO-GO** tant que les autorisations et les huit gates correspondantes ne sont pas validées.

## Références

- [Registre des mandats](02-architecture-authority-register.md)
- [Plan ADR et tests pré-E0](00-adr-tenancy-permissions-pre-e0-plan.md)
- [Exigences de permissions](../03-requirements/02-business-rules-and-permissions.md)
- [PostgreSQL 16 - Row Security Policies](https://www.postgresql.org/docs/16/ddl-rowsecurity.html)
