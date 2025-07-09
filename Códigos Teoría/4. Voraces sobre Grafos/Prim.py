def minKey(g, key, mstSet):  # Almacena el peso de la arista que está conectando mi nodo v con el árbol de recubrimiento mínimo que estoy construyendo
    # Me guardo la arista de menor peso
    min = float('inf')  # necesito la variable que me almacene eso
    min_index = -1
    for v in range(len(g)):  # Necesito saber cuál es ese nodo que me guardo. Entonces recorro el grafo
        if key[v] < min and mstSet[v] == False:  # Si el peso de mi nodo v es menor que el menor peso y ese nodo v no pertenece al árbol
            min = key[v]  # Sí que lo tengo en cuenta
            min_index = v  # lo actualizo
    return min_index  # devuelvo el index


def primMST(g):
    key = [float('inf')] * len(g)  # Ponemos primero todas las aristas a infinito porque hasta que no avance en mi algoritmo, no sabré que arista tengo que seleccionar.
    key[0] = 0
    mstSet = [False] * len(g)  # ¿El nodo pertenece a mi árbol de recubrimiento mínimo?
    cost = 0
    for cout in range(len(g)):  # Para cada nodo en mi grafo
        u = minKey(g, key, mstSet)  # Coge aquella arista que me conecte un nodo que ya esté en el grafo con otro que no
        mstSet[u] = True  # Lo añado
        for v in range(len(g)):  # para todos los nodos que tengo en mi grafo
            if 0 < g[u][v] < key[v] and not mstSet[v]:  # Si la conexión que encuentro es menor que lo que tengo almacenado y ese nodo aún no está en el árbol
                key[v] = g[u][v]
                cost += g[u][v]  # Aumento el coste
    return cost


if __name__ == '__main__':  # Forma de decirle a python que quieres que empiece a ejecutar por ahí
    # Vamos a representar el grafo como una matriz de adyacencias
    # Por cada fila represento un nodo
    g = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
    cost = primMST(g)
    print(cost)
