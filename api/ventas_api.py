from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import SessionLocal
from services.ventas_service import VentasService
from domain.ventas_model import VentaCreate, VentaUpdate, VentaResponse

router = APIRouter(prefix="/ventas", tags=["Ventas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[VentaResponse])
def listar_ventas(db: Session = Depends(get_db)):
    return VentasService(db).listar()

@router.get("/{venta_id}", response_model=VentaResponse)
def obtener_venta(venta_id: int, db: Session = Depends(get_db)):
    return VentasService(db).obtener(venta_id)

@router.post("/", response_model=VentaResponse, status_code=status.HTTP_201_CREATED)
def crear_venta(data: VentaCreate, db: Session = Depends(get_db)):
    return VentasService(db).crear(data)

@router.put("/{venta_id}", response_model=VentaResponse)
def actualizar_venta(venta_id: int, data: VentaUpdate, db: Session = Depends(get_db)):
    return VentasService(db).actualizar(venta_id, data)

@router.delete("/{venta_id}")
def eliminar_venta(venta_id: int, db: Session = Depends(get_db)):
    return VentasService(db).eliminar(venta_id)
