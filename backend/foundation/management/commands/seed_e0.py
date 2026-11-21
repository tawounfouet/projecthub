"""Idempotent fictitious organizations, users, membership, grants and sentinels."""
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from foundation.models import (
    ClientReference, Membership, Organization, Project, Workspace, WorkspaceGrant, WorkItem,
)

User = get_user_model()
DEMO_PASSWORD = os.environ.get("E0_DEMO_PASSWORD") or "-".join(("e0", "demo", "only"))
ORG_A = "aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa"
ORG_B = "bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb"
WS_A = "aaaaaaaa-aaaa-4aaa-bbbb-aaaaaaaaaaaa"
WS_B = "bbbbbbbb-bbbb-4bbb-aaaa-bbbbbbbbbbbb"
PROJECT_A = "aaaaaaaa-aaaa-4aaa-cccc-aaaaaaaaaaaa"
PROJECT_B = "bbbbbbbb-bbbb-4bbb-cccc-bbbbbbbbbbbb"
ITEM_A = "aaaaaaaa-aaaa-4aaa-dddd-aaaaaaaaaaaa"
ITEM_B = "bbbbbbbb-bbbb-4bbb-dddd-bbbbbbbbbbbb"


class Command(BaseCommand):
    help = "Create synthetic E0 dataset only, with deterministic IDs"

    def handle(self, *args, **options):
        if not settings.E0_SYNTHETIC_ONLY:
            raise CommandError("Refusing fixture seed without E0_SYNTHETIC_ONLY=1")
        with transaction.atomic():
            a, _ = Organization.objects.get_or_create(id=ORG_A, defaults={"slug": "demo-org-a", "name": "Demo-Org-A"})
            b, _ = Organization.objects.get_or_create(id=ORG_B, defaults={"slug": "demo-org-b", "name": "Demo-Org-B"})
            wa, _ = Workspace.objects.get_or_create(id=WS_A, defaults={"organization": a, "slug": "demo-workspace-a", "name": "Workspace A"})
            wb, _ = Workspace.objects.get_or_create(id=WS_B, defaults={"organization": b, "slug": "demo-workspace-b", "name": "Workspace B"})

            users = {}
            for username in ("demo_admin_a", "demo_admin_b", "demo_alice", "demo_bob", "demo_both", "demo_viewer", "demo_revoke", "demo_guest"):
                user, created = User.objects.get_or_create(
                    username=username, defaults={"email": f"{username}@example.invalid", "is_staff": False}
                )
                if created:
                    user.set_password(DEMO_PASSWORD)
                    user.save(update_fields=["password"])
                users[username] = user

            grants = (
                (a, wa, "demo_admin_a", Membership.OWNER, True),
                (b, wb, "demo_admin_b", Membership.OWNER, True),
                (a, wa, "demo_alice", Membership.MEMBER, True),
                (b, wb, "demo_bob", Membership.MEMBER, True),
                (a, wa, "demo_both", Membership.MEMBER, True),
                (b, wb, "demo_both", Membership.MEMBER, True),
                (a, wa, "demo_viewer", Membership.MEMBER, False),
                (a, wa, "demo_revoke", Membership.MEMBER, True),
            )
            for org, ws, username, role, can_write in grants:
                Membership.objects.get_or_create(organization=org, user=users[username], defaults={"role": role, "active": True})
                if role != Membership.OWNER:
                    WorkspaceGrant.objects.get_or_create(
                        workspace=ws, user=users[username],
                        defaults={"active": True, "can_write": can_write},
                    )

            pa, _ = Project.objects.get_or_create(
                id=PROJECT_A, defaults={"organization": a, "workspace": wa, "title": "Projet fictif A"}
            )
            pb, _ = Project.objects.get_or_create(
                id=PROJECT_B, defaults={"organization": b, "workspace": wb, "title": "Projet fictif B"}
            )
            WorkItem.objects.get_or_create(
                id=ITEM_A, defaults={"organization": a, "project": pa, "title": "Action fictive A"}
            )
            WorkItem.objects.get_or_create(
                id=ITEM_B, defaults={"organization": b, "project": pb, "title": "Action fictive B"}
            )
            ClientReference.objects.get_or_create(organization=a, label="ClientReference fictive B sans droits")
            ClientReference.objects.get_or_create(organization=b, label="ClientReference fictive A sans droits")
        self.stdout.write(self.style.SUCCESS("E0 synthetic dataset ready: Demo-Org-A/B only"))
