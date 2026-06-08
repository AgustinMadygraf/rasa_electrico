# Path: src/aplicacion/puertos/i_presentador_presupuesto.py

from typing import Dict, Text, Protocol
from src.dominio.entidades.presupuesto import Presupuesto

class IPresentadorPresupuesto(Protocol):
    def formatear(self, presupuesto: Presupuesto) -> Dict[Text, Text]:
        ...
    def formatear_error(self, mensaje: Text) -> Dict[Text, Text]:
        ...
