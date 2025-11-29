from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import SessionLocal
from services.insumos_service import InsumosService
from domain.insumos_model import InsumoCreate, InsumoUpdate, InsumoResponse

router = APIRouter(prefix="/insumos", tags=["Insumos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[InsumoResponse])
def listar_insumos(db: Session = Depends(get_db)):
    return InsumosService(db).listar()

@router.get("/{insumo_id}", response_model=InsumoResponse)
def obtener_insumo(insumo_id: int, db: Session = Depends(get_db)):
    return InsumosService(db).obtener(insumo_id)

@router.post("/", response_model=InsumoResponse, status_code=status.HTTP_201_CREATED)
def crear_insumo(data: InsumoCreate, db: Session = Depends(get_db)):
    return InsumosService(db).crear(data)

@router.put("/{insumo_id}", response_model=InsumoResponse)
def actualizar_insumo(insumo_id: int, data: InsumoUpdate, db: Session = Depends(get_db)):
    return InsumosService(db).actualizar(insumo_id, data)

@router.delete("/{insumo_id}")
def eliminar_insumo(insumo_id: int, db: Session = Depends(get_db)):
    return InsumosService(db).eliminar(insumo_id)
