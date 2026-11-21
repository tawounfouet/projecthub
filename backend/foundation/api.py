"""Synthetic E0 API. No global admin bypass, no cross-tenant implicit grant."""
from __future__ import annotations

import json

from django.conf import settings
from django.db import DatabaseError, connection
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.views.decorators.http import require_GET, require_POST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import (
    AuditEvent, ClientReference, Invitation, Membership, Organization,
    Project, Workspace, WorkspaceGrant, WorkItem,
)

User = get_user_model()
ADMIN_ROLES = (Membership.ADMIN, Membership.OWNER)


def e0_only():
    if not settings.E0_SYNTHETIC_ONLY:
        raise PermissionDenied("Le mode E0 synthétique n'est pas activé")


def audit(org, actor, action: str, resource_id: str = ""):
    # Fixed action codes and object UUIDs only. No credentials or payloads in logs.
    AuditEvent.objects.create(
        organization=org, actor=actor, action=action, resource_id=str(resource_id)[:40]
    )


def membership_for(request, org_id) -> Membership:
    membership = Membership.objects.select_related("organization").filter(
        organization_id=org_id, user=request.user, active=True,
    ).first()
    if membership is None:
        raise PermissionDenied("Aucune appartenance active pour cette Organization")
    return membership


def grant_for(request, workspace: Workspace, member: Membership, *, write=False):
    if member.role in ADMIN_ROLES:
        return
    grant = WorkspaceGrant.objects.filter(
        workspace=workspace, user=request.user, active=True,
    ).first()
    if not grant or (write and not grant.can_write):
        raise PermissionDenied("Aucun grant Workspace valide pour cette action")


def active_scope(request, *, write=False):
    e0_only()
    organization_id = request.session.get("e0_org")
    workspace_id = request.session.get("e0_workspace")
    if not organization_id or not workspace_id:
        raise PermissionDenied("Sélectionner un contexte explicite")
    member = membership_for(request, organization_id)
    workspace = Workspace.objects.filter(
        id=workspace_id, organization_id=organization_id,
    ).first()
    if workspace is None:
        raise PermissionDenied("Contexte absent, révoqué ou incorrect")
    grant_for(request, workspace, member, write=write)
    return member.organization, workspace, member


def admin_only(member: Membership):
    if member.role not in ADMIN_ROLES:
        raise PermissionDenied("Réservé à un administrateur de cette Organization")


def bounded(value, label, limit):
    if not isinstance(value, str) or not value.strip() or len(value.strip()) > limit:
        raise ValidationError({label: f"Chaîne requise (1..{limit} caractères)"})
    return value.strip()


def project_json(project):
    return {
        "id": str(project.id), "title": project.title,
        "organization_id": str(project.organization_id),
        "workspace_id": str(project.workspace_id),
    }


def item_json(item):
    return {
        "id": str(item.id), "title": item.title, "status": item.status,
        "organization_id": str(item.organization_id),
        "project_id": str(item.project_id),
    }


@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    """Lightweight liveness: intentionally does not query PostgreSQL."""
    return Response({"status": "ok", "mode": "synthetic-e0"})


@api_view(["GET"])
@permission_classes([AllowAny])
def ready(request):
    """E0 readiness: synthetic mode must be active and PostgreSQL reachable."""
    if not settings.E0_SYNTHETIC_ONLY:
        return Response({"status": "unavailable"}, status=503)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except DatabaseError:
        return Response({"status": "unavailable"}, status=503)
    return Response({"status": "ready"})


@require_GET
@ensure_csrf_cookie
def csrf(request):
    if not settings.E0_SYNTHETIC_ONLY:
        return JsonResponse({"detail": "E0 disabled"}, status=503)
    return JsonResponse({"csrf": "cookie-issued"})


@require_POST
@csrf_protect
def sign_in(request):
    if not settings.E0_SYNTHETIC_ONLY:
        return JsonResponse({"detail": "E0 disabled"}, status=503)
    try:
        data = json.loads(request.body)
        username, password = data["username"], data["password"]
    except (ValueError, KeyError, TypeError):
        return JsonResponse({"detail": "Identifiants invalides"}, status=400)
    if not isinstance(username, str) or not isinstance(password, str):
        return JsonResponse({"detail": "Identifiants invalides"}, status=400)
    user = authenticate(request, username=username, password=password)
    if user is None or not user.is_active:
        return JsonResponse({"detail": "Connexion refusée"}, status=403)
    login(request, user)
    return JsonResponse({"username": user.username})


