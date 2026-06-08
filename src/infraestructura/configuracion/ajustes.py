# Path: src/infraestructura/configuracion/ajustes.py  

import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# Carga las variables del archivo .env si existe
load_dotenv()

class Configuracion:
    @property
    def api_key_google_maps(self) -> str:
        # Si no se encuentra la variable, devuelve un valor por defecto o levanta un error
        return os.getenv("GOOGLE_MAPS_API_KEY", "MOCK_KEY_DESDE_CONFIG")
