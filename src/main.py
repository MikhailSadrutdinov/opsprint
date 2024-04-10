import uvicorn
from fastapi import FastAPI

from src.auth.router import router as jwt_auth_router

app = FastAPI()

app.include_router(jwt_auth_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
