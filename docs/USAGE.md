# Guía de Uso

Esta guía explica cómo interactuar con el bot y probar sus funcionalidades.

## Interacción por Consola

La forma más rápida de probar el bot es usando el comando:
```bash
rasa run actions &
rasa shell
```

### Flujo esperado:
1. **Inicio:** El bot te saluda y te pide la dirección del trabajo.
2. **Entrada:** Ingresas la dirección (ej: "Av. Siempreviva 123, Garín").
3. **Cálculo:** El bot procesa la dirección y responde con el presupuesto estimado basado en la distancia al origen preconfigurado.

## Interacción por API
*(Sin cambios)*
