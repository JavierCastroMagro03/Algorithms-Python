# Cuando he decidido que mi arista debe de añadirse porque no están en la misma componente conexa, actualizamos los valores del array en el que indicamos para cada nodo en qué componente conexa se encuentra.
def actualizar_componentes(components, new_id, old_id):  # Me guardo los dos valores. Porque python me deja machacarlos mientras itero y no lo queremos
    for i in range(len(components)):  # Recorremos el array hasta el final, para actualizar todos porque si no tendría algo inconsistente.
        #  En el momento en el que encuentre un nodo que pertenezca a x componente lo tengo que cambiar.
        if components[i] == old_id:
            components[i] = new_id  # Actualizamos la componente a la nueva a la que pertenece


def kruskal(aristas, nNodos):
    coste = 0  # Inicializamos el coste a 0
    componentes = list(range(nNodos))  # Necesito una lista que me diga en qué componente está cada nodo. En un primer momento, cada nodo estará en una componente independiente.
    nComponentes = nNodos  # Cuántas componentes tengo en este momento
    arista_act = 0  # Qué arista estoy cogiendo (la primera del orden de mayor a menor) arista_act es el iterador en mi lista aristas
    aristas_sel = set()

    while nComponentes > 1 and arista_act < len(aristas):  # Hasta cuando voy a ejecutar kruskal. Hasta que todos los nodos estén en la misma componente conexa o bien, ya he añadido todos mis candidatos (aristas) a mi árbol de recubrimiento
        peso = aristas[arista_act][0]
        origen = aristas[arista_act][1]
        destino = aristas[arista_act][2]
        # Si la componente del origen es distinta de la componente de destino
        if componentes[origen] != componentes[destino]:  # no me unas los que ya están en la misma componente conexa para evitar ciclos
            # Sumo el peso de esa arista a mi coste del árbol
            coste += peso
            # Actualizo la lista de componentes con el valor de la componente de origen en el valor de la componente destino
            actualizar_componentes(componentes, componentes[origen], componentes[destino])  # Llamo a la función actualizar_componentes pasándole mi lista de componentes y las posiciones que tiene que actualizar
            nComponentes -= 1  # Decrementamos el número de componentes que tengo
            aristas_sel.add(aristas[arista_act])  # Añadimos la arista actual a la lista de seleccionadas
        arista_act += 1  # Pasamos a evaluar la siguiente arista
    return coste, aristas_sel  # Devolvemos el coste y el conjunto de aristas seleccionadas


if __name__ == '__main__':
    nNodos, mAristas = map(int, input().split())  # Nodos y aristas
    aristas = []  # Lista de aristas
    for _ in range(mAristas):  # Por cada numero de aristas
        origen, destino, peso = map(int, input().split())  # Leemos nodo origen nodo destino y el peso de la arista que los conecta
        aristas.append((peso, origen, destino))  # Añadimos estos datos a mi lista de aristas siendo la primera posición el peso
    aristas.sort()  # Ordeno de menor a mayor peso
    coste, aristas_sel = kruskal(aristas, nNodos)  # Llamo a la función para que me devuelva el coste y las aristas seleccionadas para que todos los nodos estén en la misma componente conexa con la menor suma de pesos posible y le pasamos la lista de aristas y el número de nodos
    # g = [[] for _ in range(n)] De esto nos olvidamos en kruskal porque solo nos va a consumir tiempo
    print(coste, aristas_sel)  # Imprimimos por consola el coste y las aristas seleccionadas

# Reducimos en 1 los índices porque si no en la lista de componentes conexas, como me genera de 0 a 6 cuando llegue a 7 explota. Entonces podríamos hacer components = list(range(n+1)) para que llegue hasta 7, pero lo que vamos a hacer es modificar la entrada reduciendo uno cada componente para empezar en 0 y terminar en 6. Cuidado que en el examen a lo mejor nos dan entrada que valga 1
'''
7 10
0 2 1
0 3 2
0 6 6
1 4 2
1 5 4
1 6 7
2 3 3
2 6 5
3 5 9
4 6 8
'''
