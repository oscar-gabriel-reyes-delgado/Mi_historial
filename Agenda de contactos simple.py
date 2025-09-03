# MI CODIGO AUN NO FUNCIONA JAJAJAJAJA EN MI CASA LO TERMINO
# "Agenda de contactos simple"
#Listas a utilizar
iniciar_bucle = 0
contactos = [
    ["Nombre", "Telefono", "Correo"]
]
def mostrar_menu():
    print("\n--- Agenda de Contactos ---\n1. Agregar contacto\n2. Mostrar contactos\n3. Buscar contacto\n4. Salir\n")

def agregar_contacto():
    nombre = input("Ingresa el nombre: ")
    telefono = int(input("Ingresa el numero de telefono: "))
    correo = input("Ingresa el correo: ")
    contactos.append([nombre, telefono, correo])

def mostrar_contactos():
    for fila in contactos:
        print(fila, "\n")

def buscar_contacto():
    buscar = input("Escribe el nombre del contacto a buscar: ")
    for contacto in contactos:
        if buscar in contacto == True:
            print(contacto)
        elif buscar in contacto == False:

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
        continue