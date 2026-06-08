# Path: src/aplicacion/casos_de_uso/calcular_presupuesto.py

from typing import Text
from src.dominio.interfaces.proveedor_distancia import IProveedorDistancia
from src.dominio.entidades.presupuesto import Presupuesto

class CalcularPresupuesto:
    def __init__(self, proveedor_distancia: IProveedorDistancia):
        self.proveedor_distancia = proveedor_distancia
        self.origen_base = "Garín, Gran Buenos Aires Norte"

    def ejecutar(self, direccion_destino: Text) -> Presupuesto:
        distancia = self.proveedor_distancia.obtener_distancia(self.origen_base, direccion_destino)
        return Presupuesto.calcular(distancia, self.origen_base, direccion_destino)
