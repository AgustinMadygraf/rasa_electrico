from src.dominio.interfaces.proveedor_distancia import IProveedorDistancia
from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto
from src.dominio.excepciones import ErrorInfraestructura
import pytest

class MockDistanceProvider(IProveedorDistancia):
    def obtener_distancia(self, origen: str, destino: str) -> float:
        return 10.0

class ErrorDistanceProvider(IProveedorDistancia):
    def obtener_distancia(self, origen: str, destino: str) -> float:
        raise ErrorInfraestructura("Fallo en la API")

def test_calcular_presupuesto_exitoso():
    proveedor = MockDistanceProvider()
    caso_uso = CalcularPresupuesto(proveedor)
    presupuesto = caso_uso.ejecutar("Calle Falsa 123")
    assert presupuesto.costo_total == 1500

def test_calcular_presupuesto_fallido():
    proveedor = ErrorDistanceProvider()
    caso_uso = CalcularPresupuesto(proveedor)
    with pytest.raises(ErrorInfraestructura):
        caso_uso.ejecutar("Calle Falsa 123")
