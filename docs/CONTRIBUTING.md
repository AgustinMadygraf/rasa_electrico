# Guía de Contribución

¡Gracias por tu interés en mejorar Rasa Eléctrico!

## Principios de Desarrollo
Este proyecto sigue **Arquitectura Limpia (Clean Architecture)**. Es imperativo respetar la separación entre lógica de negocio e infraestructura.

## Flujo de Trabajo para Contribuir

1. **Documentación:** Antes de implementar una funcionalidad o cambio estructural, **actualiza la documentación** relevante en `docs/` y `README.md`.
2. **Crear una Rama:** Crea una rama descriptiva para tu cambio.
3. **Desarrollar:** Implementa respetando las capas definidas en `ARCHITECTURE.md`.
4. **Entrenar y Validar:** 
   - Ejecuta `rasa data validate` para asegurar consistencia.
   - Entrena el modelo: `rasa train`.
5. **Probar:** Realiza pruebas de conversación usando `rasa shell`.
6. **Pruebas Automatizadas:** Todo nuevo caso de uso debe incluir pruebas unitarias (preferiblemente en `actions/tests/`).
7. **Commit:** Asegúrate de seguir las convenciones de mensajes de commit de la organización.

## Estilo de Código
- **Python:** PEP 8. Mantener alta cohesión y bajo acoplamiento.
- **YAML:** Usar 2 espacios para indentación.
- **Dependencias:** Utilizar inyección de dependencias para componentes de infraestructura.
