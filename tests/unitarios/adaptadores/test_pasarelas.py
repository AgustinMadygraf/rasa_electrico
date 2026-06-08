import logging
from src.adaptadores.pasarelas.pasarela_google_maps import PasarelaGoogleMaps
from src.dominio.interfaces.i_logger import ILogger

class MockLogger(ILogger):
    def info(self, mensaje): pass
    def error(self, mensaje): pass

def test_pasarela_google_maps():
    logger = MockLogger()
    pasarela = PasarelaGoogleMaps(api_key="TEST_KEY", logger=logger)
    distancia = pasarela.obtener_distancia("Origen", "Destino")
    assert distancia == 15.5
