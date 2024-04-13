from sqlalchemy.ext.asyncio import create_async_engine

from app.config import app_settings
from app.api.v1.users.repositories import UserRepository

async_engine = create_async_engine(url=app_settings.database_url)
user_repo = UserRepository(async_engine=async_engine)
