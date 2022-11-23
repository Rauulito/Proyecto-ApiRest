
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def index():
    content = {'mensaje': '¡Hola mundo!'}
    return JSONResponse(content=content)

# headers = {"content-type": "charset=utf-8"}
    
# @app.get("/")
# async def index():
#     content = {'mensaje': '¡Hola mundo!'}
#     return JSONResponse(content=content, headers=headers)

print("Servidor de la API...")