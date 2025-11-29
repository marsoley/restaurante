from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import SessionLocal
from services.productos_service import ProductosService
from domain.productos_model import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse
)

router = APIRouter(prefix="/productos", tags=["Productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return ProductosService(db).listar()

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    return ProductosService(db).obtener(producto_id)

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(data: ProductoCreate, db: Session = Depends(get_db)):
    return ProductosService(db).crear(data)

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    return ProductosService(db).actualizar(producto_id, data)

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    return ProductosService(db).eliminar(producto_id)
