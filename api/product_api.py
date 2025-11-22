from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.product_service import (
    create_product_service, get_product_service, get_all_products_service,
    update_product_stock_service, delete_product_service
)
from app.domain.product_model import ProductCreate, ProductRead
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=ProductRead)
def crear_producto(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        return create_product_service(db, product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{pid}", response_model=ProductRead)
def obtener_producto(pid: int, db: Session = Depends(get_db)):
    try:
        return get_product_service(db, pid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[ProductRead])
def listar_productos(db: Session = Depends(get_db)):
    return get_all_products_service(db)

@router.put("/{pid}/stock", response_model=ProductRead)
def actualizar_stock(pid: int, stock: int, db: Session = Depends(get_db)):
    try:
        return update_product_stock_service(db, pid, stock)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{pid}")
def eliminar_producto(pid: int, db: Session = Depends(get_db)):
    res = delete_product_service(db, pid)
    if not res:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"eliminado": True}
