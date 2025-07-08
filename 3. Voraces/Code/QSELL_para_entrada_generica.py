# Función
def algoritmo(parejas_ordenadas, tiempoRestante):
    solucion = []  # Lista para guardar la solución
    beneficio = 0  # variable para ir acumulando el beneficio obtenido
    for pareja in parejas_ordenadas:  # Por cada pareja
        if tiempoRestante > pareja[4]:  # Comprobamos que su tiempo esté dentro del límite
            solucion.append(pareja[0])  # Agregamos su nombre a la solución
            beneficio += pareja[cualidadmasValorada]  # Incrementamos el beneficio
            tiempoRestante -= pareja[4]  # Decrementamos el tiempo restante
        else:  # En caso de que no hay tiempo suficiente
            if tiempoRestante > 0:
                fraccion = tiempoRestante / pareja[4]  # Fraccionamos el tiempo
                beneficio += pareja[cualidadmasValorada] * fraccion  # calculamos el beneficio en función del  tiempo restante
                solucion.append(pareja[0])  # Añadimos su nombre a la solución
                tiempoRestante = 0  # El tiempo se acaba
    print(*solucion)  # Imprimimos los nombres de las parejas que lograron seducir al concursante
    print("{:.2f}".format(beneficio))  # Imprimimos el beneficio obtenido con dos decimales


if __name__ == '__main__':
    # Entrada
    nConcursantes = int(input().strip())  # Variable para almacenar el número de concursantes
    for _ in range(nConcursantes):  # Por cada concursante
        parejas = []  # Lista para almacenar las parejas recibidas por la entrada
        cualidadmasValorada = (input().strip())  # Variable para guardar en string la cualidad más valorada por el concursante
        tiempoRestante = int(input().strip())  # Tiempo que le queda a ese concursante en el programa
        nPosiblesParejas = int(input().strip())  # Variable para guardar la cantidad de posibles parejas
        for _ in range(nPosiblesParejas):  # Por la cantidad de parejas
            nombre, belleza, inteligencia, amabilidad, tiempo = input().strip().split()  # Leemos su nombre, belleza, inteligencia, amabilidad y tiempo que requiere para seducir
            parejas.append((nombre, int(belleza), int(inteligencia), int(amabilidad), int(tiempo)))  # Agregamos las parejas a la lista
        #  Para convertir la cualidad más valorada en un número para facilitarme la ordenación
        if cualidadmasValorada == 'kindness':
            cualidadmasValorada = 3  # Ordenaré teniendo en cuenta la posición de índice 3 de la lista
        elif cualidadmasValorada == 'intelligence':
            cualidadmasValorada = 2  # Ordenaré teniendo en cuenta la posición de índice 2 de la lista
        elif cualidadmasValorada == 'beauty':
            cualidadmasValorada = 1  # Ordenaré teniendo en cuenta la posición de índice 1 de la lista
        else:
            print("Cualidad no válida")  # Si recibo otra cualidad, "capturar el fallo"

        parejas_ordenadas = sorted(parejas, key=lambda x: (x[cualidadmasValorada] / x[4]), reverse=True)  # Ordenamos la lista de parejas en función de la cualidad más valorada entre su tiempo requerido para seducir
        algoritmo(parejas_ordenadas, tiempoRestante)  # Llamada a la función
