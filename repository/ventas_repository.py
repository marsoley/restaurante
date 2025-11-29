from sqlalchemy.orm import Session
from database import VentaDB
from datetime import datetime

class VentasRepository:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(VentaDB).all()

    def obtener_por_id(self, venta_id: int):
        return self.db.query(VentaDB).filter(VentaDB.id == venta_id).first()

    def crear(self, producto_id: int, cantidad: int, total: float):
        venta = VentaDB(
            producto_id=producto_id,
            cantidad=cantidad,
            total=total
        )
        self.db.add(venta)
        self.db.commit()
        self.db.refresh(venta)
        return venta

    def actualizar(self, venta_db: VentaDB, cambios: dict):
        for key, value in cambios.items():
            setattr(venta_db, key, value)
        self.db.commit()
        self.db.refresh(venta_db)
        return venta_db

    def eliminar(self, venta_db: VentaDB):
        self.db.delete(venta_db)
        self.db.commit()
