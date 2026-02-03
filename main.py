#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# SISTEMA DE GESTIÓN DE PRODUCTOS
# Archivo: main.py
# Descripción: Punto de entrada principal del sistema
# Versión: 1.0.0
# Autor: Equipo de Desarrollo - Proyecto Módulo 3 Alkemy
# ============================================================================

"""
Sistema de Gestión de Productos
===============================

Este sistema permite gestionar productos y usuarios de manera eficiente,
utilizando las mejores prácticas de programación en Python.

Funcionalidades principales:
- Gestión completa de productos (CRUD)
- Gestión completa de usuarios (CRUD)
- Reportes y estadísticas
- Validación de datos de entrada
- Estructura modular y mantenible

Módulos del sistema:
- datos_basicos: Funciones de captura y formateo de datos
- validaciones: Validación de datos con condicionales
- gestion_datos: Manejo de estructuras de datos
- menu: Sistema de menús interactivos
- funciones_utiles: Funciones auxiliares y recursivas

Uso:
    $ python main.py
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

# Importar módulos del sistema
from modulos.menu import ejecutar_menu_principal
from modulos.datos_basicos import (
    crear_producto, crear_usuario,
    mostrar_producto, mostrar_usuario
)
from modulos.gestion_datos import (
    agregar_producto, agregar_usuario,
    listar_productos, listar_usuarios
)
from modulos.funciones_utiles import (
    factorial, fibonacci,
    mostrar_resumen_general
)


# ============================================================================
# DATOS DE PRUEBA INICIALES
# ============================================================================

def cargar_datos_prueba() -> None:
    """
    Carga datos de prueba iniciales para demostrar el funcionamiento del sistema.
    Estos datos son opcionales y pueden ser desactivados.
    """
    print("\n📥 Cargando datos de prueba...")
    
    # Productos de prueba
    productos_prueba = [
        crear_producto(1, "Laptop HP Pavilion", 899990.0, 15, "Electrónica"),
        crear_producto(2, "Mouse Logitech G502", 59990.0, 45, "Electrónica"),
        crear_producto(3, "Camiseta Nike Dri-FIT", 29990.0, 100, "Ropa"),
        crear_producto(4, "Zapatillas Adidas Running", 79990.0, 30, "Deportes"),
        crear_producto(5, "Arroz Integral 1kg", 2490.0, 200, "Alimentos"),
        crear_producto(6, "Silla Ergonómica", 159990.0, 8, "Hogar"),
        crear_producto(7, "Teclado Mecánico RGB", 89990.0, 25, "Electrónica"),
        crear_producto(8, "Polera Básica Algodón", 12990.0, 150, "Ropa"),
    ]
    
    # Agregar productos
    for producto in productos_prueba:
        agregar_producto(producto)
    
    # Usuarios de prueba
    usuarios_prueba = [
        crear_usuario(1, "Ana García López", "ana.garcia@email.com", 28, "Admin"),
        crear_usuario(2, "Carlos Rodríguez", "carlos.rod@email.com", 35, "Usuario"),
        crear_usuario(3, "María Fernández", "maria.fer@email.com", 22, "Usuario"),
        crear_usuario(4, "Pedro Martínez", "pedro.m@email.com", 45, "Usuario"),
        crear_usuario(5, "Laura Sánchez", "laura.s@email.com", 19, "Invitado"),
    ]
    
    # Agregar usuarios
    for usuario in usuarios_prueba:
        agregar_usuario(usuario)
    
    print("✅ Datos de prueba cargados exitosamente.\n")


# ============================================================================
# DEMOSTRACIÓN DE FUNCIONES RECURSIVAS
# ============================================================================

def demostrar_funciones_recursivas() -> None:
    """
    Demuestra el uso de funciones recursivas del sistema.
    """
    print("\n" + "="*60)
    print("  🔄 DEMOSTRACIÓN DE FUNCIONES RECURSIVAS")
    print("="*60)
    
    # Factorial
    numero = 5
    resultado_factorial = factorial(numero)
    print(f"\n  Factorial de {numero}: {resultado_factorial}")
    print(f"  {numero}! = {numero} × {numero-1} × ... × 1 = {resultado_factorial}")
    
    # Fibonacci
    posicion = 10
    print(f"\n  Secuencia Fibonacci (primeros {posicion} números):")
    secuencia = [fibonacci(i) for i in range(posicion)]
    print(f"  {secuencia}")
    
    print("\n" + "="*60)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main() -> None:
    """
    Función principal que inicia el sistema.
    """
    # Mensaje de bienvenida con f-strings
    nombre_sistema = "Sistema de Gestión de Productos"
    version = "1.0.0"
    
    print("\n" + "="*60)
    print(f"  {nombre_sistema}")
    print(f"  Versión: {version}")
    print("="*60)
    
    # Preguntar si cargar datos de prueba
    print("\n¿Desea cargar datos de prueba para explorar el sistema?")
    respuesta = input("Ingrese 's' para sí, cualquier otra tecla para no: ")
    
    if respuesta.lower() == 's':
        cargar_datos_prueba()
        
        # Mostrar demostración de funciones recursivas
        demostrar_funciones_recursivas()
        
        # Mostrar resumen inicial
        mostrar_resumen_general()
    
    # Iniciar el menú principal
    ejecutar_menu_principal()


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Se ejecuta solo si el archivo se ejecuta directamente (no importado).
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
        print("Hasta pronto. 👋")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, contacte al administrador del sistema.")
