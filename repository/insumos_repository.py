from sqlalchemy.orm import Session
from database import InsumoDB

class InsumosRepository:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(InsumoDB).all()

    def obtener_por_id(self, insumo_id: int):
        return self.db.query(InsumoDB).filter(InsumoDB.id == insumo_id).first()

    def obtener_por_nombre(self, nombre: str):
        return self.db.query(InsumoDB).filter(InsumoDB.nombre == nombre).first()

    def crear(self, nombre: str, categoria: str, cantidad: float, unidad: str):
        insumo = InsumoDB(
            nombre=nombre,
            categoria=categoria,
            cantidad=cantidad,
            unidad=unidad
        )
        self.db.add(insumo)
        self.db.commit()
        self.db.refresh(insumo)
        return insumo

    def actualizar(self, insumo_db: InsumoDB, cambios: dict):
        for key, value in cambios.items():
            setattr(insumo_db, key, value)
        self.db.commit()
        self.db.refresh(insumo_db)
        return insumo_db

    def eliminar(self, insumo_db: InsumoDB):
        self.db.delete(insumo_db)
        self.db.commit()
