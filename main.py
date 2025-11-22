from fastapi import FastAPI
from app.config.routers import include_all_routers

app = FastAPI(title="Sistema de Gestión de Inventario para Restaurantes")

include_all_routers(app)

@app.get("/")
def root():
    return {"msg": "API funcionando correctamente"}
