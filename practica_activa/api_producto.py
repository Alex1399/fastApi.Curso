from typing import Optional
from uuid import uuid4 as uuid

from fastapi import FastAPI, HTTPException
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
    producto.id = str(uuid())
    productos.append(producto)
    return{'mensaje':'Producto creado satisfactoriamente'}

@app.get('/producto/{producto_id}')
def obtener_producto_por_id(producto_id: str):
    resultado= list(filter(lambda p: p.id == producto_id, productos))
    
    if len(resultado):
        return resultado[0]
    
    raise HTTPException(status_code=404, detail= f'el producto con el ID {producto_id} no fue encontrado')

    

