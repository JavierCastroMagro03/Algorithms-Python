# esSolucion
def esSolucion(objetos, Peso_act, pMax, objetos_seleccionados):
    if Peso_act >= pMax:
        return True
    else:
        return False


# esFactible
def esFactible(objeto_act, Peso_act, pMax, objetos_seleccionados):
    pesorestante = pMax - Peso_act
    if pesorestante > 0:
        return True
    else:
        return False


# Mochila(0-1)
def mochilabt(objetos, Mejor_peso, Peso_act, pMax, Mejor_beneficio, Beneficio_act, objetos_seleccionados, objetos_mejor_sol, i):
    if esSolucion(objetos, Peso_act, pMax, objetos_seleccionados):
        if Beneficio_act > Mejor_beneficio:
            Mejor_beneficio = Beneficio_act
            Mejor_peso = Peso_act
            objetos_mejor_sol = objetos_seleccionados.copy()
    else:
        for k in range(i, len(objetos)):
            objeto_act = objetos[k]
            if esFactible(objeto_act, Peso_act, pMax, objetos_seleccionados):
                Beneficio_act += objeto_act[2]
                Peso_act += objeto_act[1]
                objetos_seleccionados.add(objeto_act[0])
                Mejor_beneficio, Mejor_peso, objetos_mejor_sol = mochilabt(objetos, Mejor_peso, Peso_act, pMax, Mejor_beneficio, Beneficio_act, objetos_seleccionados, objetos_mejor_sol, k + 1)
                Beneficio_act -= objeto_act[2]
                Peso_act -= objeto_act[1]
                objetos_seleccionados.remove(objeto_act[0])
    return Mejor_beneficio, Mejor_peso, objetos_mejor_sol


# Entrada
if __name__ == '__main__':
    nJugadores, pMax = map(int, input().strip().split())
    objetos = []
    for _ in range(nJugadores):
        nombreJ, peso, beneficio = input().strip().split()
        objetos.append((str(nombreJ), int(peso), int(beneficio)))
    # Variables
    Mejor_peso = 0
    Peso_act = 0
    Mejor_beneficio = 0
    Beneficio_act = 0
    objetos_seleccionados = set()
    objetos_mejor_sol = set()
    objetos_mejor_sol = set()
    Mejor_beneficio, Mejor_peso, objetos_mejor_sol = mochilabt(objetos, Mejor_peso, Peso_act, pMax, Mejor_beneficio, Beneficio_act, objetos_seleccionados, objetos_mejor_sol, 0)
    print(Mejor_beneficio, Mejor_peso - pMax)
    solucion = []
    for objeto in objetos_mejor_sol:
        solucion.append(objeto)
    solucion.sort()
    for sol in solucion:
        print(sol)

'''
5 735
MelvinHarwood 266 263
MaggieRautenberg 203 262
SandraLytell 268 293
CynthiaVogt 298 240
LaverneCarroll 270 229
'''

'''
5 514
RobertLu 210 271
MaryVazquez 260 244
BernadetteReper 269 207
VirginiaValentine 287 201
MarkBoyd 218 293
'''
