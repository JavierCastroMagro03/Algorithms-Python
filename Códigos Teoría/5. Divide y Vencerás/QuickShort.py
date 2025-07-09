def pivot(arr, left, right):  # Metodo pivote
    pivote = arr[left]  # el pivote es el primer elemento del array
    i = left + 1  # i es el siguiente elemento del pivote
    while i < right and arr[i] < pivote and i < len(arr):  # Mientras i sea menor que derecho
        i += 1  # lo incrementamos
    j = right  # j lo dejamos como right y lo que hay ahi sea menor que el pivote
    while j > left and arr[j] > pivote:  # mientras j sea mayor que left y lo que hay en j sea mayor que el pivote
        j -= 1  # restamos 1 a j (lo decrementamos)
    while i < j:  # mientras no se crucen los índices
        arr[i], arr[j] = arr[j], arr[i]  # vamos a hacer el intercambio (estaremos en el caso en el que lo que hay en i es mayor y lo que hay en j es menor) Python con una variable intermedia que no vemos nos deja hacer el intercambio directamente
        i += 1  # cuando intercambiamos volvemos a incrementar la i
        while arr[i] < pivote:  # Mientras lo que haya hñi sea menor o igual que el pivote
            i += 1  # aumentamos la i
        j -= 1  # decrementamos j una posición
        while arr[j] > pivote and j > 0:  # Mientras lo que haya en j sea mayor que el pivote
            j -= 1  # decrementamos j
    arr[left], arr[j] = arr[j], arr[left]  # volemos a intercambiar (esta vez left te marca la posición del pivote)
    return j  # devolvemos j para saber por dónde seguir ordenando (al devolver esto marcamos el punto en el que sabemos que los elementos que están a la izda es menor que el pivote y los que están a la derecha son mayores)


def quicksort(arr, i, j):  # Metodo le pasamos el array, la i y la j
    if i > j:
        return arr
    else:
        pivote = pivot(arr, i, j)  # REVISAR SI AL DEVOLVER J SE USA AQUÍ El pivote es la mitad del array. pero no sabemos si lo que hay a la izquierda y a la derecha está o no ordenado.
        quicksort(arr, i, pivote - 1)  # Llamamos a quickshort desde i hasta el pivote -1. Lo llamamos porque no sabemos si está ordenado
        quicksort(arr, pivote + 1, j)  # Llamamos a quickshort desde el pivote + 1 hasta j


# Vamos a utilizar el mismo vector que en mergeshort
# i y j serán el primer y el último elemento del array
if __name__ == '__main__':
    arr = [4, 6, 4, 67, 4, 3, 4, 4, 65, 34, 5, 3, 5, 3]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
