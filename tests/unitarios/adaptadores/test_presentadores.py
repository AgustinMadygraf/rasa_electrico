from src.adaptadores.presentadores.presentador_presupuesto import PresentadorPresupuesto
from src.dominio.entidades.presupuesto import Presupuesto

def test_presentador_formatear():
    presentador = PresentadorPresupuesto()
    desglose = {
        "base": 1000.0, "mano_de_obra": 500.0, "materiales": 200.0,
        "gestion_compra": 1500.0, "logistica": 150.0, "depreciacion": 100.0, "ganancia": 690.0
    }
    presupuesto = Presupuesto(costo_total=4140.0, distancia=10.0, origen="Origen", destino="Destino", desglose_costos=desglose)
    resultado = presentador.formatear(presupuesto)
    assert "mensaje" in resultado
    assert "Mano de obra" in resultado["mensaje"]
    assert "4,140.00" in resultado["mensaje"]

def test_presentador_formatear_error():
    presentador = PresentadorPresupuesto()
    resultado = presentador.formatear_error("Error crítico")
    assert "mensaje" in resultado
    assert "Error crítico" in resultado["mensaje"]
