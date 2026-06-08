# Instrucciones para Agentes Gemini

Este archivo contiene las directrices para agentes de IA que operen en este repositorio.

## Convenciones de Desarrollo
- **Framework:** Rasa 3.1+.
- **Lenguaje:** Python 3.10.
- **Formato de Datos:** YAML para configuración y datos de entrenamiento.

## Flujo de Trabajo Recomendado
1. **Investigación:** Antes de proponer cambios en NLU o Historias, analizar el `domain.yml` para asegurar consistencia en los nombres de intenciones y acciones.
2. **Validación:** Siempre que se modifiquen archivos de `data/`, se debe sugerir al usuario ejecutar `./run.sh train` para validar la integridad del modelo.
3. **Acciones:** Las acciones personalizadas deben seguir el patrón de Rasa SDK y estar documentadas en el docstring de la clase.

## Comandos Críticos
- `./run.sh train`: Reentrenar el bot.
- `./run.sh shell`: Probar cambios interactivamente.
- `rasa data validate`: Verificar la consistencia de los archivos de entrenamiento.

## Estándares de Código
- Seguir PEP 8 para archivos en `actions/`.
- Mantener las historias cortas y modulares para evitar ambigüedades en el diálogo.
- Usar respuestas (`utter_...`) en el dominio siempre que sea posible, reservando acciones personalizadas para integraciones externas.
