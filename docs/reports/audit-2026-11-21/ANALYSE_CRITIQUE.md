# Analyse critique - ProjectHub

> Document d'**opinion** : il évalue la conception du dépôt documentaire, pas seulement son état. Les faits et les neuf bugs sont dans [`CODEBASE_ANALYSIS.md`](./CODEBASE_ANALYSIS.md) ; ici, la question est : « cette organisation documentaire est-elle fiable, et pourquoi ? ».

---

## 1. Verdict global

| Dimension | Note /10 | Commentaire |
|---|---:|---|
| Fonctionnel (documentation) | 7 | Les 25 éditions sont présentes et structurées (`docs/README.md:13-25`), mais quatre énoncés d'état sont périmés (B2, B3, B7, B8). |
| Sécurité | 5 | La politique est stricte (`docs/PUBLICATION-POLICY.md:29-35`), mais une baseline `INTERNAL` est exposée (B1) et la protection de l'archive privée n'est pas versionnée (B9). |
| Architecture documentaire | 8 | Séparation privé/public, index et registres sont cohérents par conception (`docs/PUBLICATION-POLICY.md:22-27`, `docs/07-architecture/01-documentation-quality-ci-plan.md:177-186`). |
| Qualité de la rédaction | 6 | Le vocabulaire de statut est majoritairement discipliné (`docs/README.md:113-120`), mais « validées » et « préparé en PR » induisent en erreur (B3, B4). |
| Testabilité / DX | 3 | Le validateur, ses fixtures et son workflow sont décrits mais absents (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`, `:98-100`). |
| Production-readiness | 2 | Aucune application n'existe (`README.md:5`) et E1 reste `No-Go` tant que les huit gates sont `NOT_ASSESSED` (`docs/06-validation/00-pilot-validation-plan.md:111-124`). |

**En une phrase** : **la méthode de publication est meilleure que les garde-fous qui la protègent, et l'état déclaré dérive plus vite que les mécanismes chargés de le vérifier.**

---

## 2. Le problème n'est pas les bugs, c'est la dérive des garde-fous

B1, B2, B3, B7 et B9 ont la même racine : une règle est écrite dans un document, puis l'état réel évolue sans que la source de vérité évolue avec lui. La baseline doit rester hors du dépôt (`docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:46`) mais y est suivie (B1) ; `07-architecture/` n'est pas encore sur `main` selon le plan (`docs/07-architecture/01-documentation-quality-ci-plan.md:222`) mais y est (B2) ; PUBLIC-01 est encore « en proposition de PR » (`docs/00-context/03-decisions-register.md:80`) alors que le bilan atteste sa fusion (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:37-44`) (B3) ; le bilan recommande encore de créer l'index et la baseline qui existent déjà (B7) ; la règle d'ignore la plus sensible n'est pas commitée (B9).

Corriger chaque phrase isolément ne suffit pas. Ce qu'il manque, c'est une source de vérité exécutable pour trois états : la liste des fichiers publics autorisés, la classification effective de chaque fichier et l'état d'avancement des lots. Le plan de CI documentaire décrit précisément ces contrôles (`docs/07-architecture/01-documentation-quality-ci-plan.md:47-60`, `:121-142`) mais son implémentation est `NOT_IMPLEMENTED` (`:10`). Tant que ces contrôles restent une spécification, chaque ajout post-Discovery peut réintroduire la même dérive.

B5, B6 et B8 révèlent le même défaut dans le domaine métier : des catalogues très complets ne sont pas reliés à une procédure de décision unique. Une famille NFR est déclarée puis un test oublie son dernier ID (B5) ; huit items Gate sont comptés comme huit gates alors que l'un fusionne deux gates et un autre est une décision (B6) ; deux ordres de priorité coexistent pour les mêmes `PH-OPEN` (B8). Le modèle est riche, mais la correspondance entre catalogues n'est pas maintenue comme un contrat.

---

## 3. Critiques d'architecture

### 3.1 Le modèle à deux éditions est défendable, mais son exception n'est pas opérationnelle

La séparation entre corpus privé exhaustif et édition publique autonome est le choix central du projet (`docs/PUBLICATION-POLICY.md:22-27`). Il évite de diffuser des sources tierces et conserve la traçabilité par IDs stables (`:32`). Mais la baseline `PH-AEB-001` est conservée avec sa classification `INTERNAL` dans `docs/` (B1), et l'index demande une décision mainteneur explicite sans fournir de registre où la consigner (`docs/07-architecture/README.md:13-17`). C'est un choix défendable mal appliqué : remplacer l'étiquette par `public` serait pire, car cela masquerait l'exception au lieu de la traiter.

### 3.2 Les registres sont solides sur le papier, faibles sur la correspondance

