import time

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def busqueda_binaria(lista, elemento):
    lim_inicio, lim_fin = 0, len(lista) - 1

    while lim_inicio <= lim_fin:
        mitad = (lim_inicio + lim_fin) // 2
        if lista[mitad] == elemento:
            return mitad
        elif lista[mitad] < elemento:
            lim_inicio = mitad + 1
        else:
            lim_fin = mitad - 1
    return -1

def main():
    lista = []

    # Solicitar al usuario la lista
    elementos = input("Ingrese los elementos de la lista separados por espacios: ")
    lista = elementos.split()

    for i in range(len(lista)):
        lista[i] = int(lista[i])

    lista.sort()  # Asegurarse de que la lista esté ordenada para la búsqueda binaria

    while True:
        print("\n¿Qué tipo de búsqueda desea realizar?")
        print("1. Búsqueda Lineal")
        print("2. Búsqueda Binaria")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            elemento = int(input("Ingrese el elemento que desea buscar: "))
            inicio = time.time()
            resultado = busqueda_lineal(lista, elemento)
            fin = time.time()
            if resultado != -1:
                print(f"El elemento {elemento} se encuentra en la posición {resultado+1}.")
            else:
                print(f"El elemento {elemento} no se encuentra en la lista.")
            print(f"Tiempo de ejecución de búsqueda lineal: {fin - inicio} segundos")
        elif opcion == '2':
            elemento = int(input("Ingrese el elemento que desea buscar: "))
            inicio = time.time()
            resultado = busqueda_binaria(lista, elemento)
            fin = time.time()
            if resultado != -1:
                print(f"El elemento {elemento} se encuentra en la posición {resultado+1}.")
            else:
                print(f"El elemento {elemento} no se encuentra en la lista.")
            print(f"Tiempo de ejecución de búsqueda binaria: {fin - inicio} segundos")
        elif opcion == '3':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()