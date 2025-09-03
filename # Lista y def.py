# Lista y def
numeros = [1,3, 45, 65, 567, 45, 34]
def lista_creciente(numeros):
    numeros.sort()
    # Esto es para imprimir una lista ya definida de puros numeros de mayor a menor
    print(numeros)

lista_creciente(numeros)

def lista_decreciente(numeros):
    numeros.sort(reverse = True)
    # Esto es para imprimir una lista ya definida de puros numeros de menor a mayor
    print(numeros)

lista_decreciente(numeros)