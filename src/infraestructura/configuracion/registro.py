# Path: src/infraestructura/configuracion/registro.py

import logging
from typing import Text
from src.dominio.interfaces.i_logger import ILogger

class AdaptadorRegistro(ILogger):
    def __init__(self, nombre: Text):
        self._logger = logging.getLogger(nombre)
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)
            self._logger.setLevel(logging.INFO)

    def info(self, mensaje: Text) -> None:
        self._logger.info(mensaje)

    def error(self, mensaje: Text) -> None:
        self._logger.error(mensaje)
