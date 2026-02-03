# ============================================================================
# SISTEMA DE GESTIÓN DE PRODUCTOS
# Módulo: menu.py
# Descripción: Sistema de menús iterativos con control de flujo (while, for, break, continue)
# ============================================================================

"""
Módulo de menú.
Contiene funciones para gestionar los menús del sistema utilizando
bucles while y for con control de flujo (break, continue).
"""

from .datos_basicos import (
    capturar_texto, capturar_entero, capturar_decimal,
    crear_producto, crear_usuario, mostrar_producto, mostrar_usuario
)
from .validaciones import (
    validar_texto_no_vacio, validar_email, validar_edad,
    validar_precio, validar_cantidad, validar_rol, validar_categoria,
    ROLES_VALIDOS, CATEGORIAS_VALIDAS
)
from .gestion_datos import (
    agregar_producto, eliminar_producto, buscar_producto_por_id,
    buscar_productos_por_categoria, buscar_productos_por_nombre,
    actualizar_producto, listar_productos, obtener_total_productos,
    agregar_usuario, eliminar_usuario, buscar_usuario_por_id,
    buscar_usuarios_por_rol, listar_usuarios, obtener_total_usuarios,
    obtener_estadisticas_productos, obtener_estadisticas_usuarios,
    generar_siguiente_id_producto, generar_siguiente_id_usuario,
    obtener_categorias_disponibles, obtener_roles_disponibles,
    limpiar_datos
)


def mostrar_encabezado(titulo: str) -> None:
    """
    Muestra un encabezado formateado.
    
    Args:
        titulo: Título a mostrar
    """
    print(f"\n{'='*60}")
    print(f"  {titulo}")
    print(f"{'='*60}")


