# Instalación y Configuración del Entorno

Este documento describe los pasos necesarios para configurar el entorno de desarrollo local e instalar las dependencias del proyecto.

## Prerrequisitos

El proyecto requiere **Python 3.10**. Dado que las versiones más recientes de Ubuntu (como la 24.04 o superior) vienen con Python 3.12+ por defecto, se debe instalar la versión específica utilizando el repositorio de la comunidad.

### 1. Instalación de Python 3.10 en Ubuntu

Ejecuta los siguientes comandos en tu terminal para añadir el PPA de `deadsnakes` e instalar Python 3.10 junto con sus herramientas de desarrollo y manejo de entornos virtuales:

```bash
# Actualizar el sistema e instalar prerrequisitos
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y

# Añadir el repositorio PPA
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# Instalar Python 3.10 y el módulo para entornos virtuales
sudo apt install python3.10 python3.10-venv python3.10-dev -y

```

> ⚠️ **Importante:** No alteres el enlace simbólico predeterminado de `python3` de tu sistema operativo, ya que podrías romper herramientas internas de Ubuntu. Utiliza siempre el binario explícito `python3.10`.

---

## Configuración del Entorno Virtual

Para mantener las dependencias del proyecto aisladas y evitar conflictos, utilizamos un entorno virtual (`venv`).

### 2. Crear y activar el entorno

Posiciónate en la raíz del proyecto y ejecuta:

```bash
# Crear el entorno virtual usando Python 3.10
python3.10 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

```

Una vez activado, verás el prefijo `(.venv)` al principio de tu prompt en la terminal.

---

## Instalación de Dependencias

### 3. Actualizar herramientas de empaquetado

Antes de instalar los paquetes del proyecto, asegúrate de tener `pip` y `setuptools` actualizados dentro del entorno virtual:

```bash
pip install --upgrade pip setuptools wheel

```

### 4. Instalar los paquetes del proyecto

Una vez que el entorno esté activo y actualizado, instala Rasa y el resto de las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt

```

---

## Verificación de la Instalación

Para comprobar que todo se instaló correctamente, con el entorno virtual activo, ejecuta:

```bash
rasa --version

```

Deberías ver en pantalla la versión de Rasa instalada y la confirmación de que está corriendo bajo Python 3.10.

---

## Comandos Útiles de Referencia

* **Activar entorno:** `source .venv/bin/activate`
* **Desactivar entorno:** `deactivate`
* **Congelar nuevas dependencias:** `pip freeze > requirements.txt`

```
