from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VentaBase(BaseModel):
    producto_id: int
    cantidad: int
    total: float

class VentaCreate(VentaBase):
    pass

class VentaUpdate(BaseModel):
    producto_id: Optional[int] = None
    cantidad: Optional[int] = None
    total: Optional[float] = None

class VentaResponse(VentaBase):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True
