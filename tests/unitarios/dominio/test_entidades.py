from src.dominio.entidades.presupuesto import Presupuesto

def test_calculo_presupuesto_entidad():
    config = {
        "costos_produccion": {"factor_distancia": 50.0, "mano_de_obra": 500.0, "materiales_base": 200.0, "costo_gestion_compra": 1500.0},
        "costos_operativos": {"logistica": 150.0, "depreciacion": 100.0},
        "objetivos_financieros": {"utilidad_neta_porcentaje": 0.2}
    }
    presupuesto = Presupuesto.calcular(10.0, "Origen", "Destino", False, config)
    # 1000 + (10*50) + 150 + 200 + 1500 + 500 + 100 = 3950
    # + 20% (790) = 4740
    assert presupuesto.costo_total == 4740.0
