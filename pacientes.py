# ===================================
# CRM FOR THERAPISTS - BASIC VERSION
# Patient Management (No Functions)
# ===================================

# =============================
# DATABASE - CLIENT LIST
# =============================
patients = [
    {"id": 1, "nombre_completo": "Ana Torres", "correo": "ana.torres@correo.com", "telefono": "+56 9 42351234", "estado": "Cliente potencial"},
    {"id": 2, "nombre_completo": "Luis Ramírez", "correo": "luis.ramirez@correo.com", "telefono": "+56 9 93481234", "estado": "Alto interés"},
    {"id": 3, "nombre_completo": "Claudia Soto", "correo": "claudia.soto@correo.com", "telefono": "+56 9 78123456", "estado": "Cliente efectivo"},
    {"id": 4, "nombre_completo": "Jorge Fuentes", "correo": "jorge.fuentes@correo.com", "telefono": "+56 9 63547812", "estado": "En proceso de compra"},
    {"id": 5, "nombre_completo": "Marta Herrera", "correo": "marta.herrera@correo.com", "telefono": "+56 9 98124578", "estado": "Super cliente"},
    {"id": 6, "nombre_completo": "Carlos Díaz", "correo": "carlos.diaz@correo.com", "telefono": "+56 9 71234598", "estado": "Alto interés"},
    {"id": 7, "nombre_completo": "Francisca Rojas", "correo": "francisca.rojas@correo.com", "telefono": "+56 9 91234871", "estado": "Cliente efectivo"},
    {"id": 8, "nombre_completo": "Pedro Gutiérrez", "correo": "pedro.gutierrez@correo.com", "telefono": "+56 9 84567213", "estado": "Cliente potencial"},
    {"id": 9, "nombre_completo": "Valentina Bravo", "correo": "valentina.bravo@correo.com", "telefono": "+56 9 78341236", "estado": "Super cliente"},
    {"id": 10, "nombre_completo": "Diego Castro", "correo": "diego.castro@correo.com", "telefono": "+56 9 93456781", "estado": "En proceso de compra"},
    {"id": 11, "nombre_completo": "Camila Paredes", "correo": "camila.paredes@correo.com", "telefono": "+56 9 91234578", "estado": "Cliente potencial"},
    {"id": 12, "nombre_completo": "Andrés Molina", "correo": "andres.molina@correo.com", "telefono": "+56 9 89451236", "estado": "Cliente efectivo"},
    {"id": 13, "nombre_completo": "Patricia Silva", "correo": "patricia.silva@correo.com", "telefono": "+56 9 74382910", "estado": "Alto interés"},
    {"id": 14, "nombre_completo": "Matías Reyes", "correo": "matias.reyes@correo.com", "telefono": "+56 9 87234561", "estado": "En proceso de compra"},
    {"id": 15, "nombre_completo": "Isidora Méndez", "correo": "isidora.mendez@correo.com", "telefono": "+56 9 98127345", "estado": "Super cliente"},
    {"id": 16, "nombre_completo": "Sebastián Núñez", "correo": "sebastian.nunez@correo.com", "telefono": "+56 9 65432178", "estado": "Cliente efectivo"},
    {"id": 17, "nombre_completo": "Fernanda Loyola", "correo": "fernanda.loyola@correo.com", "telefono": "+56 9 72345681", "estado": "Alto interés"},
    {"id": 18, "nombre_completo": "Tomás Aravena", "correo": "tomas.aravena@correo.com", "telefono": "+56 9 83451234", "estado": "Cliente potencial"},
    {"id": 19, "nombre_completo": "Josefa Espinoza", "correo": "josefa.espinoza@correo.com", "telefono": "+56 9 96432187", "estado": "Cliente efectivo"},
    {"id": 20, "nombre_completo": "Ricardo Vergara", "correo": "ricardo.vergara@correo.com", "telefono": "+56 9 78912345", "estado": "Super cliente"}
]

last_id = 20  # Último ID usado

# =============================
# DICTIONARY OF STATES
# =============================
patient_states = {
    1: "Cliente potencial",
    2: "Alto interés",
    3: "En proceso de compra",
    4: "Cliente efectivo",
    5: "Super cliente"
}

