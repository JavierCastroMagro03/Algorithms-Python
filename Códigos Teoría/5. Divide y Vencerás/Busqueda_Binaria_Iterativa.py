def busq_bin_it(v, x):  # ITERATIVO
    i = 0  # necesitaré mi variable i
    j = len(v) - 1  # mi variable j
    while i <= j:  # Itera (while) mientras los índices no se crucen
        k = (i + j) // 2  # calculamos el medio
        if v[k] == x:  # si el elemento que hay en mi vector en esa posición es el que busco
            return k  # devuelvo k
        elif v[k] < x:  # si no si el elemento en que miro es menor que el elemento que busco
            i = k + 1  # aumento el valor de i
        else:  # si no
            j = k - 1  # reduzco el valor de j
    return -i  # si llegamos a este punto no lo habremos encontrado y podremos devolver ya -i


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8, 10, 12, 15]
    ini = 0  # i
    fin = len(arr) - 1  # j

    buscando = 3  # x
    posicion = busq_bin_it(arr, buscando)

    if posicion >= 0:
        print("El elemento", buscando, "está en la posición", posicion)
    else:
        print("El elemento", buscando, "no está en el array. Debería estar en la posición", -posicion)
