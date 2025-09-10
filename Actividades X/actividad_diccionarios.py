alumnos = {
    "AL07163611" : {"Nombre" : "Oscar", "Edad" : 17, "Carrera" : "Ing. Software"},
    "AL07291833" : {"Nombre" : "David", "Edad" : 18, "Carrera" : "Ing. Mecatronica"},
    "AL07342732" : {"Nombre" : "Quiroz", "Edad" : 25, "Carrera" : "Ing. Software"}
}
for x, y in alumnos.items():
    print(y["Nombre"])

alumnos["AL07536588"] = {"Nombre" : "Kian", "Edad" : "22", "Carrera" : "Ing. Mecatronica"}

alumnos["AL07342732"]["Edad"] = 18
print(alumnos)

alumnos.pop("AL07536588")
print(alumnos)