# =============================
# WELCOME MESSAGE
# =============================
print("=" * 50)
print("    SISTEMA CRM PARA TERAPEUTAS")
print("    Gestión de Pacientes")
print("=" * 50)

# =============================
# MAIN MENU (while con break)
# =============================
while True:
    print("\n" + "-" * 30)
    print("MENÚ PRINCIPAL")
    print("-" * 30)
    print("1. Agregar nuevo paciente")
    print("2. Listar pacientes")
    print("3. Buscar pacientes")
    print("4. Salir")
    
    option = input("\nSelecciona una opción (1-4): ")
    
    # ============================
    # OPTION 1: ADD PATIENT
    # ============================
    if option == "1":
        print("\n" + "=" * 50)
        print("REGISTRAR NUEVO PACIENTE")
        print("=" * 50)
        
        # Mostrar tipos de paciente
        print("\nSelecciona el tipo de paciente:")
        for key, value in patient_states.items():
            print(f"  {key}. {value}")
        
        patient_type = input("\nIngresa el número (1-5): ")
        
        # Validar tipo
        if patient_type.isdigit():
            patient_type = int(patient_type)
            
            if patient_type in patient_states:
                last_id += 1
                
                print(f"\nRegistrando: {patient_states[patient_type]}")
                print("-" * 30)
                
                # Datos básicos
                first_name = input("Nombre: ")
                last_name = input("Apellido: ")
                nombre_completo = first_name + " " + last_name
                
                # --- VALIDAR RUT ---
                rut_valid = False
                while not rut_valid:
                    rut = input("RUT (12345678-9): ")
                    
                    if "-" in rut:
                        parts = rut.split("-")
                        if len(parts) == 2:
                            number = parts[0]
                            digit = parts[1]
                            
                            if number.isdigit() and 7 <= len(number) <= 8:
                                if digit.isdigit() or digit.upper() == "K":
                                    rut_valid = True
                                else:
                                    print("  ✗ Dígito verificador inválido")
                            else:
                                print("  ✗ Debe tener 7-8 dígitos")
                        else:
                            print("  ✗ Formato inválido")
                    else:
                        print("  ✗ Falta el guión")
                
                # --- VALIDAR TELÉFONO ---
                phone_valid = False
                while not phone_valid:
                    phone = input("Teléfono (+56912345678): ")
                    phone = phone.replace(" ", "")
                    
                    if phone.startswith("+56"):
                        phone_number = phone[3:]
                        if phone_number.isdigit() and len(phone_number) == 9:
                            phone_valid = True
                        else:
                            print("  ✗ Después de +56 van 9 dígitos")
                    
                    elif phone.isdigit() and len(phone) == 9 and phone.startswith("9"):
                        phone = "+56" + phone
                        phone_valid = True
                    
                    else:
                        print("  ✗ Formato inválido")
                
                # --- VALIDAR EMAIL ---
                email_valid = False
                while not email_valid:
                    email = input("Correo: ")
                    
                    at_pos = email.find("@")
                    dot_pos = email.rfind(".")
                    
                    if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
                        # Verificar si ya existe
                        email_exists = False
                        for patient in patients:
                            if patient["correo"].lower() == email.lower():
                                email_exists = True
                                break
                        
                        if email_exists:
                            print("  ✗ Correo ya registrado")
                        else:
                            email_valid = True
                    else:
                        print("  ✗ Formato inválido")
                
                # --- CREAR REGISTRO ---
                new_patient = {
                    "id": last_id,
                    "nombre_completo": nombre_completo,
                    "correo": email,
                    "telefono": phone,
                    "estado": patient_states[patient_type]
                }
                
                patients.append(new_patient)
                
                print("\n✓ Paciente registrado exitosamente")
                print(f"  ID asignado: {last_id}")
            
            else:
                print("\n✗ Tipo de paciente no válido")
        else:
            print("\n✗ Ingresa un número válido")
    
    # ============================
    # OPTION 2: LIST PATIENTS
    # ============================
    elif option == "2":
        
        # --- SUBMENÚ LISTAR (while con break) ---
        while True:
            print("\n" + "-" * 30)
            print("LISTAR PACIENTES")
            print("-" * 30)
            print("1. Listar todos")
            print("2. Listar por estado")
            print("3. Volver al menú principal")
            
            sub_option = input("\nSelecciona (1-3): ")
            
            # --- 2.1 LISTAR TODOS ---
            if sub_option == "1":
                print("\n" + "=" * 50)
                print("TODOS LOS PACIENTES")
                print("=" * 50)
                
                if len(patients) == 0:
                    print("\nNo hay pacientes registrados.")
                else:
                    # FOR para recorrer (no while)
                    for patient in patients:
                        print(f"\n  ID: {patient['id']}")
                        print(f"  Nombre: {patient['nombre_completo']}")
                        print(f"  Correo: {patient['correo']}")
                        print(f"  Teléfono: {patient['telefono']}")
                        print(f"  Estado: {patient['estado']}")
                        print("  " + "-" * 30)
                    
                    print(f"\nTotal: {len(patients)} pacientes")
            
            # --- 2.2 LISTAR POR ESTADO ---
            elif sub_option == "2":
                print("\n" + "-" * 30)
                print("FILTRAR POR ESTADO")
                print("-" * 30)
                
                # Mostrar opciones de estado
                for key, value in patient_states.items():
                    print(f"  {key}. {value}")
                
                state_option = input("\nSelecciona estado (1-5): ")
                
                if state_option.isdigit():
                    state_option = int(state_option)
                    
                    if state_option in patient_states:
                        selected_state = patient_states[state_option]
                        
                        print("\n" + "=" * 50)
                        print(f"PACIENTES: {selected_state.upper()}")
                        print("=" * 50)
                        
                        # Contador para saber si encontramos
                        count = 0
                        
                        # FOR para filtrar (no while)
                        for patient in patients:
                            if patient["estado"] == selected_state:
                                count += 1
                                print(f"\n  ID: {patient['id']}")
                                print(f"  Nombre: {patient['nombre_completo']}")
                                print(f"  Correo: {patient['correo']}")
                                print(f"  Teléfono: {patient['telefono']}")
                                print("  " + "-" * 30)
                        
                        # Resultado del filtro
                        if count == 0:
                            print("\nNo hay pacientes con este estado.")
                        else:
                            print(f"\nTotal: {count} pacientes")
                    
                    else:
                        print("\n✗ Estado no válido")
                else:
                    print("\n✗ Ingresa un número válido")
            
            # --- 2.3 VOLVER ---
            elif sub_option == "3":
                break  # ← BREAK del submenú
            
            else:
                print("\n✗ Opción no válida")
    
    # ============================
    # OPTION 3: SEARCH PATIENTS
    # ============================
    elif option == "3":
        
        # --- SUBMENÚ BUSCAR (while con break) ---
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
            
            # --- 3.1 BUSCAR POR ID ---
            if search_option == "1":
                print("\n" + "-" * 30)
                print("BUSCAR POR ID")
                print("-" * 30)
                
                search_id = input("Ingresa el ID: ")
                
                if search_id.isdigit():
                    search_id = int(search_id)
                    
                    # Bandera para saber si encontramos
                    found = False
                    
                    # FOR para buscar
                    for patient in patients:
                        if patient["id"] == search_id:
                            found = True
                            print("\n✓ Paciente encontrado:")
                            print("  " + "-" * 30)
                            print(f"  ID: {patient['id']}")
                            print(f"  Nombre: {patient['nombre_completo']}")
                            print(f"  Correo: {patient['correo']}")
                            print(f"  Teléfono: {patient['telefono']}")
                            print(f"  Estado: {patient['estado']}")
                            print("  " + "-" * 30)
                            break  # ID es único, salimos del for
                    
                    if not found:
                        print(f"\n✗ No se encontró paciente con ID: {search_id}")
                else:
                    print("\n✗ El ID debe ser un número")
            
            # --- 3.2 BUSCAR POR NOMBRE ---
            elif search_option == "2":
                print("\n" + "-" * 30)
                print("BUSCAR POR NOMBRE")
                print("-" * 30)
                
                search_name = input("Ingresa nombre o parte del nombre: ").strip().lower()
                
                if search_name:
                    print("\n" + "=" * 50)
                    print(f"RESULTADOS PARA: '{search_name}'")
                    print("=" * 50)
                    
                    count = 0
                    
                    # FOR para buscar coincidencias
                    for patient in patients:
                        # Búsqueda parcial (contiene)
                        if search_name in patient["nombre_completo"].lower():
                            count += 1
                            print(f"\n  ID: {patient['id']}")
                            print(f"  Nombre: {patient['nombre_completo']}")
                            print(f"  Correo: {patient['correo']}")
                            print(f"  Teléfono: {patient['telefono']}")
                            print(f"  Estado: {patient['estado']}")
                            print("  " + "-" * 30)
                    
                    if count == 0:
                        print("\n✗ No se encontraron coincidencias")
                    else:
                        print(f"\nTotal encontrados: {count}")
                else:
                    print("\n✗ Debes ingresar un nombre")
            
            # --- 3.3 BUSCAR POR CORREO ---
            elif search_option == "3":
                print("\n" + "-" * 30)
                print("BUSCAR POR CORREO")
                print("-" * 30)
                
                search_email = input("Ingresa correo o parte del correo: ").strip().lower()
                
                if search_email:
                    print("\n" + "=" * 50)
                    print(f"RESULTADOS PARA: '{search_email}'")
                    print("=" * 50)
                    
                    count = 0
                    
                    # FOR para buscar coincidencias
                    for patient in patients:
                        if search_email in patient["correo"].lower():
                            count += 1
                            print(f"\n  ID: {patient['id']}")
                            print(f"  Nombre: {patient['nombre_completo']}")
                            print(f"  Correo: {patient['correo']}")
                            print(f"  Teléfono: {patient['telefono']}")
                            print(f"  Estado: {patient['estado']}")
                            print("  " + "-" * 30)
                    
                    if count == 0:
                        print("\n✗ No se encontraron coincidencias")
                    else:
                        print(f"\nTotal encontrados: {count}")
                else:
                    print("\n✗ Debes ingresar un correo")
            
            # --- 3.4 BUSCAR POR TELÉFONO ---
            elif search_option == "4":
                print("\n" + "-" * 30)
                print("BUSCAR POR TELÉFONO")
                print("-" * 30)
                
                search_phone = input("Ingresa teléfono o parte del número: ").strip()
                # Limpiar espacios para comparar mejor
                search_phone = search_phone.replace(" ", "")
                
                if search_phone:
                    print("\n" + "=" * 50)
                    print(f"RESULTADOS PARA: '{search_phone}'")
                    print("=" * 50)
                    
                    count = 0
                    
                    # FOR para buscar coincidencias
                    for patient in patients:
                        # Limpiar espacios del teléfono guardado
                        phone_clean = patient["telefono"].replace(" ", "")
                        
                        if search_phone in phone_clean:
                            count += 1
                            print(f"\n  ID: {patient['id']}")
                            print(f"  Nombre: {patient['nombre_completo']}")
                            print(f"  Correo: {patient['correo']}")
                            print(f"  Teléfono: {patient['telefono']}")
                            print(f"  Estado: {patient['estado']}")
                            print("  " + "-" * 30)
                    
                    if count == 0:
                        print("\n✗ No se encontraron coincidencias")
                    else:
                        print(f"\nTotal encontrados: {count}")
                else:
                    print("\n✗ Debes ingresar un teléfono")
            
            # --- 3.5 VOLVER ---
            elif search_option == "5":
                break  # ← BREAK del submenú buscar
            
            else:
                print("\n✗ Opción no válida")
    
    # ============================
    # OPTION 4: EXIT
    # ============================
    elif option == "4":
        print("\n¡Gracias por usar el CRM!")
        break  # ← BREAK del menú principal
    
    else:
        print("\n✗ Opción no válida. Selecciona 1, 2, 3 o 4.")

print("Sistema cerrado.")