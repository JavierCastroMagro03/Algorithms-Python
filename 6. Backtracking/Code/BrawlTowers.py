# esSolución
def esSolucion(fila_act):
    return fila_act == nFilas


# esFactible
def esFactible(fila_act, columna_act, nivel):
    return nivel[fila_act][columna_act] == 0


# Colocar Brawler
def ponerBrawler(matriz, fila_act, columna_act, alcance, brawlers_colocados, nFilas, nColumnas):
    brawlers_act_sol = set()
    brawlers_act_sol.add((fila_act, columna_act))
    for i in range(1, alcance + 1):
        if columna_act + i < nColumnas:
            if matriz[fila_act][columna_act + i] == 0 and (fila_act, columna_act + i) not in brawlers_colocados:
                brawlers_act_sol.add((fila_act, columna_act + i))
        if columna_act - i >= 0:
            if matriz[fila_act][columna_act - i] == 0 and (fila_act, columna_act - i) not in brawlers_colocados:
                brawlers_act_sol.add((fila_act, columna_act - i))
        if fila_act + i < nFilas:
            if matriz[fila_act + i][columna_act] == 0 and (fila_act + i, columna_act) not in brawlers_colocados:
                brawlers_act_sol.add((fila_act + i, columna_act))
        if fila_act - i >= 0:
            if matriz[fila_act - i][columna_act] == 0 and (fila_act - i, columna_act) not in brawlers_colocados:
                brawlers_act_sol.add((fila_act - i, columna_act))
    return brawlers_act_sol


# N-reinas
def brawlersbt(brawlers_colocados, fila_act, nFilas, nColumnas, nivel, brawlers, max_cubiertas):
    if esSolucion(fila_act):
        max_cubiertas[0] = max(max_cubiertas[0], len(brawlers_colocados))
    else:
        alcance = brawlers[fila_act][1]
        for columna_act in range(nColumnas):
            if esFactible(fila_act, columna_act, nivel):
                brawlers_act_sol = ponerBrawler(nivel, fila_act, columna_act, alcance, brawlers_colocados, nFilas, nColumnas)
                brawlers_colocados.update(brawlers_act_sol)
                brawlersbt(brawlers_colocados, fila_act + 1, nFilas, nColumnas, nivel, brawlers, max_cubiertas)
                brawlers_colocados.update(brawlers_act_sol)


# Entrada
if __name__ == '__main__':
    nFilas, nColumnas = map(int, input().split())
    nivel = []
    for i in range(nFilas):
        fila = list(map(int, input().split()))
        nivel.append(fila)
    nBrawlers = nFilas
    brawlers = []
    for j in range(nBrawlers):
        nombre, alcance = input().split()
        brawlers.append((nombre, int(alcance)))
    max_cubiertas = [0]
    brawlers_colocados = set()
    brawlersbt(brawlers_colocados, 0, nFilas, nColumnas, nivel, brawlers, max_cubiertas)
    print(*max_cubiertas)

'''
4 5
0 0 0 0 0
-1 0 0 0 -1
-1 -1 0 0 -1
0 0 -1 -1 0
Colt 3
Mico 1
Spike 2
Shelly 1
'''