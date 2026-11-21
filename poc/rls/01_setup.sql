-- POC ADR-0019. Everything here is synthetic and isolated in schema ph_rls_poc.
-- Must be executed as PostgreSQL maintenance user, never as a web request.
DROP SCHEMA IF EXISTS ph_rls_poc CASCADE;
DROP ROLE IF EXISTS ph_poc_app;
DROP ROLE IF EXISTS ph_poc_owner;

CREATE ROLE ph_poc_owner NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOBYPASSRLS;
CREATE ROLE ph_poc_app NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOBYPASSRLS;
CREATE SCHEMA ph_rls_poc AUTHORIZATION ph_poc_owner;
GRANT USAGE ON SCHEMA ph_rls_poc TO ph_poc_app;

CREATE TABLE ph_rls_poc.r0_rows (
    id integer PRIMARY KEY,
    organization_id uuid NOT NULL,
    label text NOT NULL
);
CREATE TABLE ph_rls_poc.r1_rows (LIKE ph_rls_poc.r0_rows INCLUDING ALL);

ALTER TABLE ph_rls_poc.r0_rows OWNER TO ph_poc_owner;
ALTER TABLE ph_rls_poc.r1_rows OWNER TO ph_poc_owner;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA ph_rls_poc TO ph_poc_app;

-- Seed is performed as a DBA for setup. These are not real organizational data.
INSERT INTO ph_rls_poc.r0_rows VALUES
 (1, 'aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa', 'synthetic A'),
 (2, 'bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb', 'synthetic B');
INSERT INTO ph_rls_poc.r1_rows SELECT * FROM ph_rls_poc.r0_rows;

ALTER TABLE ph_rls_poc.r1_rows ENABLE ROW LEVEL SECURITY;
ALTER TABLE ph_rls_poc.r1_rows FORCE ROW LEVEL SECURITY;
CREATE POLICY tenant_scope ON ph_rls_poc.r1_rows
  TO ph_poc_app, ph_poc_owner
  USING (organization_id = NULLIF(current_setting('app.organization_id', true), '')::uuid)
  WITH CHECK (organization_id = NULLIF(current_setting('app.organization_id', true), '')::uuid);
