from src.dominio.entidades.presupuesto import Presupuesto

def test_calculo_presupuesto_entidad():
    presupuesto = Presupuesto.calcular(10.0, "Origen", "Destino")
    assert presupuesto.costo_total == 1500
    assert presupuesto.distancia == 10.0
