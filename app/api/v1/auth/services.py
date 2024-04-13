from fastapi import Form, HTTPException
from starlette import status

from app.api.v1.auth.utils import auth_utils
from app.database import user_repo


class JWTAuthService:
    @staticmethod
    async def get_token(email: str = Form(), password: str = Form()) -> str:
        if not (user := await user_repo.get_user(email)):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User with such email does not found",
            )
        if not auth_utils.compare_passwords(password.encode(), user.password.encode()):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password",
            )
        return auth_utils.encode_token(
            payload={
                "sub": user.email,
            },
        )
