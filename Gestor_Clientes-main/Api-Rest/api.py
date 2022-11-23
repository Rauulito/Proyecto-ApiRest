
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


app = FastAPI(
    title="API del Gestor de clientes",
    description="Ofrece diferentes funciones para gestionar los clientes.")


print("Servidor de la API...")

