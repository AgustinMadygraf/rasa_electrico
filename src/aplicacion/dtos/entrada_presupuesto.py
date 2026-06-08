from dataclasses import dataclass
from typing import Text

@dataclass(frozen=True)
class EntradaPresupuesto:
    direccion: Text
    cliente_proporciona_materiales: bool
