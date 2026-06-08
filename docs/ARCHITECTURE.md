# Arquitectura de Rasa Eléctrico

El sistema sigue principios de **Arquitectura Limpia (Clean Architecture)** para asegurar la mantenibilidad y la escalabilidad de la lógica de presupuestación.

## Separación de Responsabilidades

El sistema se divide en capas claras:

1. **Capa de Dominio (Núcleo):**
   - Contiene las reglas de negocio, modelos de datos de presupuestos y definiciones de interfaces (puertos).
   - Es independiente de frameworks y herramientas externas.

2. **Capa de Aplicación (Casos de Uso):**
   - Orquesta el flujo de datos.
   - Implementa la lógica de negocio usando las interfaces definidas en el dominio.

3. **Capa de Infraestructura (Adaptadores):**
   - Implementaciones concretas de los puertos.
   - Aquí reside la integración con **Google Maps API** y cualquier base de datos externa.
   - El Action Server de Rasa actúa como el punto de entrada que conecta el flujo conversacional con esta arquitectura.

## Abstracción de Servicios Externos

Para calcular distancias, el sistema define un puerto `IDistanceProvider`. La lógica de presupuestación no conoce que se está utilizando Google Maps; solo sabe que puede solicitar una distancia entre dos puntos. Esto permite cambiar la implementación técnica sin afectar el núcleo del sistema.

## Configuración del Punto de Origen
El sistema está preconfigurado para calcular presupuestos con origen en **Garín, Gran Buenos Aires Norte**. Este punto de referencia es gestionado por la capa de configuración.
