from src.adaptadores.controladores.controlador_presupuestador import ControladorPresupuestador
from src.aplicacion.casos_de_uso.calcular_presupuesto import CalcularPresupuesto
from src.adaptadores.presentadores.presentador_presupuesto import PresentadorPresupuesto
from src.dominio.interfaces.proveedor_distancia import IProveedorDistancia
from src.dominio.excepciones import ErrorInfraestructura
from src.dominio.entidades.presupuesto import Presupuesto

class MockDistanceProvider(IProveedorDistancia):
    def obtener_distancia(self, origen: str, destino: str) -> float:
        return 10.0

class ErrorDistanceProvider(IProveedorDistancia):
    def obtener_distancia(self, origen: str, destino: str) -> float:
        raise ErrorInfraestructura("Fallo en la API")

def test_controlador_exito():
    proveedor = MockDistanceProvider()
    caso_uso = CalcularPresupuesto(proveedor)
    presentador = PresentadorPresupuesto()
    controlador = ControladorPresupuestador(caso_uso, presentador)
    
    resultado = controlador.calcular("Calle Falsa 123")
    assert "mensaje" in resultado
    assert "Presupuesto estimado" in resultado["mensaje"]

def test_controlador_maneja_error():
    proveedor = ErrorDistanceProvider()
    caso_uso = CalcularPresupuesto(proveedor)
    presentador = PresentadorPresupuesto()
    controlador = ControladorPresupuestador(caso_uso, presentador)
    
    resultado = controlador.calcular("Calle Falsa 123")
    assert "mensaje" in resultado
    assert "Lo siento" in resultado["mensaje"]
