# Arquitectura de Rasa Eléctrico

El sistema sigue principios de **Arquitectura Limpia (Clean Architecture)**.

## Separación de Responsabilidades
1. **Dominio**: Reglas de negocio puras.
2. **Aplicación**: Casos de uso. Orquesta el flujo entre Configuración (Global) y Contexto (Usuario).
3. **Adaptadores**: Implementaciones técnicas (Rasa, Google Maps, lector JSON).

## Gestión de Datos (Configuración vs Contexto)
- **Configuración Global (JSON)**: Parámetros del negocio que definen la estructura de costos (ej: márgenes, tarifas base).
- **Contexto de Usuario (Input)**: Parámetros epímeros específicos de una obra (ej: horas hombre, materiales usados).

## Inyección de Dependencias
Gestionada por `FactoriaServicios`. El caso de uso combina la configuración cargada del JSON con la entrada del usuario para delegar al dominio el cálculo final.

## Generación de Documentos
- **Componente**: Se integrará un generador de PDF en la capa de **Infraestructura**.
- **Interfaz**: Se definirá un puerto `IGeneradorDocumentos` en la capa de **Aplicación** para asegurar que el núcleo no dependa de la implementación específica del PDF.

## Estrategia Multi-canal
- **Abstracción de Salida**: Se definen dos grandes tipos de interfaces para la salida:
    - `IPresentador` (Visualización: Chat/Web)
    - `IExportador` (Ficheros: PDF/CSV)
- **FastAPI**: En el futuro, FastAPI actuará como un adaptador que implementará la interfaz `IPresentador` o consumirá directamente la estructura de datos del dominio para ofrecer una API REST, reutilizando la lógica ya desacoplada.

## Reglas de Negocio: Materiales
- **Compra de Materiales**: Definida por el cliente mediante un valor booleano (`cliente_proporciona_materiales`).
- **Costo de Materiales**:
    - Si el cliente proporciona: Costo = 0.
    - Si el electricista proporciona: Costo = Precio_JSON + Costo_Adquisicion.
- **Precios de Referencia**: Los valores de materiales específicos (llave termomagnética, etc.) se obtienen del JSON de configuración.

## Tecnologías de Exportación
- **Motor de PDF**: Se ha seleccionado `WeasyPrint` como estándar.
- **Razón**: Permite el uso de plantillas HTML/CSS compartidas, facilitando la consistencia estética con la futura WebApp desarrollada en FastAPI.

## Capa de Aplicación: DTOs
- **EntradaPresupuesto**: Data Transfer Object que encapsula los datos proporcionados por el usuario, tipando la información recibida desde los adaptadores (Rasa) antes de ser procesada por los casos de uso.

## Reglas de Negocio: Cargo por Gestión de Compra
- **Costo de Adquisición (Cargo Fijo)**: Se aplica un cargo fijo (`costo_gestion_compra`) cuando el electricista se encarga de comprar los materiales.
- **Transparencia**: Este cargo se suma al valor de los materiales facturados.