def mostrar_menu_principal() -> None:
    """Muestra el menú principal del sistema."""
    mostrar_encabezado("🏪 SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("  1. 📦 Gestión de Productos")
    print("  2. 👥 Gestión de Usuarios")
    print("  3. 📊 Reportes y Estadísticas")
    print("  4. ⚙️  Configuración")
    print("  5. 🚪 Salir")
    print(f"{'='*60}")


def mostrar_menu_productos() -> None:
    """Muestra el submenú de productos."""
    mostrar_encabezado("📦 GESTIÓN DE PRODUCTOS")
    print("  1. ➕ Agregar producto")
    print("  2. 📋 Listar todos los productos")
    print("  3. 🔍 Buscar producto por ID")
    print("  4. 🔎 Buscar productos por categoría")
    print("  5. 🔎 Buscar productos por nombre")
    print("  6. ✏️  Editar producto")
    print("  7. 🗑️  Eliminar producto")
    print("  8. ⬅️  Volver al menú principal")
    print(f"{'='*60}")


def mostrar_menu_usuarios() -> None:
    """Muestra el submenú de usuarios."""
    mostrar_encabezado("👥 GESTIÓN DE USUARIOS")
    print("  1. ➕ Agregar usuario")
    print("  2. 📋 Listar todos los usuarios")
    print("  3. 🔍 Buscar usuario por ID")
    print("  4. 🔎 Buscar usuarios por rol")
    print("  5. ✏️  Editar usuario")
    print("  6. 🗑️  Eliminar usuario")
    print("  7. ⬅️  Volver al menú principal")
    print(f"{'='*60}")


def mostrar_menu_reportes() -> None:
    """Muestra el submenú de reportes."""
    mostrar_encabezado("📊 REPORTES Y ESTADÍSTICAS")
    print("  1. 📈 Estadísticas de productos")
    print("  2. 📈 Estadísticas de usuarios")
    print("  3. 📋 Resumen general")
    print("  4. ⬅️  Volver al menú principal")
    print(f"{'='*60}")


def mostrar_menu_configuracion() -> None:
    """Muestra el submenú de configuración."""
    mostrar_encabezado("⚙️  CONFIGURACIÓN")
    print("  1. 📝 Ver categorías disponibles")
    print("  2. 📝 Ver roles disponibles")
    print("  3. 🗑️  Limpiar todos los datos")
    print("  4. ⬅️  Volver al menú principal")
    print(f"{'='*60}")


def solicitar_datos_producto() -> dict:
    """
    Solicita al usuario los datos para crear un producto.
    Usa while para validación y continuar pidiendo datos hasta que sean válidos.
    
    Returns:
        dict: Diccionario con los datos del producto
    """
    print("\n--- Ingreso de nuevo producto ---\n")
    
    # Obtener siguiente ID automáticamente
    id_producto = generar_siguiente_id_producto()
    print(f"📌 ID asignado automáticamente: {id_producto}")
    
    # Solicitar nombre con validación
    nombre = ""
    while True:
        nombre = capturar_texto("📝 Nombre del producto: ")
        valido, mensaje = validar_texto_no_vacio(nombre, "nombre")
        if valido:
            break
        print(f"   ❌ {mensaje}")
        continue
    
    # Solicitar precio con validación
    precio = 0.0
    while True:
        precio = capturar_decimal("💰 Precio: $")
        valido, mensaje = validar_precio(precio)
        if valido:
            break
        print(f"   ❌ {mensaje}")
        continue
    
    # Solicitar cantidad con validación
    cantidad = 0
    while True:
        cantidad = capturar_entero("📦 Cantidad en stock: ")
        valido, mensaje, _ = validar_cantidad(cantidad)
        if valido:
            break
        print(f"   ❌ {mensaje}")
        continue
    
    # Mostrar categorías disponibles y solicitar
    print("\n   Categorías disponibles:")
    categorias = obtener_categorias_disponibles()
    for i, cat in enumerate(categorias, 1):
        print(f"   {i}. {cat}")
    
    categoria = ""
    while True:
        opcion = capturar_entero("   Seleccione categoría (número): ")
        if 1 <= opcion <= len(categorias):
            categoria = categorias[opcion - 1]
            break
        print("   ❌ Opción inválida")
        continue
    
    return crear_producto(id_producto, nombre, precio, cantidad, categoria)


def solicitar_datos_usuario() -> dict:
    """
    Solicita al usuario los datos para crear un usuario.
    
    Returns:
        dict: Diccionario con los datos del usuario
    """
    print("\n--- Ingreso de nuevo usuario ---\n")
    
    # Obtener siguiente ID automáticamente
    id_usuario = generar_siguiente_id_usuario()
    print(f"📌 ID asignado automáticamente: {id_usuario}")
    
    # Solicitar nombre con validación
    nombre = ""
    while True:
        nombre = capturar_texto("👤 Nombre completo: ")
        valido, mensaje = validar_texto_no_vacio(nombre, "nombre")
        if valido:
            break
        print(f"   ❌ {mensaje}")
    
    # Solicitar email con validación
    email = ""
    while True:
        email = capturar_texto("📧 Email: ")
        valido, mensaje = validar_email(email)
        if valido:
            break
        print(f"   ❌ {mensaje}")
    
    # Solicitar edad con validación
    edad = 0
    while True:
        edad = capturar_entero("🎂 Edad: ")
        valido, mensaje, categoria = validar_edad(edad)
        if valido:
            print(f"   ℹ️  Categoría: {categoria}")
            break
        print(f"   ❌ {mensaje}")
    
    # Mostrar roles disponibles y solicitar
    print("\n   Roles disponibles:")
    roles = obtener_roles_disponibles()
    for i, rol in enumerate(roles, 1):
        print(f"   {i}. {rol}")
    
    rol = ""
    while True:
        opcion = capturar_entero("   Seleccione rol (número): ")
        if 1 <= opcion <= len(roles):
            rol = roles[opcion - 1]
            break
        print("   ❌ Opción inválida")
    
    return crear_usuario(id_usuario, nombre, email, edad, rol)


def gestionar_productos() -> None:
    """
    Menú de gestión de productos con bucle while True.
    Usa break para salir y continue para reiniciar el ciclo.
    """
    while True:
        mostrar_menu_productos()
        opcion = capturar_entero("Seleccione una opción: ")
        
        if opcion == 1:
            # Agregar producto
            producto = solicitar_datos_producto()
            agregar_producto(producto)
            
        elif opcion == 2:
            # Listar todos
            productos_lista = listar_productos()
            if not productos_lista:
                print("\n📭 No hay productos registrados.")
                continue
            
            print(f"\n📦 Total de productos: {len(productos_lista)}")
            for producto in productos_lista:
                mostrar_producto(producto)
            
        elif opcion == 3:
            # Buscar por ID
            id_buscar = capturar_entero("🔍 Ingrese ID del producto: ")
            producto = buscar_producto_por_id(id_buscar)
            if producto:
                mostrar_producto(producto)
            else:
                print(f"\n❌ No se encontró producto con ID {id_buscar}")
            
        elif opcion == 4:
            # Buscar por categoría
            print("\n   Categorías disponibles:")
            categorias = obtener_categorias_disponibles()
            for i, cat in enumerate(categorias, 1):
                print(f"   {i}. {cat}")
            
            opcion_cat = capturar_entero("   Seleccione categoría: ")
            if 1 <= opcion_cat <= len(categorias):
                categoria = categorias[opcion_cat - 1]
                productos_cat = buscar_productos_por_categoria(categoria)
                if productos_cat:
                    print(f"\n📦 Productos en '{categoria}': {len(productos_cat)}")
                    for producto in productos_cat:
                        mostrar_producto(producto)
                else:
                    print(f"\n📭 No hay productos en la categoría '{categoria}'")
            else:
                print("   ❌ Opción inválida")
            
        elif opcion == 5:
            # Buscar por nombre
            nombre_buscar = capturar_texto("🔍 Ingrese texto a buscar: ")
            productos_encontrados = buscar_productos_por_nombre(nombre_buscar)
            if productos_encontrados:
                print(f"\n📦 Productos encontrados: {len(productos_encontrados)}")
                for producto in productos_encontrados:
                    mostrar_producto(producto)
            else:
                print(f"\n❌ No se encontraron productos con '{nombre_buscar}'")
            
        elif opcion == 6:
            # Editar producto
            id_editar = capturar_entero("✏️  Ingrese ID del producto a editar: ")
            producto = buscar_producto_por_id(id_editar)
            if producto:
                mostrar_producto(producto)
                print("\nIngrese nuevos valores (Enter para mantener actual):")
                
                nuevo_nombre = capturar_texto(f"   Nombre [{producto['nombre']}]: ")
                nuevo_precio_str = capturar_texto(f"   Precio [${producto['precio']:.2f}]: ")
                nueva_cantidad_str = capturar_texto(f"   Cantidad [{producto['cantidad']}]: ")
                
                datos_nuevos = {}
                if nuevo_nombre:
                    datos_nuevos["nombre"] = nuevo_nombre
                if nuevo_precio_str:
                    try:
                        datos_nuevos["precio"] = float(nuevo_precio_str)
                    except ValueError:
                        print("   ⚠️  Precio inválido, se mantiene el actual")
                if nueva_cantidad_str:
                    try:
                        datos_nuevos["cantidad"] = int(nueva_cantidad_str)
                    except ValueError:
                        print("   ⚠️  Cantidad inválida, se mantiene la actual")
                
                if datos_nuevos:
                    actualizar_producto(id_editar, datos_nuevos)
                else:
                    print("   ℹ️  No se realizaron cambios")
            else:
                print(f"\n❌ No se encontró producto con ID {id_editar}")
            
        elif opcion == 7:
            # Eliminar producto
            id_eliminar = capturar_entero("🗑️  Ingrese ID del producto a eliminar: ")
            producto = buscar_producto_por_id(id_eliminar)
            if producto:
                mostrar_producto(producto)
                confirmacion = capturar_texto("¿Confirma eliminar? (s/n): ")
                if confirmacion.lower() == 's':
                    eliminar_producto(id_eliminar)
                else:
                    print("   ℹ️  Operación cancelada")
            else:
                print(f"\n❌ No se encontró producto con ID {id_eliminar}")
            
        elif opcion == 8:
            # Volver al menú principal
            print("\n⬅️  Volviendo al menú principal...")
            break
            
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            continue
        
        input("\nPresione Enter para continuar...")


def gestionar_usuarios() -> None:
    """
    Menú de gestión de usuarios con bucle while True.
    """
    while True:
        mostrar_menu_usuarios()
        opcion = capturar_entero("Seleccione una opción: ")
        
        if opcion == 1:
            # Agregar usuario
            usuario = solicitar_datos_usuario()
            agregar_usuario(usuario)
            
        elif opcion == 2:
            # Listar todos
            usuarios_lista = listar_usuarios()
            if not usuarios_lista:
                print("\n📭 No hay usuarios registrados.")
                continue
            
            print(f"\n👥 Total de usuarios: {len(usuarios_lista)}")
            for usuario in usuarios_lista:
                mostrar_usuario(usuario)
            
        elif opcion == 3:
            # Buscar por ID
            id_buscar = capturar_entero("🔍 Ingrese ID del usuario: ")
            usuario = buscar_usuario_por_id(id_buscar)
            if usuario:
                mostrar_usuario(usuario)
            else:
                print(f"\n❌ No se encontró usuario con ID {id_buscar}")
            
        elif opcion == 4:
            # Buscar por rol
            print("\n   Roles disponibles:")
            roles = obtener_roles_disponibles()
            for i, rol in enumerate(roles, 1):
                print(f"   {i}. {rol}")
            
            opcion_rol = capturar_entero("   Seleccione rol: ")
            if 1 <= opcion_rol <= len(roles):
                rol = roles[opcion_rol - 1]
                usuarios_rol = buscar_usuarios_por_rol(rol)
                if usuarios_rol:
                    print(f"\n👥 Usuarios con rol '{rol}': {len(usuarios_rol)}")
                    for usuario in usuarios_rol:
                        mostrar_usuario(usuario)
                else:
                    print(f"\n📭 No hay usuarios con el rol '{rol}'")
            else:
                print("   ❌ Opción inválida")
            
        elif opcion == 5:
            # Editar usuario
            id_editar = capturar_entero("✏️  Ingrese ID del usuario a editar: ")
            usuario = buscar_usuario_por_id(id_editar)
            if usuario:
                mostrar_usuario(usuario)
                print("\nIngrese nuevos valores (Enter para mantener actual):")
                
                nuevo_nombre = capturar_texto(f"   Nombre [{usuario['nombre']}]: ")
                nuevo_email = capturar_texto(f"   Email [{usuario['email']}]: ")
                nueva_edad_str = capturar_texto(f"   Edad [{usuario['edad']}]: ")
                
                datos_nuevos = {}
                if nuevo_nombre:
                    datos_nuevos["nombre"] = nuevo_nombre
                if nuevo_email:
                    valido, _ = validar_email(nuevo_email)
                    if valido:
                        datos_nuevos["email"] = nuevo_email
                    else:
                        print("   ⚠️  Email inválido, se mantiene el actual")
                if nueva_edad_str:
                    try:
                        nueva_edad = int(nueva_edad_str)
                        valido, _, _ = validar_edad(nueva_edad)
                        if valido:
                            datos_nuevos["edad"] = nueva_edad
                        else:
                            print("   ⚠️  Edad inválida, se mantiene la actual")
                    except ValueError:
                        print("   ⚠️  Edad inválida, se mantiene la actual")
                
                if datos_nuevos:
                    from .gestion_datos import actualizar_usuario
                    actualizar_usuario(id_editar, datos_nuevos)
                else:
                    print("   ℹ️  No se realizaron cambios")
            else:
                print(f"\n❌ No se encontró usuario con ID {id_editar}")
            
        elif opcion == 6:
            # Eliminar usuario
            id_eliminar = capturar_entero("🗑️  Ingrese ID del usuario a eliminar: ")
            usuario = buscar_usuario_por_id(id_eliminar)
            if usuario:
                mostrar_usuario(usuario)
                confirmacion = capturar_texto("¿Confirma eliminar? (s/n): ")
                if confirmacion.lower() == 's':
                    eliminar_usuario(id_eliminar)
                else:
                    print("   ℹ️  Operación cancelada")
            else:
                print(f"\n❌ No se encontró usuario con ID {id_eliminar}")
            
        elif opcion == 7:
            # Volver al menú principal
            print("\n⬅️  Volviendo al menú principal...")
            break
            
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            continue
        
        input("\nPresione Enter para continuar...")


def mostrar_reportes() -> None:
    """
    Menú de reportes y estadísticas.
    """
    while True:
        mostrar_menu_reportes()
        opcion = capturar_entero("Seleccione una opción: ")
        
        if opcion == 1:
            # Estadísticas de productos
            from .funciones_utiles import mostrar_estadisticas_productos
            mostrar_estadisticas_productos()
            
        elif opcion == 2:
            # Estadísticas de usuarios
            from .funciones_utiles import mostrar_estadisticas_usuarios
            mostrar_estadisticas_usuarios()
            
        elif opcion == 3:
            # Resumen general
            from .funciones_utiles import mostrar_resumen_general
            mostrar_resumen_general()
            
        elif opcion == 4:
            print("\n⬅️  Volviendo al menú principal...")
            break
            
        else:
            print("\n❌ Opción no válida.")
            continue
        
        input("\nPresione Enter para continuar...")


def gestionar_configuracion() -> None:
    """
    Menú de configuración del sistema.
    """
    while True:
        mostrar_menu_configuracion()
        opcion = capturar_entero("Seleccione una opción: ")
        
        if opcion == 1:
            # Ver categorías
            print("\n📋 Categorías disponibles en el sistema:")
            categorias = obtener_categorias_disponibles()
            for i, cat in enumerate(categorias, 1):
                print(f"   {i}. {cat}")
            
        elif opcion == 2:
            # Ver roles
            print("\n📋 Roles disponibles en el sistema:")
            roles = obtener_roles_disponibles()
            for i, rol in enumerate(roles, 1):
                print(f"   {i}. {rol}")
            
        elif opcion == 3:
            # Limpiar datos
            print("\n⚠️  ADVERTENCIA: Esta acción eliminará TODOS los datos.")
            confirmacion = capturar_texto("¿Está seguro? Escriba 'CONFIRMAR': ")
            if confirmacion == "CONFIRMAR":
                limpiar_datos()
            else:
                print("   ℹ️  Operación cancelada")
            
        elif opcion == 4:
            print("\n⬅️  Volviendo al menú principal...")
            break
            
        else:
            print("\n❌ Opción no válida.")
            continue
        
        input("\nPresione Enter para continuar...")


def ejecutar_menu_principal() -> None:
    """
    Ejecuta el menú principal del sistema.
    Bucle principal con while True y break para salir.
    """
    print("\n" + "🎉" * 20)
    print("   ¡Bienvenido al Sistema de Gestión de Productos!")
    print("🎉" * 20)
    
    while True:
        mostrar_menu_principal()
        opcion = capturar_entero("Seleccione una opción: ")
        
        if opcion == 1:
            gestionar_productos()
            
        elif opcion == 2:
            gestionar_usuarios()
            
        elif opcion == 3:
            mostrar_reportes()
            
        elif opcion == 4:
            gestionar_configuracion()
            
        elif opcion == 5:
            print("\n" + "👋" * 20)
            print("   ¡Gracias por usar el sistema!")
            print("   Hasta pronto.")
            print("👋" * 20 + "\n")
            break
            
        else:
            print("\n❌ Opción no válida. Por favor, seleccione del 1 al 5.")
            continue
