__all__ = ["get_config"]

from typing import Any, Mapping, TypedDict

import schema
import toml
from cryptography import fernet

SCHEMA = schema.Schema(
    {
        "database_host": str,
        "database_name": str,
        "database_user": str,
        "database_pass": str,
        schema.Optional(
            "session_key", default=fernet.Fernet.generate_key().decode("utf-8")
        ): str,
    }
)


class Config(TypedDict):
    database_host: str
    database_name: str
    database_user: str
    database_pass: str
    session_key: str


def validate_config(config: Mapping[str, Any]) -> Config:
    validated = SCHEMA.validate(config)
    return Config(
        database_host=validated["database_host"],
        database_name=validated["database_name"],
        database_user=validated["database_user"],
        database_pass=validated["database_pass"],
        session_key=validated["session_key"],
    )


def get_config(filename: str) -> Config:
    return validate_config(toml.load(filename))
