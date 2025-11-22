from fastapi import FastAPI
from app.api import user_api, product_api

def include_all_routers(app: FastAPI):
    app.include_router(user_api.router, prefix="/users", tags=["Usuarios"])
    app.include_router(product_api.router, prefix="/products", tags=["Productos"])
