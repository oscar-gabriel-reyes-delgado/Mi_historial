matriz = []

def dispositivos():
    numero_dispositivos = int(input("Ingresa el numero de dispositivos: "))
    return numero_dispositivos

def solicitud_dispositivos():
    for i in range(num_dispositivos):
        nombre = input("\nEscriba el nombre del dispositivo: ")
        consumo_wats = float(input("Escribe el consumo en watts: "))
        horas = float(input("Escribe las horas de consumo diario: "))
        costo_kwh = float(input("Escribe el costo por kWh en pesos (MXN): "))
        matriz.append([nombre, consumo_wats, horas, costo_kwh])

def menu():
    print("\n- - - Menu - - -\n1. Mostrar dispositivos\n2. Consultar gasto energetico y costo mensual\n3. Calcular costo y gasto de todos los dispositivos\n4. Salir")

def mostrar_dispositivos():
    for lista in matriz:
        print("Nombre:", lista[0], "\tConsumo:", lista[1], "watts\tHoras de uso", lista[2], "hrs\tCosto kWh:", lista[3], "pesos")

def gasto_consumo_mensual():
    buscar = input("¿Cual nombre del dispositivo para consultar su gasto energetico y costo mensual?\nEscribe: ")
    for lista in matriz:
        for opcion in lista:
            if buscar == opcion:
                consumo_mensual = lista[1] * lista[2] * 30 
                gasto_mensual =  lista[3] * lista[2]* 30
                print("El consumo mensual es de", consumo_mensual, "watts, y el costo mensual es de", gasto_mensual, "pesos")

sumatoria_consumo = 0
sumatoria_costo = 0
def consumo_gasto_total(sumatoria_consumo, sumatoria_costo):
    for fila in matriz:
        consumo_mensual = fila[1] * fila[2] * 30
        costo_mensual = fila[3] * fila[2] * 30
        sumatoria_consumo += consumo_mensual
        sumatoria_costo += costo_mensual
    print("El consumo mensual de todos los dispositivos es de", sumatoria_consumo, "watts, y el costo total mensual de todos los dispositivos es de", sumatoria_costo, "pesos")


num_dispositivos = int(input("¿Cuantos dispositivos registrara?\nResponde:"))
solicitud_dispositivos()

iniciar = 1
while iniciar != 0:
    menu()
    opcion_menu = input("Escribe el numero de la opcion: ")
    if opcion_menu == "1":
        mostrar_dispositivos()
    elif opcion_menu == "2":
        gasto_consumo_mensual()
    elif opcion_menu == "3":
        consumo_gasto_total(sumatoria_consumo, sumatoria_costo)
    elif opcion_menu == "4":
        break
    else:
        print("Opcion invalida, escribe el numero de la opcion")