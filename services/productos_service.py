from sqlalchemy.orm import Session
from fastapi import HTTPException

from repository.productos_repository import ProductosRepository
from domain.productos_model import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse
)

class ProductosService:
    def __init__(self, db: Session):
        self.repo = ProductosRepository(db)

    def listar(self):
        productos = self.repo.listar()
        return [ProductoResponse.from_orm(p) for p in productos]

    def obtener(self, producto_id: int):
        producto = self.repo.obtener_por_id(producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return ProductoResponse.from_orm(producto)

    def crear(self, data: ProductoCreate):
        if self.repo.obtener_por_nombre(data.nombre):
            raise HTTPException(status_code=400, detail="El nombre del producto ya existe")

        if data.stock < 0:
            raise HTTPException(status_code=400, detail="El stock no puede ser negativo")

        producto = self.repo.crear(
            nombre=data.nombre,
            descripcion=data.descripcion,
            precio=data.precio,
            stock=data.stock
        )
        return ProductoResponse.from_orm(producto)

    def actualizar(self, producto_id: int, data: ProductoUpdate):
        producto = self.repo.obtener_por_id(producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        cambios = data.dict(exclude_unset=True)

        if "stock" in cambios and cambios["stock"] < 0:
            raise HTTPException(status_code=400, detail="El stock no puede ser negativo")

        producto_act = self.repo.actualizar(producto, cambios)
        return ProductoResponse.from_orm(producto_act)

    def eliminar(self, producto_id: int):
        producto = self.repo.obtener_por_id(producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        self.repo.eliminar(producto)
        return {"mensaje": "Producto eliminado correctamente"}
