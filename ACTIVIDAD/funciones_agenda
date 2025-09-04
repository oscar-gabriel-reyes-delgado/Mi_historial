def mostrar_menu():
    print("\n--- Agenda de Contactos ---\n1. Agregar contacto\n2. Mostrar contactos\n3. Buscar contacto\n4. Salir\n")

def agregar_contacto():
    nombre = input("Ingresa el nombre: ")
    telefono = input("Ingresa el numero de telefono: ")
    correo = input("Ingresa el correo: ")
    contactos.append([nombre, telefono, correo])

def mostrar_contactos():
    print("\nEsta es la lista de tus contactos:")
    for fila in contactos:
        print("Nombre:", fila[0], "\tNumero Telefonico:", fila[1], "\tCorreo:", fila[2])

def buscar_contacto():
    buscar = input("Escribe el nombre del contacto a buscar: ")
    for contacto in contactos:
        for opcion in contacto:
            if opcion == buscar:
                print("Aqui esta el contacto que buscas:")
                print("Nombre:", contacto[0], "\tNumero Telefonico:", contacto[1], "\tCorreo:", contacto[2])
            else: print("\nNo se encontro el contacto\n")