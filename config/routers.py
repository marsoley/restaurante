from api import productos_api

from api import insumos_api
from api import ventas_api

ROUTERS = [
    productos_api.router,
    insumos_api.router,
    ventas_api.router,
]
