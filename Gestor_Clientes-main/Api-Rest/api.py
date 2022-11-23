
from fastapi import FastAPI,Response,HTTPException
from fastapi.responses import JSONResponse
import database as db
from pydantic import BaseModel, constr, validator
import helpers

app = FastAPI()

#-----------------1ero-----------------#
@app.get("/")
async def index():
    content = {'mensaje': '¡Hola mundo!'}
    return JSONResponse(content=content)


#-----------------2do-----------------#
headers = {"content-type": "charset=utf-8"}
    
@app.get("/")
async def index():
    content = {'mensaje': '¡Hola mundo!'}
    return JSONResponse(content=content, headers=headers)


@app.get("/html/")
def html():
    content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>¡Hola mundo!</title>
    </head>
    <body>
        <h1>¡Hola mundo!</h1>
    </body>
    </html>
    """
    return Response(content=content, media_type="text/html")



@app.get("/clientes/", tags=["Clientes"])
async def clientes():
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)

@app.get("/clientes/buscar/{dni}/", tags=["Clientes"])
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(content=cliente.to_dict(), headers=headers)


print("Servidor de la API...")