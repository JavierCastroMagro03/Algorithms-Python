# Recorrido en anchura
from collections import deque


def recorridoanchura(nodo_act, g, visitados, nGrupos):
    visitados.add(nodo_act)
    cola = deque()
    cola.append(nodo_act)

    while cola:
        aux = cola.popleft()
        for adj in g[aux]:
            if adj not in visitados:
                visitados.add(adj)
                cola.append(adj)
    return nGrupos


def metodo(g, nNodos):
    visitados = set()
    nGrupos = 0
    for nodo_act in range(nNodos):
        if nodo_act not in visitados:
            nGrupos += 1
            recorridoanchura(nodo_act, g, visitados, nGrupos)
    print(nGrupos)


# Entrada
nNodos, mAristas = map(int, input().strip().split())
g = [[] for _ in range(nNodos)]  # g = [[], [], [], []]
for _ in range(mAristas):
    origen, destino = map(int, input().strip().split())
    g[origen].append(destino)
    g[destino].append(origen)
# print(g)
# Llamada
metodo(g, nNodos)

'''
10 5
0 1
1 5
2 4
3 9
4 9
'''
