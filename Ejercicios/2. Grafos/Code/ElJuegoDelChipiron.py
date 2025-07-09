from collections import deque

# Direcciones posibles: (fila, columna)
Direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha


def bfsAux(g, visited, v):
    print("Visiting node:", v)
    visited[v] = True  # Ponemos el primer nodo a visitado
    q = deque()  # Inicializamos la cola vacía
    q.append(v)  # Insertamos el nodo inicial
    iterador = 1  # Inicializamos el contador

    while q:  # Mientras existan elementos en la cola
        aux = q.popleft()  # Sacamos el primer elemento de la cola
        for adj in range(len(g)):  # Recorremos la fila del nodo que estamos evaluando
            if (iterador % 2 == 0) and (g[aux][adj] == -1):
                # Cambio de dirección y avanzamos
                iterador += 1  # Incrementamos el iterador
            if g[aux][adj] == 0 and not visited[adj]:  # Evaluamos si es adyacente y si no está visitado
                print("Visiting node:", adj)
                visited[adj] = True  # Lo marcamos como visitado
                q.append(adj)  # Insertamos el nodo adyacente
                iterador += 1  # Incrementamos el iterador
            if g[aux][adj] == 2:  # Compruebo si estoy en el maletín
                print(iterador)  # Si estoy imprimo el valor del iterador
            else:
                print("No hay maletín en este laberinto")


def bfs(g):
    n = len(g)  # n Toma el valor de la longitud del laberinto
    visited = [False] * n  # Ponemos todos los elementos a no visitados en la lista visited
    for v in range(n):
        if not visited[v]:
            bfsAux(g, visited, v)


# Entrada
nFilas, mColumnas = map(int, input().strip().split())
laberinto = []
for _ in range(nFilas):
    fila = list(map(int, input().strip().split()))
    laberinto.append(fila)

# Imprimimos laberinto
# print(laberinto)

# Llamada al recorrido
bfs(laberinto)
