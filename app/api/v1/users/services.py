from fastapi import HTTPException
from starlette import status

from app.api.v1.auth.utils import auth_utils
from app.api.v1.users.repositories import UserRepository
from app.api.v1.users.schemas import UserCreate, UserCreateDB


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def add_user(self, user_info: UserCreate):
        await self._check_user_info(user_info)
        pwd_hash = auth_utils.hash_password(password=user_info.password)
        await self.repository.add_user(
            user_info=UserCreateDB(
                username=user_info.username,
                email=user_info.email,
                password=pwd_hash,
            )
        )

    async def get_users(self):
        return await self.repository.get_users()

    async def _check_user_info(self, user_info: UserCreate):
        if user := await self.repository.get_user(email=user_info.email):
            if user.email == user_info.email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"User with email {user_info.email} already exists",
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"User with username {user_info.username} already exists",
                )
