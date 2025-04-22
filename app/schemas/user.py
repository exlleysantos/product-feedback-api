from pydantic import BaseModel, EmailStr
import uuid


class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: str

    class Config:
        orm_mode = True
