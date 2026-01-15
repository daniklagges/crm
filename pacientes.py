# ==================================================
# BASE DE DATOS (Lista de diccionarios)
# ==================================================
pacientes = []

# ==================================================
# CONTADOR PARA ID AUTOINCREMENTAL
# ==================================================
ultimo_id = 0

# ==================================================
# DICCIONARIO DE ESTADOS (Switch simulado)
# ==================================================
estados_paciente = {
    1: "Paciente potencial",
    2: "Paciente con alto interés",
    3: "En proceso de compra",
    4: "Cliente efectivo",
    5: "Super cliente"
}

# ==================================================
# MENSAJE DE BIENVENIDA
# ==================================================
print("=" * 50)
print("    SISTEMA CRM PARA TERAPEUTAS")
print("    Gestión de Pacientes")
print("=" * 50)

# ==================================================
# MENÚ PRINCIPAL
# ==================================================
continuar = True

while continuar:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar nuevo paciente")
    print("2. Ver todos los pacientes")
    print("3. Salir")

    opcion = input("\nSelecciona una opción (1-3): ")

    # ==================================================
    # OPCIÓN 1: AGREGAR PACIENTE
    # ==================================================
    if opcion == "1":
        print("\n" + "=" * 50)
        print("REGISTRAR NUEVO PACIENTE")
        print("=" * 50)

        print("\nSelecciona el tipo de paciente:")
        for clave, valor in estados_paciente.items():
            print(f"{clave}. {valor}")

        try:
            tipo_paciente = int(input("\nIngresa el número (1-5): "))

            if tipo_paciente in estados_paciente:
                ultimo_id += 1

                print(f"\nRegistrando paciente como: {estados_paciente[tipo_paciente]}")
                print("-" * 50)

                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                telefono = input("Teléfono: ")
                correo = input("Correo electrónico: ")

                nuevo_paciente = {
                    "id": ultimo_id,
                    "nombre": nombre,
                    "apellido": apellido,
                    "telefono": telefono,
                    "correo": correo,
                    "estado": estados_paciente[tipo_paciente],
                    "comentarios": []
                }

                pacientes.append(nuevo_paciente)

                print("\n✓ ¡Paciente registrado exitosamente!")
                print(f"ID asignado: {ultimo_id}")

            else:
                print("\n✗ Error: Tipo de paciente no válido")

        except ValueError:
            print("\n✗ Error: Debes ingresar un número válido")

    # ==================================================
    # OPCIÓN 2: VER PACIENTES
    # ==================================================
    elif opcion == "2":
        print("\n" + "=" * 50)
        print("LISTA DE PACIENTES REGISTRADOS")
        print("=" * 50)

        if len(pacientes) == 0:
            print("\nNo hay pacientes registrados aún.")
        else:
            for paciente in pacientes:
                print(f"\nID: {paciente['id']}")
                print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
                print(f"Teléfono: {paciente['telefono']}")
                print(f"Correo: {paciente['correo']}")
                print(f"Estado: {paciente['estado']}")
                print(f"Comentarios registrados: {len(paciente['comentarios'])}")
                print("-" * 50)

            print(f"\nTotal de pacientes: {len(pacientes)}")

    # ==================================================
    # OPCIÓN 3: SALIR
    # ==================================================
    elif opcion == "3":
        print("\n¡Gracias por usar el CRM!")
        print("Cerrando sistema...")
        continuar = False

    # ==================================================
    # OPCIÓN INVÁLIDA
    # ==================================================
    else:
        print("\n✗ Opción no válida. Por favor selecciona 1, 2 o 3.")

print("\nSistema cerrado.")
