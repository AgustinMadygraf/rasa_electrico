# Presupuestador Eléctrico ⚡

Este proyecto es un chatbot basado en el framework **Rasa (3.1+)** diseñado como **asistente presupuestador para instalaciones eléctricas**.

El bot guía a los usuarios en la definición de sus proyectos eléctricos y genera estimaciones de costos iniciales.

## 🚀 Inicio Rápido

### Requisitos Previos
- **Python 3.10** (Ver [Instalación](docs/INSTALLING.md))
- **venv**

### Instalación y Ejecución
El proyecto incluye un script de automatización `run.sh` para facilitar las tareas comunes.

1. **Entrenar el modelo:**
   ```bash
   ./run.sh train
   ```

2. **Interactuar en consola:**
   ```bash
   ./run.sh shell
   ```

3. **Ejecutar servidor API (con servidor de acciones):**
   ```bash
   ./run.sh
   ```

## 📂 Estructura del Proyecto

- `actions/`: Lógica para el cálculo de presupuestos (Action Server).
- `data/`: Datos de entrenamiento (intenciones de presupuesto, historias de flujo).
- `domain.yml`: Definición de slots para datos del proyecto (tipo de instalación, metros cuadrados, etc.).
- `run.sh`: Script de utilidad para gestión del bot.

## 🛠️ Desarrollo

### Agregar funcionalidades de presupuesto
1. Define los datos necesarios (slots) en `domain.yml`.
2. Crea las historias de flujo de entrevista en `data/stories.yml`.
3. Implementa la lógica de cálculo en `actions/actions.py`.
4. Entrena y prueba: `./run.sh train && ./run.sh shell`.

---
Para más detalles sobre la arquitectura, consulta [Arquitectura](docs/ARCHITECTURE.md).
Para instrucciones detalladas de instalación, consulta [Instalación](docs/INSTALLING.md).
