"""E0 foundation only. Organization is the canonical tenant, not Workspace."""
import uuid
from django.conf import settings
from django.db import models


def uid():
    return uuid.uuid4()


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)


class Workspace(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="workspaces")
    slug = models.SlugField()
    name = models.CharField(max_length=120)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["organization", "slug"], name="uq_ws_org_slug"),
            models.UniqueConstraint(fields=["organization", "id"], name="uq_ws_org_id"),
        ]


class Membership(models.Model):
    OWNER, ADMIN, MEMBER = "owner", "admin", "member"
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="memberships")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="e0_memberships")
    role = models.CharField(max_length=12, choices=[(OWNER, "Owner"), (ADMIN, "Admin"), (MEMBER, "Member")])
    active = models.BooleanField(default=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["organization", "user"], name="uq_membership_org_user")]


class WorkspaceGrant(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    workspace = models.ForeignKey(Workspace, on_delete=models.PROTECT, related_name="grants")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="e0_workspace_grants")
    active = models.BooleanField(default=True)
    can_write = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["workspace", "user"], name="uq_grant_workspace_user")]


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="projects")
    workspace = models.ForeignKey(Workspace, on_delete=models.PROTECT, related_name="projects")
    title = models.CharField(max_length=160)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["organization", "id"], name="uq_proj_org_id")]


class WorkItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="workitems")
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="workitems")
    title = models.CharField(max_length=180)
    status = models.CharField(max_length=16, default="todo")


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="invitations")
    invited_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="e0_invitations")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="e0_sent_invitations")
    status = models.CharField(max_length=16, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)


class ClientReference(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="client_references")
    label = models.CharField(max_length=120)


class AuditEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="audit_events")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="e0_audit_events")
    action = models.CharField(max_length=60)
    resource_id = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
