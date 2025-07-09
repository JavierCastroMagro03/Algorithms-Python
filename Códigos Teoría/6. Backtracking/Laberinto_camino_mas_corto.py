# Para inicializar el laberinto
def inicializarLaberinto():
    F = 10  # Filas
    C = 10  # Columnas
    laberinto = []
    paredes = [[0, 2], [0, 7], [1, 0], [1, 2], [1, 5], [1, 6], [1, 8],[2,6],[2,8],[3,1],[3,4],[3,5],[3,6],[4,2],[4,3],[4,7],[5,5],[5,7],[6,0],[6,3],[6,4],[6,7],[6,9],[7,1],[7,2],[7,8],[7,9],[8,2],[8,4],[8,5]]

    for i in range(F):
        fila = []
        for j in range(C):
            if [i, j] not in paredes:
                fila.append(0)  # Por cada fila y columna ponemos un 0 (espacio transitable)
            else:
                fila.append(-1)  # Si esa posición de (fila, columna) está en la lista paredes se pone un -1 (celda no transitable)
        laberinto.append(fila)
    return laberinto


def esSolucion(act_cell, n, m):  # ¿Cómo sé si he llegado a una solución?
    return act_cell[0] == n-1 and act_cell[1] == m - 1  # Si estoy en la última fila y estoy en la última columna


def esFactible(laberinto, celda_act, visited):  # Para que sea factible:
    return celda_act not in visited and 0 <= celda_act[0] < len(laberinto) and 0 <= celda_act[1] < len(laberinto[0]) and laberinto[celda_act[0]][celda_act[1]] != -1  # Mi celda no esté visitada y que esté dentro del tablero (dentro de filas y columnas) y que la casilla en la que me quiero desplazar no haya un -1 (pared)


def salirDelLaberinto(laberinto, celda_act, steps, min_steps, visited):  # Metodo salida del laberinto
    if esSolucion(celda_act, len(laberinto), len(laberinto[0])):  # Si es solución (he llegado a la esquina del laberinto)
        min_steps = min(min_steps, steps)  # Minimo de pasos será el menor entre los pasos que tenía en mi mejor solución o los pasos que lleve ahora
    else:  # Si no
        # Dos arrays para mirar en posiciones diferentes
        dirs_X = [1, 0, -1, 0]
        dirs_Y = [0, 1, 0, -1]
        for i in range(len(dirs_X)):  # Por cada dirección
            next_X = celda_act[0] + dirs_X[i]  # Mi siguiente x va a moverse hacia donde me diga el vector de las x
            next_Y = celda_act[1] + dirs_Y[i]  # Mi siguiente y por donde me diga el vector de als Y
            if esFactible(laberinto, (next_X, next_Y), visited):  # Si esa posición es factible
                visited.add((next_X, next_Y))  # La añadimos a posición ya visitada
                min_steps = salirDelLaberinto(laberinto, (next_X, next_Y), steps + 1, min_steps, visited)  # Ejecutamos el backtracking con los mismos valores pero habiendo avanzado un paso
                visited.remove((next_X, next_Y))  # Cuando vuelvo del backtracking, tengo que deshacer mi movimiento
    return min_steps  # Devolvemos el número de pasos


if __name__ == '__main__':  # Main
    laberinto = inicializarLaberinto()  # inicializamos el laberinto de la diapo
    mejor_sol = float('inf')  # mejor solución
    celda_inicial = (0, 0)  # celda inicial
    steps = 1  # Doy un paso
    visited = set()  # Conjunto de celdas ya visitadas
    visited.add(celda_inicial)  # añadimos la primera celda
    mejor_sol = salirDelLaberinto(laberinto, celda_inicial, steps, mejor_sol, visited)  # para salir del laberinto necesito el laberinto, la celda inicial, los pasos que llevo, la mejor solución hasta ahora, y el conjunto de visitados
    print(mejor_sol)
