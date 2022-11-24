import database as db
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Response, HTTPException

app = FastAPI()


#listamos todos los clientes
@app.get("/clientes/")
async def clientes():
    content = db.Clientes.lista
    headers = {"content-type": "charset=utf-8"}
    return JSONResponse(content=content, headers=headers)

content = [
    {'dni': cliente.dni, 'nombre': cliente.nombre, 'apellido': cliente.apellido}
    for cliente in db.Clientes.lista
]

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}

content = [cliente.to_dict() for cliente in db.Clientes.lista]

#Buscamos a partir del dni
@app.get("/clientes/buscar/{dni}/")
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    headers = {"content-type": "charset=utf-8"}
    return JSONResponse(content=cliente.to_dict(), headers=headers)

