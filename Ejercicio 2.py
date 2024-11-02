'''Ejercicio 2: Dado un diccionario con notas de estudiantes, calcular el promedio de las notas.  len sum iteraciones'''
notas = {
    'Deltron': 4,
    'Andy': 5,
    'Marshall': 2,
    'Leo': 2,
    'Franco': 0

}

notas_totales = sum(notas.values())
alumnos = 0

for i in notas:
    alumnos += 1

promedio = notas_totales/ alumnos

print(f'Las notas son: \nDeltron: {notas['Deltron']} \nAndy: {notas['Andy']} \nMarshall: {notas['Marshall']} \nLeo {notas['Leo']} \nFranco: {notas['Franco']} \nEl promedio de las notas es: {promedio}')