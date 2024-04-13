from functools import cached_property
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field, model_validator
from pydantic_settings import BaseSettings
from sqlalchemy import URL

BASE_DIR = Path.cwd()

load_dotenv()


class JWTAuthSettings(BaseSettings):
    public_key_path: Path = BASE_DIR / "certs" / "jwt_private_key.pem"
    private_key_path: Path = BASE_DIR / "certs" / "jwt_private_key.pem"
    token_expiration_minutes: int = 15
    algorithm: str = "RS256"


class PostgresSettings(BaseSettings):
    username: str = Field(default="postgres", alias="POSTGRES_USERNAME")
    password: str = Field(default="postgres", alias="POSTGRES_PASSWORD")
    host: str = Field(default="localhost", alias="POSTGRES_HOST")
    port: int = Field(default=5432, alias="POSTGRES_PORT")
    database: str = Field(default="opsprint", alias="POSTGRES_DATABASE")

    @cached_property
    def url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )


class AppSettings(BaseSettings):
    testing: bool = Field(default=False, alias="TESTING")
    database_url: URL = PostgresSettings().url
    auth: JWTAuthSettings = JWTAuthSettings()

    @model_validator(mode="after")
    def validate_database_url_url(cls, instance):
        if instance.testing:
            instance.database_url = instance.database_url.set(
                database=f"{instance.database_url.database}_test"
            )
        return instance


app_settings = AppSettings()
