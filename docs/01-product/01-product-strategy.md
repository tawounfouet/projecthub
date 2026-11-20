---
id: PH-PROD-STR-001
title: "ProjectHub - Stratégie produit publique"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-001, PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/01-product/00-product-vision.md"
  - "docs/01-product/02-product-scope.md"
  - "docs/00-context/04-open-questions.md"
---

# ProjectHub - Stratégie produit

> **Hypothèses stratégiques - draft à valider.** La stratégie décrit une trajectoire souhaitée, pas des clients acquis, une offre commerciale disponible, un calendrier contractuel ou une différenciation concurrentielle déjà prouvée.

## 1. Synthèse

**Orientation candidate :** construire ProjectHub comme une plateforme générique de pilotage des projets, articulant **suivi, coordination, mémoire et transmission**, puis la valider d'abord par des usages réels avant d'investir dans une distribution auto-hébergeable et un service Cloud.

La stratégie poursuit quatre ambitions complémentaires :

| Volet | But | Preuve recherchée | Risque |
|---|---|---|---|
| **Engineering** | Produit maintenable, sûr et reproductible | Tests, API, déploiement et diagnostics vérifiables | Complexité prématurée |
| **Internal** | Usage quotidien dans un contexte réel | Adoption par plusieurs utilisateurs | Produit dépendant de son auteur |
| **Community** | Distribution librement exploitable selon licence à choisir | Installation indépendante, docs et mises à jour | Dépôt ouvert mais inutilisable |
| **Cloud** | Service managé répondant à un besoin solvable | Activation, rétention et coût de service maîtrisé | Commercialisation avant fiabilité |

Une offre **Enterprise** n'est qu'une possibilité future : elle ne nécessite pas de nouvelle application métier complète.

## 2. Opportunité et problème à tester

Les organisations peuvent devoir coordonner plusieurs projets sans disposer d'un récit fiable de l'état des engagements, des responsables, des blocages ou des décisions. Elles utilisent souvent des outils adaptés à chaque spécialité, sans couche de pilotage commune.

**Hypothèse :** les équipes valorisent un suivi qui permet aussi de **transmettre le travail à la personne suivante**, au lieu de seulement afficher des cartes Kanban.

Cela reste une hypothèse : les solutions existantes peuvent déjà suffire à une partie des utilisateurs et certains organismes préfèreront ne pas ajouter d'outil.

## 3. Segments et acheteurs candidats

| Segment | Problème à explorer | Utilisateur typique | Acheteur potentiel |
|---|---|---|---|
| Agences numériques et équipes multi-projets | Visibilité sur les projets, maintenance et engagements | Responsable delivery, chef de projet, lead technique | Direction, CTO |
| Associations et équipes à contributeurs variés | Coordination, rotation des responsabilités, mémoire | Coordinateur, bénévole, responsable de programme | Bureau ou instance habilitée |
| Équipes produit et engineering | Traçabilité, dépendances, liens avec la réalisation | PM, engineering lead | Direction technique / produit |

**Proposition de focalisation :** éprouver d'abord le noyau dans au moins deux types d'organisation, puis tester plus spécifiquement une commercialisation B2B auprès des équipes multi-projets.

Les deux questions sont distinctes : **qui aide-t-on avec le produit ?** et **qui est prêt à financer un service managé ?** L'ICP commercial et les personas restent à valider (`PH-OPEN-007`).

## 4. Proposition de différenciation falsifiable

| Hypothèse | Signal favorable | Signal défavorable |
|---|---|---|
| Passation et continuité | Un nouveau responsable reprend sans assistance inhabituelle | Le problème est déjà résolu avec les outils actuels |
| Structure Organization / Workspace | Plusieurs collectifs coordonnent sans confondre accès et périmètres | La structure ajoute plus de friction que de valeur |
| Interopérabilité sobre | La plateforme référence la bonne source sans double saisie | Le suivi exige des copies constantes |
| Produit pour équipes mixtes | Parcours métier et techniques fonctionnent sur le même noyau | Des variantes lourdes rendent le produit non générique |
| Community + Cloud | L'auto-hébergement et le managé offrent des valeurs distinctes | Le coût d'exploitation dépasse la valeur perçue |

Ne pas présenter ces éléments comme des avantages concurrentiels uniques avant comparaison structurée avec GitHub Projects, outils de suivi, gestion documentaire et solutions auto-hébergeables.

## 5. Stratégie de produit

### Noyau transversal candidat

Un parcours utilisable de bout en bout :
1. créer une Organization et un Workspace ;
2. inviter ou attribuer des membres selon des droits explicites ;
3. qualifier un Project, son objectif et son responsable ;
4. suivre ses WorkItems, états, échéances et blocages ;
5. retrouver historique et documents de référence ;
6. effectuer un passage de relais vérifiable ;
7. exporter les données du périmètre autorisé.

Les détails sont décrits dans le [périmètre produit](02-product-scope.md). **Le MVP ne livre pas les 13 domaines cibles en entier**.

### Extensions à subordonner à des preuves

- intégrations GitHub enrichies et synchronisation ;
- catalogues de composants, d'environnements et de services ;
- tableaux de bord avancés, automatisations et moteur de règles ;
- agents IA soumis à permissions et vérification humaine ;
- fonctionnalités commerciales Cloud et Enterprise.

L'interface peut exposer des références à des outils externes avant d'intégrer leurs données ou d'automatiser des opérations.

## 6. Modèle Community / Cloud

| Mode proposé | Valeur | Condition préalable |
|---|---|---|
| **Community** | Déploiement autonome, fonctions fondamentales, API et export | Licence et droits clarifiés, installation reproductible, sécurité documentée |
| **Cloud** | Hébergement managé, sauvegardes, mises à jour, support | Isolation multi-tenant testée, exploitation, contrats et facturation si applicable |
| **Enterprise** | Support ou hébergement adapté à une demande particulière | Besoin démontré et capacité d'exécution |

