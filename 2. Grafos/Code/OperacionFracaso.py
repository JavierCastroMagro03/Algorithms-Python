# Notas (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Fans:
# 1 → Eres tu propio fan
# 2 → Le admirarán sus adyacentes (familiares y amigos)
# 3 → Le admirarán sus adyacentes y los adyacentes de sus adyacentes
# 4 → ...

# El concursante es el id 0 en la entrada
from collections import deque


def bfsAux(g, visited, v, nota):
    visited[v] = True  # Añadimos el nodo al array de visitados
    q = deque()  # Inicializamos cola
    # Metemos el elemento
    q.append(v)  # append te lo va añadiendo por la derecha
    fans = 1

    for _ in range(nota - 1):  # Hasta el nivel nota-1
        elem_cola = len(q)  # Número de nodos que procesaremos en este nivel
        for _ in range(elem_cola):
            # Quitamos un elemento de la cola y luego metemos los adyacentes
            aux = q.popleft()
            # g[aux] # Me da los adyacentes del nodo en el que estoy
            for adj in g[aux]:  # Recorremos los adyacentes
                if not visited[adj]:  # Si no está visitado
                    visited[adj] = True  # Lo añadimos a visitados
                    fans += 1  # Incrementamos el número de fans
                    q.append(adj)  # Lo añadimos a la cola
    return fans  # Cuando llegue al nivel tope devuelvo el número de fans


def bfs(g, nota):
    # Vamos a utilizar una alternativa a los conjuntos que ofrece python
    n = len(g)  # tamaño de la lista n = 10
    visited = [False] * n
    fans = bfsAux(g, visited, 0, nota)  # Llamada a la función bfsAux empezando en el 0
    print(fans)


# Entrada
nConcursantes = int(input().strip())  # Primera línea número de concursantes
for i in range(nConcursantes):
    notaObtenida, nNodos, mAristas = map(int, input().strip().split())  # Segunda línea
    grafo = [[] for _ in range(nNodos)]  # Creamos lista vacía con tantos espacios como nodos tengamos
    for _ in range(mAristas):  # Almacenamos todas las aristas en la lista de adyacencias
        origen, destino = map(int, input().strip().split())
        grafo[origen].append(destino)
        grafo[destino].append(origen)  # Porque el grafo es no dirigido entones se tienen en cuanta las dos direcciones

    # Mostrar el grafo (para depuración)
    # for i in range(len(grafo)):
    # print(f"{i}: {grafo[i]}")

    bfs(grafo, int(notaObtenida))
