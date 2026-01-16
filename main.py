# ===================================
# MAIN.PY - Controlador principal
# ===================================

# Importar módulos
from data import patients, patient_states, last_id
from search import search_menu
from list import list_menu


# =============================
# WELCOME MESSAGE
# =============================
print("=" * 50)
print("    SISTEMA CRM PARA TERAPEUTAS")
print("    Gestión de Pacientes")
print("=" * 50)


# =============================
# MAIN MENU
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
        list_menu()  # ← Llamada al módulo list.py
    
    # ============================
    # OPTION 3: SEARCH PATIENTS
    # ============================
    elif option == "3":
        search_menu()  # ← Llamada al módulo search.py
    
    # ============================
    # OPTION 4: EXIT
    # ============================
    elif option == "4":
        print("\n¡Gracias por usar el CRM!")
        break
    
    else:
        print("\n✗ Opción no válida. Selecciona 1, 2, 3 o 4.")

print("Sistema cerrado.")