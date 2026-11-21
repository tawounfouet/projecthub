---
id: PH-REQ-NFR-001
title: "ProjectHub - Exigences non fonctionnelles candidates (édition publique)"
version: "0.1.0"
status: draft
classification: public
owner: "ProjectHub Requirements / Engineering - approbation à obtenir"
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/03-requirements/00-functional-requirements.md"
  - "docs/03-requirements/02-business-rules-and-permissions.md"
  - "docs/03-requirements/03-requirements-traceability.md"
---

# ProjectHub - Exigences non fonctionnelles

> **Édition publique expurgée, draft.** Le corpus source contient 113 exigences `PH-NFR-001..113` organisées en douze familles. Les descriptions et épreuves suivantes constituent une synthèse générique ; aucune mesure, conformité, SLO ou restauration n'est considérée comme acquise.

## 1. Distinction fondamentale

Une exigence non fonctionnelle spécifie **comment le système doit se comporter sous une contrainte observable**, par exemple confidentialité, sécurité, fiabilité, accessibilité ou qualité d'exploitation. Un libellé vague comme « sécurisé et rapide » ne suffit pas : il faut définir un risque, un contexte, un seuil convenu et une preuve.

| Priorité candidate | Nombre selon registre privé | Sens |
|---|---:|---|
| `P0-G` | 69 | Gates de sûreté et d'exploitation avant données réelles |
| `P0-C` | 22 | Qualité du parcours MVP candidat |
| `P1` | 14 | Améliorations à expérimenter |
| `P2` | 8 | Extensions ou ambitions futures |
| **Total** | **113** | Valeurs candidates, sans approbation |

Les seuils chiffrés de performance, sauvegarde ou disponibilité restent à définir avec un scénario de charge et une autorité responsable. Ne pas inventer de SLA.

## 2. Les 12 familles et plages d'IDs

| Famille | Plage stable | Objet à vérifier |
|---|---|---|
| Isolation et autorisations | `PH-NFR-001..010` | Permissions serveur, contextes, index, exports et tâches |
| Identité et sessions | `PH-NFR-011..019` | Authentification, révocation, privilèges et identité technique |
| Confidentialité des données | `PH-NFR-020..029` | Consentement, minimisation, protection, rétention, sortie |
| Sécurité applicative / supply chain | `PH-NFR-030..039` | Validation, injections, secrets, dépendances, vulnérabilités |
| Intégrité et audit | `PH-NFR-040..048` | Transactions, concurrences, horodatages et imputabilité |
| Continuité / restauration | `PH-NFR-049..058` | Exploitation, backups, restauration, rollback et RPO/RTO |
| Performance / capacité | `PH-NFR-059..067` | Mesures, pagination, charge et dégradation contrôlée |
| Accessibilité / utilisabilité | `PH-NFR-068..077` | Clavier, focus, contrastes, messages et charge cognitive |
| Observabilité / support | `PH-NFR-078..086` | Logs, alertes, runbooks et incidents |
| Maintenabilité / conception | `PH-NFR-087..096` | Modules, migrations, tests, CI, ADR et reproductibilité |
| Interopérabilité / réversibilité | `PH-NFR-097..105` | Export lisible, import contrôlé, liens et contrats externes |
| IA et automatisations futures | `PH-NFR-106..113` | Agents désactivés au MVP, permissions et validation humaine |

La présence de ces familles n'oblige pas à développer leurs extensions dès le premier incrément.

## 3. Tests de sécurité prioritaires

