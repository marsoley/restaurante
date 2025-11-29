from pydantic import BaseModel
from typing import Optional

class InsumoBase(BaseModel):
    nombre: str
    categoria: str
    cantidad: float
    unidad: str   # Ej: "kg", "litros", "unidades"

class InsumoCreate(InsumoBase):
    pass

class InsumoUpdate(BaseModel):
    nombre: Optional[str] = None
    categoria: Optional[str] = None
    cantidad: Optional[float] = None
    unidad: Optional[str] = None

class InsumoResponse(InsumoBase):
    id: int

    class Config:
        from_attributes = True
