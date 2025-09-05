# Areas figuras geometricas
def menu():
    print("\nSelecciona una figura para calcular el area\n1. Cuadrado\n2. Rectangulo\n3. Circulo\n4. Salir\n")
    opcion = input("Ingresa el numero de la opcion deseada: ")
    return opcion

def area_cuadrado():
    lado = float(input("Escribe el largo del cuadrado: "))
    return lado * lado

def area_rectangulo():
    base = float(input("Ingresa el valor de la base del cuadrado: "))
    altura = float(input("El valor del alto del cuadrado: "))
    return base * altura

def area_circulo():
    radio = float(input("Escribe el radio del circulo: "))
    return 3.1416 * radio**2

iniciar = 1
while iniciar != 0:
    menu_opcion = menu()
    if menu_opcion == "1":
        resultado =  area_cuadrado()
        print("El area del cuadrado es", resultado)
    elif menu_opcion == "2":
        resultado = area_rectangulo()
        print("El area del rectangulo es", resultado)
    elif menu_opcion == "3":
        resultado = area_circulo()
        print("El area del circulo es", resultado)
    elif menu_opcion == "4":
        print("Programa terminado")
        break
    else:
        print("Opcion invalida, intente de nuevo")