def digitos(num):
    num_str=str(num)
    return len(num_str)


numero=input("Ingrese un numero: ")

cantidad_digitos=digitos(numero)
print(f"La cantidad de digitos del numero ingresado es: {cantidad_digitos}")