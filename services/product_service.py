from sqlalchemy.orm import Session
from app.domain.product_model import ProductCreate
from app.repository.product_repository import (
    create_product, get_product_by_id, get_all_products, update_product_stock, delete_product
)

def create_product_service(db: Session, product: ProductCreate):
    if product.stock < 0:
        raise ValueError("El stock debe ser mayor o igual a 0")
    return create_product(db, product.name, product.stock)

def get_product_service(db: Session, pid: int):
    product = get_product_by_id(db, pid)
    if not product:
        raise ValueError("Producto no encontrado")
    return product

def get_all_products_service(db: Session):
    return get_all_products(db)

def update_product_stock_service(db: Session, pid: int, stock: int):
    if stock < 0:
        raise ValueError("Stock no puede ser negativo")
    return update_product_stock(db, pid, stock)

def delete_product_service(db: Session, pid: int):
    return delete_product(db, pid)
