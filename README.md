# Presupuestador Eléctrico ⚡

Este proyecto es un chatbot basado en el framework **Rasa (3.1+)** diseñado como **asistente presupuestador para instalaciones eléctricas**.

El bot guía a los usuarios en la definición de sus proyectos eléctricos desde el saludo inicial, solicitando la ubicación del trabajo para generar estimaciones de costos.

## 🚀 Inicio Rápido

### Requisitos Previos
- **Python 3.10**
- **venv**

### Instalación y Ejecución

1. **Entrenar el modelo:**
   ```bash
   rasa train
   ```

2. **Interactuar en consola:**
   ```bash
   rasa run actions &
   rasa shell
   ```

3. **Ejecutar servidor API:**
   ```bash
   rasa run --enable-api --cors "*"
   ```

## 📂 Estructura del Proyecto

- `actions/`: Lógica para el cálculo de presupuestos (Action Server).
- `data/`: Datos de entrenamiento (intenciones de presupuesto, historias de flujo).
- `domain.yml`: Definición de slots para datos del proyecto.

## 🛠️ Desarrollo

### Agregar funcionalidades de presupuesto
1. Define los datos necesarios (slots) en `domain.yml`.
2. Crea las historias de flujo de entrevista en `data/stories.yml`.
3. Implementa la lógica de cálculo en `actions/actions.py`.
4. Entrena y prueba: `rasa train && rasa shell`.

---
Para más detalles sobre la arquitectura, consulta [Arquitectura](docs/ARCHITECTURE.md).
Para instrucciones detalladas de instalación, consulta [Instalación](docs/INSTALLING.md).
