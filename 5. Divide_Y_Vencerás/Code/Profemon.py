# Nos dan un listado de números y dos índices, por lo tanto, tendremos que buscar en una lista de números los que hay entre dos índices
# La lista de entrada no tiene por qué estar ordenada
# Nos tenemos que dar cuenta de que la búsqueda binaria hay que lanzarla dos veces (una por índice)


def binary_search(data, start, end, search):  # Por último nos queda por implementar la búsqueda binaria (que es tal cual)
    if start > end:  # Si mis indíces se han cruzado
        return start  # en start debería de estar el elemento que busco
    else:  # Si no
        mid = (start + end) // 2  # divido a la mitad y evalúo
        if search == data[mid]:  # Si lo que busco es la mitad lo devuelvo
            return mid
        else:  # Si no
            if search > data[mid]:  # Voy hacia un lado, o
                return binary_search(data, mid + 1, end, search)
            else:  # me voy por el otro
                return binary_search(data, start, mid - 1, search)


if __name__ == '__main__':
    nProfemons, nEstudiantes = map(int, input().strip().split())  # Recibimos un entero que indica el número de profemons y el número de estudiantes que hay
    profemon = sorted(list(map(int, input().strip().split())))  # La lista que leemos que sabemos que es de enteros (profemons disponibles), lo mapeamos y convertimos a lista
    # Primero que nada ordenamos la lista ¿Por qué? Porque vamos a hacer una búsqueda binaria
    # print(profemon)
    max_profemons = 0  # variable que nos diga cuál es el máximo de profemon
    best_students = []  # Por otro lado, tenemos que imprimir de menor a mayor cuáles son los estudiantes que tienen ese número de profemons. Necesitaremos una estructura de datos para guardarnos eso mejores estudiantes
    for _ in range(nEstudiantes):  # Por cada estudiante
        stu_id, p1, p2 = map(int, input().strip().split())  # Nos guardamos su id y el resto de info(p1, p2) que hacen referencia al primer y último profemon del estudiante
        p1_idx = binary_search(profemon, 0, nProfemons-1, p1)  # Luego buscamos dónde está en mi lista desde 0 hasta n-1 ese primer índice
        p2_idx = binary_search(profemon, 0, nProfemons-1, p2)  # y dónde está el segundo (dos búsquedas binarias, pero buscando dos cosas diferentes)
        if max_profemons < (p2_idx - p1_idx + 1):  # Miramos los que están entre medias
            max_profemons = p2_idx - p1_idx + 1  # Ese máximo será justamente eso
            best_students = []  # Como hemos actualizado ese número máximo, todos los estudiantes que tenía guardados ya no tendrán el máximo, tengo que reiniciarla
            best_students.append(stu_id)  # Añado el estudiante que acabo de encontrar
        elif max_profemons == (p2_idx - p1_idx + 1):  # En otro caso
            best_students.append(stu_id)  # Solo añado a ese estudiante y si no no lo añado
    for s in best_students:  # Para cada uno de los estudiantes que me he guardado los imprimo
        print(str(s), end=" ")  # Con un espacio entre medias
    print()
    print(str(max_profemons))  # Imprimo el número máximo que he encontrado
