"""E0 PostgreSQL integration tests: API scope, revocation, CSRF and DB integrity."""
from __future__ import annotations

import json
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.db import IntegrityError, connection, transaction
from django.test import TestCase, override_settings
from rest_framework.test import APIClient

from foundation.management.commands.seed_e0 import (
    DEMO_PASSWORD, ORG_A, ORG_B, WS_A, WS_B, PROJECT_A, PROJECT_B, ITEM_B,
)
from foundation.models import AuditEvent, Invitation, Membership, Organization, Project, Workspace, WorkItem

User = get_user_model()


class Slice00Tests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_e0", verbosity=0)

    def login_as(self, username):
        api = APIClient()
        api.force_login(User.objects.get(username=username))
        return api

    def select(self, api, org=ORG_A, workspace=WS_A):
        return api.post("/api/context/", {"organization_id": org, "workspace_id": workspace}, format="json")

    def test_readiness_uses_database_and_supports_rewrite_alias(self):
        self.assertEqual(self.client.get("/api/health/").status_code, 200)
        self.assertEqual(self.client.get("/api/ready/").json()["status"], "ready")
        self.assertEqual(self.client.get("/api/ready").status_code, 200)

    @override_settings(E0_SYNTHETIC_ONLY=False)
    def test_readiness_refuses_outside_synthetic_mode(self):
        self.assertEqual(self.client.get("/api/ready/").status_code, 503)

    def test_organizations_filter_by_active_membership(self):
        api = self.login_as("demo_alice")
        data = api.get("/api/organizations/").json()["organizations"]
        self.assertEqual([r["id"] for r in data], [ORG_A])
        self.assertEqual(self.select(api, ORG_B, WS_B).status_code, 403)

    def test_both_memberships_require_explicit_context_switch(self):
        api = self.login_as("demo_both")
        self.assertEqual(self.select(api).status_code, 200)
        self.assertEqual([p["title"] for p in api.get("/api/projects/").json()["projects"]], ["Projet fictif A"])
        self.assertEqual(api.get(f"/api/projects/{PROJECT_B}/").status_code, 404)
        self.assertEqual(self.select(api, ORG_B, WS_B).status_code, 200)
        self.assertEqual([p["title"] for p in api.get("/api/projects/").json()["projects"]], ["Projet fictif B"])
        self.assertEqual(api.get(f"/api/projects/{PROJECT_A}/").status_code, 404)

    def test_cannot_enumerate_foreign_workspace(self):
        api = self.login_as("demo_alice")
        self.assertEqual(api.get(f"/api/workspaces/?organization_id={ORG_B}").status_code, 403)

    def test_viewer_can_read_but_not_write(self):
        api = self.login_as("demo_viewer")
        self.assertEqual(self.select(api).status_code, 200)
        self.assertEqual(api.get("/api/projects/").status_code, 200)
        self.assertEqual(api.post("/api/projects/", {"title": "forbidden"}, format="json").status_code, 403)
        self.assertEqual(api.patch(f"/api/workitems/{ITEM_B}/", {"status": "done"}, format="json").status_code, 403)

    def test_foreign_workitem_parent_and_forged_org_denied(self):
        api = self.login_as("demo_alice")
        self.select(api)
        self.assertEqual(
            api.post("/api/workitems/", {"project_id": PROJECT_B, "title": "forged"}, format="json").status_code,
            404,
        )
        self.assertEqual(api.get(f"/api/workitems/{ITEM_B}/").status_code, 404)
        self.assertEqual(
            api.post("/api/projects/", {"workspace_id": WS_B, "title": "forged"}, format="json").status_code,
            403,
        )
        self.assertEqual(
            api.post("/api/projects/", {"organization_id": ORG_B, "title": "forged"}, format="json").status_code,
            403,
        )

    def test_same_tenant_create_and_change_workitem(self):
        api = self.login_as("demo_alice")
        self.select(api)
        project = api.post("/api/projects/", {"title": "Exemple A"}, format="json")
        self.assertEqual(project.status_code, 201)
        item = api.post("/api/workitems/", {"project_id": project.json()["id"], "title": "Action A"}, format="json")
        self.assertEqual(item.status_code, 201)
        self.assertEqual(
            api.patch(f"/api/workitems/{item.json()['id']}/", {"status": "done"}, format="json").status_code,
            200,
        )
        self.assertEqual(
            api.patch(f"/api/workitems/{item.json()['id']}/", {"organization_id": ORG_B, "status": "done"}, format="json").status_code,
            403,
        )

    def test_composite_fk_rejects_cross_tenant_project_and_workitem(self):
        a = Organization.objects.get(id=ORG_A)
        b = Organization.objects.get(id=ORG_B)
        wb = Workspace.objects.get(id=WS_B)
        pb = Project.objects.get(id=PROJECT_B)
        # Detect low-level bypass of API via PostgreSQL composite keys.
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Project.objects.create(organization=a, workspace=wb, title="invalid link")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                WorkItem.objects.create(organization=a, project=pb, title="invalid link")
        self.assertEqual(WorkItem.objects.filter(organization=b).count(), 1)

    def test_invitation_stays_pending_without_grant(self):
        admin = self.login_as("demo_admin_a")
        self.select(admin)
        response = admin.post("/api/invitations/", {"username": "demo_guest"}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["status"], "pending")
        self.assertFalse(Membership.objects.filter(organization_id=ORG_A, user__username="demo_guest").exists())
        guest = self.login_as("demo_guest")
        self.assertEqual(self.select(guest).status_code, 403)

    def test_admin_cannot_approve_without_business_mandate(self):
        admin = self.login_as("demo_admin_a")
        self.select(admin)
        self.assertEqual(admin.post("/api/approvals/", {"decision_id": "synthetic"}, format="json").status_code, 403)

    def test_client_reference_is_not_a_membership(self):
        a = self.login_as("demo_alice")
        self.select(a)
        self.assertEqual(len(a.get("/api/client-references/").json()["clients"]), 1)
        self.assertEqual(self.select(a, ORG_B, WS_B).status_code, 403)

    def test_revocation_invalidates_existing_session_and_preserves_audit(self):
        actor = self.login_as("demo_revoke")
        admin = self.login_as("demo_admin_a")
        self.assertEqual(self.select(actor).status_code, 200)
        self.assertEqual(actor.get("/api/projects/").status_code, 200)
        self.select(admin)
        membership = Membership.objects.get(organization_id=ORG_A, user__username="demo_revoke")
        self.assertEqual(admin.post(f"/api/memberships/{membership.id}/revoke/").status_code, 200)
        self.assertEqual(actor.get("/api/projects/").status_code, 403)
        self.assertIsNone(actor.get("/api/context/").json()["selected"])
        self.assertTrue(AuditEvent.objects.filter(organization_id=ORG_A, action="MEMBERSHIP_REVOKED").exists())

    def test_last_owner_protected(self):
        admin = self.login_as("demo_admin_a")
        self.select(admin)
        m = Membership.objects.get(organization_id=ORG_A, user__username="demo_admin_a")
        self.assertEqual(admin.post(f"/api/memberships/{m.id}/revoke/").status_code, 403)
        m.refresh_from_db()
        self.assertTrue(m.active)

    def test_cross_tenant_export_contains_only_active_context(self):
        api = self.login_as("demo_both")
        self.select(api)
        data = api.get("/api/export/").json()
        self.assertEqual(data["organization_id"], ORG_A)
        self.assertNotIn("Projet fictif B", json.dumps(data))
        self.assertNotIn("Action fictive B", json.dumps(data))

    def test_unauthed_api_denies(self):
        self.assertIn(APIClient().get("/api/organizations/").status_code, (401, 403))

    def test_csrf_required_on_session_mutation(self):
        api = APIClient(enforce_csrf_checks=True)
        api.force_login(User.objects.get(username="demo_alice"))
        self.assertEqual(
            api.post("/api/context/", {"organization_id": ORG_A, "workspace_id": WS_A}, format="json").status_code,
            403,
        )

    def test_csrf_issued_and_login_successfully(self):
        api = APIClient(enforce_csrf_checks=True)
        self.assertEqual(api.get("/api/auth/csrf/").status_code, 200)
        token = api.cookies["csrftoken"].value
        res = api.post(
            "/api/auth/login/",
            data=json.dumps({"username": "demo_alice", "password": DEMO_PASSWORD}),
            content_type="application/json",
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(api.get("/api/me/").status_code, 200)

    def test_login_rejects_wrong_password(self):
        api = APIClient(enforce_csrf_checks=True)
        api.get("/api/auth/csrf/")
        r = api.post(
            "/api/auth/login/",
            data=json.dumps({"username": "demo_alice", "password": "bad"}),
            content_type="application/json",
            HTTP_X_CSRFTOKEN=api.cookies["csrftoken"].value,
        )
        self.assertEqual(r.status_code, 403)

    def test_revoked_scope_rejects_fresh_org_list(self):
        user = User.objects.get(username="demo_revoke")
        membership = Membership.objects.get(user=user, organization_id=ORG_A)
        membership.active = False
        membership.save(update_fields=["active"])
        api = self.login_as("demo_revoke")
        self.assertEqual(api.get("/api/organizations/").json()["organizations"], [])

    @override_settings(E0_SYNTHETIC_ONLY=False)
    def test_e0_fixture_disabled_by_default(self):
        api = self.login_as("demo_alice")
        self.assertEqual(api.get("/api/organizations/").status_code, 403)
        self.assertEqual(api.get("/api/auth/csrf/").status_code, 503)

    def test_audit_is_scoped_and_sanitized(self):
        admin = self.login_as("demo_admin_a")
        alice = self.login_as("demo_alice")
        self.select(admin)
        self.select(alice)
        self.assertEqual(alice.get("/api/audit/").status_code, 403)
        events = admin.get("/api/audit/").json()["events"]
        self.assertTrue(events)
        self.assertTrue(all(e["action"] == "CONTEXT_SELECTED" for e in events))
        self.assertNotIn(DEMO_PASSWORD, json.dumps(events))
