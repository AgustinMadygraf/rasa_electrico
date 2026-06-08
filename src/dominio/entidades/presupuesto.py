# Path: src/dominio/entidades/presupuesto.py

from dataclasses import dataclass
from typing import Text

@dataclass
class Presupuesto:
    costo_total: float
    distancia: float
    origen: Text
    destino: Text

    @classmethod
    def calcular(cls, distancia: float, origen: Text, destino: Text) -> 'Presupuesto':
        # Regla de negocio encapsulada en la entidad
        costo_total = 1000 + (distancia * 50)
        return cls(costo_total=costo_total, distancia=distancia, origen=origen, destino=destino)
