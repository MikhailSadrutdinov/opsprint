from fastapi import APIRouter, Depends

from app.api.v1.auth.schemas import TokenResponse
from app.api.v1.auth.services import JWTAuthService
from app.api.v1.shared.schemas import APITags

router = APIRouter(prefix="/auth", tags=[APITags.JWT_AUTH])


@router.post(path="/token", response_model=TokenResponse)
async def get_token(token: str = Depends(JWTAuthService.get_token)):
    return TokenResponse(token=token, token_type="Bearer")
