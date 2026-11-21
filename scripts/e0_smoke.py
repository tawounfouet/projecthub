#!/usr/bin/env python3
"""Real HTTP E0 smoke through the Next.js /api same-origin reverse proxy."""
from __future__ import annotations

import json
import os
from http.cookiejar import CookieJar
from urllib.error import HTTPError
from urllib.request import HTTPCookieProcessor, ProxyHandler, Request, build_opener

BASE = os.environ.get("E0_SMOKE_URL", "http://127.0.0.1:3000").rstrip("/")
DEMO_USER = "demo_alice"
DEMO_PASSWORD = os.environ.get("E0_DEMO_PASSWORD") or "-".join(("e0", "demo", "only"))
ORG_A = "aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa"
ORG_B = "bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb"
WS_A = "aaaaaaaa-aaaa-4aaa-bbbb-aaaaaaaaaaaa"
WS_B = "bbbbbbbb-bbbb-4bbb-aaaa-bbbbbbbbbbbb"
PROJECT_B = "bbbbbbbb-bbbb-4bbb-cccc-bbbbbbbbbbbb"


def main():
    cookies = CookieJar()
    client = build_opener(ProxyHandler({}), HTTPCookieProcessor(cookies))

    def csrf_value():
        return next((c.value for c in cookies if c.name == "csrftoken"), "")

    def request(method, route, payload=None, expected=200):
        data = None if payload is None else json.dumps(payload).encode()
        headers = {"Content-Type": "application/json"}
        if method != "GET":
            headers["X-CSRFToken"] = csrf_value()
        req = Request(BASE + route, data=data, headers=headers, method=method)
        try:
            response = client.open(req, timeout=10)
            status = response.status
            obj = json.load(response)
        except HTTPError as err:
            status = err.code
            raw = err.read().decode(errors="replace")
            try:
                obj = json.loads(raw)
            except json.JSONDecodeError:
                obj = {"detail": raw[:300], "content_type": err.headers.get("Content-Type", "unknown")}

        if status != expected:
            raise AssertionError(f"{method} {route}: expected {expected}, got {status}, body={obj}")
        return obj

    request("GET", "/api/health/")
    request("GET", "/api/auth/csrf/")
    request("POST", "/api/auth/login/", {"username": DEMO_USER, "password": DEMO_PASSWORD})
    member = request("GET", "/api/organizations/")["organizations"]
    assert len(member) == 1 and member[0]["id"] == ORG_A, member
    request("POST", "/api/context/", {"organization_id": ORG_B, "workspace_id": WS_B}, expected=403)
    request("POST", "/api/context/", {"organization_id": ORG_A, "workspace_id": WS_A})
    only_a = request("GET", "/api/projects/")["projects"]
    assert len(only_a) == 1 and only_a[0]["organization_id"] == ORG_A, only_a
    request("GET", f"/api/projects/{PROJECT_B}/", expected=404)
    request("POST", "/api/approvals/", {"id": "synthetic"}, expected=403)
    exported = request("GET", "/api/export/")
    assert exported["organization_id"] == ORG_A
    assert "Projet fictif B" not in json.dumps(exported)
    print("E0_HTTP_SMOKE_PASSED: login, context, foreign tenant refusal, approval refusal, export isolation")


if __name__ == "__main__":
    main()
