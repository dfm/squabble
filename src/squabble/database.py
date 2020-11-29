# -*- coding: utf-8 -*-

__all__ = ["get_connection"]

import asyncpg

from .config import Config


async def get_connection(config: Config) -> asyncpg.Connection:
    return await asyncpg.connect(
        user=config["database_user"], password=config["database_pass"]
    )
