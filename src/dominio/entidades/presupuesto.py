# Path: src/dominio/entidades/presupuesto.py

from typing import Any
from dataclasses import dataclass
from typing import Text, Dict

@dataclass
class Presupuesto:
    costo_total: float
    distancia: float
    origen: Text
    destino: Text
    desglose_costos: Dict[Text, float]

    @classmethod
    def calcular(cls, distancia: float, origen: Text, destino: Text, 
                 cliente_proporciona_materiales: bool, 
                 config: Dict[Text, Any]) -> 'Presupuesto':
        
        # 1. Costo Base (Logística + Distancia)
        logistica = config['costos_operativos']['logistica']
        base = 1000 + (distancia * config['costos_produccion'].get('factor_distancia', 50.0))
        
        # 2. Costo Materiales
        costo_materiales = 0.0
        cargo_gestion = 0.0
        if not cliente_proporciona_materiales:
            costo_materiales = config['costos_produccion']['materiales_base']
            cargo_gestion = config['costos_produccion']['costo_gestion_compra']
            
        # 3. Mano de Obra, Depreciación
        mano_de_obra = config['costos_produccion']['mano_de_obra']
        depreciacion = config['costos_operativos']['depreciacion']
        
        # 4. Total antes de ganancia
        subtotal = base + logistica + costo_materiales + cargo_gestion + mano_de_obra + depreciacion
        
        # 5. Aplicar ganancia
        ganancia = subtotal * config['objetivos_financieros']['utilidad_neta_porcentaje']
        costo_total = subtotal + ganancia
        
        desglose = {
            "base": base,
            "logistica": logistica,
            "materiales": costo_materiales,
            "gestion_compra": cargo_gestion,
            "mano_de_obra": mano_de_obra,
            "depreciacion": depreciacion,
            "ganancia": ganancia
        }
        
        return cls(costo_total=costo_total, distancia=distancia, origen=origen, destino=destino, desglose_costos=desglose)
