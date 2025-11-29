from sqlalchemy.orm import Session
from fastapi import HTTPException

from repository.insumos_repository import InsumosRepository
from domain.insumos_model import (
    InsumoCreate,
    InsumoUpdate,
    InsumoResponse
)

class InsumosService:
    def __init__(self, db: Session):
        self.repo = InsumosRepository(db)

    def listar(self):
        insumos = self.repo.listar()
        return [InsumoResponse.from_orm(i) for i in insumos]

    def obtener(self, insumo_id: int):
        insumo = self.repo.obtener_por_id(insumo_id)
        if not insumo:
            raise HTTPException(status_code=404, detail="Insumo no encontrado")
        return InsumoResponse.from_orm(insumo)

    def crear(self, data: InsumoCreate):
        if self.repo.obtener_por_nombre(data.nombre):
            raise HTTPException(status_code=400, detail="El insumo ya existe")

        if data.cantidad < 0:
            raise HTTPException(status_code=400, detail="La cantidad no puede ser negativa")

        insumo = self.repo.crear(
            nombre=data.nombre,
            categoria=data.categoria,
            cantidad=data.cantidad,
            unidad=data.unidad
        )

        return InsumoResponse.from_orm(insumo)

    def actualizar(self, insumo_id: int, data: InsumoUpdate):
        insumo = self.repo.obtener_por_id(insumo_id)

        if not insumo:
            raise HTTPException(status_code=404, detail="Insumo no encontrado")

        cambios = data.dict(exclude_unset=True)

        if "cantidad" in cambios and cambios["cantidad"] < 0:
            raise HTTPException(status_code=400, detail="La cantidad no puede ser negativa")

        insumo_mod = self.repo.actualizar(insumo, cambios)
        return InsumoResponse.from_orm(insumo_mod)

    def eliminar(self, insumo_id: int):
        insumo = self.repo.obtener_por_id(insumo_id)
        if not insumo:
            raise HTTPException(status_code=404, detail="Insumo no encontrado")

        self.repo.eliminar(insumo)
        return {"mensaje": "Insumo eliminado correctamente"}
