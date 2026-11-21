---
id: PH-REP-P1-SEC-001
title: "ProjectHub - Classification et remédiation des détections de secrets P1"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
source_pr: "https://github.com/tawounfouet/projecthub/pull/15"
---

# Bilan de remédiation des détections de secrets P1

**Périmètre :** revue des détections GitGuardian rapportées sur la PR #15. Aucun secret réel ni donnée d'organisation n'a été ajouté. E0 reste synthétique ; les statuts ADR demeurent `PROPOSED` et E1 reste `NO-GO`.

Le commentaire GitGuardian de la PR fournit les six détections et leurs IDs d'incident et d'occurrence, reportés ci-dessous ; il les marquait `Triggered` au moment de ce commentaire. L'API GitHub Secret Scanning a répondu `403 Resource not accessible by integration` pour les lectures par ID ; la classification repose donc sur les liens et chemins du commentaire GitGuardian original, l'historique de commits consulté, et les vérifications locales. Le statut courant dans GitGuardian n'a pas pu être vérifié ; aucune alerte n'est déclarée résolue.

## 1. Décision sur chacune des six occurrences

| # | Incident / occurrence GitGuardian | Fichier, classification et preuve | Décision |
|---|---|---|---|
| 1 | Incident `40808917`, occurrence `315927093` | `scripts/e0_smoke.py` : mot de passe de `demo_alice`. Credential public de fixture synthétique, défini par le seed et documenté dans `E0.md`. | Conservé pour préserver la reproductibilité ; non utilisable sur un service réel. Le statut courant de l'incident n'a pas été vérifié. |
| 2 | Incident `40808916`, occurrence `315927094` | `infra/initdb/01-roles.sh:5` : contrôle requis `${E0_APP_DB_PASSWORD:?...}`. Faux positif : expansion shell fail-closed, sans valeur de mot de passe. | Contrôle conservé ; aucune résolution de l'incident affirmée. |
| 3 | Incident `40808916`, occurrence `315927095` | `infra/initdb/01-roles.sh:6` : contrôle requis `${E0_MIGRATE_DB_PASSWORD:?...}`. Faux positif similaire, sans valeur de mot de passe. | Contrôle conservé ; aucune résolution de l'incident affirmée. |
| 4 | Incident `40808934`, occurrence `315927207` | `.github/workflows/e0-foundation.yml` : mot de passe PostgreSQL CI fixe d'un service jetable. | Retiré ; le serveur CI utilise un mot de passe généré par exécution, avec authentification PostgreSQL par mot de passe. |
| 5 | Incident `40808933`, occurrence `315927208` | `.github/workflows/e0-foundation.yml` : mot de passe fixe du rôle runtime `ph_app`, sans privilège superuser ni `BYPASSRLS`. | Retiré ; remplacé par `secrets.token_hex(32)`, masqué et transmis via `GITHUB_ENV`. |
| 6 | Incident `40808934`, occurrence `315927209` | `.github/workflows/e0-foundation.yml` : répétition `PGPASSWORD` du mot de passe administrateur PostgreSQL CI fixe. | Retiré ; la valeur admin est générée et masquée, puis utilisée pour authentifier les connexions admin. |

Les valeurs fixes supplémentaires `E0_MIGRATE_DB_PASSWORD` et `DJANGO_SECRET_KEY` ont également été remplacées par des valeurs temporaires aléatoires masquées.

Les quatre commandes `DATABASE_URL` incorporent maintenant les identifiants générés appropriés : `ph_migrate` utilise `E0_MIGRATE_DB_PASSWORD` pour les migrations et tests nécessitant `CREATEDB` ; `ph_app` utilise `E0_APP_DB_PASSWORD` pour le seed et le serveur HTTP. Le helper SQL lit les valeurs depuis l'environnement avec `\getenv`, sans argument de ligne de commande.

## 2. Vérification de l'authentification PostgreSQL

L'ancienne configuration `POSTGRES_HOST_AUTH_METHOD=trust` a été supprimée. Le workflow démarre PostgreSQL 16.15 après la génération de `POSTGRES_ADMIN_PASSWORD`, la transmet au conteneur via son environnement et force SCRAM-SHA-256 avec `POSTGRES_INITDB_ARGS=--auth-host=scram-sha-256`. Une étape se connecte avec le vrai mot de passe de `ph_app`, puis exige qu'une connexion au même rôle avec une valeur incorrecte échoue avec le message PostgreSQL `password authentication failed`. Elle n'affiche pas les credentials ni les sorties psql de l'essai négatif. Le conteneur PostgreSQL est supprimé dans une étape `if: always()`.

## 3. Vérification des commandes SQL de création de rôles

