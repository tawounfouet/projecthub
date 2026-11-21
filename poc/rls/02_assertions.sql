-- Exit nonzero when ANY assertion fails. Uses SQL assertions rather than counting output manually.
-- ON_ERROR_STOP=1 is set in the invoker. Never use the superuser for scoped queries.
DO $$
BEGIN
 IF (SELECT rolbypassrls OR rolsuper FROM pg_roles WHERE rolname = 'ph_poc_app') THEN
   RAISE EXCEPTION 'POC app must not have superuser or BYPASSRLS';
 END IF;
 IF NOT (SELECT relforcerowsecurity AND relrowsecurity
         FROM pg_class WHERE oid = 'ph_rls_poc.r1_rows'::regclass) THEN
   RAISE EXCEPTION 'RLS or FORCE RLS not enabled';
 END IF;
 IF (SELECT pg_get_userbyid(relowner) FROM pg_class WHERE oid = 'ph_rls_poc.r1_rows'::regclass)
     = 'ph_poc_app' THEN
   RAISE EXCEPTION 'Web role must not own protected tables';
 END IF;
END $$;

SET ROLE ph_poc_app;
-- Missing tenant context must fail closed, even when SELECT has no WHERE.
DO $$
BEGIN
 IF (SELECT COUNT(*) FROM ph_rls_poc.r1_rows) <> 0 THEN
   RAISE EXCEPTION 'RLS leaked rows with no context';
 END IF;
END $$;

BEGIN;
SELECT set_config('app.organization_id', 'aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa', true);
DO $$
DECLARE denied boolean := false; changed integer;
BEGIN
 -- R-0 has no policy and demonstrates accidental unfiltered SQL exposure.
 IF (SELECT COUNT(*) FROM ph_rls_poc.r0_rows) <> 2 THEN
   RAISE EXCEPTION 'R-0 control should expose both synthetic tenants';
 END IF;
 -- R-1 shields the same unfiltered SQL under a correct transaction context.
 IF (SELECT COUNT(*) FROM ph_rls_poc.r1_rows) <> 1 THEN
   RAISE EXCEPTION 'R-1 should expose only A';
 END IF;
 IF EXISTS(SELECT 1 FROM ph_rls_poc.r1_rows WHERE organization_id='bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb') THEN
   RAISE EXCEPTION 'R-1 cross-tenant read leaked B';
 END IF;

 BEGIN
   INSERT INTO ph_rls_poc.r1_rows VALUES
     (3, 'bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb', 'forged B');
 EXCEPTION WHEN insufficient_privilege THEN denied := true;
 END;
 IF NOT denied THEN RAISE EXCEPTION 'RLS must refuse cross-tenant INSERT'; END IF;

 UPDATE ph_rls_poc.r1_rows SET label='forged B'
  WHERE organization_id='bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb';
 GET DIAGNOSTICS changed = ROW_COUNT;
 IF changed <> 0 THEN RAISE EXCEPTION 'RLS must refuse cross-tenant UPDATE'; END IF;
END $$;
COMMIT;

-- This is the SAME PostgreSQL session after COMMIT. The local setting must disappear.
DO $$
BEGIN
 IF (SELECT COUNT(*) FROM ph_rls_poc.r1_rows) <> 0 THEN
   RAISE EXCEPTION 'SET LOCAL tenant leaked across transactions';
 END IF;
END $$;

BEGIN;
SELECT set_config('app.organization_id', 'bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb', true);
DO $$
BEGIN
 IF (SELECT COUNT(*) FROM ph_rls_poc.r1_rows) <> 1 THEN
   RAISE EXCEPTION 'Second transaction should see only B';
 END IF;
END $$;
COMMIT;

RESET ROLE;
-- FORCE ROW LEVEL SECURITY must also constrain the owner (normally exempt).
SET ROLE ph_poc_owner;
BEGIN;
SELECT set_config('app.organization_id', 'aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa', true);
DO $$
BEGIN
 IF (SELECT COUNT(*) FROM ph_rls_poc.r1_rows) <> 1 THEN
   RAISE EXCEPTION 'FORCE RLS did not constrain table owner';
 END IF;
END $$;
COMMIT;
RESET ROLE;

SELECT 'RLS_POC_ASSERTIONS_PASSED' AS result;
