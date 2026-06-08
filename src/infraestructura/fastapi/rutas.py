# Path: src/infraestructura/fastapi/rutas.py

from fastapi import APIRouter, Depends
from src.infraestructura.fastapi.schemas import PresupuestoRequest
from src.infraestructura.fastapi.dependencias import get_caso_uso
from src.adaptadores.controladores.controlador_api import ControladorApi
from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto

router = APIRouter()

@router.post("/presupuesto")
async def calcular_presupuesto(
    request: PresupuestoRequest,
    caso_uso: CalcularPresupuesto = Depends(get_caso_uso)
):
    controlador = ControladorApi(caso_uso)
    return controlador.calcular_presupuesto(
        request.direccion, 
        request.cliente_proporciona_materiales
    )

@router.get("/")
async def root():
    return {"status": "Rasa Eléctrico API - Online", "version": "1.0.0"}
