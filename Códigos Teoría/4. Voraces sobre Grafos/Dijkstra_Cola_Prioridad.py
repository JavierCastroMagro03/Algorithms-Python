# ESTE ES EL QUE ME TENGO QUE APRENDER
import heapq


# Algoritmo Dijkstra
def dijkstra(start, g):
    distancias = [float('inf')] * len(g)  # Inicializamos la lista que guardará la distancia mínima para cada nodo a infinito
    distancias[start] = 0  # Marcamos la distancia de nuestro nodo de inicio a distancia 0
    colaprioridad = [(0, start)]  # Inicialización cola de prioridad con tupla (distancia, nodo)
    while len(colaprioridad) > 0:  # Mientras queden elementos en la cola
        distancia_act, nodo_act = heapq.heappop(colaprioridad)  # Sacamos el que tenga la menor distancia acumulada
        for adj, peso in g[nodo_act]:  # Para cada adyacente de ese nodo
            distancia = distancia_act + peso  # Se calcula la distancia para cada nodo adj pasando por el seleccionado
            if distancia < distancias[adj]:  # Si la distancia es menor que la que tenía almacenada
                distancias[adj] = distancia  # La actualizo
                heapq.heappush(colaprioridad, (distancia, adj))  # Metemos ese nodo a la cola con su nueva distancia para procesarlo después.
    return distancias  # Devuelve la lista de distancias mínimas desde el nodo 0 a todos los demás nodos.


# Lectura de entrada
if __name__ == '__main__':
    nNodos, mAristas = map(int, input().strip().split())  # Leemos el número de nodos y el número de aristas
    g = [[] for _ in range(nNodos)]  # Inicializamos el grafo
    for _ in range(mAristas):  # Por cada numero de aristas
        origen, destino, peso = map(int, input().strip().split())  # Leemos cada arista y su peso
        g[origen].append((destino, peso))  # Guardamos en el grafo (dirigido) para cada nodo sus adyacentes junto con su peso
    # print(g)
    solucion = dijkstra(0, g)  # Llamamos al algoritmo pasándole nuestro nodo de inicio y el grafo (lista de adyacencias)
    print(solucion)  # Imprimimos la lista de distancias mínimas desde el nodo 0 a todos los demás nodos.