**Préférence de travail :** un cœur fonctionnel commun, sans appauvrissement artificiel de la sécurité ou de la portabilité de Community. Le choix exact entre Open Source et Open Core, la licence et les droits de contribution restent ouverts.

Le dépôt public **n'est pas automatiquement sous licence open source**. Tant qu'un texte de licence n'est pas adopté, ne pas promettre de droits de réutilisation, redistribution ou modification qui ne sont pas accordés.

## 7. Packaging et monétisation

La monétisation est envisagée autour de la **simplicité d'exploitation**, du temps économisé, de la fiabilité, des sauvegardes, des mises à jour, de l'onboarding et du support.

**Aucun tarif n'est approuvé.** Tester d'abord :
- le problème effectivement payé aujourd'hui ;
- l'autorité d'achat et le budget ;
- les alternatives et leur coût total ;
- la pertinence d'une facturation par utilisateur, organisation ou usage ;
- la différence de valeur perçue entre Community et Cloud ;
- les coûts réels d'hébergement et d'assistance.

Les simulations de revenus ne sont ni des prévisions ni une grille officielle.

## 8. Programme d'apprentissage et pilotes

Les terrains pilotes potentiels doivent apporter des **preuves complémentaires**, pas imposer un produit spécifique à chacun :

| Type de terrain | Parcours à expérimenter | Preuve attendue |
|---|---|---|
| Équipe associative | Prioriser, coordonner, documenter et transmettre | Reprise d'une initiative par une autre personne |
| Agence / équipe engineering | Suivre projets, livrables, risques et références techniques | Réunion ou reprise facilitée sans surcroît de saisie |
| Réseau de membres | Coordonner initiatives et commissions | Collaboration compréhensible pour les contributeurs |
| Groupe d'évaluation accessibilité | Naviguer, comprendre et agir sur les parcours principaux | Tests d'usage et points de friction corrigés |

Il s'agit de **catégories d'expérimentation**, pas d'annonces d'accords de partenariat. Chaque participation nécessitera l'approbation compétente, un cadre de données, une modalité de sortie et une définition des responsabilités.

**Règle :** une passation opérationnelle ne doit pas dépendre de la livraison de ProjectHub.

## 9. Hypothèses et protocole de validation

| Expérience candidate | Question | Résultat observable |
|---|---|---|
| Visibilité | Un responsable peut-il situer les projets prioritaires ? | État, propriétaire et blocage retrouvés |
| Relais | Une autre personne peut-elle reprendre un dossier ? | Prochaines actions identifiées et réalisées |
| Interopérabilité | L'outil évite-t-il la double saisie ? | Moins de duplication sur le parcours testé |
| Accès | Des utilisateurs d'organisations distinctes sont-ils isolés ? | Tests négatifs réussis |
| Accessibilité | Les parcours sont-ils utilisables par différents profils ? | Problèmes identifiés, résolus puis retestés |
| Viabilité | Existe-t-il un décideur prêt à acheter le service ? | Intention d'achat qualifiée, idéalement contractualisée |

La mesure se fonde sur un **point de départ** et une observation réelle ; les seuils proposés ne doivent pas être présentés comme des résultats atteints.

## 10. Roadmap par portes de validation

| Porte | Résultat attendu | Ne prouve pas encore |
|---|---|---|
| **G0 - Discovery** | Sources, besoins, MVP candidat et réserves documentés | Adhésion utilisateur |
| **G1 - E0 démontrable** | Parcours de bout en bout sur données fictives | Autorisation d'utiliser des données réelles |
| **G2 - Pilotes E1 consentis** | Accords, contrôles, exploitation et mesures | Marché commercial prouvé |
| **G3 - Community** | Licence, installation, documentation et contribution | SaaS opérationnel |
| **G4 - Cloud bêta** | Provisioning, isolation, restauration, support, cadre contractuel | Rentabilité ou échelle |
| **G5 - Commercial** | Premiers comptes payants, valeur et coûts constatés | Croissance garantie |

Ce sont des **portes de décision**, pas une feuille de route calendaire contractuelle.

## 11. Gouvernance, risques et limites

Risques stratégiques principaux :
- développer une solution générique trop large sans parcours moteur ;
- surestimer l'intérêt commercial à partir d'usages internes ;
- confondre organisation pilote et client acheteur ;
- créer des dépendances à des composants internes non audités ;
- publier des sources de tiers sans droit de diffusion ;
- annoncer un produit, une disponibilité ou une certification avant preuve ;
- multiplier les variantes Community/Cloud et perdre un noyau commun.

Contre-mesures proposées : entretiens, décisions enregistrées, tests de bout en bout, droits stricts, publication sélective, seuils de sortie et confrontation régulière au coût d'exploitation.

## 12. Arbitrages à prendre

- `PH-OPEN-001` : MVP final.
- `PH-OPEN-007` : segment et valeur prioritaire.
- `PH-OPEN-002`, `006`, `020` : permissions et modèle multi-tenant.
- `PH-OPEN-005`, `014` : licence et propriété intellectuelle.
- `PH-OPEN-009` : cadre et accords pilotes.
- `PH-OPEN-008` : modèle de prix.
- `PH-OPEN-015` : autorité de publication.
- `PH-OPEN-030` : autorité d'approbation de la baseline.

**Lire aussi :** [vision](00-product-vision.md), [scope](02-product-scope.md), [questions ouvertes](../00-context/04-open-questions.md), [politique de publication](../PUBLICATION-POLICY.md).
