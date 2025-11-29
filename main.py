from fastapi import FastAPI
from config.routers import ROUTERS

app = FastAPI(
    title="API Restaurante",
    description="API para gestión de inventario de restaurante",
    version="1.0.0"
)

for router in ROUTERS:
    app.include_router(router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

