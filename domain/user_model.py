from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
