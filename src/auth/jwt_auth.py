import jwt

from src.config import app_settings


class JWTAuth:
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


jwt_auth_utils = JWTAuth()
