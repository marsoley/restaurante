from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    descripcion: str | None = None

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    descripcion: str | None

    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None

class ProductoResponse(ProductoBase):
    id: int

    class Config:
        from_attributes = True
