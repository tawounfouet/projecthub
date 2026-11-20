---
id: PH-PROD-VIS-001
title: "ProjectHub - Vision produit publique"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-20"
updated_at: "2026-11-20"
sources: [PH-CNV-001, PH-CNV-004, PH-OPS-001, PH-OPS-002]
related_documents:
  - "docs/00-context/02-canonical-context.md"
  - "docs/01-product/01-product-strategy.md"
  - "docs/01-product/02-product-scope.md"
---

# ProjectHub - Vision produit

> **Vision candidate - pas encore validée par un marché ou des pilotes.** ProjectHub est en conception. Les fonctionnalités décrites ci-dessous représentent des intentions ou capacités proposées, et non un logiciel déjà utilisable.

## 1. Notre intention

**ProjectHub aide les organisations à transformer leurs objectifs en travail collectif visible, suivi et transmissible, sans perdre le lien avec les outils et la mémoire opérationnelle existants.**

Cette formulation est une vision **à éprouver**. La mission opérationnelle candidate consiste à permettre aux équipes de :
- comprendre quelles initiatives sont prioritaires ;
- identifier clairement les responsables et contributeurs ;
- suivre les actions, échéances, blocages et décisions ;
- retrouver le contexte des choix et documents de référence ;
- assurer un relais de responsabilités vérifiable ;
- exporter les données qu'elles sont autorisées à conserver.

L'enjeu n'est pas seulement de mieux assigner des tâches : il est de rendre le travail collectif **compréhensible par la personne suivante**.

## 2. Problèmes utilisateurs explorés

| Problème candidat | Conséquence possible | Ce que nous voulons tester |
|---|---|---|
| Suivi dispersé entre plusieurs outils | Visibilité incomplète des engagements | Vue de pilotage utile sans double saisie |
| Responsabilités implicites ou changeantes | Délais, blocages et dépendance à une personne | Propriétaire et relais explicités |
| Informations difficiles à retrouver | Revues et reprises coûteuses | Historique et références fiables |
| Décisions séparées des actions | Priorités difficiles à expliquer | Liens traçables entre décisions et travail |
| Multiplicité des projets et équipes | Arbitrages peu visibles | Navigation par Organization et Workspace |
| Départ ou rotation des responsables | Perte de contexte | Passation réellement vérifiée |

Ces problèmes ont été formulés à partir de sources privées étudiées et de discussions de conception. Leur importance relative, leur fréquence et la disposition à payer **restent à mesurer**.

## 3. Utilisateurs et bénéficiaires candidats

- Responsable d'organisation ou de programme : visibilité et arbitrages.
- Responsable de projet : suivi, dépendances, blocages et livrables.
- Contributeur : actions attribuées et contexte nécessaire à leur réalisation.
- Administrateur : règles d'accès, données et gouvernance technique.
- Responsable technique : suivi transversal sans remplacer les outils engineering.
- Successeur / nouveau responsable : reprise des dossiers et décisions.

Un persona n'est pas un rôle RBAC, et un responsable métier n'est pas nécessairement administrateur.

## 4. Proposition de valeur

```text
Objectifs et engagements
         ↓
Projects et livrables
         ↓
WorkItems, responsables et échéances
         ↓
Historique, références et décisions
         ↓
Continuité et transmission
```

ProjectHub doit pouvoir relier les objets de pilotage entre eux sans prétendre devenir la source de vérité de tous les outils. Les fichiers de conception, dépôts Git, documents partagés et automatisations demeurent dans leurs systèmes d'origine lorsque cela est pertinent.

## 5. Principes de conception

1. **Générique plutôt que codé pour un seul pilote.** Les besoins spécifiques servent à valider le modèle, pas à le rendre dépendant d'une organisation.
2. **Frontières de données claires.** Organization et Workspace sont des concepts distincts ; toute utilisation réelle requiert une isolation démontrée.
3. **Interopérabilité.** Référencer ou intégrer les outils spécialisés, au lieu de les répliquer automatiquement.
4. **Continuité.** Préserver la mémoire des changements de responsables et tester la capacité de reprise.
5. **Traçabilité.** Relier les besoins, décisions, actions et preuves d'avancement.
6. **Portabilité.** Rendre possible l'export des données autorisées et une sortie maîtrisée.
7. **Accessibilité.** Concevoir des parcours utilisables au-delà des seuls profils techniques.
8. **Excellence d'ingénierie.** Tests, maintenance, sécurité, documentation et exploitation proportionnées.

## 6. Architecture cible au service de la vision

La cartographie contient 13 domaines : `core`, `identity`, `organizations`, `portfolios`, `projects`, `workitems`, `planning`, `views`, `collaboration`, `governance`, `integrations`, `automation`, `reporting`.

Cette cartographie est un horizon de conception. Elle n'impose ni 13 microservices ni la livraison immédiate de 13 applications fonctionnelles complètes.

Les concepts structurants envisagés sont `Organization -> Workspace -> Project -> WorkItem`, avec Teams, décisions, risques, plans et intégrations transversaux.

## 7. À quoi pourrait ressembler le premier résultat utile ?

Un coordinateur crée une initiative dans son Workspace, définit les responsables, rattache des actions et des documents de référence, suit les blocages, prépare une revue, transmet le contexte à un successeur et peut exporter son périmètre autorisé.

Nous cherchons à tester **un parcours de bout en bout**, et non à afficher le plus grand nombre de fonctionnalités.

Avant une démonstration avec des données réelles, des contrôles de permissions, sauvegarde, confidentialité, exploitation et sortie devront être vérifiés.

## 8. Ce que ProjectHub n'a pas vocation à remplacer

- Un gestionnaire de dépôt Git, de code review et de CI/CD.
- Une GED, une suite bureautique ou un système complet de messagerie.
- Un ERP, un CRM, un logiciel de paie ou un système comptable.
- Un moteur d'orchestration d'entreprise généraliste.
- Un agent IA autonome disposant implicitement des droits de tous.
- La gouvernance humaine ou les validations officielles d'une organisation.

Ces frontières sont des **non-objectifs** du produit initial ; elles peuvent évoluer uniquement après recherche et décision explicite.

## 9. Horizon communautaire et commercial

La vision envisage une édition Community auto-hébergeable, associée à une offre Cloud managée et, éventuellement plus tard, des services Enterprise.

La licence, le calendrier, le modèle de revenus et le périmètre précis des offres ne sont pas approuvés. L'intention commerciale ne permet pas d'annoncer un service déjà disponible.

## 10. Mesurer plutôt qu'affirmer

La vision sera soutenue si des utilisateurs indépendants du concepteur peuvent :
- retrouver l'état d'un projet et son responsable sans intervention extérieure ;
- conduire une revue de plusieurs projets à partir d'informations à jour ;
- accomplir une action sans recopier inutilement des données ;
- recevoir une passation et expliquer les prochains gestes à réaliser ;
- exporter leur périmètre sans fuite vers une autre organisation.

Ces observations nécessitent **des tests, des entretiens et des preuves**, pas seulement des maquettes ou un corpus documentaire.

**Lectures associées :** [stratégie](01-product-strategy.md), [périmètre](02-product-scope.md), [contexte](../00-context/02-canonical-context.md) et [questions ouvertes](../00-context/04-open-questions.md).
