# 🏪 Sistema de Gestión de Productos

## 📋 Descripción del Proyecto

Sistema de gestión de productos desarrollado en Python como proyecto evaluativo del Módulo 3 de Alkemy. Este sistema permite la administración completa de productos y usuarios, implementando las mejores prácticas de programación vistas en el módulo.

## 🎯 Objetivo

Diseñar e implementar un sistema de gestión de productos basado en Python, aplicando:
- Estructuras de control (condicionales y bucles)
- Funciones personalizadas y recursivas
- Estructuras de datos (listas, diccionarios, tuplas, sets)
- Modularización del código

## 🚀 Características

### Funcionalidades Principales

- ✅ **Gestión de Productos**: Crear, listar, buscar, editar y eliminar productos
- ✅ **Gestión de Usuarios**: CRUD completo de usuarios con roles
- ✅ **Validación de Datos**: Validación robusta de entradas
- ✅ **Reportes y Estadísticas**: Visualización de métricas del sistema
- ✅ **Menú Interactivo**: Interfaz de consola amigable

### Aspectos Técnicos Implementados

| Requerimiento | Implementación |
|---------------|----------------|
| Entrada/Salida de datos | `input()`, `print()`, f-strings |
| Estructuras de control | `if`, `elif`, `else`, `for`, `while`, `break`, `continue` |
| Funciones | Parámetros, `return`, funciones recursivas |
| Estructuras de datos | `list`, `dict`, `tuple`, `set` |
| Modularización | Múltiples archivos `.py`, imports |

## 📁 Estructura del Proyecto

```
sistema_gestion/
│
├── main.py                 # Punto de entrada principal
├── README.md               # Documentación del proyecto
│
└── modulos/
    ├── __init__.py         # Inicializador del paquete
    ├── datos_basicos.py    # Funciones de captura de datos
    ├── validaciones.py     # Validaciones con condicionales
    ├── gestion_datos.py    # Manejo de estructuras de datos
    ├── menu.py             # Sistema de menús iterativos
    └── funciones_utiles.py # Funciones auxiliares y recursivas
```

## 🛠️ Requisitos

- Python 3.8 o superior
- No requiere librerías externas (solo librería estándar)

## ⚙️ Instalación y Ejecución

1. **Clonar o descargar** el proyecto
2. **Navegar** al directorio del proyecto:
   ```bash
   cd sistema_gestion
   ```
3. **Ejecutar** el programa:
   ```bash
   python main.py
   ```

## 📖 Guía de Uso

### Menú Principal

```
============================================================
  🏪 SISTEMA DE GESTIÓN DE PRODUCTOS
============================================================
  1. 📦 Gestión de Productos
  2. 👥 Gestión de Usuarios
  3. 📊 Reportes y Estadísticas
  4. ⚙️  Configuración
  5. 🚪 Salir
============================================================
```

### Gestión de Productos

- **Agregar**: Ingresa nombre, precio, cantidad y categoría
- **Listar**: Muestra todos los productos registrados
- **Buscar**: Por ID, categoría o nombre
- **Editar**: Modifica datos de un producto existente
- **Eliminar**: Remueve un producto del sistema

### Gestión de Usuarios

- **Agregar**: Ingresa nombre, email, edad y rol
- **Roles disponibles**: Admin, Usuario, Invitado
- **Validación de email**: Formato correcto requerido
- **Emails únicos**: No se permiten duplicados

## 🔧 Estructuras de Datos Utilizadas

### Listas (`list`)
```python
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 899990, ...},
    {"id": 2, "nombre": "Mouse", "precio": 59990, ...}
]
```

### Diccionarios (`dict`)
```python
producto = {
    "id": 1,
    "nombre": "Laptop HP",
    "precio": 899990.0,
    "cantidad": 15,
    "categoria": "Electrónica",
    "activo": True
}
```

### Tuplas (`tuple`)
```python
ROLES_VALIDOS = ('Admin', 'Usuario', 'Invitado')
CATEGORIAS_VALIDAS = ('Electrónica', 'Ropa', 'Alimentos', 'Hogar', 'Deportes', 'Otros')
```

### Conjuntos (`set`)
```python
emails_registrados = {"ana@email.com", "carlos@email.com"}
ids_productos = {1, 2, 3, 4, 5}
```

## 🔄 Funciones Recursivas

El sistema implementa varias funciones recursivas:

- `factorial(n)`: Calcula el factorial de un número
- `fibonacci(n)`: Calcula el n-ésimo número de Fibonacci
- `suma_lista_recursiva()`: Suma elementos de una lista
- `busqueda_binaria_recursiva()`: Búsqueda binaria en lista ordenada
- `potencia_recursiva()`: Calcula potencias
- `invertir_cadena_recursiva()`: Invierte una cadena

## 📊 Validaciones Implementadas

| Campo | Validaciones |
|-------|-------------|
| Nombre | No vacío, sin caracteres especiales |
| Email | Formato válido, único en el sistema |
| Edad | Positiva, categorización automática |
| Precio | Positivo, dentro de límites |
| Cantidad | No negativa, nivel de stock |
| Rol | Debe estar en roles permitidos |
| Categoría | Debe estar en categorías permitidas |

## 🎨 Estilo de Código

El código sigue las convenciones de **PEP 8**:
- Indentación de 4 espacios
- Nombres de variables en `snake_case`
- Nombres de constantes en `MAYUSCULAS`
- Docstrings en funciones
- Comentarios explicativos

## 📈 Ejemplo de Ejecución

```
============================================================
  Sistema de Gestión de Productos
  Versión: 1.0.0
============================================================

¿Desea cargar datos de prueba para explorar el sistema?
Ingrese 's' para sí, cualquier otra tecla para no: s

📥 Cargando datos de prueba...
✅ Producto 'Laptop HP Pavilion' agregado exitosamente.
✅ Producto 'Mouse Logitech G502' agregado exitosamente.
...
✅ Datos de prueba cargados exitosamente.
```

## 🧪 Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Paradigma**: Programación estructurada y modular
- **Estilo**: PEP 8
- **Documentación**: Docstrings, comentarios, README

## 📚 Referencias

- [Python Data Structures - Real Python](https://realpython.com/python-data-structures/)
- [Python Modules and Packages - Real Python](https://realpython.com/python-modules-packages/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

## 👨‍💻 Autor

**Proyecto Módulo 3 - Alkemy**

---

## 📝 Licencia

Este proyecto fue desarrollado con fines educativos como parte del programa de formación de Alkemy.

---

*Sistema de Gestión de Productos v1.0.0* 🚀🐍
