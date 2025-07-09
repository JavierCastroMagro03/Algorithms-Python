import heapq as hq


def prim_pq(g):
    cola_prioridad = []
    hq.heappush(cola_prioridad, (0, 0, 0))  # coste, nodo_origen, nodo_destino # Añado el primer nodo por el que empiezo que tendrá peso 0
    visitados = set()  # Conjunto de visitados (aquellos nodos que pertenecen ya al árbol de recubrimiento mínimo)
    coste = 0  # Coste (suma de los pesos)
    aristas_sel = []
    while cola_prioridad:  # while len(cola_prioridad) > 0  # Vamos a iterar mientras haya elementos en la cola
        pair = hq.heappop(cola_prioridad)  # Me devuelve la arista de mayor prioridad (la que menor peso tenga)
        peso = pair[0]  # De la cola me quedo con su coste
        origen = pair[1]
        destino = pair[2]
        if destino not in visitados:  # Si no está en el conjunto de visitados
            coste += peso  # Sumo el coste de ese nodo
            visitados.add(destino)  # Lo añadimos al conjunto de visitados
            if origen != destino:  # Si no es un ciclo
                aristas_sel.append((origen, destino))  # Me guardo la arista
            for ady in g[destino]:  # para todos los adyacentes de este nuevo nodo
                if ady[1] not in visitados:  # Por cada adyacente que no está visitado
                    hq.heappush(cola_prioridad, (ady[2], ady[0], ady[1]))  # coste, nodo_origen, nodo_destino  # lo añado a mi cola con el coste asociado a ese nodo y el nodo
    return coste, aristas_sel


# En prim sí que hace falta definir el grafo
if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]
    for _ in range(m):  # Por cada arista leo su coste y los dos nodos que conecta
        origen, destino, peso = map(int, input().strip().split())
        # Añado las aristas a la lista de adyacencias
        g[origen].append((origen, destino, peso))
        g[destino].append((destino, origen, peso))
    coste, aristas_sel = prim_pq(g)
    print(coste)
    print(aristas_sel)

''' 
7 11
0 2 1
0 3 2
0 6 6
1 5 4
1 4 2
1 6 7
2 3 3
2 6 5
3 4 1
3 5 9
4 6 8
'''
