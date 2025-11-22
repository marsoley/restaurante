from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)
    stock: int = Field(..., ge=0)

class ProductRead(BaseModel):
    id: int
    name: str
    stock: int

    class Config:
        orm_mode = True
