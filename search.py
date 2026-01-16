# ===================================
# SEARCH.PY - Módulo de búsqueda
# ===================================

# Importar datos desde data.py
from data import patients


# =============================
# HELPER: MOSTRAR UN PACIENTE
# =============================
def show_patient(patient):
    """Muestra los datos de un paciente"""
    print(f"\n  ID: {patient['id']}")
    print(f"  Nombre: {patient['nombre_completo']}")
    print(f"  Correo: {patient['correo']}")
    print(f"  Teléfono: {patient['telefono']}")
    print(f"  Estado: {patient['estado']}")
    print("  " + "-" * 30)


# =============================
# BUSCAR POR ID
# =============================
def search_by_id():
    """Busca un paciente por su ID (búsqueda exacta)"""
    print("\n" + "-" * 30)
    print("BUSCAR POR ID")
    print("-" * 30)
    
    search_id = input("Ingresa el ID: ")
    
    if search_id.isdigit():
        search_id = int(search_id)
        found = False
        
        for patient in patients:
            if patient["id"] == search_id:
                found = True
                print("\n✓ Paciente encontrado:")
                show_patient(patient)
                break
        
        if not found:
            print(f"\n✗ No se encontró paciente con ID: {search_id}")
    else:
        print("\n✗ El ID debe ser un número")


# =============================
# BUSCAR POR NOMBRE
# =============================
def search_by_name():
    """Busca pacientes por nombre (búsqueda parcial)"""
    print("\n" + "-" * 30)
    print("BUSCAR POR NOMBRE")
    print("-" * 30)
    
    search_name = input("Ingresa nombre o parte del nombre: ").strip().lower()
    
    if search_name:
        print("\n" + "=" * 50)
        print(f"RESULTADOS PARA: '{search_name}'")
        print("=" * 50)
        
        count = 0
        
        for patient in patients:
            if search_name in patient["nombre_completo"].lower():
                count += 1
                show_patient(patient)
        
        if count == 0:
            print("\n✗ No se encontraron coincidencias")
        else:
            print(f"\nTotal encontrados: {count}")
    else:
        print("\n✗ Debes ingresar un nombre")


# =============================
# BUSCAR POR CORREO
# =============================
def search_by_email():
    """Busca pacientes por correo (búsqueda parcial)"""
    print("\n" + "-" * 30)
    print("BUSCAR POR CORREO")
    print("-" * 30)
    
    search_email = input("Ingresa correo o parte del correo: ").strip().lower()
    
    if search_email:
        print("\n" + "=" * 50)
        print(f"RESULTADOS PARA: '{search_email}'")
        print("=" * 50)
        
        count = 0
        
        for patient in patients:
            if search_email in patient["correo"].lower():
                count += 1
                show_patient(patient)
        
        if count == 0:
            print("\n✗ No se encontraron coincidencias")
        else:
            print(f"\nTotal encontrados: {count}")
    else:
        print("\n✗ Debes ingresar un correo")


# =============================
# BUSCAR POR TELÉFONO
# =============================
def search_by_phone():
    """Busca pacientes por teléfono (búsqueda parcial)"""
    print("\n" + "-" * 30)
    print("BUSCAR POR TELÉFONO")
    print("-" * 30)
    
    search_phone = input("Ingresa teléfono o parte del número: ").strip()
    search_phone = search_phone.replace(" ", "")
    
    if search_phone:
        print("\n" + "=" * 50)
        print(f"RESULTADOS PARA: '{search_phone}'")
        print("=" * 50)
        
        count = 0
        
        for patient in patients:
            phone_clean = patient["telefono"].replace(" ", "")
            
            if search_phone in phone_clean:
                count += 1
                show_patient(patient)
        
        if count == 0:
            print("\n✗ No se encontraron coincidencias")
        else:
            print(f"\nTotal encontrados: {count}")
    else:
        print("\n✗ Debes ingresar un teléfono")


# =============================
# MENÚ DE BÚSQUEDA
# =============================
def search_menu():
    """Submenú de búsqueda con todas las opciones"""
    while True:
        print("\n" + "-" * 30)
        print("BUSCAR PACIENTES")
        print("-" * 30)
        print("1. Buscar por ID")
        print("2. Buscar por nombre")
        print("3. Buscar por correo")
        print("4. Buscar por teléfono")
        print("5. Volver al menú principal")
        
        search_option = input("\nSelecciona (1-5): ")
        
        if search_option == "1":
            search_by_id()
        
        elif search_option == "2":
            search_by_name()
        
        elif search_option == "3":
            search_by_email()
        
        elif search_option == "4":
            search_by_phone()
        
        elif search_option == "5":
            break
        
        else:
            print("\n✗ Opción no válida")