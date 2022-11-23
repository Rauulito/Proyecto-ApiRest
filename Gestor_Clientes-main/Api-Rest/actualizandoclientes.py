

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import database as db

headers = {"content-type": "charset=utf-8"}

class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)


@ app.put("/clientes/actualizar/", tags=["Clientes"])
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404)

{
  "dni": "15J",
  "nombre": "Victoria",
  "apellido": "Pérez"
}

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