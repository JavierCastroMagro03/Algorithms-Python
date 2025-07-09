# Decidir cuál es el orden en el que van a ocupar dicho recurso
# Vamos a ordenar a los miembros de la familia
# Primero va el que tiene más urgencia (paciencia/urgencia) ordenado de menor a mayor. En caso de que tengan mismo nivel de paciencia, irá delante el que más urgencia tenga.
# No es una mochila al uso porque no tengo un límite de espacio, sino que tengo que saber un orden y un tiempo de espera

def mochila(familiares):
    orden = []  # Necesitamos saber en qué orden van a entrar los objetos a mi mochila
    suma = 0  # Tengo que guardarme cuanto tiempo total lleva esperando la gente
    for i in range(len(familiares)):
        orden.append((familiares[i][1], suma))  # Me guardo cuál es el nombre del familiar que guardo en la posición (0, 1) y el tiempo que lleva esperando
        suma += familiares[i][4]  # Y me guardo el tiempo
    return orden  # Devuelvo el orden


# Entrada
if __name__ == '__main__':
    n = int(input().strip())  # Familiares
    familiares = []  # Lista de familiares
    for _ in range(n):  # Por cada familiar
        nombre, paciencia, urgencia, tiempo = input().strip().split()  # Leemos su nombre, paciencia, urgencia y tiempo
        familiares.append((int(paciencia)/int(urgencia), nombre, int(paciencia), int(urgencia), int(tiempo)))  # Añadimos los datos. Siendo lo primero paciencia/urgencia
        familiares.sort()  # Ordenamos de menor a mayor por paciencia/urgencia
    orden_mochila = mochila(familiares)  # Recibo el orden
    for familiar in orden_mochila:  # Para cada familiar en la mochila
        print(familiar[0])  # Imprimimos su nombre
    orden_mochila.sort()  # Ordenar de nuevo los familiares que hemos añadido para tenerlos ordenados alfabéticamente
    print(orden_mochila[0][1])  # Imprimir el tiempo del primero ya estando ordenados
