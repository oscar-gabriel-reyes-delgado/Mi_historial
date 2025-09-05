lista_materias = ["calculo", "quimica", "civica_y_etica", "lengua_materna", "ingles", "geografia"]
print(lista_materias[0], lista_materias[-1])
print("=============================================")
#####################################################
lista_nombres = []
for limite in range(5):
    lista_nombres.append(input("Escribe un nombre: "))
print(lista_nombres[::-1])
print("=============================================")
#####################################################
lista_temperaturas = [45.3, 23.6, 56.7, 98.7, 34.5]
promedio = sum(lista_temperaturas)/len(lista_temperaturas)
print("El promedio de temperaturas es", promedio)
print("La temperatura maxima es", max(lista_temperaturas))
print("La temperatura minima es", min(lista_temperaturas))
