def es_binario(var):
    for i in var:
        if i !="0" and i !="1":
            return False
    return True

cadena=input("Ingrese una cadena: ")

if es_binario(cadena):
    print(f"La cadena {cadena} es una expresion binaria.")
else:
    print(f"La cadena {cadena} no es una expresion binaria.")