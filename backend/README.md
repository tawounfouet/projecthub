# Backend E0 (Django / DRF)

Backend **strictement expérimental** de `SLICE-00`. Il requiert PostgreSQL, `DJANGO_SECRET_KEY`, `DATABASE_URL` et `E0_SYNTHETIC_ONLY=1`. Sans ce dernier drapeau, les opérations de démonstration sont refusées.

- `Organization` est la frontière des données. `Workspace` est un sous-scope ; `Membership` et `WorkspaceGrant` sont contrôlés à chaque requête, y compris après révocation.
- Les objets de Project/WorkItem servent de **sentinelles de tests et d'aperçu read-only** ; cela ne constitue pas la livraison de `SLICE-01`.
- Sessions Django avec cookies HttpOnly, CSRF same-origin et réécriture `/api` depuis Next.js. Aucun token API de service exposé au navigateur.
- La sécurité métier n'est pas déléguée à une politique PostgreSQL RLS dans ce lot : l'option `R-2` est recommandée mais non approuvée.
- Les tables relationnelles ont des contraintes composites pour refuser un Project/WorkItem rattaché à un parent d'un autre tenant.
- L'import des fixtures est explicite : `python manage.py seed_e0` ne s'exécute que sous `E0_SYNTHETIC_ONLY=1`.

La compilation et les tests CI doivent être consultés avant de qualifier le lot de reproductible. **Interdiction de données réelles E1.**
