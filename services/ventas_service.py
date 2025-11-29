from sqlalchemy.orm import Session
from fastapi import HTTPException

from repository.ventas_repository import VentasRepository
from repository.productos_repository import ProductosRepository
from domain.ventas_model import VentaCreate, VentaUpdate, VentaResponse

class VentasService:
    def __init__(self, db: Session):
        self.repo = VentasRepository(db)
        self.repo_producto = ProductosRepository(db)

    def listar(self):
        ventas = self.repo.listar()
        return [VentaResponse.from_orm(v) for v in ventas]

    def obtener(self, venta_id: int):
        venta = self.repo.obtener_por_id(venta_id)
        if not venta:
            raise HTTPException(status_code=404, detail="Venta no encontrada")
        return VentaResponse.from_orm(venta)

    def crear(self, data: VentaCreate):

        producto = self.repo_producto.obtener_por_id(data.producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no existe")

        if data.cantidad <= 0:
            raise HTTPException(status_code=400, detail="Cantidad inválida")

        if data.total <= 0:
            raise HTTPException(status_code=400, detail="Total inválido")

        venta = self.repo.crear(
            producto_id=data.producto_id,
            cantidad=data.cantidad,
            total=data.total
        )

        return VentaResponse.from_orm(venta)

    def actualizar(self, venta_id: int, data: VentaUpdate):
        venta = self.repo.obtener_por_id(venta_id)

        if not venta:
            raise HTTPException(status_code=404, detail="Venta no encontrada")

        cambios = data.dict(exclude_unset=True)

        venta_mod = self.repo.actualizar(venta, cambios)
        return VentaResponse.from_orm(venta_mod)

    def eliminar(self, venta_id: int):
        venta = self.repo.obtener_por_id(venta_id)
        if not venta:
            raise HTTPException(status_code=404, detail="Venta no encontrada")

        self.repo.eliminar(venta)
        return {"mensaje": "Venta eliminada correctamente"}