@require_POST
@csrf_protect
def sign_out(request):
    logout(request)
    return JsonResponse({"signed_out": True})


@api_view(["GET"])
def me(request):
    e0_only()
    return Response({"username": request.user.username, "synthetic": True})


@api_view(["GET"])
def organizations(request):
    e0_only()
    members = Membership.objects.filter(user=request.user, active=True).select_related("organization")
    return Response({"organizations": [
        {"id": str(m.organization_id), "name": m.organization.name, "role": m.role}
        for m in members.order_by("organization__slug")
    ]})


@api_view(["GET"])
def workspaces(request):
    e0_only()
    org_id = request.query_params.get("organization_id")
    if not org_id:
        raise ValidationError({"organization_id": "Requis"})
    member = membership_for(request, org_id)
    qs = Workspace.objects.filter(organization_id=member.organization_id)
    if member.role not in ADMIN_ROLES:
        qs = qs.filter(grants__user=request.user, grants__active=True)
    return Response({"workspaces": [
        {"id": str(w.id), "name": w.name, "organization_id": str(w.organization_id)}
        for w in qs.distinct().order_by("slug")
    ]})


@api_view(["GET", "POST"])
def context(request):
    e0_only()
    if request.method == "GET":
        try:
            org, workspace, member = active_scope(request)
        except PermissionDenied:
            return Response({"selected": None})
        return Response({"selected": {
            "organization_id": str(org.id), "organization_name": org.name,
            "workspace_id": str(workspace.id), "workspace_name": workspace.name,
            "role": member.role,
        }})
    org_id, workspace_id = request.data.get("organization_id"), request.data.get("workspace_id")
    if not org_id or not workspace_id:
        raise ValidationError({"context": "organization_id et workspace_id requis"})
    member = membership_for(request, org_id)
    workspace = Workspace.objects.filter(id=workspace_id, organization_id=member.organization_id).first()
    if workspace is None:
        raise PermissionDenied("Workspace absent dans cette Organization")
    grant_for(request, workspace, member)
    request.session["e0_org"] = str(member.organization_id)
    request.session["e0_workspace"] = str(workspace.id)
    audit(member.organization, request.user, "CONTEXT_SELECTED", workspace.id)
    return Response({"selected": {"organization_id": str(member.organization_id), "workspace_id": str(workspace.id)}})


@api_view(["GET", "POST"])
def projects(request):
    org, workspace, member = active_scope(request, write=request.method == "POST")
    if request.method == "GET":
        return Response({"projects": [
            project_json(p) for p in Project.objects.filter(organization=org, workspace=workspace).order_by("title")
        ]})
    if request.data.get("organization_id") not in (None, str(org.id)) or request.data.get("workspace_id") not in (None, str(workspace.id)):
        raise PermissionDenied("Parentage incohérent")
    title = bounded(request.data.get("title"), "title", 160)
    project = Project.objects.create(organization=org, workspace=workspace, title=title)
    audit(org, request.user, "PROJECT_CREATED", project.id)
    return Response(project_json(project), status=201)


@api_view(["GET", "PATCH"])
def project_detail(request, project_id):
    org, workspace, member = active_scope(request, write=request.method == "PATCH")
    project = get_object_or_404(Project, id=project_id, organization=org, workspace=workspace)
    if request.method == "PATCH":
        if any(k in request.data for k in ("organization_id", "workspace_id")):
            raise PermissionDenied("Parentage immuable dans E0")
        project.title = bounded(request.data.get("title"), "title", 160)
        project.save(update_fields=["title"])
        audit(org, request.user, "PROJECT_CHANGED", project.id)
    return Response(project_json(project))


@api_view(["GET", "POST"])
def workitems(request):
    org, workspace, member = active_scope(request, write=request.method == "POST")
    qs = WorkItem.objects.filter(organization=org, project__workspace=workspace)
    if request.method == "GET":
        return Response({"workitems": [item_json(i) for i in qs.order_by("title")]})
    if request.data.get("organization_id") not in (None, str(org.id)):
        raise PermissionDenied("Tenant de WorkItem interdit")
    project = get_object_or_404(Project, id=request.data.get("project_id"), organization=org, workspace=workspace)
    title = bounded(request.data.get("title"), "title", 180)
    item = WorkItem.objects.create(organization=org, project=project, title=title)
    audit(org, request.user, "WORKITEM_CREATED", item.id)
    return Response(item_json(item), status=201)


