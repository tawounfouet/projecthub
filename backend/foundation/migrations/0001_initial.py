# Initial E0 foundation tables and PostgreSQL composite tenancy foreign keys.
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import foundation.models


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("slug", models.SlugField(unique=True)),
                ("name", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Workspace",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("slug", models.SlugField()),
                ("name", models.CharField(max_length=120)),
                ("organization", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="workspaces", to="foundation.organization")),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("role", models.CharField(choices=[("owner", "Owner"), ("admin", "Admin"), ("member", "Member")], max_length=12)),
                ("active", models.BooleanField(default=True)),
                ("organization", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="memberships", to="foundation.organization")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="e0_memberships", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="WorkspaceGrant",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("active", models.BooleanField(default=True)),
                ("can_write", models.BooleanField(default=False)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="e0_workspace_grants", to=settings.AUTH_USER_MODEL)),
                ("workspace", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="grants", to="foundation.workspace")),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=160)),
                ("organization", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="projects", to="foundation.organization")),
                ("workspace", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="projects", to="foundation.workspace")),
            ],
        ),
        migrations.CreateModel(
            name="WorkItem",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=180)),
                ("status", models.CharField(default="todo", max_length=16)),
                ("organization", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="workitems", to="foundation.organization")),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="workitems", to="foundation.project")),
            ],
        ),
        migrations.CreateModel(
            name="Invitation",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("status", models.CharField(default="pending", max_length=16)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="e0_sent_invitations", to=settings.AUTH_USER_MODEL)),
                ("invited_user", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="e0_invitations", to=settings.AUTH_USER_MODEL)),
                ("organization", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="invitations", to="foundation.organization")),
            ],
        ),
        migrations.CreateModel(
            name="ClientReference",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("label", models.CharField(max_length=120)),
                ("organization", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="client_references", to="foundation.organization")),
            ],
        ),
        migrations.CreateModel(
            name="AuditEvent",
            fields=[
                ("id", models.UUIDField(default=foundation.models.uid, editable=False, primary_key=True, serialize=False)),
                ("action", models.CharField(max_length=60)),
                ("resource_id", models.CharField(blank=True, max_length=40)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("actor", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="e0_audit_events", to=settings.AUTH_USER_MODEL)),
                ("organization", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="audit_events", to="foundation.organization")),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddConstraint(model_name="workspace", constraint=models.UniqueConstraint(fields=("organization", "slug"), name="uq_ws_org_slug")),
        migrations.AddConstraint(model_name="workspace", constraint=models.UniqueConstraint(fields=("organization", "id"), name="uq_ws_org_id")),
        migrations.AddConstraint(model_name="membership", constraint=models.UniqueConstraint(fields=("organization", "user"), name="uq_membership_org_user")),
        migrations.AddConstraint(model_name="workspacegrant", constraint=models.UniqueConstraint(fields=("workspace", "user"), name="uq_grant_workspace_user")),
        migrations.AddConstraint(model_name="project", constraint=models.UniqueConstraint(fields=("organization", "id"), name="uq_proj_org_id")),
        migrations.RunSQL(
            sql=[
                """ALTER TABLE foundation_project ADD CONSTRAINT fk_project_ws_org
                FOREIGN KEY (organization_id, workspace_id)
                REFERENCES foundation_workspace (organization_id, id)
                DEFERRABLE INITIALLY IMMEDIATE""",
                """ALTER TABLE foundation_workitem ADD CONSTRAINT fk_item_project_org
                FOREIGN KEY (organization_id, project_id)
                REFERENCES foundation_project (organization_id, id)
                DEFERRABLE INITIALLY IMMEDIATE""",
            ],
            reverse_sql=[
                "ALTER TABLE foundation_workitem DROP CONSTRAINT fk_item_project_org",
                "ALTER TABLE foundation_project DROP CONSTRAINT fk_project_ws_org",
            ],
        ),
    ]
