def busquedabinaria(v, elem, i, j):  # Vector que necesitamos, elemento que buscamos, índice inicial, índice final
    if i > j:  # primero miramos si inicio es mayor que fin
        return i  # Si lo es devolvemos -ini ¿por qué? Para representar que mi elemento no está en el vector. Valor negativo para representar que no está el elemento. Devolvemos la posición en la que debería de estar mi elemento buscado en caso de estar en el vector. si devolviésemos -1 no sabríamos la posición en la que debería de estar.
    else:  # si no
        k = (i + j) // 2  # calculamos k (el punto pedio)
        if v[k] == elem:  # Si el elemento de la mitad es igual que el que buscamos (elem)
            return k  # devolvemos dónde está situado
        elif v[k] < elem:  # Si no comprobamos si k es menor que el elemento que busco
            return busquedabinaria(v, elem, k + 1,
                                   j)  # Buscamos en el lado derecho del array (desplazamos i a esta parte). Importante poner el return al hacer la llamada recursiva
        else:  # Si no, estaré en el caso contrario y lo que tendré que hacer es:
            return busquedabinaria(v, elem, i,
                                   k - 1)  # Mover la j hacia la izda (para mirar el lado izquierdo del array). Comprobaremos que el elemento que estamos mirando ahora, es mayor.


# Lectura de entrada
if __name__ == '__main__':
    tamañomatriz = int(input().strip())
    matriz = []
    for _ in range(tamañomatriz):
        entrada = (input().strip().split())
        for i in entrada:
            matriz.append(int(i))
    # print(matriz)

    nEliminar = list(map(int, input().strip().split()))
    # print(nEliminar)

    ini = 0
    fin = len(matriz) - 1
    posiciones = set()
    for elem in nEliminar:
        pos = busquedabinaria(matriz, elem, ini, fin)
        # print(pos)
        if pos not in posiciones:
            posiciones.add(pos)
        else:
            while pos < len(matriz):
                if pos not in posiciones:
                    posiciones.add(pos)
                    break
                pos += 1
    # print(posiciones)
    for posicion in posiciones:
        matriz[posicion] = 'X'
    # print(posiciones)
    print(*matriz)

# Conjunto de elementos que mato, ir comprobando si ya lo he matado o no
'''
3
1 2 3
4 5 6
7 8 10
1 5 9
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
X 3 X 9 12 X X X X X X 42 53 76 89 93
'''

# Probar a hacer con dos búsquedas binarias una para saber en que fila buscar y otra para buscar en esa fila
