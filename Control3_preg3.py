def potencia(num, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / potencia(num, -exp)
    else:
        return num * potencia(num, exp - 1)


numero = int(input("Ingrese el número base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(numero, exponente)
print(f"{numero} elevado a la potencia {exponente} es: {resultado}")
