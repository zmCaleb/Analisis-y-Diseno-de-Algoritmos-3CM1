import heapq
import time

class Grafo:
    def __init__(self):
        self.vertices = {}
    #La inicialización de distancias es O(V), donde V es el número de vértices en el grafo.
    def agregar_vertice(self, vertice):
        self.vertices[vertice] = {}
    
    def agregar_arista(self, inicio, fin, peso):
        self.vertices[inicio][fin] = peso

def dijkstra(grafo, inicio):
    #El bucle principal se ejecuta en O(E log V), donde E es el número de aristas y V es el número de vértices.
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[vertice_actual]:
            continue

        for vecino, peso in grafo.vertices[vertice_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias

def tiempo_ejecucion(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio
if __name__ == "__main__":
    # Crear grafo de ejemplo
    grafo = Grafo()
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_vertice("E")
    grafo.agregar_vertice("F")
    grafo.agregar_arista("A", "B", 3)
    grafo.agregar_arista("A", "C", 6)
    grafo.agregar_arista("B", "C", 2)
    grafo.agregar_arista("C", "D", 4)
    grafo.agregar_arista("C", "E", 8)
    grafo.agregar_arista("B", "F", 13)
    grafo.agregar_arista("F", "E", 1)
    grafo.agregar_arista("D", "E", 2)

    # Ejecutar Dijkstra en el grafo de ejemplo
    vertice_inicio = "A"
    
    # Medir el tiempo de ejecución
    inicio_tiempo = time.time()
    
    # Calcular los caminos mínimos
    resultado = dijkstra(grafo, vertice_inicio)
    
    # Calcular el tiempo de ejecución
    tiempo = time.time() - inicio_tiempo

    # Mostrar resultados
    print(f"Caminos mínimos desde {vertice_inicio}: {resultado}")
    print(f"Tiempo de ejecución: {tiempo} segundos")
