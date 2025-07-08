# pared (-1), suelo (0) o un enemigo (1).

def esFactible(sala, nuevaFila, nuevaColumna, distancia_luna, visitados):
    celda_act = (nuevaFila, nuevaColumna)
    # Es factible si está dentro de los límites de la base, si no ha sido ya visitada, y si no es un muro y si mi me quedan más pasos por dar
    if 0 <= nuevaFila < len(sala) and 0 <= nuevaColumna < len(sala[0]) and celda_act not in visitados and sala[nuevaFila][nuevaColumna] != -1 and distancia_luna > 0:
        return True
    else:
        return False


def esSolucion(distancia_luna, nEnemigos):
    return distancia_luna == 0 or nEnemigos == 0


def caballerolunaBT(sala, fila_act, columna_act, distancia_luna, todos_muertos, visitados, nEnemigos):
    if esSolucion(distancia_luna, nEnemigos):  # Si es solución
        if nEnemigos == 0:  # Si he matado a todos los enemigos
            todos_muertos = True  # Flag a true para que no siga iterando
        else:  # Si no esq es solución de haberme quedado sin pasos y debería de seguir probando
            todos_muertos = False
    else:  # Si no es solución
        desplazamientos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        i = 0
        while i < len(desplazamientos) and not todos_muertos:  # Mientras me pueda seguir desplazando y todos muertos sea False
            nuevaFila = fila_act + desplazamientos[i][0]  # Mi nueva fila va a ser fila + mi desplazamiento i en la pos 0
            nuevaColumna = columna_act + desplazamientos[i][1]  # Mi nueva columna va a ser mi columna actual + mi desplazamiento i en la pos 1
            if esFactible(sala, nuevaFila, nuevaColumna, distancia_luna, visitados):  # Si la nueva celda es factible
                visitados.add((nuevaFila, nuevaColumna))  # La añado al conjunto de visitados
                if sala[nuevaFila][nuevaColumna] == 1:  # Si en la nueva celda hay un enemigo
                    nEnemigos -= 1  # Lo mato
                todos_muertos = caballerolunaBT(sala, nuevaFila, nuevaColumna, distancia_luna - 1, todos_muertos, visitados, nEnemigos)  # Llamada recursiva

                # Al volver deshacemos nuestro movimiento
                if sala[nuevaFila][nuevaColumna] == 1:
                    nEnemigos += 1
                visitados.remove((nuevaFila, nuevaColumna))
            i += 1
    return todos_muertos


if __name__ == '__main__':
    nFilas, mColumnas, nEnemigos = map(int, input().split())
    sala = []
    for i in range(nFilas):
        fila = list(map(int, input().split()))
        sala.append(fila)
    start_x, start_y, distancia_luna = map(int, input().split())
    visitados = set()  # Conjunto de visitados
    visitados.add((start_x, start_y))

    todos_muertos = caballerolunaBT(sala, start_x, start_y, distancia_luna, False, visitados, nEnemigos)
    if todos_muertos:
        print("ATACA")
    else:
        print("CORRE")

'''
4 5 3
0 0 0 0 0
-1 1 0 1 0
-1 1 -1 0 0
0 0 0 -1 -1
3 1 3
'''
'''
CORRE
'''

'''
4 5 3
0 0 0 0 0
-1 1 0 1 0
-1 1 -1 0 0
0 0 0 -1 -1
3 1 4
'''
'''
ATACA
'''

'''
6 6 4
1 0 0 0 0 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 1
2 2 19
'''