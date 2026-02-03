# ============================================================================
# SISTEMA DE GESTIÓN DE PRODUCTOS
# Módulo: validaciones.py
# Descripción: Funciones de validación usando estructuras condicionales
# ============================================================================

"""
Módulo de validaciones.
Contiene funciones para validar datos de entrada utilizando
condicionales (if, elif, else) y expresiones booleanas.
"""

import re


# Tupla con roles válidos (inmutable)
ROLES_VALIDOS = ('Admin', 'Usuario', 'Invitado')

# Tupla con categorías válidas (inmutable)
CATEGORIAS_VALIDAS = ('Electrónica', 'Ropa', 'Alimentos', 'Hogar', 'Deportes', 'Otros')


def validar_texto_no_vacio(texto: str, nombre_campo: str = "campo") -> tuple:
    """
    Valida que un texto no esté vacío.
    
    Args:
        texto: Texto a validar
        nombre_campo: Nombre del campo para el mensaje de error
        
    Returns:
        tuple: (es_valido: bool, mensaje: str)
    """
    if texto is None:
        return (False, f"El {nombre_campo} no puede ser nulo")
    elif texto.strip() == "":
        return (False, f"El {nombre_campo} no puede estar vacío")
    else:
        return (True, "Validación exitosa")


def validar_email(email: str) -> tuple:
    """
    Valida el formato de un correo electrónico.
    
    Args:
        email: Correo electrónico a validar
        
    Returns:
        tuple: (es_valido: bool, mensaje: str)
    """
    if not email:
        return (False, "El email no puede estar vacío")
    
    # Patrón básico de email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(patron, email):
        return (True, "Email válido")
    else:
        return (False, "Formato de email inválido")


def validar_edad(edad: int) -> tuple:
    """
    Valida la edad y determina la categoría del usuario.
    
    Args:
        edad: Edad a validar
        
    Returns:
        tuple: (es_valido: bool, mensaje: str, categoria: str)
    """
    if edad < 0:
        return (False, "La edad no puede ser negativa", None)
    elif edad < 13:
        return (True, "Usuario menor de edad", "Niño")
    elif edad < 18:
        return (True, "Usuario adolescente", "Adolescente")
    elif edad < 60:
        return (True, "Usuario adulto", "Adulto")
    elif edad <= 120:
        return (True, "Usuario adulto mayor", "Adulto Mayor")
    else:
        return (False, "La edad ingresada no es válida", None)


def validar_precio(precio: float) -> tuple:
    """
    Valida que el precio sea positivo y razonable.
    
    Args:
        precio: Precio a validar
        
    Returns:
        tuple: (es_valido: bool, mensaje: str)
    """
    if precio < 0:
        return (False, "El precio no puede ser negativo")
    elif precio == 0:
        return (False, "El precio no puede ser cero")
    elif precio > 1000000000:
        return (False, "El precio excede el límite permitido")
    else:
        return (True, "Precio válido")


def validar_cantidad(cantidad: int) -> tuple:
    """
    Valida que la cantidad sea válida para el inventario.
    
    Args:
        cantidad: Cantidad a validar
        
    Returns:
        tuple: (es_valido: bool, mensaje: str, nivel_stock: str)
    """
    if cantidad < 0:
        return (False, "La cantidad no puede ser negativa", None)
    elif cantidad == 0:
        return (True, "Sin stock disponible", "Sin Stock")
    elif cantidad < 10:
        return (True, "Stock bajo", "Bajo")
    elif cantidad < 50:
        return (True, "Stock normal", "Normal")
    elif cantidad < 100:
        return (True, "Stock alto", "Alto")
    else:
        return (True, "Stock muy alto", "Muy Alto")


def validar_rol(rol: str) -> tuple:
    """
    Valida que el rol sea uno de los permitidos.
    
    Args:
        rol: Rol a validar
        
    Returns:
        tuple: (es_valido: bool, mensaje: str)
    """
    if not rol:
        return (False, "El rol no puede estar vacío")
    elif rol in ROLES_VALIDOS:
        return (True, f"Rol '{rol}' válido")
    else:
        roles_str = ", ".join(ROLES_VALIDOS)
        return (False, f"Rol inválido. Roles permitidos: {roles_str}")


