# ============================================================================
# SISTEMA DE GESTIÓN DE PRODUCTOS
# Módulo: funciones_utiles.py
# Descripción: Funciones utilitarias, incluyendo funciones recursivas
# ============================================================================

"""
Módulo de funciones útiles.
Contiene funciones generales reutilizables, incluyendo:
- Funciones recursivas para cálculos específicos
- Funciones de formato y presentación
- Funciones de utilidad general
"""

from typing import List, Dict, Any
from .gestion_datos import (
    obtener_estadisticas_productos, obtener_estadisticas_usuarios,
    listar_productos, listar_usuarios, obtener_total_productos,
    obtener_total_usuarios
)


# ============================================================================
# FUNCIONES RECURSIVAS
# ============================================================================

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número de forma recursiva.
    
    Args:
        n: Número para calcular factorial
        
    Returns:
        int: Factorial de n
        
    Example:
        >>> factorial(5)
        120
    """
    # Caso base
    if n <= 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calcula el n-ésimo número de Fibonacci de forma recursiva.
    
    Args:
        n: Posición en la secuencia
        
    Returns:
        int: Número de Fibonacci en la posición n
        
    Example:
        >>> fibonacci(6)
        8
    """
    # Casos base
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)


def suma_lista_recursiva(lista: List[float], indice: int = 0) -> float:
    """
    Suma todos los elementos de una lista de forma recursiva.
    
    Args:
        lista: Lista de números
        indice: Índice actual (para uso interno)
        
    Returns:
        float: Suma de todos los elementos
    """
    # Caso base: llegamos al final de la lista
    if indice >= len(lista):
        return 0
    # Caso recursivo: elemento actual + suma del resto
    return lista[indice] + suma_lista_recursiva(lista, indice + 1)


def busqueda_binaria_recursiva(lista: List[int], objetivo: int, 
                                inicio: int, fin: int) -> int:
    """
    Realiza búsqueda binaria de forma recursiva en una lista ordenada.
    
    Args:
        lista: Lista ordenada de números
        objetivo: Número a buscar
        inicio: Índice de inicio
        fin: Índice de fin
        
    Returns:
        int: Índice donde se encuentra el elemento, -1 si no existe
    """
    # Caso base: no se encontró
    if inicio > fin:
        return -1
    
    # Calcular punto medio
    medio = (inicio + fin) // 2
    
    # Caso base: encontramos el elemento
    if lista[medio] == objetivo:
        return medio
    # Caso recursivo: buscar en mitad izquierda o derecha
    elif lista[medio] > objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)


def potencia_recursiva(base: float, exponente: int) -> float:
    """
    Calcula la potencia de un número de forma recursiva.
    
    Args:
        base: Número base
        exponente: Exponente (entero no negativo)
        
    Returns:
        float: base elevado a exponente
    """
    # Caso base
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia_recursiva(base, -exponente)
    # Caso recursivo
    return base * potencia_recursiva(base, exponente - 1)


def contar_elementos_lista(lista: List[Any], indice: int = 0) -> int:
    """
    Cuenta los elementos de una lista de forma recursiva.
    
    Args:
        lista: Lista a contar
        indice: Índice actual
        
    Returns:
        int: Cantidad de elementos
    """
    # Caso base
    if indice >= len(lista):
        return 0
    # Caso recursivo
    return 1 + contar_elementos_lista(lista, indice + 1)


def invertir_cadena_recursiva(cadena: str) -> str:
    """
    Invierte una cadena de texto de forma recursiva.
    
    Args:
        cadena: Texto a invertir
        
    Returns:
        str: Texto invertido
    """
    # Caso base
    if len(cadena) <= 1:
        return cadena
    # Caso recursivo
    return cadena[-1] + invertir_cadena_recursiva(cadena[:-1])


def calcular_descuento_acumulado(precio: float, descuentos: List[float], 
                                  indice: int = 0) -> float:
    """
    Calcula el precio final aplicando descuentos acumulativos de forma recursiva.
    
    Args:
        precio: Precio original
        descuentos: Lista de porcentajes de descuento (ej: [10, 5, 3])
        indice: Índice actual del descuento
        
    Returns:
        float: Precio final después de aplicar todos los descuentos
    """
    # Caso base: no hay más descuentos
    if indice >= len(descuentos):
        return precio
    
    # Aplicar descuento actual
    descuento = descuentos[indice] / 100
    nuevo_precio = precio * (1 - descuento)
    
    # Caso recursivo: aplicar siguiente descuento
    return calcular_descuento_acumulado(nuevo_precio, descuentos, indice + 1)


# ============================================================================
# FUNCIONES DE FORMATO Y PRESENTACIÓN
# ============================================================================

def crear_linea(caracter: str = "=", longitud: int = 60) -> str:
    """
    Crea una línea decorativa.
    
    Args:
        caracter: Carácter a repetir
        longitud: Longitud de la línea
        
    Returns:
        str: Línea generada
    """
    return caracter * longitud


