import heapq


def dijkstra(start, g):
    distancias = [float('inf')] * len(g)
    distancias[start] = 0
    colaprioridad = [(0, start)]
    while len(colaprioridad) > 0:
        distancia_actual, nodo_actual = heapq.heappop(colaprioridad)
        for adj, peso in g[nodo_actual]:
            distancia = distancia_actual + peso
            if distancia < distancias[adj]:
                distancias[adj] = distancia
                heapq.heappush(colaprioridad, (distancia, adj))
    return distancias


# Lectura entrada
nNodos, mAristas, tMax = map(int, input().strip().split())
g = [[] for _ in range(nNodos)]
suma = 0
for _ in range(mAristas):
    origen, destino, peso = map(int, input().strip().split())
    # Funciona en grafos no dirigidos. En decora como puedas, hay que asumir que existen aristas en ambas direcciones
    g[origen].append((destino, peso))
    g[destino].append((origen, peso))
solucion = dijkstra(0, g)
# print(solucion)
for i in solucion:
    suma += i
if tMax >= suma:
    print(suma)
else:
    print("Aleg, ¡a decorar!")

'''
5 6 20
0 1 3
0 2 1
2 4 8
3 4 8
2 1 1
1 3 2
'''

'''
10 21 231
0 1 50
0 4 36
0 8 9
0 9 39
1 2 42
1 5 48
1 8 26
2 5 44
3 5 2
3 8 29
3 9 46
4 6 23
4 8 33
4 9 29
5 7 18
5 8 2
6 7 34
6 8 21
6 9 28
7 9 10
8 9 44
'''
