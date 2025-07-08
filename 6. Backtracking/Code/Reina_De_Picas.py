# Alternativa a laberinto en el que no hay muros, pero hay torretas
# Cada torreta abarca 360º Incluye diagonales
# Para que sea solución tengo que haber recogido todas las recompensas.

# Cuidado al leer la entrada, ya que al leer las torretas ya se por dónde no puedo pasar
# Al leer las recompensas, puedo saber si está en un área en el que haya torreta, no podré recogerla.
# Los caminos iniciales nos los dan en la entrada también


def esSolucion(f, c, end_f, end_c, recompensas):  # EsSolucion
    return f == end_f and c == end_c and recompensas == 0  # Si hemos llegado a esa situación y no quedan recompensas


def esFactible(lab, newF, newC):  # Para ver si un movimiento es factible
    if 0 <= newF < len(lab) and 0 <= newC < len(lab[0]):  # Si mi fila está dentro del laberinto y mi columna también lo está,
        return -1 <= lab[newF][newC] <= 0  # Lo que tengo que ver es que en mi casilla actual o bien haya una recompensa () o bien sea una casilla que aún no he transitado(0)
    else:  # Si no
        return False  # Return false


def reinapicasBT(lab, bestSol, f, c, pasos, recompensas, end_f, end_c):  # Backtraking
    if esSolucion(f, c, end_f, end_c, recompensas):  # Si es solución(en el laberinto que estoy, la fila, la columna en la que estoy, end fila, end columna, recompensas)
        if pasos < bestSol:  # Veo si he dado menos pasos que los que tengo como mejor solución
            bestSol = pasos  # Actualizo mi mejor solución
            # if bestSol - 1 == 25:  # Para depurar
                # imprimir(lab)
    else:  # Si no es solución
        desplazamientos = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # Con los desplazamientos
        i = 0  # i = 0
        while i < len(desplazamientos):  # Mientras yo pueda seguir desplazando
            nuevaFila = f + desplazamientos[i][0]  # Mi nueva fila va a ser fila + mi desplazamiento i en la pos 0
            nuevaColumna = c + desplazamientos[i][1]  # Mi nueva columna...
            if esFactible(lab, nuevaFila, nuevaColumna):  # Si es factible(esta nueva fila, esta nueva columna)
                old = lab[nuevaFila][nuevaColumna]  # Me guardo esta posición del laberinto
                if old == -1:  # Miro si hay recompensa
                    recompensas -= 1  # Si hay me quedará una menos
                lab[nuevaFila][nuevaColumna] = pasos  # Marco en mi laberinto con los pasos que lleve dados
                bestSol = reinapicasBT(lab, bestSol, nuevaFila, nuevaColumna, pasos + 1, recompensas, end_f, end_c)  # De nuevo hacemos la llamada con lo nuevo y las cosas actualizadas
                lab[nuevaFila][nuevaColumna] = old  # Cuando vuelva deshago el movimiento devolviendo el valor que me guarde
                if old == -1:  # Y si había recogido recompensa quitarla de mi cuenta
                    recompensas += 1  # Volver a añadirla al laberinto
            i += 1  # Incremento i
    return bestSol  # Devuelvo mis mejores pasos


def fillTurret(lab, n, m, x, y):  # Torretas
    # Donde estaba una torreta, mirar alrededor y marcarlo como transitable y si cubre una recompensa también la tengo que quitar porque nunca la podré recoger
    minusRewards = 0  # De primeras quito 0 recompensas
    # Podríamos hacer lo de las direcciones, pero vamos a hacer un truco.
    for i in range(max(0, x - 1), min(n, x + 2)):  # Recorrer siempre el máximo entre x -1 siendo x la posición que estoy mirando y voy hasta el minimo entre n y x+2. Con esto cubrimos también los casos en los que la torreta esté en las esquinas y en columna o fila limites
        for j in range(max(0, y - 1), min(m, y + 2)):  # Para las columnas entre 0 e y -1 lo que mas me de y entre m e y + 2 lo que menos me de
            if lab[i][j] == -1:  # Si me encuentro un -1 significa que tengo una recompensa
                minusRewards += 1  # Quito una a las que tengo que encontrar
            lab[i][j] = -2  # Pongo -2 a las casillas para marcar que por ellas no puedo pasar
    return minusRewards  # Devolvemos las recompensas que sí qeu puedo coger


# def imprimir(laberinto):  # Para imprimir el laberinto a la y poder ver el camino que va haciendo y depurar
    # for f in range(len(laberinto)):
        # for c in range(len(laberinto[0])):
            # print(laberinto[f][c], end='\t')
        # print()
    # print()


if __name__ == '__main__':  # Main
    nFilas, mColumnas = map(int, input().strip().split())  # n y m filas por columnas
    laberinto = []  # Laberinto de n filas por m columnas (all a ceros (suelo transitable), manejaremos mi entrada a enteros no con letras)
    recompensas = 0  # Numero de recompensas
    start = None  # Inicio del laberinto
    end = None  # Salida del laberinto
    for i in range(nFilas):  # Por cada fila en el laberinto
        laberinto.append([0] * mColumnas)  # Vamos a añadir un 0 por cada columna
    # Al leer la entrada iremos actualizando esos valores
    for i in range(nFilas):  # Para cada fila
        line = input().strip().split()  # Me guardo la fila en un array
        for j in range(mColumnas):  # Por cada columna
            if line[j] == 'w':  # Si en mi linea en j hay una w
                laberinto[i][j] = -2  # Ponemos un muro que lo marcamos con el número -2
            elif line[j] == 't':  # Si no tengo una w puedo tener una t
                recompensas -= fillTurret(laberinto, nFilas, mColumnas, i, j)  # Reducimos el número de recompensas con lo que abarque mi torreta en esa posición
                # Si tiene una torreta all lo que esté alrededor en mi laberinto
            elif line[j] == 'r' and laberinto[i][j] >= 0:  # Si tengo algo que puedo transitar y hay una recompensa
                recompensas += 1  # Añado mi recompensa
                laberinto[i][j] = -1  # Marcamos que ya la hemos recogido a -1
            elif line[j] == 's':  # Si no me queda por leer la entrada y la salida del laberinto
                start = (i, j)  # Mi start es lo que está en la posición j
            elif line[j] == 'e':  # Si no, estaré en la salida
                end = (i, j)
    laberinto[start[0]][start[1]] = 1  # Marcamos el comienzo del laberinto(en la salida) un 1 (mi primer paso)
    bestSol = reinapicasBT(laberinto, float('inf'), start[0], start[1], 2, recompensas, end[0], end[1])  # Tenemos que guardarnos nuestra mejor solución y le mandamos mi laberinto, el minimo de pasos hasta el momento, donde empiezo, los pasos que llevo, el número de recompensas que me quedan por recoger y donde acabo
    print(bestSol - 1)  # La imprimimos con un -1 para que me guarde bien los steps porque en la última llamada le suma 1 cuando en verdad ya estaría fuera de mi laberinto
    # print(laberinto)

'''
6 8
f f w w f f r r
f s f f f f f f
f f w f t f f r
r f w r f f f f
f f f r f f e f
r f f f f f f f
'''
