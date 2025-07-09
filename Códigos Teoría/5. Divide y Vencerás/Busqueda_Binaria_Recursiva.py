def busq_bin(v, elem, i, j):  # Vector que necesitamos, elemento que buscamos, índice inicial, índice final
    if i > j:  # primero miramos si inicio es mayor que fin
        return -i  # Si lo es devolvemos -ini ¿por qué? Para representar que mi elemento no está en el vector. Valor negativo para representar que no está el elemento. Devolvemos la posición en la que debería de estar mi elemento buscado en caso de estar en el vector. si devolviésemos -1 no sabríamos la posición en la que debería de estar.
    else:  # si no
        k = (i + j) // 2  # calculamos k (el punto pedio)
        if v[k] == elem:  # Si el elemento de la mitad es igual que el que buscamos (elem)
            return k  # devolvemos dónde está situado
        elif v[k] < elem:  # Si no comprobamos si k es menor que el elemento que busco
            return busq_bin(v, elem, k + 1, j)  # Buscamos en el lado derecho del array (desplazamos i a esta parte). Importante poner el return al hacer la llamada recursiva
        else:  # Si no, estaré en el caso contrario y lo que tendré que hacer es:
            return busq_bin(v, elem, i, k - 1)  # Mover la j hacia la izda (para mirar el  lado izquierdo del array). Comprobaremos que el elemento que estamos mirando ahora, es mayor.


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8, 10, 12, 15]
    # Importante índice a 0 y j al tamaño del array - 1 porque si no nos saldremos del array
    ini = 0  # i
    fin = len(arr) - 1  # j
    buscando = 3  # x
    posicion = busq_bin(arr, buscando, ini, fin)
    # Podremos decir si está en la posición x y los números de la izda se desplazan o que esta en el hueco de la decha y el elemento que esté ahí se desplaza. Este criterio lo definirá el enunciado del examen.
    if posicion >= 0:
        print("El elemento", buscando, "está en la posición", posicion)
    else:
        print("El elemento", buscando, "no está en el array. Debería estar en la posición", -posicion)
