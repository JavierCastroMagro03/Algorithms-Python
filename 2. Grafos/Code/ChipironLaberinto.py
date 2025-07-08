from collections import deque


# Recibe la cuadrícula, la matriz de visitados, la fila y la columna a la que te quieres mover y el turno actual.
def esValido(laberinto, visitados, nuevaFila, nuevaColumna, turno):
    if 0 <= nuevaFila < len(laberinto) and 0 <= nuevaColumna < len(laberinto[0]) and (laberinto[nuevaFila][nuevaColumna] != -1 or turno % 2 == 1) and not visitados[nuevaFila][nuevaColumna]:
        return True
    return False


def distancia_min_maletin(laberinto):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Movimientos arriba, abajo, izquierda, derecha
    movFila = [-1, 1, 0, 0]
    movColumna = [0, 0, -1, 1]

    # Recorrido en anchura para dar con la distancia mínima
    cola = deque([(0, 0, 0)])  # (fila, columna, distancia)
    visitados = [[False for _ in range(columnas)] for _ in range(filas)]  # Inicializamos visitados con todos sus elementos a Falso
    visitados[0][0] = True  # Se marca el nodo inicial como visitado

    while cola:  # Mientras haya elementos en la cola
        fila, columna, distancia = cola.popleft()

        # Si encontramos el maletín, devolver la distancia
        if laberinto[fila][columna] == 2:
            return distancia

        # Explorar los movimientos posibles
        for i in range(4):
            nueva_Fila = fila + movFila[i]
            nueva_Columna = columna + movColumna[i]
            if esValido(laberinto, visitados, nueva_Fila, nueva_Columna, distancia + 1):
                visitados[nueva_Fila][nueva_Columna] = True
                cola.append((nueva_Fila, nueva_Columna, distancia + 1))

    # Si no se puede llegar al maletín
    return -1


# Entrada
nFilas, mColumnas = map(int, input().split())
laberinto = []
for _ in range(nFilas):
    fila = list(map(int, input().split()))
    laberinto.append(fila)

distancia_minima = distancia_min_maletin(laberinto)

# Salida
print(distancia_minima)

'''
4 6
0 0 0 0 2 0
0 -1 -1 -1 0 0
0 0 0 0 0 0
0 -1 0 0 0 0
'''

'''
5 5
0 -1 2 0 0
0 -1 0 0 0
0 0 0 0 0
0 -1 0 0 0
0 -1 0 0 0
'''
