# Recorrido en profundidad de forma recursiva
# Depth-first search

# IMPLEMENTACIÓN DEL ALGORITMO

def dfsRec(nodo_act, g, visitados):  # g lo recibimos como una nueva variable g es un puntero copia de gAdjList
    print("Visiting node: " + str(nodo_act))
    visitados.add(nodo_act)  # Añadimos el nodo al conjunto
    for ady in g[nodo_act]:  # Mientras existan nodos en el grafo
        if ady not in visitados:  # Comprobamos si ha sido visitado
            dfsRec(ady, g, visitados)  # Llamada recursiva


# Para hacer recorrido en profundidad para cada uno de los nodos (empezando desde cualquier nodo)
def dfs(g):
    visitados = set()
    nNodos = len(g)  # Nº nodos
    for nodo_act in range(1, nNodos):  # Primer valor que toma v es 1 y el último es n pq n es 10
        if nodo_act not in visitados:
            dfsRec(nodo_act, g, visitados)  # Si visited == n el grafo es conexo (ya que habría visitado todos)


# DATOS
# Lo primero que tenemos que hacer para un recorrido en profundidad es definir un grafo
# Dos formas → Matriz de adyacencia o lista de adyacencia
# Vamos a hacerlo como una lista de adyacencias
gAdjList = [
    [],  # Posición vacía para que al buscar adyacentes al 2 tengo que poner 2, al 3 3 ...
    [2, 4, 8],  # Adyacentes al nodo 1
    [1, 3, 4],  # Adyacentes al nodo 2
    [2, 4, 5],  # ...
    [1, 2, 3, 7],
    [3, 6],
    [5, 7],
    [4, 6, 9],
    [1, 9],
    [7, 8]
]
# Adyacentes del nodo 3 gAdjList[3]
# Primer adyacente del nodo 3 gAdjList[3][0] → 2
node = 1  # Nodo inicial

# LLAMADA AL ALGORITMO CON LOS DATOS

# Conjunto para almacenar los nodos visitados(es la estructura más eficiente para comprobar si un elemento existe o no)

dfs(gAdjList)  # Llamada a la función

# Buscar casos particulares de uso del recorrido de grafos en profundidad
