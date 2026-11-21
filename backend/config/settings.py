"""Synthetic E0 settings. Refuse use without an explicit non-production flag."""
from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import unquote, urlsplit
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parents[1]
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ImproperlyConfigured("DJANGO_SECRET_KEY is required; use local test-only value")
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"
E0_SYNTHETIC_ONLY = os.environ.get("E0_SYNTHETIC_ONLY", "0") == "1"
ALLOWED_HOSTS = [s for s in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,backend,testserver").split(",") if s]
CSRF_TRUSTED_ORIGINS = [s for s in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "http://localhost:3000").split(",") if s]
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "rest_framework",
    "foundation",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = []
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

url = os.environ.get("DATABASE_URL")
if not url:
    raise ImproperlyConfigured("DATABASE_URL is required; PostgreSQL is mandatory for E0")
parsed = urlsplit(url)
if parsed.scheme not in ("postgres", "postgresql") or not parsed.hostname or not parsed.path.strip("/"):
    raise ImproperlyConfigured("DATABASE_URL must be a complete PostgreSQL URL")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": unquote(parsed.path.lstrip("/")),
        "USER": unquote(parsed.username or ""),
        "PASSWORD": unquote(parsed.password or ""),
        "HOST": parsed.hostname,
        "PORT": parsed.port or 5432,
        "CONN_MAX_AGE": 0,
    }
}
AUTH_PASSWORD_VALIDATORS = []  # E0 fixture users only, never production accounts.
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_AGE = 3600
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = False  # Browser sends X-CSRFToken to same-origin /api BFF.
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.SessionAuthentication"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}
