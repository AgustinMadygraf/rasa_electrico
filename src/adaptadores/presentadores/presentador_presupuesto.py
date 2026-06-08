# Path: src/adaptadores/presentadores/presentador_presupuesto.py

from typing import Dict, Text
from src.dominio.entidades.presupuesto import Presupuesto
from src.aplicacion.puertos.i_presentador_presupuesto import IPresentadorPresupuesto

class PresentadorPresupuesto(IPresentadorPresupuesto):
    def formatear(self, presupuesto: Presupuesto) -> Dict[Text, Text]:
        return {
            "mensaje": f"Presupuesto estimado: ${presupuesto.costo_total}. (Distancia calculada: {presupuesto.distancia} km desde {presupuesto.origen})"
        }
        
    def formatear_error(self, mensaje: Text) -> Dict[Text, Text]:
        return {
            "mensaje": f"Lo siento, hubo un problema al calcular tu presupuesto: {mensaje}"
        }
