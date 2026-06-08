from typing import Dict, Text
from src.dominio.entidades.presupuesto import Presupuesto
from src.aplicacion.puertos.i_presentador_presupuesto import IPresentadorPresupuesto

class PresentadorPresupuesto(IPresentadorPresupuesto):
    def formatear(self, presupuesto: Presupuesto) -> Dict[Text, Text]:
        d = presupuesto.desglose_costos
        mensaje = (
            f"Presupuesto estimado: ${presupuesto.costo_total:,.2f}\n"
            f"- Base: ${d['base']:,.2f}\n"
            f"- Mano de obra: ${d['mano_de_obra']:,.2f}\n"
            f"- Materiales: ${d['materiales']:,.2f}\n"
            f"- Gestión compra: ${d['gestion_compra']:,.2f}\n"
            f"- Logística: ${d['logistica']:,.2f}\n"
            f"- Depreciación: ${d['depreciacion']:,.2f}\n"
            f"- Ganancia: ${d['ganancia']:,.2f}"
        )
        return {"mensaje": mensaje}
        
    def formatear_error(self, mensaje: Text) -> Dict[Text, Text]:
        return {
            "mensaje": f"Lo siento, hubo un problema al calcular tu presupuesto: {mensaje}"
        }
