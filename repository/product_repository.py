from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from app.database import Base

# Modelo para la tabla productos
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    stock = Column(Integer, default=0)

def create_product(db: Session, name: str, stock: int):
    db_product = Product(name=name, stock=stock)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product_by_id(db: Session, pid: int):
    return db.query(Product).filter(Product.id == pid).first()

def get_all_products(db: Session):
    return db.query(Product).all()

def update_product_stock(db: Session, pid: int, stock: int):
    product = get_product_by_id(db, pid)
    if product:
        product.stock = stock
        db.commit()
        db.refresh(product)
    return product

def delete_product(db: Session, pid: int):
    product = get_product_by_id(db, pid)
    if product:
        db.delete(product)
        db.commit()
    return product
