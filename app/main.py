import uvicorn
from fastapi import FastAPI

from app.api.v1.auth.routers import router as jwt_auth_router
from app.api.v1.users.routers import router as users_router

app = FastAPI()

app.include_router(jwt_auth_router)
app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
