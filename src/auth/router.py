from fastapi import APIRouter

from src.base.schemas import APITags

router = APIRouter(prefix="/auth", tags=[APITags.JWT_AUTH])


@router.post(path="/token")
async def get_token():
    pass
