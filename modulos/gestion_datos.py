# ============================================================================
# SISTEMA DE GESTIÓN DE PRODUCTOS
# Módulo: gestion_datos.py
# Descripción: Gestión de estructuras de datos (listas, diccionarios, tuplas, sets)
# ============================================================================

"""
Módulo de gestión de datos.
Contiene funciones para manipular las estructuras de datos del sistema:
- Listas: Almacenar colecciones de productos y usuarios
- Diccionarios: Representar entidades con pares clave-valor
- Tuplas: Datos inmutables (roles, categorías)
- Sets: Evitar duplicados (emails, IDs)
"""

from typing import List, Dict, Optional, Set, Tuple


# ============================================================================
# ESTRUCTURAS DE DATOS GLOBALES
# ============================================================================

# Lista de productos (cada producto es un diccionario)
productos: List[Dict] = []

# Lista de usuarios (cada usuario es un diccionario)
usuarios: List[Dict] = []

# Set para emails únicos (evita duplicados)
emails_registrados: Set[str] = set()

# Set para IDs de productos (evita duplicados)
ids_productos: Set[int] = set()

# Set para IDs de usuarios (evita duplicados)
ids_usuarios: Set[int] = set()

# Tuplas inmutables para datos del sistema
ROLES_SISTEMA: Tuple[str, ...] = ('Admin', 'Invitado', 'Usuario')
CATEGORIAS_SISTEMA: Tuple[str, ...] = ('Electrónica', 'Ropa', 'Alimentos', 'Hogar', 'Deportes', 'Otros')
ESTADOS_SISTEMA: Tuple[str, ...] = ('Activo', 'Inactivo', 'Pendiente')


# ============================================================================
# FUNCIONES PARA GESTIÓN DE PRODUCTOS
# ============================================================================

def agregar_producto(producto: Dict) -> bool:
    """
    Agrega un producto a la lista de productos.
    
    Args:
        producto: Diccionario con los datos del producto
        
    Returns:
        bool: True si se agregó correctamente, False si el ID ya existe
    """
    id_producto = producto.get("id")
    
    if id_producto in ids_productos:
        print(f"⚠️  Error: El producto con ID {id_producto} ya existe.")
        return False
    
    productos.append(producto)
    ids_productos.add(id_producto)
    print(f"✅ Producto '{producto.get('nombre')}' agregado exitosamente.")
    return True


def eliminar_producto(id_producto: int) -> bool:
    """
    Elimina un producto de la lista por su ID.
    
    Args:
        id_producto: ID del producto a eliminar
        
    Returns:
        bool: True si se eliminó, False si no se encontró
    """
    for i, producto in enumerate(productos):
        if producto.get("id") == id_producto:
            nombre = producto.get("nombre")
            productos.remove(producto)
            ids_productos.discard(id_producto)
            print(f"✅ Producto '{nombre}' eliminado exitosamente.")
            return True
    
    print(f"⚠️  Error: No se encontró el producto con ID {id_producto}.")
    return False


def buscar_producto_por_id(id_producto: int) -> Optional[Dict]:
    """
    Busca un producto por su ID.
    
    Args:
        id_producto: ID del producto a buscar
        
    Returns:
        Dict o None: Producto encontrado o None si no existe
    """
    for producto in productos:
        if producto.get("id") == id_producto:
            return producto
    return None


def buscar_productos_por_categoria(categoria: str) -> List[Dict]:
    """
    Busca productos por categoría.
    
    Args:
        categoria: Categoría a buscar
        
    Returns:
        List[Dict]: Lista de productos de esa categoría
    """
    resultado = []
    for producto in productos:
        if producto.get("categoria") == categoria:
            resultado.append(producto)
    return resultado


def buscar_productos_por_nombre(nombre: str) -> List[Dict]:
    """
    Busca productos que contengan el texto en su nombre.
    
    Args:
        nombre: Texto a buscar en el nombre
        
    Returns:
        List[Dict]: Lista de productos que coinciden
    """
    resultado = []
    nombre_lower = nombre.lower()
    for producto in productos:
        if nombre_lower in producto.get("nombre", "").lower():
            resultado.append(producto)
    return resultado