def centrar_texto(texto: str, longitud: int = 60, caracter: str = " ") -> str:
    """
    Centra un texto en un ancho determinado.
    
    Args:
        texto: Texto a centrar
        longitud: Ancho total
        caracter: Carácter de relleno
        
    Returns:
        str: Texto centrado
    """
    return texto.center(longitud, caracter)


def formatear_tabla(datos: List[Dict], columnas: List[str]) -> str:
    """
    Formatea datos como una tabla simple.
    
    Args:
        datos: Lista de diccionarios con los datos
        columnas: Lista de nombres de columnas
        
    Returns:
        str: Tabla formateada como string
    """
    if not datos:
        return "Sin datos para mostrar"
    
    # Calcular anchos de columnas
    anchos = {}
    for col in columnas:
        anchos[col] = max(
            len(str(col)),
            max(len(str(fila.get(col, ""))) for fila in datos)
        )
    
    # Crear línea de encabezado
    lineas = []
    separador = "+" + "+".join("-" * (anchos[col] + 2) for col in columnas) + "+"
    
    lineas.append(separador)
    encabezado = "|" + "|".join(
        f" {col.center(anchos[col])} " for col in columnas
    ) + "|"
    lineas.append(encabezado)
    lineas.append(separador)
    
    # Crear filas de datos
    for fila in datos:
        fila_str = "|" + "|".join(
            f" {str(fila.get(col, '')).ljust(anchos[col])} " for col in columnas
        ) + "|"
        lineas.append(fila_str)
    
    lineas.append(separador)
    return "\n".join(lineas)


# ============================================================================
# FUNCIONES DE ESTADÍSTICAS Y REPORTES
# ============================================================================

def mostrar_estadisticas_productos() -> None:
    """
    Muestra las estadísticas de productos de forma formateada.
    """
    stats = obtener_estadisticas_productos()
    
    print(f"\n{'='*60}")
    print(centrar_texto("📊 ESTADÍSTICAS DE PRODUCTOS"))
    print(f"{'='*60}")
    
    if stats["total"] == 0:
        print("\n  📭 No hay productos registrados en el sistema.")
        return
    
    print(f"\n  📦 Total de productos: {stats['total']}")
    print(f"  💰 Valor total del inventario: ${stats['valor_total_inventario']:,.2f}")
    print(f"  💵 Precio promedio: ${stats['precio_promedio']:,.2f}")
    print(f"  📊 Cantidad total en stock: {stats['cantidad_total_stock']:,}")
    
    if stats['producto_mas_caro']:
        print(f"\n  🔺 Producto más caro: {stats['producto_mas_caro']['nombre']}")
        print(f"     Precio: ${stats['producto_mas_caro']['precio']:,.2f}")
    
    if stats['producto_mas_barato']:
        print(f"\n  🔻 Producto más barato: {stats['producto_mas_barato']['nombre']}")
        print(f"     Precio: ${stats['producto_mas_barato']['precio']:,.2f}")
    
    print(f"\n  📂 Productos por categoría:")
    for categoria, cantidad in stats['productos_por_categoria'].items():
        porcentaje = (cantidad / stats['total']) * 100
        print(f"     • {categoria}: {cantidad} ({porcentaje:.1f}%)")
    
    print(f"\n{'='*60}")


def mostrar_estadisticas_usuarios() -> None:
    """
    Muestra las estadísticas de usuarios de forma formateada.
    """
    stats = obtener_estadisticas_usuarios()
    
    print(f"\n{'='*60}")
    print(centrar_texto("📊 ESTADÍSTICAS DE USUARIOS"))
    print(f"{'='*60}")
    
    if stats["total"] == 0:
        print("\n  📭 No hay usuarios registrados en el sistema.")
        return
    
    print(f"\n  👥 Total de usuarios: {stats['total']}")
    print(f"  🎂 Edad promedio: {stats['edad_promedio']:.1f} años")
    print(f"  📧 Emails únicos registrados: {stats['emails_unicos']}")
    
    print(f"\n  🏷️  Usuarios por rol:")
    for rol, cantidad in stats['usuarios_por_rol'].items():
        porcentaje = (cantidad / stats['total']) * 100
        print(f"     • {rol}: {cantidad} ({porcentaje:.1f}%)")
    
    print(f"\n{'='*60}")


