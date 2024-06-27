notas = []
while True:
    nota = float(input("Ingresa una nota (0 para terminar): "))
    if nota == 0:
        break
    notas.append(nota)

cantidad_notas = len(notas)
promedio = sum(notas) / cantidad_notas if cantidad_notas > 0 else 0
if nota<4.0:
    cantidad_bajo_4=+1
cantidad_igual_o_mayor_4 = len([nota for nota in notas if nota >= 4.0])

print("Cantidad de notas: ", cantidad_notas)
print("Promedio de notas: ", promedio)
print("Cantidad de notas bajo 4.0: ", cantidad_bajo_4)
print("Cantidad de notas igual o mayor a 4.0: ", cantidad_igual_o_mayor_4)
