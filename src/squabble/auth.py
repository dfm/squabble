# -*- coding: utf-8 -*-

__all__ = ["AuthPolicy", "check_credentials"]

from typing import Dict, Optional

import asyncpg
from aiohttp_security.abc import AbstractAuthorizationPolicy
from passlib.hash import pbkdf2_sha256


def hash_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pbkdf2_sha256.verify(password, hashed)


class AuthPolicy(AbstractAuthorizationPolicy):
    def __init__(self, dbpool: asyncpg.Pool):
        self.dbpool = dbpool

    async def authorized_userid(self, identity: str) -> Optional[str]:
        async with self.dbpool.acquire() as connection:
            async with connection.transaction():
                result = await connection.fetchone(
                    "SELECT id, username WHERE username=$1", identity
                )
                print(result)
                if result:
                    return result["id"]
                return None

    async def permits(
        self, identity: str, permission: str, context: Optional[Dict] = None
    ) -> bool:
        return identity is not None


async def check_credentials(
    dbpool: asyncpg.pool.Pool, username: str, password: str
) -> bool:
    async with dbpool.acquire() as connection:
        async with connection.transaction():
            result = await connection.face(
                "SELECT password WHERE username=$1", username
            )
            if result is not None:
                return verify_password(password, result[0])
    return False
