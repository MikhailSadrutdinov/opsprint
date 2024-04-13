from datetime import datetime, timedelta

import bcrypt
import jwt

from app.config import app_settings


class AuthUtils:
    def __init__(
        self,
        public_key: str = app_settings.auth.public_key_path.read_text(),
        private_key: str = app_settings.auth.private_key_path.read_text(),
        token_expiration_minutes: int = app_settings.auth.token_expiration_minutes,
        algorithm: int = app_settings.auth.algorithm,
    ):
        self._public_key = public_key
        self._private_key = private_key
        self._token_expiration_minutes = token_expiration_minutes
        self._algorithm = algorithm

    def encode_token(
        self,
        payload: dict,
    ) -> str:
        payload["iat"] = datetime.utcnow()
        payload["exp"] = payload["iat"] + timedelta(
            minutes=self._token_expiration_minutes
        )
        return jwt.encode(
            payload=payload,
            key=self._private_key,
            algorithm=self._algorithm,
        )

    def decode_token(
        self,
        token: str | bytes,
    ) -> dict:
        return jwt.decode(
            jwt=token,
            key=self._public_key,
            algorithms=[self._algorithm],
        )

    @staticmethod
    def hash_password(password: str) -> bytes:
        return bcrypt.hashpw(
            password=password.encode(),
            salt=bcrypt.gensalt(),
        )

    @staticmethod
    def compare_passwords(password: bytes, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(
            password=password,
            hashed_password=hashed_password,
        )


auth_utils = AuthUtils()
