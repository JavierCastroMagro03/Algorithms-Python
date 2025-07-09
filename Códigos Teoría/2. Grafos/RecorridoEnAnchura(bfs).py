# importación de la cola
from collections import deque


# Recorrido en Anchura (bfs)
# breath-first search
# Procedimiento iterativo

# IMPLEMENTACIÓN
def bfsAux(nodo_act, g, visitados):
    print("Visiting node: " + str(nodo_act))  # Imprimimos por pantalla el valor
    visitados.add(nodo_act)  # visited[nodo_act] = True Añadimos el nodo al array de visitados
    # Vamos a implementar una bi cola (ED doblemente enlazada) dependiendo de por donde inserte y borre elementos,
    # tendremos el comportamiento de una pila o de una cola (esa es la ED que utiliza python)
    # Nosotros haremos borrado por el comienzo(izda) e inserción por el final(derecha), es decir, la usaremos como una cola
    cola = deque()
    # metemos el elemento
    cola.append(nodo_act)  # append te lo va añadiendo por la derecha

    while cola:  # mientras me queden elementos
        # Eliminamos el primer elemento de la cola y luego metemos los adyacentes
        aux = cola.popleft()
        # g[aux] # Me da los adyacentes del nodo en el que estoy
        for adj in g[aux]:
            if adj not in visitados:  # if not visited[adj]:
                print("Visiting node: " + str(adj))  # imprimimos
                visitados.add(adj)  # visited[adj] = True lo añadimos a visitados
                cola.append(adj)  # lo añadimos a la cola


def bfs(g):
    # Vamos a utilizar una alternativa a los conjuntos que ofrece python la dejaré comentada
    nNodos = len(g)  # tamaño de la lista n = 10
    visitados = set()  # visitados = [False] * nNodos
    for nodo_act in range(1, nNodos):  # Quiero que pare en 9 como mi n es 10 y el último es exclusivo no tengo que poner n-1
        if nodo_act not in visitados:  # if not visitados[nodo_act]:  # Si v no está en la lista de visitados
            bfsAux(nodo_act, g, visitados)  # Llamada a la función bfsAux


# DATOS
# De nuevo lo vamos a definir como una lista de adyacencias
gAdjList = [
    [],  # recordar la utilidad de la posición vacía para coherencia
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

# LLAMADA AL ALGORITMO
bfs(gAdjList)  # Para depurar poner el punto de ruptura aquí

# Grafo conexo (da igual recorrido en anchura o profundidad)
# Componente conexa más grande? (los dos recorrido valen)

# Recorrido en anchura frente a, recorrido en profundidad. Me da un grafo grande. ¿Existe un camino de 5 aristas entre
# el nodo 23 y el nodo 5? Para saber distancia real entre nodos haciendo uso de aristas. PREGUNTA EXAMEN
# porque cuando haces un recorrido se genera un árbol. En el de anchura las distancias son reales en el de profundidad
# NO

# si el grafo es fuertemente conexo o si contiene ciclos tmb me da igual cuál de los dos recorridos hacer
# Recorrido en profundidad es pre-orden

# En las diapositivas, las aristas punteadas son aristas no utilizadas para realizar el recorrido