Quatre registres canoniques sont nommés avec leurs plages (`docs/07-architecture/01-documentation-quality-ci-plan.md:177-185`) et la règle « première colonne seulement » empêche de compter des citations répétées (`:169-199`). Pourtant, la correspondance entre la famille `PH-NFR-001..010` et la fiche `001..009` est rompue (B5), et celle entre les items `PH-BLG-038..045` et les gates `G-*` est approximative (B6). Le système de traçabilité décrit en `docs/README.md:93-100` n'est donc pas encore une matrice vérifiable de bout en bout.

### 3.3 La CI documentaire est sur-conçue par rapport à son état réel

Le plan de 615 lignes définit neuf objectifs, un workflow, un validateur Python, des fixtures et cinq étapes de mise en service (`docs/07-architecture/01-documentation-quality-ci-plan.md:47-60`, `:228-280`, `:298-471`, `:490-500`). Rien n'est implémenté (`:10-11`, `:588`). Ce n'est pas un défaut de conception : les précautions sur `pull_request_target`, les permissions `contents: read` et l'absence de filtre `paths` sont justifiées (`:282-292`). Le défaut est d'ordre de priorisation : l'énergie est passée à spécifier le contrôle futur alors qu'un contrôle minimal pourrait déjà détecter B1 à B9.

### 3.4 La pile cible est décrite avant les décisions qui l'autorisent

La baseline propose monolithe modulaire Django/DRF, PostgreSQL et Next.js/React/TypeScript (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:91-93`, `:192`) alors que les 20 ADR sont `PROPOSED` et les responsables à désigner (`docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:60-85`). Le document le reconnaît lui-même en demandant une revue des alternatives (baseline `:93`) et en indiquant `implementation_status: "Not evidenced by this document"` (`:12`). Cette histoire est honnête, mais le risque est réel : un futur contributeur peut lire les exemples ORM et CI comme un contrat déjà adopté.

### 3.5 Le rapport de fin de lot décrit un état déjà dépassé

Le bilan du 2026-11-21 déclare le programme PUBLIC-01 à PUBLIC-04 terminé (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:147-149`), puis recommande dans la même page de corriger l'index et de préparer la baseline (`:136`, `:139`). Or l'index référence déjà le bilan et la baseline (`docs/README.md:11`, `:88`). Ce n'est pas seulement une phrase obsolète (B7) : cela montre qu'un document de clôture n'a pas été relu après les ajouts qui l'ont rendu faux.

---

## 4. Critique sécurité, au-delà de la liste des failles

1. La menée principale n'est pas un attaquant distant mais une publication accidentelle. Il n'y a pas d'endpoint (`README.md:5`), alors que l'archive privée contient des sources non redistribuables (`resources/LISEZ-MOI.txt:15-17`) et que sa protection n'est pas commitée (B9). Le scénario réaliste est un `git add -A` sur un clone neuf, pas une injection SQL.
2. La classification est un informateur, pas un contrôle. La baseline garde `INTERNAL` (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:6`) mais reste lisible (B1). Le plan CI prévoit justement de signaler l'anomalie sans changer l'étiquette automatiquement (`docs/07-architecture/01-documentation-quality-ci-plan.md:135-141`) ; ce garde-fou n'existe pas encore.
3. Les avertissements de confidentialité dans les issues sont rédigés en langage naturel (`.github/ISSUE_TEMPLATE/feature_request.yml:7`, `.github/ISSUE_TEMPLATE/bug_report.yml:7`). Ils ne peuvent empêcher un utilisateur de coller un verbatim ou un secret ; la politique renvoie explicitement à un canal privé pour les vulnérabilités (`.github/ISSUE_TEMPLATE/bug_report.yml:7`).
4. Le risque E1 n'est pas une faille de code mais une faille de gouvernance : accords institutionnels et huit gates restent requis (`docs/06-validation/00-pilot-validation-plan.md:111-124`, `docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:1648`). Aucune réussite de scanner ne peut les remplacer (`docs/07-architecture/01-documentation-quality-ci-plan.md:24`).

---

## 5. Critique de l'interface

Il n'existe pas de frontend applicatif (`README.md:5`). L'interface réelle est la rendered GitHub : README racine, index `docs/README.md`, pages Markdown et deux formulaires d'issue. Le README mise sur une illustration et des badges de pile cible (`README.md:7-9`, `:25-35`), ce qui donne une impression de maturité technique alors que le statut `Discovery` est quelques lignes plus haut (`README.md:5`) et que les versions restent à ADR (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:660-667`).

Le point de fragilité de cette interface est la visibilité des statuts : B3 et B4 ne sont pas des bugs de code, mais des phrases qui changent la lecture d'une page entière. Une navigation saine devrait afficher un unique bandeau d'état généré ou validé par le même contrôle que les frontmatters ; aujourd'hui, chaque README doit être corrigé manuellement (`docs/README.md:113-120`).