| ID | Résultat attendu candidat | Épreuve vérifiable |
|---|---|---|
| `PH-NFR-001` | Toutes les opérations respectent l'Organization autorisée côté serveur | GET, PATCH, DELETE, recherche et export entre deux tenants fictifs |
| `PH-NFR-002` | Contexte actif explicite | Utilisateur membre de deux Organizations, bascule sans fuite |
| `PH-NFR-003` | Objets enfants cloisonnés | WorkItem/Project par ID étranger, parentage imbriqué |
| `PH-NFR-005` | Fichiers et exports séparés | Vérifier que le fichier A n'inclut jamais d'objet B |
| `PH-NFR-006` | Recherche bornée aux droits | Sentinelle uniquement dans B invisible à A |
| `PH-NFR-007` | Jobs asynchrones avec contexte contrôlé | Exécution retardée après révocation du droit |
| `PH-NFR-009` | Permissions par acte et ressource | Lecture permise, approbation refusée selon mandat |
| `PH-NFR-010` | Index et permissions hérités correctement dans les sous-objets | Sous-objet créé dans un contexte A invisible depuis B |
| `PH-NFR-013` | Révocation effective | Refus d'une session ou action anciennement autorisée |
| `PH-NFR-020` | Données pilotes classifiées et autorisées | Refuser toute importation non approuvée |
| `PH-NFR-022` | Données de démo synthétiques | Jeu E0 sans personne ou projet réel |
| `PH-NFR-023` | Pas d'ingestion implicite des documents privés | Connecteur désactivé et accès non présumé |
| `PH-NFR-024` | Secrets non diffusés dans les contenus | Test d'exposition et procédure de rotation |
| `PH-NFR-030` | Menaces d'autorisation explicitement testées | IDOR / BOLA et contournement de scopes |
| `PH-NFR-033` | Secrets hors dépôt | Revue Git et contrôles de publication |
| `PH-NFR-089` | Tests automatisés de sécurité et autorisations | Tests négatifs obligatoires sur code modifié |

Il s'agit de **tests proposés, non exécutés**.

## 4. Exploitation et données réelles

| ID | Exigence candidate | Preuve attendue avant E1 |
|---|---|---|
| `PH-NFR-049` | Responsable d'exploitation identifié | Rôles, astreinte ou procédure documentés |
| `PH-NFR-050` | Politique de sauvegarde explicite | Périmètre, cadence, rétention et accès approuvés |
| `PH-NFR-051` | Restauration complète vérifiée | Journal d'un exercice de restauration |
| `PH-NFR-052` | Objectifs RPO/RTO convenus | Objectifs décidés selon le risque, non supposés |
| `PH-NFR-056` | Rollback documenté | Exercice ou procédure validée |
| `PH-NFR-057` | Continuité organisationnelle sans l'outil | Procédure de repli indépendante |
| `PH-NFR-078` | Traces exploitables | Diagnostic reproductible sans donnée privée en clair |
| `PH-NFR-079` | Absence de secrets dans les logs | Inspection de journaux représentatifs |
| `PH-NFR-082` | Circuit de signalement | Contact, escalade et réponse d'incident |
| `PH-NFR-097` | Export complet du périmètre autorisé | Export revu par tenant et rôle |
| `PH-NFR-098` | Export réutilisable | Schéma lisible et échantillon interprétable |
| `PH-NFR-099` | Sortie d'un pilote | Plan d'export, rétention et fermeture approuvé |

Une sauvegarde configurée ne prouve pas la restauration ; un journal créé ne prouve pas l'absence de secrets ; une API écrite ne prouve pas l'isolation.

## 5. Accessibilité et performance

| Domaine | IDs | Méthode à retenir |
|---|---|---|
| Clavier et focus | `PH-NFR-068..069` | Naviguer et valider un parcours sans souris |
| Contraste et informations | `PH-NFR-070..071` | Vérifier les états non uniquement visuels, erreurs explicites |
| Référentiel WCAG candidat | `PH-NFR-072` | Définir la version et le niveau visés, auditer puis retester |
| Vocabulaire et simplicité | `PH-NFR-073..075` | Tests avec profils non techniques et données manquantes |
| Responsive / zoom | `PH-NFR-076` | Vérification sur différentes tailles de vue |
| Budget de performance | `PH-NFR-059` | Seuil à fixer après mesure et scénario de charge |
| Pagination | `PH-NFR-061` | Grand nombre d'objets fictifs sans requête illimitée |
| Requêtes N+1 | `PH-NFR-062` | Profiling SQL du parcours critique |

Ne pas publier de chiffres de performance, disponibilité ou conformité non mesurés.

## 6. Agents IA et systèmes externes

Les automations sont des extensions, pas une précondition de valeur du premier MVP. `PH-NFR-106` prévoit les agents désactivés au MVP initial ; `PH-NFR-107..113` esquissent leurs contraintes ultérieures : droits minimaux, journalisation, provenance, validation humaine, révocation et protection des corpus.

