# Path: src/aplicacion/casos_de_uso/calcular_presupuesto.py

from typing import Dict, Any, Text
from src.dominio.interfaces.proveedor_distancia import IProveedorDistancia
from src.dominio.entidades.presupuesto import Presupuesto

class CalcularPresupuesto:
    def __init__(self, proveedor_distancia: IProveedorDistancia):
        self.proveedor_distancia = proveedor_distancia
        self.origen_base = "Garín, Gran Buenos Aires Norte"

    def ejecutar(self, direccion_destino: Text) -> Dict[Text, Any]:
        distancia = self.proveedor_distancia.obtener_distancia(self.origen_base, direccion_destino)
        
        # Uso de la Entidad de Dominio para calcular
        presupuesto = Presupuesto.calcular(distancia, self.origen_base, direccion_destino)
        
        return {'costo_total': presupuesto.costo_total, 'distancia': presupuesto.distancia}
