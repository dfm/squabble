# -*- coding: utf-8 -*-

__all__ = []

import asyncpg


async def get_connection(config):
    return await asyncpg.connect(user=config.user, password=password)
