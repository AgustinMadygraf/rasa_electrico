# Path: src/dominio/entidades/trabajo.py

from dataclasses import dataclass
from typing import Text, Dict

@dataclass
class Trabajo:
    categoria: Text
    descripcion: Text
    factor_complejidad: float
    
    @classmethod
    def crear_con_factor(cls, categoria: Text, descripcion: Text, factores: Dict[Text, float]) -> 'Trabajo':
        factor = factores.get(categoria, 1.0)
        return cls(categoria=categoria, descripcion=descripcion, factor_complejidad=factor)
