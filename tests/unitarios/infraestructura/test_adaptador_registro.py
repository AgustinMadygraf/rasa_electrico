import logging
from src.infraestructura.configuracion.registro import AdaptadorRegistro

def test_adaptador_registro():
    adaptador = AdaptadorRegistro("TestLogger")
    adaptador.info("Mensaje de info")
    adaptador.error("Mensaje de error")
    assert isinstance(adaptador, AdaptadorRegistro)
