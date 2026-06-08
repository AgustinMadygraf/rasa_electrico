# Path: src/infraestructura/fastapi/dependencias.py

from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto

def get_caso_uso() -> CalcularPresupuesto:
    raise NotImplementedError("Debe ser inyectado por el Composition Root")
