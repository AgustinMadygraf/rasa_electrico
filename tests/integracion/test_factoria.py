from src.infraestructura.factoria import FactoriaServicios
from src.adaptadores.controladores.controlador_presupuestador import ControladorPresupuestador

def test_creacion_controlador():
    controlador = FactoriaServicios.crear_controlador_presupuestador()
    assert isinstance(controlador, ControladorPresupuestador)
