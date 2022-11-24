from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import database as db

headers = {"content-type": "charset=utf-8"}

app = FastAPI()

@app.delete("/clientes/borrar/{dni}/")
async def clientes_borrar(dni: str):
    if db.Clientes.buscar(dni=dni):
        cliente = db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404)