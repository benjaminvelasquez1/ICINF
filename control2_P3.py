palabras=[]
print("Ingrese una palabra a la lista: ")

while True:
    palabra=input("Ingrese una palabra: ")
    if palabra=="":
        break
    palabras.append(palabra)

longitud_maxima=0
for palabra in palabras:
    if len(palabra)>longitud_maxima:
        longitud_maxima=len(palabra)

if palabras:
    print("La palabra con mayor cantidad de caracteres tiene", longitud_maxima, "caracteres")
else:
    print("No se ingresaron palabras")


