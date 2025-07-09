from collections import deque


def recorridoanchura(juego, grafo, visitados, juegos, tipoJ):
    visitados.add(juego)
    cola = deque()
    cola.append(juego)
    ElemCConexa = 1  # lo inicializamos con el primer juego que me interese y esta variable me guarda el número de elementos de la componente conexa

    while cola:  # Mientras queden elementos en la cola
        aux = cola.popleft()  # Sacamos el primer elemento de la cola
        for adj in grafo[aux]:  # Por cada adyacente al juego
            if adj not in visitados:   # Se comprueba si está en el conjunto de visitados y si es del tipo que nos interesa
                visitados.add(adj)  # Lo añadimos al conjunto de visitados
                cola.append(adj)  # Lo añadimos a la cola
                if juegos[adj] == tipoJ:
                    ElemCConexa += 1  # Incrementamos el número de elementos visitados en esa componente conexa

    return ElemCConexa


def metodo(grafo, juegos, nJuegos, tipoJ):
    opciones = 0  # Variable para almacenar el número de componentes conexas
    juegosComprados = 0  # Variable que almacena el max número de juegos que compro de un tipo concreto de una componente conexa
    visitados = set()  # Conjunto de visitados

    for juego in range(int(nJuegos)):  # Por cada juego
        if juego not in visitados:  # Si no está en el conjunto de visitados y es del tipo que me interesa
            ElemCConexa = recorridoanchura(juego, grafo, visitados, juegos, tipoJ)  # Llamada al recorrido en anchura
            # Esto se ejecuta por cada componente conexa
            opciones += 1  # Acumulamos componentes conexas
            if ElemCConexa > juegosComprados:
                juegosComprados = ElemCConexa

    return opciones, juegosComprados


# Lectura entrada
nJuegos, mAristas, tipoJ = input().strip().split()
grafo = [[] for _ in range(int(nJuegos))]
juegos = [''] * int(nJuegos)

for _ in range(int(nJuegos)):
    id, plataforma = input().strip().split()  # Identificador y plataforma del juego
    id = int(id)
    juegos[id] = plataforma
# print(juegos)

for _ in range(int(mAristas)):
    origen, destino = map(int, input().strip().split())  # Indica que dos juegos se pueden coger a la vez (que hay arista entre ellos)
    if juegos[origen] == juegos[destino]:
        grafo[origen].append(destino)
        grafo[destino].append(origen)
# print(grafo)

opciones, juegosComprados = metodo(grafo, juegos, nJuegos, tipoJ)
if opciones == 1:
    print("Hay", opciones, "opción")  # Número de componentes conexas que hay
else:
    print("Hay", opciones, "opciones")
if juegosComprados == 1:
    print("Se compra", juegosComprados, "juego de", tipoJ)
else:
    print("Se compran", juegosComprados, "juegos de", tipoJ)  # Max número de juegos de un tipo en una componente conexa

# Entrada 1
'''
3 1 PS5
0 PS5
1 PS5
2 PS5
0 1
'''

# Salida 1
'''
Hay 2 opciones
Se compran 2 juegos de PS5
'''

# Entrada 2
'''
5 4 switch
0 switch
1 PS5
2 PS5
3 switch
4 switch
0 1
0 2
1 2
3 4
'''

# Salida 2
'''
Hay 3 opciones
Se compran 2 juegos de switch
'''
