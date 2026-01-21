# Guía Funcional: Liberar Tipos de Documentos LATAM

## 1. Introducción
Este módulo está diseñado para proporcionar flexibilidad administrativa sobre los **Tipos de Documento** en localizaciones latinoamericanas (como Argentina). Su propósito principal es permitir a los administradores activar documentos que Odoo oculta por defecto y forzar su disponibilidad en las facturas, ignorando las restricciones estándar de letras (Letra A, B, C, etc.) y responsabilidades fiscales (AFIP).

## 2. Instalación
El módulo es gratuito y se puede descargar desde el Marketplace de Odoo. Requiere que los siguientes módulos estén instalados previamente:
* `account` (Contabilidad)
* `l10n_latam_invoice_document` (Módulo base de documentos LATAM)

## 3. Acceso al Módulo
Para gestionar los documentos, navegue a:
**Contabilidad > Configuración > Liberar Tipos de Documentos**

Esta vista mostrará **todos** los documentos del sistema, incluyendo aquellos que están inactivos o marcados como "archivable".

## 4. Gestión de Documentos

### 4.1 Activar y Desactivar
Puede cambiar el estado de un documento de dos maneras:
1.  **Individual**: Use el interruptor (toggle) en la columna **Activo** directamente en la lista.
2.  **Masivo**: Seleccione varios documentos, haga clic en el botón **Acción** y elija:
    * **Activate Documents**: Activa todos los seleccionados.
    * **Deactivate Documents**: Desactiva todos los seleccionados.
    * **Toggle Active State**: Alterna el estado de cada uno.

### 4.2 Forzar Disponibilidad (`Force Availability`)
Esta es la funcionalidad core del módulo. Por defecto, Odoo solo muestra los documentos que coinciden exactamente con la responsabilidad AFIP del cliente y la compañía.

Al marcar **Forzar** (campo `force_available`):
* El documento aparecerá en el selector de tipo de documento al crear una factura, incluso si no cumple con las reglas fiscales estándar.
* Sigue respetando el tipo de movimiento (ej: no mostrará una Nota de Crédito si está haciendo una Factura de Venta).
* **Uso sugerido**: Ambientes de prueba, migraciones de datos o casos de negocio excepcionales.

## 5. Vistas y Filtros
El módulo incluye una vista de búsqueda mejorada:
* **Filtros**: Puede filtrar por documentos Activos, Inactivos o específicamente aquellos con "Disponibilidad Forzada".
* **Agrupación**: Facilita la vista agrupando por **País**, **Tipo Interno** (Factura, Nota de Crédito, etc.) o **Estado**.

## 6. Advertencias
* El uso de la opción **Forzar Disponibilidad** en un entorno de producción debe hacerse con precaución, ya que permite emitir documentos que podrían no cumplir con la normativa fiscal estricta de la AFIP si se usan de forma incorrecta.
