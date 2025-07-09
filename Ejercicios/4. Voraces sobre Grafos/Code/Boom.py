# Tengo que lanzar dijkstra por cada nodo y luego cuando acabe dijkstra por cada nodo actualizar mi distancia mínima si
# la hubiese y si los nodos son del mismo tipo
import heapq


def dijkstra(start, g):
    distancias = [float('inf')] * len(g)  # Inicializamos la lista que guardará la distancia mínima para cada nodo a infinito
    distancias[start] = 0  # Marcamos la distancia de nuestro nodo de inicio a distancia 0
    colaprioridad = [(0, start)]  # Inicialización cola de prioridad con (distancia, nodo, ¿tipo????????????)
    while len(colaprioridad) > 0:  # Mientras queden elementos en la cola
        distancia_act, nodo_act = heapq.heappop(colaprioridad)  # Sacamos el que tenga la menor distancia acumulada
        for adj, weight in g[nodo_act]:  # Para cada adyacente de ese nodo
            distancia = distancia_act + weight  # Se calcula la distancia para cada nodo adj pasando por el seleccionado
            if distancia < distancias[adj]:  # Si la distancia es menor que la que tenía almacenada
                distancias[adj] = distancia  # La actualizo
                heapq.heappush(colaprioridad, (distancia, adj))  # Metemos ese nodo a la cola con su nueva distancia para procesarlo después.
    return distancias  # Devuelve la lista de distancias mínimas desde el nodo start a todos los demás nodos.


# Lectura entrada
nNodos, mAristas = map(int, input().strip().split())  # Leo el número de nodos y el número de aristas
g = [[] for _ in range(nNodos)]  # Inicializo el grafo
tipo_componentes = list(map(int, input().strip().split()))  # Me guardo en una lista el tipo de cada nodo
# print(tipo_componentes)

for _ in range(mAristas):  # Por cada conexión
    # Genero el grafo
    origen, destino, longitud = map(int, input().strip().split())
    g[origen].append((destino, longitud))
    g[destino].append((origen, longitud))
# print(g)

tipos = set(tipo_componentes)  # Conjunto de tipos diferentes que existen
# print(tipos)
solucion = [[] for _ in tipos]  # ED para guardarme la solución
for tipo in tipos:  # Por cada tipo
    solucion[tipo] = float('inf')  # Establezco en la solución una distancia inicial infinito

for n in range(nNodos):  # Por cada nodo
    distancias = dijkstra(n, g)  # Lanzo dijkstra
    # print(distancias)
    tipo_nodo = tipo_componentes[n]  # Leo el tipo de ese nodo
    for i in range(nNodos):  # Recorro distancias
        if i != n and tipo_componentes[i] == tipo_nodo:  # Si el tipo del siguiente nodo es igual del anterior y no son el mismo nodo (para no contar el 0)
            solucion[tipo_nodo] = min(solucion[tipo_nodo], distancias[i])  # En mi solución guardo en la posición de ese tipo la distancia menor
print(*solucion)

'''         
6 10
0 0 0 1 1 1
0 1 2
0 3 1
0 2 5
1 2 3
1 3 2
2 3 3
2 4 1
2 5 5
3 4 1
4 5 1
'''
