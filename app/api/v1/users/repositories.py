from sqlalchemy.ext.asyncio import AsyncEngine

from app.api.v1.users.models import user_table
from app.api.v1.users.schemas import UserCreateDB, UserRead, UserReadDB


class UserRepository:
    def __init__(self, async_engine: AsyncEngine):
        self.async_engine = async_engine

    async def add_user(self, user_info: UserCreateDB):
        async with self.async_engine.begin() as conn:
            await conn.execute(user_table.insert().values(**user_info.model_dump()))

    async def get_user(self, email: str) -> UserReadDB | None:
        async with self.async_engine.begin() as conn:
            result = (
                (await conn.execute(user_table.select().filter_by(email=email)))
                .mappings()
                .one_or_none()
            )
            return UserReadDB(**result) if result else None

    async def get_users(self):
        async with self.async_engine.begin() as conn:
            result = (await conn.execute(user_table.select())).mappings()
            return [UserRead(**row) for row in result]
