#!/bin/sh
# Run only on a disposable E0 PostgreSQL instance, via docker-entrypoint-initdb.d
# or a CI job with PostgreSQL connection settings configured by the caller.
set -eu
for name in E0_APP_DB_PASSWORD E0_MIGRATE_DB_PASSWORD; do
  if [ -z "$(printenv "$name")" ]; then
    echo "missing required environment value: $name"
    exit 1
  fi
done
psql -X -v ON_ERROR_STOP=1 \
  --username "${POSTGRES_USER:-postgres}" --dbname "${POSTGRES_DB:-projecthub}" \
  <<'SQL'
\getenv app_pw E0_APP_DB_PASSWORD
\getenv migrate_pw E0_MIGRATE_DB_PASSWORD
SELECT format('CREATE ROLE ph_migrate LOGIN PASSWORD %L NOSUPERUSER NOCREATEROLE NOBYPASSRLS CREATEDB', :'migrate_pw') \gexec
SELECT format('CREATE ROLE ph_app LOGIN PASSWORD %L NOSUPERUSER NOCREATEDB NOCREATEROLE NOBYPASSRLS', :'app_pw') \gexec
GRANT CONNECT ON DATABASE projecthub TO ph_migrate, ph_app;
GRANT USAGE, CREATE ON SCHEMA public TO ph_migrate;
GRANT USAGE ON SCHEMA public TO ph_app;
ALTER DEFAULT PRIVILEGES FOR ROLE ph_migrate IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ph_app;
ALTER DEFAULT PRIVILEGES FOR ROLE ph_migrate IN SCHEMA public
  GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO ph_app;
SQL
