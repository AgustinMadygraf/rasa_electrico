# Path: src/infraestructura/fastapi/app.py

from fastapi import FastAPI
from src.infraestructura.fastapi.rutas import router

app = FastAPI(title="Rasa Eléctrico API")
app.include_router(router)
