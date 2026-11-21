---
id: PH-REP-CI-E0-RELIABILITY-001
title: "ProjectHub - Stabilité HTTP E0, diagnostic et protocole Docker Compose"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-21"
updated_at: "2026-11-21"
source_issue: "https://github.com/tawounfouet/projecthub/issues/19"
proof_status: PENDING_CI
---

# Issue #19 - Diagnostic et expérience reproductible

Lors de la PR #18, la première tentative du [run #44870588111](https://github.com/tawounfouet/projecthub/actions/runs/44870588111) a renvoyé un code HTTP 500 sur `POST /api/context/`, avec `ECONNRESET` côté reverse proxy Next. L'API Django avait répondu au healthcheck et au refus A vers B juste avant. Le deuxième essai sur le même SHA a réussi. La **cause exacte n'est pas démontrée**.

Hypothèses, non prouvées : `runserver` et sa gestion des connexions HTTP/autoreload derrière Next ; intervalle entre démarrage du frontend et disponibilité réelle de PostgreSQL et des sessions ; socket persistante fermée avant sa réutilisation.

## Changement expérimental

1. Serveur WSGI Gunicorn à version épinglée et sans autoreload pour Compose et le smoke CI.
2. Endpoint `/api/health/` conservé pour la liveness ; `/api/ready/` exige le mode synthétique et un aller-retour PostgreSQL sans dévoiler de détails de connexion.
3. Healthcheck backend basé sur la readiness et healthcheck frontend traversant le proxy Next.
4. Trois cycles Compose **avec volumes neufs** en CI : migrations, seed, CSRF, authentification, refus A/B, approbation refusée et export tenant-scoped à chaque cycle.
5. Aucune relance automatique d'une requête métier ayant échoué. Un 500, un socket reset, ou un 401/403 inattendu fait échouer le cycle.
6. Logs de conteneurs bornés uniquement en cas d'échec, sans impression des variables secrètes.

## Critères de sortie

| Exigence | Résultat requis |
|---|---|
| Trois démarrages propres avec PostgreSQL 16 | 3/3 traces dans le même run |
| Endpoint readiness et mode E0 | 200 avec DB disponible ; 503 en dehors du mode E0 |
| Tests positifs/négatifs de tenancy, sessions, CSRF, export | 3/3 cycles, aucun retry des opérations échouées |
| Tests Django, PostgreSQL RLS et build Next.js | Succès sur le même SHA |
| Diagnostic de cause racine | **Non prouvée**, surveillance à poursuivre en cas de récidive |
| Données réelles, approbations ADR, E1 | Strictement exclus |

Les trois démarrages réussis prouveront la stabilité dans ces conditions de CI, pas une garantie générale d'absence d'incidents. Ce lot n'est pas une autorisation officielle E0 et E1 reste NO-GO.
