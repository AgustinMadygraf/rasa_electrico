# Path: src/infraestructura/fastapi/schemas.py

from pydantic import BaseModel

class PresupuestoRequest(BaseModel):
    direccion: str
    cliente_proporciona_materiales: bool
