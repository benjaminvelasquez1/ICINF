capitales_paises={}

for i in range(5):
    capital=input("Ingrese el nombre de la capital: ")
    pais=input("Ingrese el pais de la capital: ")
    capitales_paises[capital]=pais

nombre_turista=input("Ingrese el nombre del turista: ")
capital_procedencia=input("Ingrese de que capital viene el turista: ")

if capital_procedencia in capitales_paises:
    pais_procedencia=capitales_paises[capital_procedencia]
    print("El turista con el nombre", nombre_turista, "viene de la capital", capital_procedencia, "y su pais es", pais_procedencia)
else:
    print("La capital", capital_procedencia, "NO se encuntra en el diccionario")