---

## 6. Critique du processus

Aucun pipeline n'est configuré (`docs/PUBLICATION-POLICY.md:158`) et le plan de CI documentaire n'est pas implémenté (`docs/07-architecture/01-documentation-quality-ci-plan.md:10-11`). Sur 48 fichiers suivis et 41 fichiers Markdown, la seule vérification mécanique citée est `git diff --check` (`docs/COLLABORATION-BEST-PRACTICES.md:320-329`). Le coût de cette absence est mesurable dans l'audit : neuf défauts B1..B9 ont été trouvés par lecture, alors que six d'entre eux (B1, B2, B3, B4, B7, B9) relèvent de contrôles de classification, de présence de fichiers ou de cohérence d'état automatisables.

Le facteur humain est également un goulot : les responsables d'ADR et les quatre rôles de gouvernance sont « à désigner » (`docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:48-56`), et la baseline porte `architecture_authority: null` et `product_authority: null` (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:1657-1658`). Tant que ces rôles ne sont pas nommés, une checklist « validation humaine obtenue » (`docs/PUBLICATION-POLICY.md:156`) ne peut pas être objectivement satisfaite pour une décision structurante.

---

## 7. Ce qui mérite d'être sauvegardé

- La politique de publication et son principe « confidentialité par défaut » (`docs/PUBLICATION-POLICY.md:22-35`).
- Le maintien du statut `draft` après fusion des quatre lots (`docs/README.md:66`, `:78`).
- La distinction explicite entre publication documentaire et validation métier (`docs/reports/2026-11-21-discovery-baseline-publication-bilan.md:19`, `:33`).
- Les IDs stables et la règle de comptage des registres (`docs/07-architecture/01-documentation-quality-ci-plan.md:169-199`).
- L'absence de secret avec valeur dans les fichiers analysés et l'usage de placeholders dans les exemples de configuration (`docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md:1240-1253`).
- Le contrôle manuel des liens relatifs : 243 liens locaux analysés, aucun ne pointant vers une cible manquante au moment de l'audit.

---

## 8. Réparer ou réécrire ?

| Option | Effort estimé | Verdict |
|---|---:|---|
| Réparer les neuf bugs et versionner les garde-fous | 1 à 3 jours de relecture, plus 2 à 3 jours pour un validateur minimal | **Recommandé.** Les défauts sont localisés et les correctifs sont compatibles avec les IDs existants (B1..B9). |
| Réécrire les 25 éditions depuis le corpus privé | plusieurs semaines | Déconseillé. Le corpus privé n'est pas publiable tel quel (`docs/PUBLICATION-POLICY.md:27`) et le risque de réexposition est supérieur au bénéfice. |
| Démarrer l'implémentation E0 avant les ADR | non chiffrable | Hors périmètre et prématuré : ADR `PROPOSED`, POC `NOT_RUN`, responsables à désigner (`docs/07-architecture/00-adr-tenancy-permissions-pre-e0-plan.md:11-12`, `:48-56`). |

**Quel que soit le chemin, trois non-négociables :**

1. Ne jamais relabelliser automatiquement la baseline `INTERNAL` ; sa classification et l'exception doivent être traitées par une décision humaine (B1, `docs/07-architecture/README.md:15-17`).
2. Conserver les IDs `PH-OPEN`, `PH-BLG`, `MVP-UJ`, `PH-REV` et corriger les correspondances plutôt que renuméroter (B5, B6, B8, `docs/07-architecture/01-documentation-quality-ci-plan.md:193-199`).
3. Exécuter les contrôles locaux et la relecture humaine avant de rendre un check obligatoire en CI (`docs/PUBLICATION-POLICY.md:145-158`, `docs/07-architecture/01-documentation-quality-ci-plan.md:490-500`).

---

## 9. Conclusion

Le dépôt a une discipline documentaire remarquablement explicite pour un projet à ce stade : deux éditions, statuts visibles, IDs stables et limites de preuve répétées. Mais cette discipline repose encore sur des documents qui ne se vérifient pas entre eux et sur une règle de confidentialité non versionnée. Le travail utile n'est donc pas d'ajouter un catalogue de plus, mais de transformer les garde-fous écrits en garde-fous exécutables, puis de corriger les neuf écarts déjà identifiés (B1..B9) sans toucher aux IDs.

> **Note finale : 6/10 en l'état - potentiel 8/10 atteignable en corrigeant B1..B9, en versionnant la règle `resources/` et en implémentant le contrôle documentaire minimal avant toute décision ADR ou E0.**

Le plan opérationnel est dans [`RECOMMANDATIONS.md`](./RECOMMANDATIONS.md).
