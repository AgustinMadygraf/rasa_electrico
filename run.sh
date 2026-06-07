#!/bin/bash

# --- Configuración ---
VENV_DIR=".venv"
PORT=5005
ACTION_PORT=5055

# Colores para la terminal
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m" # No Color

log() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# --- Limpieza al salir ---
cleanup() {
    log "Deteniendo procesos..."
    # Matar procesos en segundo plano del grupo de este script
    kill $(jobs -p) 2>/dev/null
    exit
}
trap cleanup SIGINT SIGTERM

# --- 1. Liberar puertos ---
free_port() {
    local port=$1
    local pid=$(lsof -t -i:"$port")
    if [ ! -z "$pid" ]; then
        warn "Liberando puerto $port (PID: $pid)..."
        kill -9 "$pid"
        sleep 0.5
    fi
}

free_port $PORT
free_port $ACTION_PORT

# --- 2. Entorno Virtual ---
if [ ! -d "$VENV_DIR" ]; then
    warn "Entorno virtual no encontrado. Creándolo..."
    python3 -m venv "$VENV_DIR" || { error "No se pudo crear el venv"; exit 1; }
fi

source "$VENV_DIR/bin/activate" || { error "No se pudo activar el venv"; exit 1; }

# --- 3. Dependencias ---
if ! command -v rasa &> /dev/null; then
    warn "Rasa no instalado. Instalando requerimientos..."
    pip install --upgrade pip
    pip install -r requirements.txt || { error "Fallo en la instalación"; exit 1; }
fi

# --- 4. Ejecución ---
case "$1" in
    train)
        log "Entrenando modelo..."
        rasa train
        ;;
    shell)
        log "Iniciando Rasa Shell..."
        rasa run actions &
        sleep 2
        rasa shell
        ;;
    *)
        log "Iniciando Rasa y Servidor de Acciones..."
        # Iniciar servidor de acciones en segundo plano
        rasa run actions --log-file out_actions.log &
        # Iniciar Rasa server
        rasa run --enable-api --cors "*"
        ;;
esac