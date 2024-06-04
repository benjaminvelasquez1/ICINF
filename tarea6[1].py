def show_menu():
    print("\nMenú de opciones:")
    print("1. Ingresar algo a la lista")
    print("2. Modificar algo de la lista según el índice")
    print("3. Eliminar algo de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar algo de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")

def ingresar_element(list):
    element = input("Ingrese el elemento a agregar: ")
    list.append(element)
    print(f"Elemento '{element}' agregado a la lista.")

def mod_element(list):
    try:
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        if 0 <= indice < len(list):
            new_element = input("Ingrese el nuevo valor: ")
            list[indice] = new_element
            print(f"Elemento en el índice {indice} modificado a '{new_element}'.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido para el índice.")

def delete_element(list):
    try:
        indice = int(input("Ingrese el índice del elemento a eliminar: "))
        if 0 <= indice < len(list):
            element_deleted = list.pop(indice)
            print(f"Elemento '{element_deleted}' en el índice {indice} eliminado.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido para el índice.")

def delete_last_element(list):
    if list:
        element_deleted = list.pop()
        print(f"Último elemento '{element_deleted}' eliminado de la lista.")
    else:
        print("La lista está vacía, no se puede eliminar el último elemento.")

def search_element(list):
    element = input("Ingrese el elemento a buscar: ")
    try:
        indice = list.index(element)
        print(f"Elemento '{elemento}' encontrado en el índice {indice}.")
    except ValueError:
        print(f"Elemento '{element}' no encontrado en la lista.")

def show_element(list):
    if list:
        print("Elementos en la lista:")
        for i, element in enumerate(list):
            print(f"{i}: {elemento}")
    else:
        print("La lista está vacía.")

def main():
    list = []
    while True:
        show_menu()
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == '1':
            ingresar_element(list)
        elif opcion == '2':
            mod_element(list)
        elif opcion == '3':
            delete_element(list)
        elif opcion == '4':
            delete_last_element(list)
        elif opcion == '5':
            search_element(list)
        elif opcion == '6':
            show_element(list)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()
