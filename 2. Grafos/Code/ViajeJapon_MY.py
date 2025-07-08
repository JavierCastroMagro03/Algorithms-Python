def recorridoprofundidad(nodo, grafo, visitados):
    visitados.add(nodo)
    for adj in grafo[nodo]:
        if adj not in visitados:
            recorridoprofundidad(adj, grafo, visitados)


def metodo(nodo, grafo, visitados):
    if nodo not in visitados:
        recorridoprofundidad(nodo, grafo, visitados)


# Lectura entrada
nNodos, mAristas = map(int, input().strip().split())
g = [[] for _ in range(nNodos)]
gtranspuesto = [[] for _ in range(nNodos)]

for _ in range(mAristas):
    origen, destino = map(int, input().strip().split())
    g[origen].append(destino)
    gtranspuesto[destino].append(origen)

visitadosg = set()
metodo(0, g, visitadosg)
visitadosgtranspuesto = set()
metodo(0, gtranspuesto, visitadosgtranspuesto)
if len(visitadosg) == nNodos and len(visitadosgtranspuesto) == nNodos:
    print("PERFECTO")
else:
    print("CAMBIA EL ITINERARIO")

# Ejemplos entrada
'''
10 19
0 8
0 6
1 8
1 7
2 6
2 9
3 6
3 5
4 0
4 6
5 3
6 2
6 9
7 8
7 6
8 6
8 5
9 6
9 3
'''

'''
5 9
0 3
0 4
1 3
1 2
2 1
3 0
3 4
4 3
4 1
'''
