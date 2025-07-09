def esSolucion(solucion, nodo):  # Es solucion
    return nodo == len(solucion)  # Cuando hayamos llegado a un punto en el que el nodo que queremos pintar es igual a la longitud de la solución (habríamos comprobado ya que es factible y avanzaríamos a un nodo en el que me estoy saliendo de la lista)


def esFactible(grafo, solucion, nodo, color):  # Es factible
    factible = True  # Flag que me dice si es factible
    i = 0  # i = 0
    while factible and i < len(grafo[nodo]):  # Mientras sea factible, e i sea menor que los adyacentes de ese nodo
        if solucion[grafo[nodo][i]] == color:  # Si en mi solución, ese nodo adyacente por el que voy tiene el mismo color que con el que quiero pintar
            factible = False  # Deja de ser factible
        i += 1  # Y si no pues sigo iterando
    return factible  # Devuelvo si es factible o no


def esMejor(solucion, mejorSol):  # Solucion mejor que otra
    return max(solucion) - min(solucion) < max(mejorSol) - min(mejorSol)  # Ver cuántos colores he utilizado. (Ver que el numero de colores que he usado en mi solución actual)


def coloring_bt(grafo, m, solucion, mejorSol, nodo, soluciones):  # Metodo coloreado backtraking
    if esSolucion(solucion, nodo):  # Vemos si la solucione en la que estoy (el nodo por el que voy) es solución
        if esMejor(solucion, mejorSol):  # Vemos si es mejor la solución de ahora que la que tengo hasta el momento
            mejorSol = solucion.copy()  # solucion[:] (otra forma de hacerlo) Actualizamos mejor sol con la copia de esta solución. Usamos copy porque las dos listas son arrays de enteros (tipos primitivos)
        soluciones.append(solucion.copy())  # En soluciones nos guardamos la solución también
    else:  # Si no
        color = 1  # Empezamos por el color 1
        while color <= m:
            if esFactible(grafo, solucion, nodo, color):  # Si es factible que mi grafo con mi solución con el nodo que voy por el color que voy
                solucion[nodo] = color  # En mi solución para este nodo pongo el color que toque
                mejorSol = coloring_bt(grafo, m, solucion, mejorSol, nodo + 1, soluciones)  # Llamada recursiva sigo explorando mi grafo
            # Si no es factible
            color += 1  # Tendré que probar con el siguiente color
            solucion[nodo] = 0  # Y deshacer el movimiento que hice que es descolorear ese nodo
    return mejorSol  # Cuando salga de lo anterior esto devolveré mi mejor solución


if __name__ == '__main__':  # Main (vamos a hacer dos aproximaciones. Distinguiremos cuál es mi mejor solución y me guardaré también todas las soluciones)
    grafo = [[1, 2, 3], [0], [0, 3], [0, 2]]  # Grafo con lista de adyacencias (es el de las diapos)
    solucion = [0] * len(grafo)  # Solución almacenará inicialmente un 0 por cada nodo del grafo (no está coloreado)
    mejorSol = list(range(1, len(grafo) + 1))  # Mejor solución para guardarme la mejor solución (la que utiliza un menor número de colores). La inicializamos de tal forma que haya más colores que nodos en el grafo
    m = 5  # Cinco colores
    soluciones = []  # Soluciones
    mejorSol = coloring_bt(grafo, m, solucion, mejorSol, 0, soluciones)  # Le pasamos el grafo, el número de colores, la solución actual, la mejor solución, 0, Soluciones
    print(mejorSol)  # Imprimimos la mejor solución
    print(soluciones)  # Imprimimos todas las soluciones a las que llegue
