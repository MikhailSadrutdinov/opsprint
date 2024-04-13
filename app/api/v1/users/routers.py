from fastapi import APIRouter

from app.api.v1.shared.schemas import APITags
from app.database import user_repo
from app.api.v1.users.services import UserService
from app.api.v1.users.schemas import UserCreate

router = APIRouter(prefix="/users", tags=[APITags.USERS])


@router.get(path="/")
async def get_users():
    res = await UserService(repository=user_repo).get_users()
    return res


@router.post(path="/")
async def create_user(user_info: UserCreate):
    await UserService(repository=user_repo).add_user(user_info)
    return {"message": "User created successfully"}
