# MI CODIGO AUN NO FUNCIONA JAJAJAJAJA EN MI CASA LO TERMINO
# "Agenda de contactos simple"
# Listas a utilizar
iniciar_bucle = 0
contactos = [["Nombre", "Telefono", "Correo"]]
def mostrar_menu():
    print("\n--- Agenda de Contactos ---\n1. Agregar contacto\n2. Mostrar contactos\n3. Buscar contacto\n4. Salir\n")

def agregar_contacto():
    nombre = input("Ingresa el nombre: ")
    telefono = input("Ingresa el numero de telefono: ")
    correo = input("Ingresa el correo: ")
    contactos.append([nombre, telefono, correo])

def mostrar_contactos():
    for fila in contactos:
        print(fila)

def buscar_contacto():
    buscar = input("Escribe el nombre del contacto a buscar: ")
    for contacto in contactos:
        for opcion in contacto:
            if opcion == buscar:
                print(contacto)

while iniciar_bucle == 0:
    mostrar_menu()
    accion = int(input("Ingrese la opcion: "))
    if accion == 1:
        agregar_contacto()
    elif accion == 2:
        mostrar_contactos()
    elif accion == 3:
        buscar_contacto()
    elif accion == 4:
        break
    else:
        print("Opcion no valida, intente de nuevo.")