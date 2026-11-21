# Frontend E0 (Next.js 16 / React 19 / TypeScript)

Interface **expérimentale**, sans données réelles. Elle communique en same-origin par la réécriture Next.js de ` /api/* ` vers Django, avec sessions HttpOnly et CSRF.

Depuis la racine du dépôt, préférer `docker compose up --build` avec `.env` local. Sinon :

```bash
cd frontend
npm ci
BACKEND_INTERNAL_URL=http://127.0.0.1:8000 npm run build
npm run start
```

Le backend Django doit déjà être accessible et ses fixtures fictives créées. La destination des rewrites est fixée **au build Next.js**. Dans l'image Compose, elle est définie à `http://backend:8000`.

Comptes synthétiques : `demo_alice`, `demo_both`, `demo_admin_a`, `demo_viewer`. Le mot de passe vient de `E0_DEMO_PASSWORD` ou d'une valeur fictive reconstruite à l'exécution ; il n'est valable que sur la base locale. N'utiliser ce code ni avec des comptes réels ni derrière une URL publique.

Le démonstrateur permet de changer de contexte, voir les sentinelles Project/WorkItem, déclencher des accès étrangers refusés, vérifier l'absence de mandat et révoquer un compte. Les fonctions de projets affichées ici ne sont qu'un aperçu technique, pas une livraison de `SLICE-01`.

Versions de dépendances directes fixées dans `package.json`. Le fichier `package-lock.json` issu de la résolution CI est maintenant suivi. Utiliser `npm ci` pour reproduire exactement les versions npm vérifiées.
