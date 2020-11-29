# -*- coding: utf-8 -*-

__all__ = ["app_factory"]

import base64

import aiohttp_security
import aiohttp_session
import asyncpg
from aiohttp import web
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from . import auth, config


async def app_factory(cfg: config.Config) -> web.Application:
    app = web.Application()

    app["config"] = cfg

    dbpool = app["dbpool"] = await asyncpg.create_pool(
        database=cfg["database_name"],
        host=cfg["database_host"],
        user=cfg["database_user"],
        password=cfg["database_pass"],
    )

    aiohttp_session.setup(
        app,
        EncryptedCookieStorage(
            base64.urlsafe_b64decode(app["config"]["session_key"])
        ),
    )
    aiohttp_security.setup(
        app, aiohttp_security.SessionIdentityPolicy(), auth.AuthPolicy(dbpool)
    )

    return app
