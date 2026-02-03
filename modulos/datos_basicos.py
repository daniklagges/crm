# ============================================================================
# SISTEMA DE GESTIÓN DE PRODUCTOS
# Módulo: datos_basicos.py
# Descripción: Funciones para captura y manejo básico de datos
# ============================================================================

"""
Módulo de datos básicos.
Contiene funciones para la captura, conversión y manejo inicial de datos
ingresados por el usuario.
"""


def capturar_texto(mensaje: str) -> str:
    """
    Captura un texto ingresado por el usuario.
    
    Args:
        mensaje: Prompt a mostrar al usuario
        
    Returns:
        str: Texto ingresado por el usuario (sin espacios al inicio/fin)
    """
    entrada = input(mensaje)
    return entrada.strip()


def capturar_entero(mensaje: str, valor_defecto: int = 0) -> int:
    """
    Captura un número entero del usuario con validación.
    
    Args:
        mensaje: Prompt a mostrar al usuario
        valor_defecto: Valor a retornar si la conversión falla
        
    Returns:
        int: Número entero ingresado o valor por defecto
    """
    try:
        entrada = input(mensaje)
        return int(entrada)
    except ValueError:
        print(f"⚠️  Entrada inválida. Se usará el valor por defecto: {valor_defecto}")
        return valor_defecto


def capturar_decimal(mensaje: str, valor_defecto: float = 0.0) -> float:
    """
    Captura un número decimal del usuario con validación.
    
    Args:
        mensaje: Prompt a mostrar al usuario
        valor_defecto: Valor a retornar si la conversión falla
        
    Returns:
        float: Número decimal ingresado o valor por defecto
    """
    try:
        entrada = input(mensaje)
        return float(entrada)
    except ValueError:
        print(f"⚠️  Entrada inválida. Se usará el valor por defecto: {valor_defecto}")
        return valor_defecto


def crear_producto(id_producto: int, nombre: str, precio: float, 
                   cantidad: int, categoria: str) -> dict:
    """
    Crea un diccionario con la información de un producto.
    
    Args:
        id_producto: Identificador único del producto
        nombre: Nombre del producto
        precio: Precio unitario del producto
        cantidad: Cantidad en stock
        categoria: Categoría del producto
        
    Returns:
        dict: Diccionario con los datos del producto
    """
    producto = {
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
        "activo": True
    }
    return producto


def crear_usuario(id_usuario: int, nombre: str, email: str, 
                  edad: int, rol: str) -> dict:
    """
    Crea un diccionario con la información de un usuario.
    
    Args:
        id_usuario: Identificador único del usuario
        nombre: Nombre completo del usuario
        email: Correo electrónico
        edad: Edad del usuario
        rol: Rol asignado (Admin, Usuario, Invitado)
        
    Returns:
        dict: Diccionario con los datos del usuario
    """
    usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "rol": rol,
        "activo": True
    }
    return usuario


def mostrar_producto(producto: dict) -> None:
    """
    Muestra la información de un producto con formato.
    
    Args:
        producto: Diccionario con los datos del producto
    """
    print(f"\n{'='*50}")
    print(f"📦 PRODUCTO ID: {producto['id']}")
    print(f"{'='*50}")
    print(f"   Nombre:    {producto['nombre']}")
    print(f"   Precio:    ${producto['precio']:,.2f}")
    print(f"   Cantidad:  {producto['cantidad']} unidades")
    print(f"   Categoría: {producto['categoria']}")
    print(f"   Estado:    {'✅ Activo' if producto['activo'] else '❌ Inactivo'}")
    print(f"{'='*50}")


def mostrar_usuario(usuario: dict) -> None:
    """
    Muestra la información de un usuario con formato.
    
    Args:
        usuario: Diccionario con los datos del usuario
    """
    print(f"\n{'='*50}")
    print(f"👤 USUARIO ID: {usuario['id']}")
    print(f"{'='*50}")
    print(f"   Nombre: {usuario['nombre']}")
    print(f"   Email:  {usuario['email']}")
    print(f"   Edad:   {usuario['edad']} años")
    print(f"   Rol:    {usuario['rol']}")
    print(f"   Estado: {'✅ Activo' if usuario['activo'] else '❌ Inactivo'}")
    print(f"{'='*50}")


def formatear_moneda(valor: float) -> str:
    """
    Formatea un valor numérico como moneda.
    
    Args:
        valor: Valor numérico a formatear
        
    Returns:
        str: Valor formateado como moneda
    """
    return f"${valor:,.2f}"


def formatear_cantidad(valor: int) -> str:
    """
    Formatea una cantidad con separador de miles.
    
    Args:
        valor: Cantidad a formatear
        
    Returns:
        str: Cantidad formateada
    """
    return f"{valor:,}"
