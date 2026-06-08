# Path: actions/actions.py

from typing import Any, Text, List, Dict
from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore
from rasa_sdk.types import DomainDict  # type: ignore
from src.infraestructura.factoria import FactoriaServicios

class AccionPresupuestar(Action):
    def __init__(self):
        # La acción orquesta la obtención de dependencias
        controlador = FactoriaServicios.crear_controlador_presupuestador()
        self.controlador = controlador

    def name(self) -> Text:
        return 'action_calcular_presupuesto'

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: DomainDict) -> List[Dict[Text, Any]]:

        direccion = tracker.get_slot('direccion_trabajo')
        
        if not direccion:
            dispatcher.utter_message(text='Lo siento, no he recibido la dirección del lugar de trabajo.')
            return []

        resultado = self.controlador.calcular(direccion)

        mensaje = f"Presupuesto estimado: ${resultado['mensaje']}"
        dispatcher.utter_message(text=mensaje)

        return []
