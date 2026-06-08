# Path: src/adaptadores/controladores/controlador_api.py

from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto
from src.aplicacion.dtos.entrada_presupuesto import EntradaPresupuesto

class ControladorApi:
    def __init__(self, caso_uso: CalcularPresupuesto):
        self.caso_uso = caso_uso

    def calcular_presupuesto(self, direccion: str, cliente_proporciona_materiales: bool):
        entrada = EntradaPresupuesto(
            direccion=direccion,
            cliente_proporciona_materiales=cliente_proporciona_materiales
        )
        presupuesto = self.caso_uso.ejecutar(entrada)
        
        return {
            "costo_total": presupuesto.costo_total,
            "desglose": presupuesto.desglose_costos
        }
