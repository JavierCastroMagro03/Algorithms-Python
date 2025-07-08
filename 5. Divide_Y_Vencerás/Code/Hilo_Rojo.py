#  dados dos conjuntos de personas, situados cada uno en una posición, sea capaz de decirnos en qué posición de
#  cada conjunto se encuentran los dos extremos del hilo rojo.

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
    # Lectura de entrada
    nPGrupo1 = int(input().strip())
    grupo1 = list(map(int, input().strip().split()))
    # print(grupo1)

    nPGrupo2 = int(input().strip())
    grupo2 = list(map(int, input().strip().split()))
    # print(grupo2)

    nParejasConectadas = int(input().strip())

    ini = 0  # i
    fin1 = len(grupo1) - 1  # j
    fin2 = len(grupo2) - 1  # j
    for _ in range(nParejasConectadas):
        pareja1, pareja2 = map(int, input().strip().split())
        posicion1 = busq_bin(grupo1, pareja1, ini, fin1)
        posicion2 = busq_bin(grupo2, pareja2, ini, fin2)

        if posicion1 >= 0 and posicion2 >= 0:
            print(posicion1, posicion2)
        else:
            print("SIN DESTINO")

'''
6
5 21 32 42 87 92
4
10 50 78 97
3
87 97
21 10
32 40
'''
