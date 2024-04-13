from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username: str = Field(max_length=60)
    password: str = Field(min_length=8)
    email: EmailStr = Field(max_length=255)


class UserCreateDB(UserCreate):
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserRead(BaseModel):
    username: str
    email: str
    created_at: datetime


class UserReadDB(UserRead):
    password: str
