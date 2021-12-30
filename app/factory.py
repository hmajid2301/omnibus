from functools import lru_cache
from typing import List

from fastapi_cloudauth.auth0 import Auth0
from fastapi_cloudauth.base import ScopedAuth

from app.core.config import get_settings


def get_read_scopes():
    scopes = _get_auth_scope(["admin:read"])
    return scopes


def get_write_scopes():
    scopes = _get_auth_scope(["admin:write"])
    return scopes


def _get_auth_scope(scopes: List[str]) -> ScopedAuth:
    auth = _get_auth()
    return auth.scope(scopes)


@lru_cache()
def _get_auth():
    config = get_settings()
    auth = Auth0(domain=config.AUTH0_DOMAIN, customAPI=config.AUTH0_CUSTOM_API)
    return auth
