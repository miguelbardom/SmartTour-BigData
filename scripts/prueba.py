# creamos dos conjuntos en python con el nombre de 5 alumnos de dos clases

# cargamos los datos de un csv
import csv

grupo1 = set()  # no es ni necesario
grupo2 = set()

# grupo1 = {"Miguel", "Marco", "Clara", "Pedro", "Ana"}
# grupo2 = {"Ana", "Lucas", "Jose Luis", "Marco", "Sebas"}

with open("grupo1.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        grupo1.add(fila[0])

with open("grupo2.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        grupo2.add(fila[0])

# union |
union = grupo1 | grupo2

# interseccion &
interseccion = grupo1 & grupo2

# diferencia -
diferencia = grupo1 - grupo2

# diferencia simetrica ^
simetrica = grupo1 ^ grupo2

print("Grupo 1: ", grupo1)
print("Grupo 2: ", grupo2)

print("Union: ", union)
print("Intersección: ", interseccion)
print("Diferencia: ", diferencia)
print("Diferencia simétrica: ", simetrica)
