from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr, constr
from typing import Any


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    role: str = 'user'
    verified: bool = False
    def __init__(self, **data: Any) -> None:
        print("==========================", data)
        super().__init__(**data)

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class AllUserResponse(UserBaseSchema):
    id: uuid.UUID
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    profile_url: Any