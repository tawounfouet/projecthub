"""Stable E0 API routes, accepting either slash form behind Next rewrites."""
from django.urls import path
from foundation import api

API_ROUTES = [
    ("api/health/", api.health),
    ("api/auth/csrf/", api.csrf),
    ("api/auth/login/", api.sign_in),
    ("api/auth/logout/", api.sign_out),
    ("api/me/", api.me),
    ("api/organizations/", api.organizations),
    ("api/workspaces/", api.workspaces),
    ("api/context/", api.context),
    ("api/projects/", api.projects),
    ("api/projects/<uuid:project_id>/", api.project_detail),
    ("api/workitems/", api.workitems),
    ("api/workitems/<uuid:item_id>/", api.workitem_detail),
    ("api/invitations/", api.invitations),
    ("api/memberships/", api.memberships),
    ("api/memberships/<uuid:membership_id>/revoke/", api.revoke_membership),
    ("api/client-references/", api.client_references),
    ("api/audit/", api.audit_events),
    ("api/approvals/", api.approvals),
    ("api/export/", api.export_demo),
]

# The external Next rewrite may strip the final slash. Both aliases invoke the
# identical Django/DRF view, so their authentication and tenant checks match.
urlpatterns = [path(route, view) for route, view in API_ROUTES]
urlpatterns += [path(route[:-1], view) for route, view in API_ROUTES if route.endswith("/")]
