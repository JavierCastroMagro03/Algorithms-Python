# Recorrido en profundidad con matriz de adyacencia (DFS)

def dfsRec(nodo_act, g, visitados):
    print("Visiting node:", nodo_act)
    visitados.add(nodo_act)

    # Recorrer la fila de la matriz correspondiente a 'node'
    # Recorremos todas las posibles conexiones (recorremos la fila del nodo que estamos evaluando)
    for ady in range(len(g)):
        if g[nodo_act][ady] == 1 and ady not in visitados:  # Si hay conexión y no está visitado
            dfsRec(ady, g, visitados)  # Llamada recursiva
    # Cuando se hace la llamada recursiva con el 2 como no está visitado y se imprime, ahora node es 2 (siguiente fila)
    # adj es el nuevo nodo_act

def dfs(g):
    visitados = set()
    nNodos = len(g)  # Nº de nodos (10)
    for nodo_act in range(nNodos):  # Se itera por todos los nodos
        if nodo_act not in visitados:  # Se comprueba si está visitado o no
            dfsRec(nodo_act, g, visitados)  # Se llama al siguiente método


# Grafo representado con matriz de adyacencia (indexado desde 0)
gMatrix = [
    # 0  1  2  3  4  5  6  7  8  9  (Nodos)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Nodo 0 (no se usa)
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],  # Nodo 1
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],  # Nodo 2
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],  # Nodo 3
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],  # Nodo 4
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],  # Nodo 5
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # Nodo 6
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # Nodo 7
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],  # Nodo 8
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],  # Nodo 9
]

# Llamar al algoritmo con la matriz de adyacencia
dfs(gMatrix)
