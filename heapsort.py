def construir_heap(arr, n, i):
    maximo = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and arr[i] < arr[izquierda]:
        maximo = izquierda

    if derecha < n and arr[maximo] < arr[derecha]:
        maximo = derecha

    if maximo != i:
        arr[i], arr[maximo] = arr[maximo], arr[i]
        construir_heap(arr, n, maximo)

def heap_sort(arr):
    n = len(arr)

    # Construir un heap máximo
    for i in range(n // 2 - 1, -1, -1):
        construir_heap(arr, n, i)

    # Extraer elementos uno por uno y reconstruir el heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el máximo actual con el último elemento sin ordenar
        construir_heap(arr, i, 0)

# Solicitar al usuario que ingrese el tamaño del arreglo
n = int(input("Ingresa la cantidad de elementos en el arreglo: "))
arr = []

# Solicitar al usuario que ingrese cada elemento uno por uno
for i in range(n):
    elemento = int(input(f"Ingresa el elemento {i + 1}: "))
    arr.append(elemento)

heap_sort(arr)
print("Arreglo ordenado:")
for elemento in arr:
    print(elemento)
