def esSolucion(objetos, Peso_act, pMax, objetos_seleccionados): # Si no me cabe otro objeto
    min_peso = float('inf')
    for objeto in objetos:
        # De todos mis objetos disponibles buscamos el que menos pesa. Porque si ese no lo puedo añadir, ninguno más podrá ser añadido.
        if objeto[1] < min_peso and objeto[0] not in objetos_seleccionados:  # Si pesa menos y no está ya seleccionado
            min_peso = objeto[1]  # Actualizo mi peso mínimo
    return Peso_act + min_peso > pMax  # Devolvemos true si mi peso actual más el peso del objeto (de los que quedan) que menos pesa es menor que el peso total que aguanta mi mochila


def esFactible(obj_actual, Peso_act, objetos_seleccionados, pMax):
    # Es factible si el peso actual de la mochila más el peso de mi nuevo objeto es menor que el peso que soporta la mochila y además si ese objeto aún no ha sido seleccionado.
    return Peso_act + obj_actual[1] <= pMax and obj_actual[0] not in objetos_seleccionados


def backtraking(objetos, Peso_act, Beneficio_act, Mejor_beneficio, Mejor_peso, objetos_mejor_sol, i, pMax, objetos_seleccionados):
    if esSolucion(objetos, Peso_act, pMax, objetos_seleccionados):  # Caso base.
        if Beneficio_act > Mejor_beneficio:  # Si el beneficio actual es mejor que el mejor beneficio obtenido hasta el momento
            Mejor_beneficio = Beneficio_act  # Lo actualizo
            Mejor_peso = Peso_act  # Guardarme su peso
            objetos_mejor_sol = objetos_seleccionados.copy()
    else:
        for k in range(i, len(objetos)):  # Para cada objeto (nombre, peso, beneficio)
            o = objetos[k]  # Seleccionamos objeto
            if esFactible(o, Peso_act, objetos_seleccionados, pMax):  # Si es factible
                Peso_act += o[1]  # Actualizo el coste
                Beneficio_act += o[2]  # Actualizo el beneficio
                objetos_seleccionados.add(o[0])  # Añado el objeto al conjunto de objetos seleccionados
                Mejor_beneficio, Mejor_peso, objetos_mejor_sol = backtraking(objetos, Peso_act, Beneficio_act, Mejor_beneficio, Mejor_peso, objetos_mejor_sol, k + 1, pMax, objetos_seleccionados)  # Vuelta atrás
                # Deshacer
                Peso_act -= o[1]
                Beneficio_act -= o[2]
                objetos_seleccionados.remove(o[0])
    return Mejor_beneficio, Mejor_peso, objetos_mejor_sol


if __name__ == '__main__':
    # Lectura de entrada
    nObjetos, pMax, bMin = map(int, input().strip().split())
    objetos = []
    for _ in range(nObjetos):
        nombreO, peso, beneficio = (input().strip().split())
        objetos.append((str(nombreO), int(peso), int(beneficio)))
    # print(pMax)
    # print(bMin)
    # print(objetos)

    # Variables
    Peso_act = 0
    Mejor_peso = 0
    Beneficio_act = 0
    Mejor_beneficio = 0
    objetos_seleccionados = set()
    objetos_mejor_sol = set()
    beneficio, peso, seleccionados = backtraking(objetos, Peso_act, Beneficio_act, Mejor_beneficio, Mejor_peso, objetos_mejor_sol, 0, pMax, objetos_seleccionados)
    solucion = []
    for sol in seleccionados:
        solucion.append(sol)
    solucion.sort()
    print(*solucion)
    print(peso)
    print(beneficio)
    if beneficio <= bMin:
        print("VUELVE")
    else:
        print("SE VA")


# Entrada 1
'''
3 50 25
LibrosDeAlgoritmos 45 50
Toalla 25 30
GafasDeSol 25 30
'''

# Salida 1
'''
GafasDeSol Toalla
50 60
SE VA
'''