from typing import Text, Dict, Any
from src.dominio.interfaces.proveedor_distancia import IProveedorDistancia
from src.dominio.entidades.presupuesto import Presupuesto
from src.aplicacion.dtos.entrada_presupuesto import EntradaPresupuesto

class CalcularPresupuesto:
    def __init__(self, proveedor_distancia: IProveedorDistancia, config: Dict[Text, Any]):
        self.proveedor_distancia = proveedor_distancia
        self.origen_base = "Garín, Gran Buenos Aires Norte"
        self.config = config

    def ejecutar(self, entrada: EntradaPresupuesto) -> Presupuesto:
        distancia = self.proveedor_distancia.obtener_distancia(self.origen_base, entrada.direccion)
        return Presupuesto.calcular(
            distancia, 
            self.origen_base, 
            entrada.direccion,
            entrada.cliente_proporciona_materiales,
            self.config
        )
