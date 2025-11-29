from sqlalchemy.orm import Session
from database import ProductoDB

class ProductosRepository:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(ProductoDB).all()

    def obtener_por_id(self, producto_id: int):
        return self.db.query(ProductoDB).filter(ProductoDB.id == producto_id).first()

    def obtener_por_nombre(self, nombre: str):
        return self.db.query(ProductoDB).filter(ProductoDB.nombre == nombre).first()

    def crear(self, nombre: str, descripcion: str, precio: float, stock: int):
        producto = ProductoDB(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto

    def actualizar(self, producto_db: ProductoDB, cambios: dict):
        for key, value in cambios.items():
            setattr(producto_db, key, value)

        self.db.commit()
        self.db.refresh(producto_db)
        return producto_db

    def eliminar(self, producto_db: ProductoDB):
        self.db.delete(producto_db)
        self.db.commit()
