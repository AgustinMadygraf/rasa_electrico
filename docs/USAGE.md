# Guía de Uso

Esta guía explica cómo interactuar con el bot y probar sus funcionalidades.

## Interacción por Consola

La forma más rápida de probar el bot es usando el comando:
```bash
./run.sh shell
```
Esto iniciará el servidor de acciones en segundo plano y abrirá un prompt interactivo.

### Comandos útiles dentro de la consola:
- `/stop`: Salir de la conversación.
- `/restart`: Reiniciar el estado del bot.
- `/visualize`: (Si está configurado) Muestra el flujo de la conversación.

## Interacción por API

Si ejecutas el bot con `./run.sh`, se abrirá un servidor en el puerto `5005`.

### Endpoint de Mensajes:
**POST** `http://localhost:5005/webhooks/rest/webhook`

**Cuerpo:**
```json
{
  "sender": "usuario_test",
  "message": "Hola"
}
```

## Depuración
Puedes ver los logs del servidor de acciones en el archivo `out_actions.log` generado al ejecutar el bot.