def actualizar_producto(id_producto: int, datos_nuevos: Dict) -> bool:
    """
    Actualiza los datos de un producto existente.
    
    Args:
        id_producto: ID del producto a actualizar
        datos_nuevos: Diccionario con los nuevos valores
        
    Returns:
        bool: True si se actualizó, False si no se encontró
    """
    for producto in productos:
        if producto.get("id") == id_producto:
            # Actualizar usando el método update del diccionario
            producto.update(datos_nuevos)
            print(f"✅ Producto ID {id_producto} actualizado exitosamente.")
            return True
    
    print(f"⚠️  Error: No se encontró el producto con ID {id_producto}.")
    return False


def listar_productos() -> List[Dict]:
    """
    Retorna la lista completa de productos.
    
    Returns:
        List[Dict]: Lista de todos los productos
    """
    return productos.copy()


def obtener_total_productos() -> int:
    """
    Retorna el total de productos registrados.
    
    Returns:
        int: Cantidad de productos
    """
    return len(productos)


# ============================================================================
# FUNCIONES PARA GESTIÓN DE USUARIOS
# ============================================================================

def agregar_usuario(usuario: Dict) -> bool:
    """
    Agrega un usuario a la lista de usuarios.
    
    Args:
        usuario: Diccionario con los datos del usuario
        
    Returns:
        bool: True si se agregó correctamente, False si hubo error
    """
    id_usuario = usuario.get("id")
    email = usuario.get("email")
    
    # Verificar ID duplicado
    if id_usuario in ids_usuarios:
        print(f"⚠️  Error: El usuario con ID {id_usuario} ya existe.")
        return False
    
    # Verificar email duplicado usando set
    if email in emails_registrados:
        print(f"⚠️  Error: El email '{email}' ya está registrado.")
        return False
    
    usuarios.append(usuario)
    ids_usuarios.add(id_usuario)
    emails_registrados.add(email)
    print(f"✅ Usuario '{usuario.get('nombre')}' agregado exitosamente.")
    return True


def eliminar_usuario(id_usuario: int) -> bool:
    """
    Elimina un usuario de la lista por su ID.
    
    Args:
        id_usuario: ID del usuario a eliminar
        
    Returns:
        bool: True si se eliminó, False si no se encontró
    """
    for usuario in usuarios:
        if usuario.get("id") == id_usuario:
            nombre = usuario.get("nombre")
            email = usuario.get("email")
            usuarios.remove(usuario)
            ids_usuarios.discard(id_usuario)
            emails_registrados.discard(email)
            print(f"✅ Usuario '{nombre}' eliminado exitosamente.")
            return True
    
    print(f"⚠️  Error: No se encontró el usuario con ID {id_usuario}.")
    return False


def buscar_usuario_por_id(id_usuario: int) -> Optional[Dict]:
    """
    Busca un usuario por su ID.
    
    Args:
        id_usuario: ID del usuario a buscar
        
    Returns:
        Dict o None: Usuario encontrado o None si no existe
    """
    for usuario in usuarios:
        if usuario.get("id") == id_usuario:
            return usuario
    return None


def buscar_usuario_por_email(email: str) -> Optional[Dict]:
    """
    Busca un usuario por su email.
    
    Args:
        email: Email a buscar
        
    Returns:
        Dict o None: Usuario encontrado o None si no existe
    """
    for usuario in usuarios:
        if usuario.get("email") == email:
            return usuario
    return None


def buscar_usuarios_por_rol(rol: str) -> List[Dict]:
    """
    Busca usuarios por su rol.
    
    Args:
        rol: Rol a buscar
        
    Returns:
        List[Dict]: Lista de usuarios con ese rol
    """
    resultado = []
    for usuario in usuarios:
        if usuario.get("rol") == rol:
            resultado.append(usuario)
    return resultado


def actualizar_usuario(id_usuario: int, datos_nuevos: Dict) -> bool:
    """
    Actualiza los datos de un usuario existente.
    
    Args:
        id_usuario: ID del usuario a actualizar
        datos_nuevos: Diccionario con los nuevos valores
        
    Returns:
        bool: True si se actualizó, False si no se encontró
    """
    for usuario in usuarios:
        if usuario.get("id") == id_usuario:
            # Si cambia el email, actualizar el set
            email_anterior = usuario.get("email")
            email_nuevo = datos_nuevos.get("email")
            
            if email_nuevo and email_nuevo != email_anterior:
                if email_nuevo in emails_registrados:
                    print(f"⚠️  Error: El email '{email_nuevo}' ya está en uso.")
                    return False
                emails_registrados.discard(email_anterior)
                emails_registrados.add(email_nuevo)
            
            usuario.update(datos_nuevos)
            print(f"✅ Usuario ID {id_usuario} actualizado exitosamente.")
            return True
    
    print(f"⚠️  Error: No se encontró el usuario con ID {id_usuario}.")
    return False


