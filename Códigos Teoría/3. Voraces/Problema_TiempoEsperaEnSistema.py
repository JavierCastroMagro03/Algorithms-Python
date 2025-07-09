tareas = [(5, 0), (10, 1), (3, 2)]  # Tiempo de cada tarea
tareas.sort()  # Ordenamos las tareas de menor a mayor porque es el voraz que sabíamos en el que teníamos que ordenar
sumatiempo = 0  # Tiempo total
accumulado = 0  # Tiempo ya acumulado en el sistema
orden = ""
for e in tareas:  # Recorremos tareas
    accumulado += e[0]  # El tiempo acumulado es igual a el primer índice de la primera tuple de la lista tareas
    sumatiempo += accumulado  # El tiempo total será tiempo total + el acumulado
    orden += str(e[1]) + ","  # imprimimos el orden
print("{:.2f}".format(sumatiempo / len(tareas)))  # Tiempo promedio ajustado a dos decimales
print(orden)
# Si quiero recuperar en el resultado final en que orden debo de realizar las tareas.
# En que orden hago las tareas para que me haya devuelto 9.67
# Añadimos una segunda propiedad a cada elemento
