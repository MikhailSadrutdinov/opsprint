from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path.cwd()


class JWTAuthSettings(BaseSettings):
    public_key_path: str = BASE_DIR / "certs" / "jwt_private_key.pem"
    private_key_path: str = BASE_DIR / "certs" / "jwt_private_key.pem"
    token_expiration_minutes: int = 15
    algorithm: str = "RS256"


class AppSettings(BaseSettings):
    auth: JWTAuthSettings = JWTAuthSettings()


app_settings = AppSettings()