def mostrar_resumen_general() -> None:
    """
    Muestra un resumen general del sistema.
    """
    productos = listar_productos()
    usuarios = listar_usuarios()
    
    print(f"\n{'='*60}")
    print(centrar_texto("📋 RESUMEN GENERAL DEL SISTEMA"))
    print(f"{'='*60}")
    
    print(f"\n  {'─'*50}")
    print("  PRODUCTOS")
    print(f"  {'─'*50}")
    print(f"  Total registrados: {len(productos)}")
    
    if productos:
        total_stock = sum(p.get('cantidad', 0) for p in productos)
        valor_total = sum(p.get('precio', 0) * p.get('cantidad', 0) for p in productos)
        print(f"  Total en stock: {total_stock:,} unidades")
        print(f"  Valor del inventario: ${valor_total:,.2f}")
    
    print(f"\n  {'─'*50}")
    print("  USUARIOS")
    print(f"  {'─'*50}")
    print(f"  Total registrados: {len(usuarios)}")
    
    if usuarios:
        activos = sum(1 for u in usuarios if u.get('activo', False))
        print(f"  Usuarios activos: {activos}")
        print(f"  Usuarios inactivos: {len(usuarios) - activos}")
    
    print(f"\n{'='*60}")
    print(centrar_texto("Sistema de Gestión v1.0"))
    print(f"{'='*60}")


# ============================================================================
# FUNCIONES DE UTILIDAD GENERAL
# ============================================================================

def calcular_iva(precio: float, porcentaje_iva: float = 19.0) -> dict:
    """
    Calcula el IVA y el total de un precio.
    
    Args:
        precio: Precio base sin IVA
        porcentaje_iva: Porcentaje de IVA (default 19%)
        
    Returns:
        dict: Diccionario con precio base, IVA y total
    """
    iva = precio * (porcentaje_iva / 100)
    total = precio + iva
    
    return {
        "precio_base": precio,
        "porcentaje_iva": porcentaje_iva,
        "monto_iva": iva,
        "total": total
    }


def calcular_promedio(valores: List[float]) -> float:
    """
    Calcula el promedio de una lista de valores.
    
    Args:
        valores: Lista de números
        
    Returns:
        float: Promedio de los valores
    """
    if not valores:
        return 0.0
    return sum(valores) / len(valores)


def encontrar_maximo(valores: List[float]) -> float:
    """
    Encuentra el valor máximo en una lista.
    
    Args:
        valores: Lista de números
        
    Returns:
        float: Valor máximo
    """
    if not valores:
        return 0.0
    
    maximo = valores[0]
    for valor in valores[1:]:
        if valor > maximo:
            maximo = valor
    return maximo


def encontrar_minimo(valores: List[float]) -> float:
    """
    Encuentra el valor mínimo en una lista.
    
    Args:
        valores: Lista de números
        
    Returns:
        float: Valor mínimo
    """
    if not valores:
        return 0.0
    
    minimo = valores[0]
    for valor in valores[1:]:
        if valor < minimo:
            minimo = valor
    return minimo


def ordenar_productos_por_precio(productos: List[Dict], 
                                  ascendente: bool = True) -> List[Dict]:
    """
    Ordena una lista de productos por precio.
    
    Args:
        productos: Lista de productos
        ascendente: True para orden ascendente, False para descendente
        
    Returns:
        List[Dict]: Lista ordenada de productos
    """
    return sorted(productos, 
                  key=lambda p: p.get('precio', 0), 
                  reverse=not ascendente)


def ordenar_usuarios_por_edad(usuarios: List[Dict], 
                               ascendente: bool = True) -> List[Dict]:
    """
    Ordena una lista de usuarios por edad.
    
    Args:
        usuarios: Lista de usuarios
        ascendente: True para orden ascendente, False para descendente
        
    Returns:
        List[Dict]: Lista ordenada de usuarios
    """
    return sorted(usuarios, 
                  key=lambda u: u.get('edad', 0), 
                  reverse=not ascendente)


def filtrar_productos_por_rango_precio(productos: List[Dict], 
                                        precio_min: float, 
                                        precio_max: float) -> List[Dict]:
    """
    Filtra productos por rango de precio.
    
    Args:
        productos: Lista de productos
        precio_min: Precio mínimo
        precio_max: Precio máximo
        
    Returns:
        List[Dict]: Productos dentro del rango
    """
    resultado = []
    for producto in productos:
        precio = producto.get('precio', 0)
        if precio_min <= precio <= precio_max:
            resultado.append(producto)
    return resultado


def generar_codigo_producto(categoria: str, id_producto: int) -> str:
    """
    Genera un código único para un producto.
    
    Args:
        categoria: Categoría del producto
        id_producto: ID del producto
        
    Returns:
        str: Código generado (ej: "ELE-00001")
    """
    # Obtener las 3 primeras letras de la categoría
    prefijo = categoria[:3].upper()
    return f"{prefijo}-{id_producto:05d}"


def validar_stock_minimo(productos: List[Dict], stock_minimo: int = 10) -> List[Dict]:
    """
    Retorna productos con stock por debajo del mínimo.
    
    Args:
        productos: Lista de productos
        stock_minimo: Cantidad mínima de stock
        
    Returns:
        List[Dict]: Productos con stock bajo
    """
    productos_bajo_stock = []
    for producto in productos:
        if producto.get('cantidad', 0) < stock_minimo:
            productos_bajo_stock.append(producto)
    return productos_bajo_stock
