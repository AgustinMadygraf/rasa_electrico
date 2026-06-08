# Path: src/dominio/interfaces/proveedor_distancia.py

from abc import ABC, abstractmethod
from typing import Text

class IProveedorDistancia(ABC):
    @abstractmethod
    def obtener_distancia(self, origen: Text, destino: Text) -> float:
        pass
