import contextlib
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import helpers
import database as db

app = FastAPI()

class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)

#dni funcion especial
class ModeloCrearCliente(ModeloCliente):
    @validator("dni")
    def validar_dni(cls, dni):
        if not helpers.dni_valido(dni, db.Clientes.lista):
            raise ValueError("Cliente ya existente o DNI incorrecto")
        return dni

#recuperamos los datos de la petición POST y crear el cliente
@app.post("/clientes/crear/")
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        headers = {"content-type": "charset=utf-8"}
        return JSONResponse(content=contextlib.to_dict(), headers=headers)
    raise HTTPException(status_code=404)

{"dni":"36N","nombre":"Fernando","apellido":"López"}

{
"detail": [
    {
    "loc": [
        "body",
        "dni"
    ],
    "msg": "ensure this value has at least 3 characters",
    "type": "value_error.any_str.min_length",
    "ctx": {
        "limit_value": 3
    }
    },
    {
    "loc": [
        "body",
        "nombre"
    ],
    "msg": "ensure this value has at least 2 characters",
    "type": "value_error.any_str.min_length",
    "ctx": {
        "limit_value": 2
    }
    },
    {
    "loc": [
        "body",
        "apellido"
    ],
    "msg": "ensure this value has at least 2 characters",
    "type": "value_error.any_str.min_length",
    "ctx": {
        "limit_value": 2
    }
    }
]
}

{
"detail": [
    {
    "loc": [
        "body",
        "dni"
    ],
    "msg": "Cliente ya existente o DNI incorrecto",
    "type": "value_error"
    }
]
}
