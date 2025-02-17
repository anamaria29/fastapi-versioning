#tarea
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

api = FastAPI(
    title= 'Tarea 2'
)

usuarios = []  # Lista para almacenar los usuarios temporalmente

@api.post("/user")
async def crear_usuario(nombre: str):
    usuario = {"nombre": nombre}
    usuarios.append(usuario)
    return {"mensaje": "Usuario guardado", "usuario": usuario}

@api.get("/user")
async def obtener_usuario():
    if usuarios:
        return {"usuarios": usuarios}
    return {"mensaje": "No hay usuarios guardados"}
