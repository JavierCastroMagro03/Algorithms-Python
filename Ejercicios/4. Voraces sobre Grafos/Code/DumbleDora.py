def actualizar_componentes(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(aristas, nNodos):
    coste = 0
    componentes = list(range(nNodos))
    nComponentes = nNodos
    arista_act = 0
    aristas_sel = []
    while nComponentes > 1 and arista_act < len(aristas):
        origen = aristas[arista_act][1]
        destino = aristas[arista_act][2]
        peso = aristas[arista_act][0]
        if componentes[origen] != componentes[destino]:
            coste += peso
            actualizar_componentes(componentes, componentes[origen], componentes[destino])
            aristas_sel.append(aristas[arista_act])
            nComponentes -= 1
        arista_act += 1
    return coste, aristas_sel


# Lectura Entrada
nNodos, mAristas = map(int, input().split())
aristas = []
for _ in range(mAristas):
    origen, destino, peso = map(int, input().split())
    aristas.append((peso, origen, destino))
aristas.sort()
coste, aristas_sel = kruskal(aristas, nNodos)

# Imprimir salida
print("Coste total:", coste)
# Coste de cada habitación = la suma de los pesos de las aristas (incidentes) a esa habitación y de salida de esa habitación

aristas_sel.sort(key=lambda x: x[0])
# print(aristas_sel)
coste_por_habitacion = [0] * nNodos
for arista in aristas_sel:  # Recorremos nuestras aristas seleccionadas (peso, origen, destino)
    coste_por_habitacion[arista[1]] += arista[0]  # En la lista de coste por habitación vamos acumulando el peso para cada habitación
    coste_por_habitacion[arista[2]] += arista[0]

i = 0
while i < len(coste_por_habitacion):
    print("H" + str(i) + ":", coste_por_habitacion[i])
    i += 1

# Entrada 1
'''
10 11
0 3 105
0 7 74
0 9 42
1 5 60
1 8 35
2 6 11
2 8 92
3 4 79
3 5 58
4 7 57
4 8 39
'''

# Salida 1
'''
Coste total: 468
H0: 116
H1: 95
H2: 103
H3: 58
H4: 96
H5: 118
H6: 11
H7: 131
H8: 166
H9: 42
'''

# Entrada 2
'''
10 16
0 2 93
0 9 114
1 4 14
1 5 115
1 7 86
2 3 118
2 4 127
2 6 36
2 9 136
4 5 37
4 6 124
4 7 128
4 9 25
5 6 85
6 9 91
8 9 11
'''

# Salida 2
'''
Coste total: 505
H0: 93
H1: 100
H2: 247
H3: 118
H4: 76
H5: 122
H6: 121
H7: 86
H8: 11
H9: 36
'''
