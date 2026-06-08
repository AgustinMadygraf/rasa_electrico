# Path: src/adaptadores/pasarelas/pasarela_google_maps.py

from typing import Text
from src.dominio.interfaces.proveedor_distancia import IProveedorDistancia
from src.dominio.interfaces.i_logger import ILogger
from src.dominio.excepciones import ErrorInfraestructura

class PasarelaGoogleMaps(IProveedorDistancia):
    def __init__(self, api_key: Text, logger: ILogger):
        self.api_key = api_key
        self.logger = logger

    def obtener_distancia(self, origen: Text, destino: Text) -> float:
        self.logger.info(f"Calculando distancia entre {origen} y {destino} mediante Google Maps.")
        
        # Simulación de fallo técnico
        if self.api_key == "INVALID":
            self.logger.error("Error al conectar con Google Maps: API Key inválida")
            raise ErrorInfraestructura("No se pudo conectar con el servicio de mapas.")
            
        return 15.5
