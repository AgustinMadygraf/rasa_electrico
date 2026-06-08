# Path: src/adaptadores/controladores/controlador_presupuestador.py

from typing import Text, Dict
from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto
from src.aplicacion.puertos.i_presentador_presupuesto import IPresentadorPresupuesto
from src.dominio.excepciones import ErrorDominio

class ControladorPresupuestador:
    def __init__(self, caso_de_uso: CalcularPresupuesto, presentador: IPresentadorPresupuesto):
        self.caso_de_uso = caso_de_uso
        self.presentador = presentador

    def calcular(self, direccion: Text) -> Dict[Text, Text]:
        try:
            presupuesto = self.caso_de_uso.ejecutar(direccion)
            return self.presentador.formatear(presupuesto)
        except ErrorDominio as e:
            return self.presentador.formatear_error(str(e))
    
    @property
    def origen_base(self) -> Text:
        return self.caso_de_uso.origen_base