def listar_usuarios() -> List[Dict]:
    """
    Retorna la lista completa de usuarios.
    
    Returns:
        List[Dict]: Lista de todos los usuarios
    """
    return usuarios.copy()


def obtener_total_usuarios() -> int:
    """
    Retorna el total de usuarios registrados.
    
    Returns:
        int: Cantidad de usuarios
    """
    return len(usuarios)


# ============================================================================
# FUNCIONES DE REPORTES Y ESTADÍSTICAS
# ============================================================================

def obtener_estadisticas_productos() -> Dict:
    """
    Calcula estadísticas de los productos.
    
    Returns:
        Dict: Diccionario con estadísticas
    """
    if not productos:
        return {
            "total": 0,
            "valor_total_inventario": 0,
            "precio_promedio": 0,
            "producto_mas_caro": None,
            "producto_mas_barato": None,
            "productos_por_categoria": {}
        }
    
    precios = [p.get("precio", 0) for p in productos]
    cantidades = [p.get("cantidad", 0) for p in productos]
    
    # Calcular valor total del inventario
    valor_inventario = sum(
        p.get("precio", 0) * p.get("cantidad", 0) for p in productos
    )
    
    # Contar productos por categoría
    por_categoria = {}
    for producto in productos:
        cat = producto.get("categoria", "Sin categoría")
        por_categoria[cat] = por_categoria.get(cat, 0) + 1
    
    # Encontrar producto más caro y más barato
    producto_caro = max(productos, key=lambda p: p.get("precio", 0))
    producto_barato = min(productos, key=lambda p: p.get("precio", 0))
    
    return {
        "total": len(productos),
        "valor_total_inventario": valor_inventario,
        "precio_promedio": sum(precios) / len(precios),
        "cantidad_total_stock": sum(cantidades),
        "producto_mas_caro": producto_caro,
        "producto_mas_barato": producto_barato,
        "productos_por_categoria": por_categoria
    }


def obtener_estadisticas_usuarios() -> Dict:
    """
    Calcula estadísticas de los usuarios.
    
    Returns:
        Dict: Diccionario con estadísticas
    """
    if not usuarios:
        return {
            "total": 0,
            "edad_promedio": 0,
            "usuarios_por_rol": {},
            "emails_unicos": 0
        }
    
    edades = [u.get("edad", 0) for u in usuarios]
    
    # Contar usuarios por rol
    por_rol = {}
    for usuario in usuarios:
        rol = usuario.get("rol", "Sin rol")
        por_rol[rol] = por_rol.get(rol, 0) + 1
    
    return {
        "total": len(usuarios),
        "edad_promedio": sum(edades) / len(edades),
        "usuarios_por_rol": por_rol,
        "emails_unicos": len(emails_registrados)
    }


def obtener_categorias_disponibles() -> Tuple[str, ...]:
    """
    Retorna las categorías disponibles del sistema.
    
    Returns:
        Tuple[str, ...]: Tupla con las categorías
    """
    return CATEGORIAS_SISTEMA


def obtener_roles_disponibles() -> Tuple[str, ...]:
    """
    Retorna los roles disponibles del sistema.
    
    Returns:
        Tuple[str, ...]: Tupla con los roles
    """
    return ROLES_SISTEMA


def generar_siguiente_id_producto() -> int:
    """
    Genera el siguiente ID disponible para productos.
    
    Returns:
        int: Siguiente ID disponible
    """
    if not ids_productos:
        return 1
    return max(ids_productos) + 1


def generar_siguiente_id_usuario() -> int:
    """
    Genera el siguiente ID disponible para usuarios.
    
    Returns:
        int: Siguiente ID disponible
    """
    if not ids_usuarios:
        return 1
    return max(ids_usuarios) + 1


def limpiar_datos() -> None:
    """
    Limpia todos los datos del sistema (para reiniciar).
    """
    global productos, usuarios, emails_registrados, ids_productos, ids_usuarios
    productos.clear()
    usuarios.clear()
    emails_registrados.clear()
    ids_productos.clear()
    ids_usuarios.clear()
    print("🗑️  Todos los datos han sido eliminados.")
