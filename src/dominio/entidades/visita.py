# Path: src/dominio/entidades/visita.py

from dataclasses import dataclass
from typing import Text, Dict
from datetime import datetime

@dataclass
class Visita:
    fecha_hora: datetime
    direccion_destino: Text
    
    def calcular_costo_traslado(self, costo_base_traslado: float, config_nocturnidad: Dict) -> float:
        recargo = config_nocturnidad['recargo']
        h_inicio = config_nocturnidad['hora_inicio']
        h_fin = config_nocturnidad['hora_fin']
        
        # Lógica basada en configuración externa
        es_nocturno = self.fecha_hora.hour >= h_inicio or self.fecha_hora.hour < h_fin
        factor = recargo if es_nocturno else 1.0
        return costo_base_traslado * factor
