import time

def bb(arr):
    n = len(arr)

    for i in range(n - 1):
       
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

def bbo(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True


if __name__ == "__main__":
    arr = []  
    
    n = int(input("Ingrese la cantidad de elementos en la lista: "))

   
    for i in range(n):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        arr.append(elemento)

    while True:
        print("\nSeleccione una opción:")
        print("1. Ordenar utilizando Bubble Sort (normal)")
        print("2. Ordenar utilizando Bubble Sort (optimizado)")
        print("3. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            start_time = time.time()
            bb(arr)
            end_time = time.time()
            print("Lista ordenada con Bubble Sort (normal):")
            print(arr)
            print(f"Tiempo de ejecución: {end_time - start_time} segundos")
        elif opcion == 2:
            start_time = time.time()
            bbo(arr)
            end_time = time.time()
            print("Lista ordenada con burbuja optimizada:")
            print(arr)
            print(f"Tiempo de ejecución: {end_time - start_time} segundos")
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")