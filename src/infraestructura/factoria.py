from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto
from src.adaptadores.pasarelas.pasarela_google_maps import PasarelaGoogleMaps
from src.adaptadores.presentadores.presentador_presupuesto import PresentadorPresupuesto
from src.adaptadores.controladores.controlador_presupuestador import ControladorPresupuestador
from src.infraestructura.configuracion.ajustes import Configuracion
from src.infraestructura.configuracion.registro import AdaptadorRegistro
from src.infraestructura.configuracion.lector_json import LectorConfiguracionJson

class FactoriaServicios:
    @staticmethod
    def _crear_caso_uso_base():
        config = Configuracion()
        registro = AdaptadorRegistro("PasarelaGoogleMaps")
        
        datos_presupuesto = LectorConfiguracionJson.leer('data/configuracion_presupuesto.json')
        
        pasarela = PasarelaGoogleMaps(
            api_key=config.api_key_google_maps,
            logger=registro
        )
        return CalcularPresupuesto(pasarela, datos_presupuesto)

    @staticmethod
    def crear_controlador_presupuestador() -> ControladorPresupuestador:
        caso_uso = FactoriaServicios._crear_caso_uso_base()
        presentador = PresentadorPresupuesto()
        return ControladorPresupuestador(caso_uso, presentador)

    @staticmethod
    def crear_caso_uso_presupuesto() -> CalcularPresupuesto:
        return FactoriaServicios._crear_caso_uso_base()
