# Path: src/dominio/excepciones.py

class ErrorDominio(Exception):
    pass

class ErrorInfraestructura(ErrorDominio):
    pass

class ErrorCalculoPresupuesto(ErrorDominio):
    pass
