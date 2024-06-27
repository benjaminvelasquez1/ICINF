precios_dolar=[]
usd_clp=950

for i in range(10):
    precio=float(input("Ingrese precio en dolar: "))
    precios_dolar.append(precio)

precios_clp=[precio*usd_clp for precio in precios_dolar]

print("Lista de precios en CLP")
for precio in precios_clp:
    print("$", precio)