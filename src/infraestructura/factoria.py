# Path: src/infraestructura/factoria.py

from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto
from src.adaptadores.pasarelas.pasarela_google_maps import PasarelaGoogleMaps
from src.adaptadores.presentadores.presentador_presupuesto import PresentadorPresupuesto
from src.adaptadores.controladores.controlador_presupuestador import ControladorPresupuestador
from src.infraestructura.configuracion.ajustes import Configuracion
from src.infraestructura.configuracion.registro import AdaptadorRegistro

class FactoriaServicios:
    @staticmethod
    def crear_controlador_presupuestador() -> ControladorPresupuestador:
        config = Configuracion()
        logger = AdaptadorRegistro("PasarelaGoogleMaps")
        
        pasarela = PasarelaGoogleMaps(
            api_key=config.api_key_google_maps,
            logger=logger
        )
        
        caso_uso = CalcularPresupuesto(pasarela)
        presentador = PresentadorPresupuesto()
        return ControladorPresupuestador(caso_uso, presentador)
