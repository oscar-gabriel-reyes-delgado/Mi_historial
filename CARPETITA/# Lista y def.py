# Lista y def

# Notas: El lista.sort()
# Se deja vacio el parentesis para que te acomode los numeros de menor a mayor
# Se pone reverse=True dentro del parentesis para que se acomoden de mayor a menor


numeros = [1,3, 45, 65, 567, 45, 34]
def lista_creciente(numeros):
    numeros.sort()
    print(numeros)

lista_creciente(numeros)

def lista_decreciente(numeros):
    numeros.sort(reverse = True)
    print(numeros)

lista_decreciente(numeros)