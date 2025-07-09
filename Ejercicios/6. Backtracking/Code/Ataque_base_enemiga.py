def esSolucion(nuevaFila, nuevaColumna, endX, endY, nEnemigos):
    # Es solución cuando hemos llegado a la salida del laberinto y hemos matado a todos los enemigos
    return nuevaFila == endX and nuevaColumna == endY and nEnemigos == 0


def esFactible(base, nuevaFila, nuevaColumna, visitados):
    celda_act = (nuevaFila, nuevaColumna)
    # Es factible si está dentro de los límites de la base, si no ha sido ya visitada, y si no es un muro
    if 0 <= nuevaFila < len(base) and 0 <= nuevaColumna < len(base[0]) and celda_act not in visitados and base[nuevaFila][nuevaColumna] != -2:
        return True
    else:
        return False


def salirlaberintoBt(base, fila_act, columna_act, endX, endY, pasos, mejor_sol, visitados, nEnemigos):
    if esSolucion(fila_act, columna_act, endX, endY, nEnemigos):
            mejor_sol = min(mejor_sol, pasos)  # Actualizo mi mejor solución
    else:
        desplazamientos = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # Con los desplazamientos
        i = 0  # i = 0
        while i < len(desplazamientos):  # Mientras yo pueda seguir desplazando
            nuevaFila = fila_act + desplazamientos[i][0]  # Mi nueva fila va a ser fila + mi desplazamiento i en la pos 0
            nuevaColumna = columna_act + desplazamientos[i][1]
            if esFactible(base, nuevaFila, nuevaColumna, visitados):  # Si esa posición es factible
                visitados.add((nuevaFila, nuevaColumna))  # Añadimos la posición al conjunto de visitados
                if base[nuevaFila][nuevaColumna] == - 1:  # Si en esa posición hay un enemigo
                    nEnemigos -= 1  # Lo eliminamos
                mejor_sol = salirlaberintoBt(base, nuevaFila, nuevaColumna, endX, endY, pasos + 1, mejor_sol, visitados, nEnemigos)  # Llamada recursiva
                # Deshacer
                visitados.remove((nuevaFila, nuevaColumna))
                if base[nuevaFila][nuevaColumna] == - 1:
                    nEnemigos += 1
            i += 1
    return mejor_sol


if __name__ == '__main__':
    nFilas, mColumnas, nEnemigos = map(int, input().split())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    base = []
    for i in range(nFilas):
        fila = list(map(int, input().split()))
        base.append(fila)
    visitados = set()
    visitados.add((startX, startY))
    pasos = 1
    mejor_sol = float('inf')
    mejor_sol = salirlaberintoBt(base, startX, startY, endX, endY, pasos, mejor_sol, visitados, nEnemigos)
    print(mejor_sol)

'''
4 5 3
0 1
0 3
0 0 0 0 0
-2 0 0 -2 0
-2 0 -1 -2 0
0 0 -1 0 -1
'''
