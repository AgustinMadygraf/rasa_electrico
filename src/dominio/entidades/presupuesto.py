# Path: src/dominio/entidades/presupuesto.py

from typing import Any, Text, Dict
from dataclasses import dataclass
from src.dominio.entidades.trabajo import Trabajo
from src.dominio.entidades.visita import Visita

@dataclass
class Presupuesto:
    costo_total: float
    distancia: float
    origen: Text
    destino: Text
    desglose_costos: Dict[Text, float]

    @classmethod
    def calcular(cls, trabajo: Trabajo, visita: Visita, 
                 distancia: float, config: Dict[Text, Any]) -> 'Presupuesto':
        
        # 1. Costo Base y Lógica
        logistica_base = config['costos_operativos']['logistica']
        base = config['costos_operativos']['costo_base_fijo'] + (distancia * config['costos_produccion'].get('factor_distancia', 50.0))
        
        # 2. Uso de lógica encapsulada en entidades
        costo_traslado = visita.calcular_costo_traslado(logistica_base, config['nocturnidad'])
        
        # 3. Mano de Obra ajustada por complejidad
        mano_de_obra = config['costos_produccion']['mano_de_obra'] * trabajo.factor_complejidad
        
        # 4. Otros costos
        costo_materiales = config['costos_produccion']['materiales_base']
        cargo_gestion = config['costos_produccion']['costo_gestion_compra']
        depreciacion = config['costos_operativos']['depreciacion']
            
        # 5. Total antes de ganancia
        subtotal = base + costo_traslado + costo_materiales + cargo_gestion + mano_de_obra + depreciacion
        
        # 6. Aplicar ganancia
        ganancia = subtotal * config['objetivos_financieros']['utilidad_neta_porcentaje']
        costo_total = subtotal + ganancia
        
        desglose: Dict[Text, float] = {
            "base": float(base),
            "logistica": float(costo_traslado),
            "materiales": float(costo_materiales),
            "gestion_compra": float(cargo_gestion),
            "mano_de_obra": float(mano_de_obra),
            "depreciacion": float(depreciacion),
            "ganancia": float(ganancia)
        }
        
        return cls(costo_total=float(costo_total), distancia=float(distancia), origen=config['costos_operativos']['origen_base'], 
                   destino=visita.direccion_destino, desglose_costos=desglose)
