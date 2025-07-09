def esSolucion(actCost, objetos, P, objetos_seleccionados):  # Metodo esSolución
    min_peso = float('inf')  # Inicializo la variable (a infinito) en la que acumularé el peso mínimo del objeto que pueda añadir a la mochila
    for objeto in objetos:  # Para todos los objetos que tengo
        # De todos mis objetos disponibles buscamos el que menos pesa. Porque si ese no lo puedo añadir, ninguno más podrá ser añadido.
        if objeto[1] < min_peso and objeto[0] not in objetos_seleccionados:  # Si mi objeto[1(peso)] pesa menos que el peso mínimo que tengo guardado y no lo he añadido ya a la mochila
                min_peso = objeto[1]  # Actualizo mi peso mínimo
    return actCost + min_peso > P  # Devolvemos true si el coste actual + el nuevo peso de mi objeto que menos pesa. Si me cabe en la mochila


def esFactible(obj_actual, actCost, objetos_seleccionados, P):  # Metodo esFactible
    return actCost + obj_actual[1] <= P and obj_actual[0] not in objetos_seleccionados  # devolvemos true si mi coste actual + el del objeto es menor o igual que el peso total de mi mochila y además no está en la mochila


def bt(objetos, actCost, actProfit, bestProfit, i, P, objetos_seleccionados):  # Primero vamos a hacer el backtraking (definimos la función) le pasamos los objetos el coste que llevo hasta ese momento, el valor y llevar en una variable el mejor beneficio que llevo hasta ahora
    # o = (nombre, coste, beneficio) # los objetos van a ser nombre, coste, beneficio
    if esSolucion(actCost, objetos, P, objetos_seleccionados):  # Como nos apoyamos en la recursividad. Primero tendremos que definir el caso base. Si es solución mi mochila con el coste actual, los objetos que tengo y mi peso
        if actProfit > bestProfit:  # Si el beneficio actual de mi mochila es mejor que el mayor que tenía hasta el momento
            bestProfit = actProfit  # Nos guardamos el mejor beneficio que tenemos hasta el momento
    else:  # Si no estoy en el caso de haber llegado a una solución
        for k in range(i, len(objetos)):  # Para cada k en mis objetos
            o = objetos[k]  # Seleccionamos el objeto que toca
            if esFactible(o, actCost, objetos_seleccionados, P):  # Mirar si es factible teniendo en cuenta el coste que llevo
                actCost += o[1]  # Actualizamos mi coste con lo que cueste el objeto
                actProfit += o[2]  # Actualizo el beneficio con el beneficio del objeto
                objetos_seleccionados.add(o[0])  # Añadimos el nombre del objeto a mi lista de objetos seleccionados
                bestProfit = bt(objetos, actCost, actProfit, bestProfit, k + 1, P, objetos_seleccionados)  # Llamada recursiva guardándonos lo que me devuelva como el mejor profit
                # A la vuelta de la recursión es cuando veremos si tenemos que volver atrás porque la recursividad ya ha hecho todas las llamadas recursivas para ese caso concreto.
                # Entonces restamos lo que le sumé tanto al coste como al beneficio
                actCost -= o[1]
                actProfit -= o[2]
                objetos_seleccionados.remove(o[0])
    return bestProfit  # Devolvemos el mejor profit que tengo hasta ahora

# LA I LA AÑADIÓ DESPUÉS. CON ELLA YA NO ANALIZAMOS SOLUCIONES POR LAS QUE YA PASAMOS. AÚN ASÍ HACEMOS EXPLÍCITA LA COMPROBACIÓN EN ESFACTIBLE


# Objetos de la diapo
# Inicialización de las variables
if __name__ == '__main__':
    objetos = [("obj1", 2, 3), ("obj2", 3, 5), ("obj3", 4, 6), ("obj4", 5, 10)]
    actCost = 0
    actProfit = 0
    bestProfit = 0
    W = 8  # W = P
    beneficio = bt(objetos, actCost, actProfit, bestProfit, 0, W, set())
    print(beneficio)

# ADEMÁS, EL PROFE HA PROPUESTO AÑADIR A ESTA MOCHILA LO NECESARIO PARA DEVOLVER TAMBIÉN LOS OBJETOS QUE HEMOS METIDO EN LA MOCHILA Y QUE NOS DEVUELVEN LA MEJOR SOLUCIÓN
