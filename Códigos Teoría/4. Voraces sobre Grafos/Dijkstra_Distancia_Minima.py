def selectMinDistance(distances, visited):
    minDistance = float('inf')  # Variable que me diga cuál es la distancia mínima. La inicializamos a infinito
    bestItem = None
    for i in range(len(distances)):  # Por cada nodo
        if not visited[i] and distances[i] < minDistance:  # Que no esté visitado y la distancia hacia él es menor que la distancia que tengo almacenada
            minDistance = distances[i]  # Almaceno la nueva distancia mínima
            bestItem = i
    return bestItem  # Es el nodo que voy a devolver


def greedyDijkstra(origin, g):
    n = len(g)  # Nº de nodos
    distances = [float('inf')] * n  # Ponemos distancias a infinito
    distances[origin] = 0
    visited = [False] * n  # Nodos visitados o no con todos a false al comienzo (alternativa a usar conjuntos)
    visited[origin] = True
    for (start, end, weight) in g[origin]:  # Para cada arista que tengo (para cada adyacente a mi nodo origen)
        distances[end] = weight  # La distancia que voy a tener es el peso de esa arista (paso 0 diapositivas)

    for _ in range(1, n):  # Desde el nodo siguiente hasta n
        nextNode = selectMinDistance(distances, visited)  # De array de distancias cogeré el siguiente nodo que tenga menor distancia desde mi nodo origen
        visited[nextNode] = True  # Lo marco como visitado
        # Tengo que comprobar ahora si tengo algún camino más corto que el que tenía almacenado
        for (start, end, weight) in g[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight)
    return distances


if __name__ == '__main__':
    # Grafo de la diapositiva modo juez
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        origin, dest, cost = map(int, input().strip().split())
        g[origin].append((origin, dest, cost))
    solucion = greedyDijkstra(0, g)
    print(solucion)

'''
5 7
0 1 5
0 3 3
1 4 1
3 2 11
3 1 1
3 4 6
4 2 1
'''
