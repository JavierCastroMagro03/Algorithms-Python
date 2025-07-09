def busquedabinaria(LvlE, LvlCaballero, i, j):
    if i > j:
        return i  # Si no está el elemento devolvemos la posición en la que debería de estar
    else:
        k = (i + j) // 2
        if LvlE[k] == LvlCaballero:
            return k
        elif LvlE[k] < LvlCaballero:
            return busquedabinaria(LvlE, LvlCaballero, k + 1, j)
        else:
            return busquedabinaria(LvlE, LvlCaballero, i, k - 1)


# Lectura entrada
if __name__ == '__main__':
    nEnemigos = int(input().strip())
    LvlE = list(map(int, input().strip().split()))
    # print(LvlE)
    PuntosSumados = []
    suma = 0
    for iterador in range(len(LvlE)):
        suma += LvlE[iterador]
        PuntosSumados.append(suma)
    # print(PuntosSumados)
    nCPrueba = int(input().strip())
    solucion = []
    ini = 0  # i
    fin = len(LvlE) - 1  # j
    for caso in range(nCPrueba):
        puntos = 0
        LvlCaballero = int(input().strip())
        posicion = busquedabinaria(LvlE, LvlCaballero, ini, fin)
        # print(posicion)
        if LvlCaballero < LvlE[0]:
            solucion.append((0, 0))

        elif posicion >= len(PuntosSumados):  # Si es más alto que el enemigo de mayor nivel mata a todos
            solucion.append((posicion, PuntosSumados[posicion - 1]))

        elif LvlCaballero < LvlE[posicion]:  # Si el nivel de caballero que estoy comprobando es menor que el nivel del enemigo que está en posición, mato hasta esa posición
            solucion.append((posicion, PuntosSumados[posicion - 1]))

        else: # Si encuentro un enemigo con el mismo nivel que mi caballero mato a todos hasta esa posición + 1 (para que también me cuente como matado el de esa posición)
            solucion.append((posicion + 1, PuntosSumados[posicion]))

    for Eeliminados, puntos in solucion:
        print(Eeliminados, puntos)

'''
7
1 2 3 4 5 6 7
3
3
10
2
'''
'''
7
1 2 3 4 5 6 7
3
0
10
2
'''
