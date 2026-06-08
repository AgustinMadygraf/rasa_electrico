from src.dominio.interfaces.proveedor_distancia import IProveedorDistancia
from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto
from src.aplicacion.dtos.entrada_presupuesto import EntradaPresupuesto
from src.dominio.excepciones import ErrorInfraestructura
import pytest

# Dummy config
CONFIG = {
    "costos_produccion": {"factor_distancia": 50.0, "mano_de_obra": 500.0, "materiales_base": 200.0, "costo_gestion_compra": 1500.0},
    "costos_operativos": {"logistica": 150.0, "depreciacion": 100.0},
    "objetivos_financieros": {"utilidad_neta_porcentaje": 0.2}
}

class MockDistanceProvider(IProveedorDistancia):
    def obtener_distancia(self, origen: str, destino: str) -> float:
        return 10.0

class ErrorDistanceProvider(IProveedorDistancia):
    def obtener_distancia(self, origen: str, destino: str) -> float:
        raise ErrorInfraestructura("Fallo en la API")

def test_calcular_presupuesto_exitoso():
    proveedor = MockDistanceProvider()
    caso_uso = CalcularPresupuesto(proveedor, CONFIG)
    entrada = EntradaPresupuesto(direccion="Calle Falsa 123", cliente_proporciona_materiales=False)
    presupuesto = caso_uso.ejecutar(entrada)
    assert presupuesto.costo_total > 0

def test_calcular_presupuesto_fallido():
    proveedor = ErrorDistanceProvider()
    caso_uso = CalcularPresupuesto(proveedor, CONFIG)
    entrada = EntradaPresupuesto(direccion="Calle Falsa 123", cliente_proporciona_materiales=False)
    with pytest.raises(ErrorInfraestructura):
        caso_uso.ejecutar(entrada)
