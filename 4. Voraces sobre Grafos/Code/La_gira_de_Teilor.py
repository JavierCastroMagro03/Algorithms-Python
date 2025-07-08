
# Actualizar componentes
def actualizarcomponentes(componentes, new_id, old_id):
    for i in range(len(componentes)):
        if componentes[i] == old_id:
            componentes[i] = new_id

# Kruskal
def kruskal(nNodos, aristas, g):
    coste = 0
    componentes = list(range(nNodos))
    nComponentes = nNodos
    arista_act = 0
    while nComponentes > 1 and arista_act < len(aristas):
        peso = aristas[arista_act][0]
        origen = aristas[arista_act][1]
        destino = aristas[arista_act][2]
        if componentes[origen] != componentes[destino]:
            coste += peso
            actualizarcomponentes(componentes, componentes[origen], componentes[destino])
            nComponentes -= 1
            g[origen].append(peso)
            g[destino].append(peso)
        arista_act += 1
    return coste


# Entrada
if __name__ == '__main__':
    nNodos, mAristas = map(int, input().strip().split())
    aristas = []
    g = [[] for _ in range(nNodos)]
    for _ in range(mAristas):
        origen, destino, peso = map(int, input().strip().split())
        aristas.append((peso, origen, destino))
    aristas.sort()
    coste = kruskal(nNodos, aristas, g)
    media = coste / nNodos
    print("Fuerzas desplegadas: " + str(coste))

    pesos = [[] for _ in range(nNodos)]
    solucion = []
    for i in range(nNodos):
        suma = 0
        for peso in g[i]:
            suma += peso
        pesos[i].append(suma)
    for i in range(len(pesos)):
        if pesos[i][0] < media:
            solucion.append(i)

    print(*solucion)


'''
10 13
0 2 71
0 8 28
1 4 75
1 7 116
2 7 125
3 5 124
3 9 20
4 7 68
5 7 55
5 9 94
6 8 33
7 8 31
7 9 16
'''


'''
10 19
0 1 67
0 6 179
0 8 17
0 9 38
1 3 152
1 6 119
1 7 61
2 4 51
2 6 23
2 7 111
2 8 19
3 6 105
3 9 103
4 5 48
4 9 13
5 7 150
5 9 110
6 7 73
6 9 165
'''