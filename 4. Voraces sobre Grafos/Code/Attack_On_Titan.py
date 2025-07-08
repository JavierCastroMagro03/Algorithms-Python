import math


def actualizar_componentes(componentes, new_id, old_id):
    for i in range(len(componentes)):
        if componentes[i] == old_id:
            componentes[i] = new_id


def kruskal(aristas, nNodos):
    distanciatotal = 0
    componentes = list(range(nNodos))
    nComponentes = nNodos
    arista_act = 0

    while nComponentes > 1 and arista_act < len(aristas):
        origen = aristas[arista_act][1]
        destino = aristas[arista_act][2]
        distancia = aristas[arista_act][0]
        if componentes[origen] != componentes[destino]:
            distanciatotal += distancia
            actualizar_componentes(componentes, componentes[origen], componentes[destino])
            nComponentes -= 1
        arista_act += 1
    return distanciatotal


# Lectura entrada
nNodos, mAristas = map(int, input().strip().split())
aristas = []
for _ in range(mAristas):
    origen, destino, distancia = map(int, input().strip().split())
    aristas.append((distancia, origen, destino))
aristas.sort()  # Ordenamos las aristas de menor a mayor distancia
distanciatotal = kruskal(aristas, nNodos)

# Creo que debería de haber una forma más fácil de hacer esto
# precio = distanciatotal/5
# precio_extra = precio % 10
# if precio_extra != 0:
    # print(distanciatotal//5 + 1)
# else:
    # print(precio)

print(math.ceil(distanciatotal/5)) # math.ceil lo que hace es redondearme hacia arriba


'''
10 13
0 2 125
0 8 59
1 4 89
1 7 24
2 7 90
3 5 86
3 9 15
4 7 47
5 7 43
5 9 36
6 8 57
7 8 80
7 9 103
'''