@api_view(["GET", "PATCH"])
def workitem_detail(request, item_id):
    org, workspace, member = active_scope(request, write=request.method == "PATCH")
    item = get_object_or_404(WorkItem, id=item_id, organization=org, project__workspace=workspace)
    if request.method == "PATCH":
        if any(k in request.data for k in ("organization_id", "project_id")):
            raise PermissionDenied("Parentage immuable dans E0")
        status_value = request.data.get("status")
        if status_value not in ("todo", "in_progress", "done"):
            raise ValidationError({"status": "Etat inconnu"})
        item.status = status_value
        item.save(update_fields=["status"])
        audit(org, request.user, "WORKITEM_CHANGED", item.id)
    return Response(item_json(item))


@api_view(["GET", "POST"])
def invitations(request):
    org, workspace, member = active_scope(request)
    admin_only(member)
    if request.method == "GET":
        return Response({"invitations": [
            {"id": str(i.id), "username": i.invited_user.username, "status": i.status}
            for i in Invitation.objects.filter(organization=org).select_related("invited_user")
        ]})
    username = bounded(request.data.get("username"), "username", 150)
    invited = get_object_or_404(User, username=username)
    invite = Invitation.objects.create(organization=org, invited_user=invited, created_by=request.user)
    audit(org, request.user, "INVITATION_PENDING", invite.id)
    return Response({"id": str(invite.id), "status": "pending"}, status=201)


@api_view(["GET", "POST"])
def memberships(request):
    org, workspace, member = active_scope(request)
    admin_only(member)
    if request.method == "GET":
        return Response({"memberships": [
            {"id": str(m.id), "username": m.user.username, "role": m.role, "active": m.active}
            for m in Membership.objects.filter(organization=org).select_related("user")
        ]})
    username = bounded(request.data.get("username"), "username", 150)
    user = get_object_or_404(User, username=username)
    existing = Membership.objects.filter(organization=org, user=user).first()
    if existing:
        raise ValidationError({"username": "Membership existant ou révoqué, réactivation interdite"})
    new_member = Membership.objects.create(organization=org, user=user, role=Membership.MEMBER)
    audit(org, request.user, "MEMBERSHIP_GRANTED", new_member.id)
    return Response({"id": str(new_member.id), "role": new_member.role, "active": True}, status=201)


@api_view(["POST"])
def revoke_membership(request, membership_id):
    org, workspace, member = active_scope(request)
    admin_only(member)
    target = get_object_or_404(Membership, id=membership_id, organization=org)
    if not target.active:
        raise ValidationError({"membership": "Déjà révoqué"})
    if target.role == Membership.OWNER and Membership.objects.filter(
        organization=org, role=Membership.OWNER, active=True
    ).count() <= 1:
        raise PermissionDenied("Impossible de révoquer le dernier propriétaire")
    target.active = False
    target.save(update_fields=["active"])
    WorkspaceGrant.objects.filter(user=target.user, workspace__organization=org).update(active=False)
    audit(org, request.user, "MEMBERSHIP_REVOKED", target.id)
    return Response({"revoked": True})


@api_view(["GET"])
def client_references(request):
    org, workspace, member = active_scope(request)
    return Response({"clients": [
        {"id": str(c.id), "label": c.label}
        for c in ClientReference.objects.filter(organization=org).order_by("label")
    ]})


@api_view(["GET"])
def audit_events(request):
    org, workspace, member = active_scope(request)
    admin_only(member)
    return Response({"events": [
        {"action": ev.action, "resource_id": ev.resource_id, "at": ev.created_at.isoformat()}
        for ev in AuditEvent.objects.filter(organization=org)[:100]
    ]})


@api_view(["POST"])
def approvals(request):
    org, workspace, member = active_scope(request)
    # No BusinessMandate has been approved or activated for E0. Fail closed even for OrgAdmin.
    raise PermissionDenied("Aucun mandat métier approuvé pour cette décision")


@api_view(["GET"])
def export_demo(request):
    org, workspace, member = active_scope(request)
    projects = list(Project.objects.filter(organization=org, workspace=workspace).order_by("title"))
    items = WorkItem.objects.filter(organization=org, project__in=projects).order_by("title")
    return Response({
        "synthetic": True,
        "organization_id": str(org.id),
        "workspace_id": str(workspace.id),
        "projects": [project_json(p) for p in projects],
        "workitems": [item_json(item) for item in items],
    })
