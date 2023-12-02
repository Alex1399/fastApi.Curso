from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    prec_compra: float
    prec_venta: float
    proveedor: str
    

app= FastAPI()

productos= []
@app.get('/')
def index():
    return {'mensaje':'Binevenh'}

@app.get('/producto')
def obtener_productos():
    return productos

@app.post('/producto')
def crear_producto(producto: Producto):
    productos.append(producto)
    return{'mensaje':'Producto creado satisfactoriamente'}

