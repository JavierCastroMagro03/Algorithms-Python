# Topological short
# Vamos a utilizar diccionarios para definir el grafo (aquí aprovecha para explicar los punteros)
# El diccionario funciona como un array, pero en vez de acceder con índices 1,2,3,4... en este caso accedemos con
# calcetines, pantalon, camisa...
# - El uso del diccionario simplemente le añade complejidad al algoritmo.
# - Lo hace con diccionario para enseñarnos una estructura de datos "especial" que en verdad funciona como un array de nombres.
# - Vamos a usar dos estructuras de datos más. Una que me guarda los números que me guardan a la izda (d) y otra que me guarda los de la derecha (f) de finish.
from collections import deque


# IMPLEMENTACIÓN
def topSortVisit(data, k):
    data["state"][k] = "VISITED"  # Marcamos como visitado (color gris)
    data["time"] += 1  # incrementamos el iterador
    data["d"]["k"] = data["time"]  # Asignamos a d en qué iteración lo visitamos
    # Recorrer los adyacentes de un nodo y si no están visitados hacemos la llamada recursiva desde cada uno de los nodos
    for adj in data["graph"][k]:
        if data["state"][adj] == "NOT VISITED":
            topSortVisit(data, adj)  # Llamada recursiva
    # Hasta aquí es un recorrido en profundidad. Ahora van las instrucciones específicas de la ordenación topológica.
    data["state"][k] = "FINISHED"  # Marcamos como terminado (color negro)
    data["time"] += 1
    data["f"][k] = data["time"]  # Asignamos a f la iteración en el que lo visitamos. Para que no coincida con el de la izquierda le incrementamos 1
    data["sol"].appendleft(k)  # Ahora metemos los valores en la solución. Recordar que queremos hacer las inserciones por la izquierda


def topSort(g1):
    # g1 apunta al mismo contenido que g. si modifico g1 modifico el contenido
    data = {  # Data es otra estructura de datos que tiene graph que punta tmb al diccionario original.
        # Podemos acceder, por lo tanto, a la misma estructura de datos a través de g, g1 y "data" usando g1
        "graph": g1,
        "state": dict(),
        # Es el color correspondiente (blanco, gris, negro) # Es un puntero a un diccionario que está vacío
        "d": dict(),
        "f": dict(),
        "time": 0,  # Número de iteraciones (el que incrementaremos por cada nodo visitado)
        "sol": deque()
        # Solución en la que me va a poner el grafo en el orden ya correcto (el que imprimiré por pantalla). Usaremos una bicola
    }
    for k in g1.keys():  # keys saca calcetines, pantalon, camisa, zapatos... y k adquiere ese valor
        data["state"][
            k] = "NOT VISITED"  # data de state de zapatos, data de state de pantalon... los marcamos como "blanco"
        data["d"][k] = 0
        data["f"][k] = 0
        data["time"] = 0

    # for v in range(1, n):
    # if v not in visited:
    # dfsRec(v, g, visited)
    for k in g1.keys():
        if data["state"][k] == "NOT VISITED":
            topSortVisit(data, k)
    print(data["sol"])  # lo imprimimos por aquí porque sabemos que cuando este bucle llegue al final significa que se ha recorrido todo el grafo


# DATOS
# g = dict()
g = {
    "calcetines": ["zapatos"],  # zapatos es adyacente a calcetines
    "pantalon": ["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [],  # como no tiene adyacentes lo ponemos como lista vacía
    "pantalon": [],
    "jersey": [],
    "cinturon": []
}

# LLAMADA
topSort(g)
