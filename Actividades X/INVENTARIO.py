inventario = {}

def menu():
    print("\n = = = Menu = = =\n1. Mostrar inventario\n2. Agregar producto\n3. Actualizar cantidad\n4. Eliminar producto")

def mostrar_inventario(inventario):
    print("\n| Material\t| Cantidad \t|")
    for material, cantidad in inventario.items():
        print("|", material, "\t|", cantidad, "\t|")

def agregar_producto(inventario):
    nombre = input("\nEscribe el nombre: ")
    cantidad = input("Escribe la cantidad: ")
    inventario[nombre] = cantidad

def update(inventario):
    cambiar = input("De que objeto desea cambiar cantidad?: ")
    update = input("Cantidad nueva: ")
    existe = False
    for nombre, cantidad in inventario.items():
        if cambiar == nombre:
            existe = True
    if existe == True:
        update = input("Cantidad nueva: ")
        inventario[cambiar] = update
    elif existe == False:
        print("El objeto no existe")

iniciar = True
while iniciar == True:
    menu()
    respuesta = input("\nIngrese el numero de la opcion: ")
    if respuesta == "1":
        mostrar_inventario(inventario)
    elif respuesta == "2":
        agregar_producto(inventario)
    elif respuesta == "3":
        update(inventario)
    