def busquedabinaria(matriz, elem, i, j):  # Vector que necesitamos, elemento que buscamos, índice inicial, índice final
    if i > j:  # primero miramos si inicio es mayor que fin
        return j  # Si lo es devolvemos -ini ¿por qué? Para representar que mi elemento no está en el vector. Valor negativo para representar que no está el elemento. Devolvemos la posición en la que debería de estar mi elemento buscado en caso de estar en el vector. si devolviésemos -1 no sabríamos la posición en la que debería de estar.
    else:  # si no
        k = (i + j) // 2  # calculamos k (el punto pedio)
        if matriz[k][0] == elem:  # Si el elemento de la mitad es igual que el que buscamos (elem)
            return k  # devolvemos dónde está situado
        elif matriz[k][0] < elem:  # Si no comprobamos si k es menor que el elemento que busco
            return busquedabinaria(matriz, elem, k + 1, j)  # Buscamos en el lado derecho del array (desplazamos i a esta parte). Importante poner el return al hacer la llamada recursiva
        else:  # Si no, estaré en el caso contrario y lo que tendré que hacer es:
            return busquedabinaria(matriz, elem, i, k - 1)  # Mover la j hacia la izda (para mirar el lado izquierdo del array). Comprobaremos que el elemento que estamos mirando ahora, es mayor.


def busquedabinariafilas(matriz, elem, i, j, pos_fila):
    if i > j:
        return i
    else:  # si no
        k = (i + j) // 2
        if matriz[pos_fila][k] == elem:
            return k
        elif matriz[pos_fila][k] < elem:
            return busquedabinariafilas(matriz, elem, k + 1, j, pos_fila)
        else:
            return busquedabinariafilas(matriz, elem, i, k - 1, pos_fila)


# Lectura de entrada
if __name__ == '__main__':
    tamañomatriz = int(input().strip())
    matriz = []
    for _ in range(tamañomatriz):
        fila = list(map(int, input().strip().split()))
        matriz.append(fila)
    print(matriz)

    nEliminar = list(map(int, input().strip().split()))
    print(nEliminar)

    ini = 0
    fincol = tamañomatriz - 1
    finfila = tamañomatriz - 1

    posiciones = set()
    for elem in nEliminar:
        pos_fila = busquedabinaria(matriz, elem, ini, fincol)
        print(pos_fila)

        pos = busquedabinariafilas(matriz, elem, ini, finfila, pos_fila)
        print(pos)

        while (pos_fila, pos) in posiciones:
            pos += 1
            if pos >= tamañomatriz:
                pos_fila += 1
                pos = 0
            if pos_fila >= tamañomatriz:
                break  # Ya no hay más sitio
        posiciones.add((pos_fila, pos))
    print(posiciones)

    for pos_fila, pos in posiciones:
        matriz[pos_fila][pos] = 'X'

    for fila in matriz:
        print(*fila)

# Conjunto de elementos que mato, ir comprobando si ya lo he matado o no
'''
3
1 2 3
4 5 6
7 8 10
1 5 9
'''
'''
X 2 3
4 X 6
7 8 X
'''

'''
4
1 3 7 9
12 15 19 20
23 34 39 42
53 76 89 93
1 6 13 14 15 16 17 29
'''
'''
X 3 X 9 
12 X X X 
X X X 42 
53 76 89 93
'''

# Probar a hacer con dos búsquedas binarias una para saber en que fila buscar y otra para buscar en esa fila