def validar_categoria(categoria: str) -> tuple:
    """
    Valida que la categoría sea una de las permitidas.
    
    Args:
        categoria: Categoría a validar
        
    Returns:
        tuple: (es_valido: bool, mensaje: str)
    """
    if not categoria:
        return (False, "La categoría no puede estar vacía")
    elif categoria in CATEGORIAS_VALIDAS:
        return (True, f"Categoría '{categoria}' válida")
    else:
        categorias_str = ", ".join(CATEGORIAS_VALIDAS)
        return (False, f"Categoría inválida. Categorías permitidas: {categorias_str}")


def validar_id(id_valor: int, lista_ids: set) -> tuple:
    """
    Valida que un ID sea único y válido.
    
    Args:
        id_valor: ID a validar
        lista_ids: Conjunto de IDs existentes
        
    Returns:
        tuple: (es_valido: bool, mensaje: str)
    """
    if id_valor <= 0:
        return (False, "El ID debe ser un número positivo")
    elif id_valor in lista_ids:
        return (False, f"El ID {id_valor} ya existe en el sistema")
    else:
        return (True, "ID válido y único")


def obtener_permisos_por_rol(rol: str) -> dict:
    """
    Retorna los permisos según el rol del usuario.
    
    Args:
        rol: Rol del usuario
        
    Returns:
        dict: Diccionario con los permisos del rol
    """
    if rol == "Admin":
        return {
            "puede_crear": True,
            "puede_editar": True,
            "puede_eliminar": True,
            "puede_ver_reportes": True,
            "puede_gestionar_usuarios": True
        }
    elif rol == "Usuario":
        return {
            "puede_crear": True,
            "puede_editar": True,
            "puede_eliminar": False,
            "puede_ver_reportes": True,
            "puede_gestionar_usuarios": False
        }
    elif rol == "Invitado":
        return {
            "puede_crear": False,
            "puede_editar": False,
            "puede_eliminar": False,
            "puede_ver_reportes": False,
            "puede_gestionar_usuarios": False
        }
    else:
        return {
            "puede_crear": False,
            "puede_editar": False,
            "puede_eliminar": False,
            "puede_ver_reportes": False,
            "puede_gestionar_usuarios": False
        }


def clasificar_producto_por_precio(precio: float) -> str:
    """
    Clasifica un producto según su rango de precio.
    
    Args:
        precio: Precio del producto
        
    Returns:
        str: Clasificación del producto
    """
    if precio < 10000:
        return "Económico"
    elif precio < 50000:
        return "Estándar"
    elif precio < 100000:
        return "Premium"
    else:
        return "Lujo"


def validar_producto_completo(producto: dict) -> tuple:
    """
    Realiza validación completa de un producto.
    
    Args:
        producto: Diccionario con datos del producto
        
    Returns:
        tuple: (es_valido: bool, lista_errores: list)
    """
    errores = []
    
    # Validar nombre
    val_nombre = validar_texto_no_vacio(producto.get("nombre", ""), "nombre")
    if not val_nombre[0]:
        errores.append(val_nombre[1])
    
    # Validar precio
    val_precio = validar_precio(producto.get("precio", 0))
    if not val_precio[0]:
        errores.append(val_precio[1])
    
    # Validar cantidad
    val_cantidad = validar_cantidad(producto.get("cantidad", 0))
    if not val_cantidad[0]:
        errores.append(val_cantidad[1])
    
    # Validar categoría
    val_categoria = validar_categoria(producto.get("categoria", ""))
    if not val_categoria[0]:
        errores.append(val_categoria[1])
    
    if len(errores) == 0:
        return (True, [])
    else:
        return (False, errores)


def validar_usuario_completo(usuario: dict) -> tuple:
    """
    Realiza validación completa de un usuario.
    
    Args:
        usuario: Diccionario con datos del usuario
        
    Returns:
        tuple: (es_valido: bool, lista_errores: list)
    """
    errores = []
    
    # Validar nombre
    val_nombre = validar_texto_no_vacio(usuario.get("nombre", ""), "nombre")
    if not val_nombre[0]:
        errores.append(val_nombre[1])
    
    # Validar email
    val_email = validar_email(usuario.get("email", ""))
    if not val_email[0]:
        errores.append(val_email[1])
    
    # Validar edad
    val_edad = validar_edad(usuario.get("edad", 0))
    if not val_edad[0]:
        errores.append(val_edad[1])
    
    # Validar rol
    val_rol = validar_rol(usuario.get("rol", ""))
    if not val_rol[0]:
        errores.append(val_rol[1])
    
    if len(errores) == 0:
        return (True, [])
    else:
        return (False, errores)
