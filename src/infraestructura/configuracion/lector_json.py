# Path: src/infraestructura/configuracion/lector_json.py

import json
from typing import Dict, Any

class LectorConfiguracionJson:
    @staticmethod
    def leer(ruta: str) -> Dict[str, Any]:
        with open(ruta, 'r') as f:
            return json.load(f)