Les références documentaires restent dans leur système maître, sans transfert automatique de droits. Une intégration partielle ne doit pas être présentée comme une synchronisation bidirectionnelle fiable.

## 7. Format d'une fiche de vérification

Une NFR ne peut être marquée `PASS` que si son scénario, sa mesure et son critère ont été fixés avant l'exécution, et si le résultat observé respecte ce critère. Lorsque la décision dépend d'un seuil, le responsable habilité doit en approuver la valeur et la justification avant le test. Un seuil absent ou une preuve incomplète signifie `NOT_ASSESSED`, pas une réussite implicite.

| NFR / question liée | Mesure à préciser avant le test | Condition de décision |
|---|---|---|
| `PH-NFR-001..010` / `PH-OPEN-002`, `PH-OPEN-006` — isolation et autorisations | Matrice des acteurs, actions, ressources et chemins testés : liste, détail, recherche, modification, job et export selon le cas | Toute divulgation ou action non autorisée est un `FAIL`. Un succès couvre uniquement les combinaisons effectivement testées |
| `PH-NFR-051..052` / `PH-OPEN-021` — restauration | Point de restauration, périmètre, temps de restauration observé et objectifs RPO/RTO approuvés avant l'exercice | Comparer les résultats aux objectifs fixés ; sans objectifs ou exercice réel, `NOT_ASSESSED` |
| `PH-NFR-059..062` / `PH-OPEN-021` — performance et capacité | Parcours, volume de données, charge, environnement, distribution des temps de réponse et erreurs | Fixer le budget et la méthode avant la mesure ; aucune valeur par défaut ni promesse de performance n'est supposée |
| `PH-NFR-068..076` / `PH-OPEN-027` — accessibilité et utilisabilité | Référentiel, version, niveau visé, parcours évalués et méthodes manuelles/automatisées appropriées | Évaluer les parcours définis et retester les barrières corrigées ; ne pas généraliser à une conformité non auditée |
| `PH-NFR-097..099` / `PH-OPEN-026` — export et sortie | Entités/champs attendus, périmètre autorisé, méthode de lecture indépendante et vérification des enregistrements | L'export doit être exploitable et complet pour le périmètre convenu ; toute donnée hors périmètre est un `FAIL` |

États de suivi recommandés : `NOT_ASSESSED` (aucun jugement étayé), `IN_PROGRESS` (évaluation commencée mais non conclue), `PASS` (critère préétabli atteint dans le scénario borné), `FAIL` (critère non atteint ou invariant violé) et `DEFERRED` (exclusion de phase décidée, avec déclencheur de réexamen). `DEFERRED` n'est jamais équivalent à `PASS`. Les exigences de sécurité obligatoires avant E1 ne peuvent pas être reportées pour rendre le jalon admissible.

La décision d'un seuil, le choix du référentiel d'accessibilité et le périmètre d'exploitation restent à attribuer aux responsables compétents ; aucune valeur chiffrée ou approbation n'est ajoutée par cette édition.

```text
NFR ID :
Statut :
Criticité et propriétaire / autorité :
Objectif de qualité et risque couvert :
Scénario et population/charge :
Environnement + version/commit testés :
Mesure, unité et seuil / règle de décision approuvés avant le test :
Autorité, date et justification de l'approbation :
Procédure de test :
Résultat observé :
Preuves et anomalies :
Décision de validation et portée :
```

Seules les preuves **effectivement produites** doivent renseigner une validation. Une proposition de test est un plan, pas un résultat.

## 8. Portes E0 et E1

- **E0** : jeux de données fictifs, parcours vérifiables, tests d'accès, erreurs gérées, aucun service réel de pilote.
- **E1** : autorisation institutionnelle, traitement des données, permissions, secrets, restauration, exploitation, procédure d'incident, accessibilité, export et maîtrise des changements.

La porte E1 reste **No-Go tant que les preuves et accords manquent**, quel que soit le nombre d'exigences documentées.

Voir [exigences fonctionnelles](00-functional-requirements.md), [permissions](02-business-rules-and-permissions.md) et [traçabilité](03-requirements-traceability.md).
