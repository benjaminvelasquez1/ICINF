def cont_vocal_consonant(palabra):
    vocal = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    num_vocal = 0
    num_consonant = 0
    
    for letra in palabra:
        if letra.isalpha():
            if letra in vocal:
                num_vocal += 1
            else:
                num_consonant += 1
    
    return num_vocal, num_consonant

def main():
    palabras = []
    
    print("Introduce palabras (deja en blanco y presiona Enter para finalizar):")
    while True:
        palabra = input()
        if palabra == "":
            break
        palabras.append(palabra)
    
    for palabra in palabras:
        vocal, consonant = cont_vocal_consonant(palabra)
        print(f"Palabra: {palabra}, Vocales: {vocal}, Consonantes: {consonant}")

if __name__ == "__main__":
    main()
