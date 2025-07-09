
def top_sort(g, nNodos):  # Definimos la función que recibe el grafo y el número de nodos
    aristas_entrantes = [0] * nNodos  # Definimos la lista aristas_entrantes que almacena el número de aristas que apuntan a cada uno de los nodos. Para nuestro caso lo inicializa así: aristas_entrantes = [[0], [0], [0], [0], [0]]
    for nodo_act in range(nNodos):  # Recorremos los nodos del grafo [[2, 1, 4], [2], [4, 3], [], []]
        for ady in g[nodo_act]:  # Por cada nodo, recorremos sus adyacentes "ady"
            aristas_entrantes[ady] += 1  # Al nodo ady le añadimos un nodo entrante. Es decir le añade una arista entrante al 2, al 1, al 4 luego pasa al nodo 1, lee su adyacente y le añade una arista entrante al 2

    nodos_iniciales = []  # Creamos la lista en la que  guardaremos los nodos que vayan teniendo 0 aristas incidentes
    for i in range(nNodos):  # Por cada nodo
        if aristas_entrantes[i] == 0:  # Si en la lista aristas_entrantes ese nodo tiene 0 aristas entrantes
            nodos_iniciales.append([i, 0])  # Lo añadimos a la lista de nodos_iniciales

    solucion = []  # Creamos la lista en la que iremos guardando los nodos
    Profundidad = 0

    while nodos_iniciales:  # Mientras haya nodos en nodos_iniciales (con 0 aristas incidentes)
        nodos_iniciales.sort()  # Los ordenamos para tener el orden lexicográfico
        origen = nodos_iniciales.pop(0)  # Sacamos el primero
        solucion.append(origen)  # Lo añadimos a la solución
        for adj in g[origen[0]]:  # En el grafo, por cada adjunto que hubiese en nuestro nodo origen
            aristas_entrantes[adj] -= 1  # En la lista de aristas incidentes le quitamos el nodo incidente que ya hemos añadido a la solución
            if aristas_entrantes[adj] == 0:  # Si al restarle la arista entrante se queda a 0
                nodos_iniciales.append([adj, Profundidad])  # Lo añadimos a nodos iniciales
        Profundidad += 1
    return solucion



# Entrada
if __name__ == '__main__':
    nNodos, mAristas = map(int, input().strip().split())  # Leemos el número de nodos y el número de aristas en la primera línea de la entrada
    g = [[] for _ in range(nNodos)]  # Por cada nNodos creamos en nuestro grafo []. Para este caso sería g = [[], [], [], [], []] donde se almacenarán los adyacentes a 0, los adyacentes a 1, los adyacentes a 2... hasta el nodo 4
    for _ in range(mAristas):  # Por cada número de aristas
        orig, dest = map(int, input().strip().split())  # nos guardamos en origen la arista de origen y en destino la arista de destino
        g[orig].append(dest)  # Por cada [] en la lista de adyacencias añadimos al [origen] su adyacente dest

    preguntas = []
    nPreguntas = int(input().strip())
    for _ in range(nPreguntas):
        nodoA, nodoB = map(int, input().strip().split())
        preguntas.append((nodoA, nodoB))
    solucion = top_sort(g, nNodos)  # Le pasamos al método el grafo y el número de nodos

    # Imprimimos la solución
    for tarea in solucion:  # Recorremos la lista solución
        print(tarea, end=' ')  # Imprimimos cada solución
    print(" ")
    for i in preguntas:
        a, b = i
        solucion.sort(key=lambda x: x[0])
        if solucion[a][1] > solucion[b][1]:
            print("Mayor rango")
        elif solucion[a][1] < solucion[b][1]:
            print("Menor rango")
        else:
            print("Rango similar")

'''
6 6
5 2
5 0
4 0
4 1
2 3
3 1
8
4 5
3 5
5 3
1 2
2 5
2 0
5 1
4 2
'''