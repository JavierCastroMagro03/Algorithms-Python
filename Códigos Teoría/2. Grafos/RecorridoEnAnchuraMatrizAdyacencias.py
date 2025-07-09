# Recorrido en Anchura (bfs)
# breath-first search
# Procedimiento iterativo

from collections import deque


def bfsAux(g, visited, v):
    print("Visiting node:", v)
    visited[v] = True
    q = deque()  # Inicializamos la cola vacía
    q.append(v)  # Insertamos el nodo inicial

    while q:
        aux = q.popleft()
        for adj in range(len(g)):  # Recorremos la fila del nodo que estamos evaluando
            if g[aux][adj] == 1 and not visited[adj]:
                print("Visiting node:", adj)
                visited[adj] = True
                q.append(adj)  # Insertamos el nodo adyacente
        # Cuando salga de este for el que estaba evaluando ya no estará en la cola


def bfs(g):
    n = len(g)
    visited = [False] * n
    # Desde uno porque el 0 nos lo saltamos es una línea para cumplir con el convenio que seguimos en profundidad
    for v in range(1, n):
        if not visited[v]:
            bfsAux(g, visited, v)


# Matriz de adyacencias
gAdjMatrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
]

# Llamada al algoritmo
bfs(gAdjMatrix)
