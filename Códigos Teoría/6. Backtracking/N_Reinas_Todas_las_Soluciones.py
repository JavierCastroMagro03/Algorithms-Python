def esSolucion(sol, fila_act):  # Método essolucion
    return fila_act == len(sol)  # Es solución si la fila actual es len de sol (he colocado todas las reinas)


def esFactible(sol, fila_act, col):  # Método es factible
    es_factible = True  # flag de si es factible o no
    i = 1  # Truquito i = 1
    while es_factible and i <= len(sol):  # Para poder usar nuestro vector y evaluar fila columna y diagonales, podemos hacer uso de indices. Mientras sea factible e i sea menor que el tamaño de mi solución
        factibleCol = sol[fila_act - i] == -1 or sol[fila_act - i] != col  # Primero vemos si la columna es factible (siempre y cuando en mi fila por la que voy - esa i que nos recorre las posiciones anteriores a la mía sea -1 o que en esa fila que estoy mirando haya algo diferente a la columna que estoy mirando ahora. Eso implicaría que en esa columna ya había colocado una reina previamente) (que en las posiciones anteriores no haya nada colocado o que en mi posición actual no haya ya una reina)
        facibleDiag1 = sol[fila_act - i] == -1 or sol[fila_act - i] != (col - i)  # Diagonal factible (si en alguna de las diagonales tengo alguna reina colocada ya) (esto para diagonal de arriba izda a abajo dcha)
        factibleDiag2 = sol[fila_act - i] == -1 or sol[fila_act - i] != (col + i)  # La otra diagonal
        es_factible = factibleCol and facibleDiag1 and factibleDiag2  # Que lo anterior sea factible lo hará factible
        i += 1  # Incrementamos i para mirar las posiciones
    return es_factible  # Devolvemos el flag


def n_queens(sol, fila_act, N, soluciones):  # Método n-reinas
    if esSolucion(sol, fila_act):  # Caso base es ver si la solución en la que estoy y la fila por la que voy
        soluciones.append(sol.copy())  # solucion_encontrada = True  # En este caso cambiamos el parámetro
    else:  # Si no (si no he llegado a una solución)
        col = 0  # Voy a mirar todas las columnas
        while fila_act < N and col < N:  # Mientras queden reinas por colocar
            if esFactible(sol, fila_act, col):  # Si es factible en mi solución actual colocar en una fila y en la columna actual
                sol[fila_act] = col  # Colocamos la reina en esa solución (Hacemos movimiento)
                soluciones = n_queens(sol, fila_act + 1, N, soluciones)  # sol, solucion_encontrada = n_queens(sol, fila_act + 1, N, solucion_encontrada)  # Backtraking (seguimos explorando)
                # if not solucion_encontrada:  # Llamada recursiva
                # Si llegamos aquí es que por el camino anterior no llegamos a una solución
                # Si aún no he encontrado solución
                sol[fila_act] = -1  # Quitamos la reina. Deshacemos la última decisión tomada. (deshacemos movimiento)
            col += 1  # Incrementamos la columna para probar por otro lado.
    return soluciones  # sol.copy(), solucion_encontrada  # Devolvemos los dos valores de la llamada recursiva. Necesitamos hacer una copia para recuperar el estado de la lista antes de la llamada recursiva


if __name__ == '__main__':
    N = 8  # Vamos a empezar con 4 reinas
    sol = [-1] * N  # Nuestro vector de solución es un array en el que tenemos un -1 por cada reina. Ejemplo: [1, 3, 2, 0] en la fila 0 la reina está en la columna 1, en la fila 2 la reina está en la columna 3, en la fila 2 la reina está en la columna 2...
    soluciones = []  # Lista para guardarme todas las soluciones
    sol = n_queens(sol, 0, N, soluciones)  # Para este método necesitaré mi vector, cuál es la fila en la que voy a empezar(0), cuántas reinas tengo que colocar y el último parámetro indica si he encontrado una solución o no
    print(sol)  # Una vez tenga colocadas las reinas, imprimo en que fila las he colocado
