Sistema de Gestión de Inventario en Python
Este es un sencillo pero funcional sistema de gestión de inventario desarrollado en Python. Permite a los usuarios realizar operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar) sobre una lista de objetos, guardando los datos de forma persistente en un archivo local.

✨ Características
Agregar Objetos: Añade nuevos artículos al inventario especificando nombre, precio, cantidad y características.

Mostrar Inventario: Visualiza la lista completa de objetos, junto con el número total de artículos y el valor total del inventario.

Eliminar Objetos: Borra un artículo del inventario seleccionándolo por su ID.

Modificar Objetos: Edita los atributos (nombre, precio, cantidad, características) de un artículo existente a través de un submenú interactivo.

Persistencia de Datos: Guarda automáticamente el inventario en un archivo inventario.json para que la información no se pierda al cerrar el programa.

Manejo de Errores: Incluye validaciones para entradas de usuario incorrectas (por ejemplo, texto en lugar de números para precios o IDs).