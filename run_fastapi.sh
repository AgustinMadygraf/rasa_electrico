#!/bin/bash

# 1. Liberar el puerto 8000 si está ocupado
echo "Liberando puerto 8000..."
fuser -k 8000/tcp > /dev/null 2>&1

# 2. Activar el entorno virtual
source .venv/bin/activate

# 3. Ejecutar el servidor
echo "Iniciando servidor en puerto 8000..."
python -m uvicorn src.infraestructura.fastapi.app:app --reload --host 127.0.0.1 --port 8000
