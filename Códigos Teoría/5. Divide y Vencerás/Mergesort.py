def merge(left, right, arr):  # fusion
    l = r = a = 0  # l primer vector (indice para el vector left) r segundo vector(indice para el vector right) y a el resultado en que lo tengo que colocar
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:  # Si en mi vector izquierdo en la posicion izquierdo es menor o igual que mi array derecho en la posición r
            arr[a] = left[l]  # En mi array en la posición a tendré que colocar el menor
            l += 1  # E incrementamos el índice izquierdo.
        else:  # en el caso contrario (el indice del vector de la derecha tiene un elemento menor o igual que el índice de mi vector de la izquierda)
            arr[a] = right[r]  # añado ese elemento a mi array final
            r += 1  # incremento el índice r
            a += 1  # incrementamos el índice de mi array final

    if r == len(right):  # si r es el final de mi vector de la derecha,
        f = l  # entonces mi primer vector ahora es l
    else:  # y si no
        f = r  # es r
    if r == len(right):  # Esto me indica cual es el índice en el que me he quedado sin ordenar cosas
        resto = left  # el resto de cosas que me quedan por ordenar son
    else:  # si he llegado a ordenar completamente el vector de la derecha
        resto = right  # el array que me queda por ordenar es el de la derecha
    for i in range(f, len(resto)): # ahora por cada elemento desde f que es el nuevo índice de donde me había quedado hasta el resto
        arr[a] = resto[i]  # en el array final en donde estaba (a) meto ese elemento
        a += 1  # E incrementamos


# Caso base: vector de tamaño 1
def mergesort(arr):
    if len(arr) == 1:
        return  # devolvemos (porque ese vector ya estará ordenado)
    else:  # Si no estoy en el caso en el que el array es de tamaño uno
        mid = len(arr) // 2  # lo divido a la mitad
        # y tendré dos vectores diferentes parte derecha de los : es intervalo abierto )
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)  # aplicar mergesort sobre el vector izquierdo
        mergesort(right)  # mergesort sobre el vector derecho
        merge(left, right, arr)  # y fusionar el izquierdo sobre el derecho en el array.
# Este método no se puede transformar a iterativo.


if __name__ == '__main__':
    arr = [3, 1, 4, 1, 7, 9, 2, 6, 5, 3, 5, 8]
    mergesort(arr)
    print(arr)