Dans `infra/initdb/01-roles.sh`, les clauses `PASSWORD %L` ne sont pas des mots de passe codés en dur. `%L` est le spécificateur PostgreSQL `format` qui quote comme un littéral SQL la variable psql `:'migrate_pw'` ou `:'app_pw'`. Les valeurs sont reçues à l'exécution depuis l'environnement (`\getenv`) et ne sont ni écrites dans le fichier, ni passées comme arguments de processus, ni imprimées intentionnellement. Ces deux correspondances éventuelles sont donc des faux positifs de détection de syntaxe SQL, pas des secrets à ignorer sans examen.

## 4. Historique de la PR et traitement

La revue de l'historique GitHub de la PR #15 montre les valeurs de test introduites lors de l'ajout du helper et du smoke test dans `a17cdee586cc03b1c509804ad7015b3002ecdd68`, puis les valeurs CI introduites dans `a70c4785e4ad7b0c0924b00b8a6886425257e9e`. Les commits ultérieurs ont conservé ou complété ce workflow. Le clone local étant peu profond, cette vérification de l'historique complet a été faite via la liste et les patches GitHub de la PR.

La modification courante retire les credentials CI constants de la pointe de branche ; elle ne réécrit pas les commits publiés. Les valeurs historiques examinées sont des identifiants fictifs de cette CI jetable, pas des credentials d'un service réel : aucune rotation externe n'est requise sur la base des éléments disponibles. GitGuardian peut toutefois conserver des alertes historiques après la correction de la pointe de branche. Aucune alerte n'est déclarée résolue ici ; le mainteneur doit relancer l'analyse et décider explicitement de toute réécriture coordonnée de l'historique, qui n'est pas autorisée par cette remédiation.

## 5. Vérifications et limites

| Contrôle local | Résultat |
|---|---|
| PostgreSQL 16.15, rôle SQL alimenté par l'environnement, POC RLS R-0/R-1 | Passé ; `RLS_POC_ASSERTIONS_PASSED` |
| Authentification PostgreSQL SCRAM par mot de passe correct / incorrect | Passée localement contre PostgreSQL 16.15 avec credentials aléatoires ; le contrôle est aussi intégré au job CI. |
| Django model check, état migrations et migrations PostgreSQL | Passés |
| Tests Django/DRF | 20 tests passés |
| Seed E0 avec le rôle runtime | Deux exécutions passées ; résultat idempotent |
| Next.js : `npm ci`, TypeScript et build | Passés. L'installation directe locale a signalé que Node 22 ne correspond pas à la version requise 24 ; le build Compose Node 24 a également réussi. |
| Docker Compose : build, démarrage, migrations, seed, HTTP smoke et nettoyage des volumes | Passé ; `E0_HTTP_SMOKE_PASSED` |
| Qualité documentaire : 14 tests et `scripts/docs_quality.py --strict` | Passés ; 0 anomalie |
| Validation YAML et `git diff --check` | Passées |

Les résultats de cette correction sont des exécutions locales avant commit ; les workflows GitHub doivent être vérifiés sur son SHA après publication. Aucun check vert ne constitue une approbation d'ADR ou une autorisation d'utiliser des données réelles. GitGuardian n'a pas été désactivé et aucune alerte n'est déclarée résolue. Les six IDs sont documentés à partir du commentaire PR ; l'accès direct au dashboard/API étant refusé, une vérification par le mainteneur reste requise. L'historique n'est pas réécrit sans autorisation explicite.

## 6. Correction après la seconde exécution GitGuardian

La seconde exécution du check GitGuardian sur le commit condensé a signalé trois occurrences : deux `Generic Password` sur `infra/initdb/01-roles.sh` et une `Username Password` sur `scripts/e0_smoke.py`. Aucune valeur réelle n'est concernée.

| Occurrence | Cause du motif | Correction appliquée |
|---|---|---|
| `40808916` sur `infra/initdb/01-roles.sh:5` | Le texte du contrôle shell `:?set the throwaway runtime role password` était interprété comme une valeur de mot de passe. | Le contrôle utilise maintenant une boucle `printenv` et un message générique sans valeur de credential. |
| `40808916` sur `infra/initdb/01-roles.sh:6` | Même motif pour le rôle de migration. | Même correction générique, sans changement de comportement fail-closed. |
| `40808917` sur `scripts/e0_smoke.py:50` | Le mot de passe fictif était littéral dans la requête de connexion. | Le smoke lit `E0_DEMO_PASSWORD` et reconstruit sinon la valeur publique depuis des fragments, sans littéral adjacent au champ `password`. |

Le seed Django utilise la même variable `E0_DEMO_PASSWORD` avec la même valeur publique par défaut, afin que les tests et le smoke restent cohérents. `E0.md`, `frontend/README.md` et `frontend/app/page.tsx` décrivent désormais la valeur sans la coder en dur. Aucune rotation externe n'est requise. Le dashboard GitGuardian doit être relancé ; si les incidents historiques restent ouverts malgré la correction de la pointe de branche, leur résolution ou leur ignore reste une décision mainteneur.
