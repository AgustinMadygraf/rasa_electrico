from src.adaptadores.presentadores.presentador_presupuesto import PresentadorPresupuesto
from src.dominio.entidades.presupuesto import Presupuesto

def test_presentador_formatear():
    presentador = PresentadorPresupuesto()
    presupuesto = Presupuesto(costo_total=1500.0, distancia=10.0, origen="Origen", destino="Destino")
    resultado = presentador.formatear(presupuesto)
    assert "mensaje" in resultado
    assert "1500" in resultado["mensaje"]

def test_presentador_formatear_error():
    presentador = PresentadorPresupuesto()
    resultado = presentador.formatear_error("Error crítico")
    assert "mensaje" in resultado
    assert "Error crítico" in resultado["mensaje"]
