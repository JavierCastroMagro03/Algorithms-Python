def mochila(videojuegos, presupuestomax):
    solucion = set()
    cantDiversion = 0
    videojuegos_ordenados = sorted(videojuegos, key=lambda x: (x[1]/x[2]), reverse=True)
    # print(videojuegos_ordenados)
    for videojuego in videojuegos_ordenados:
        if videojuego[2] <= presupuestomax:
            solucion.add(videojuego[0])
            presupuestomax -= videojuego[2]
            cantDiversion += videojuego[1]

        elif presupuestomax > 0:
            fraccion = presupuestomax * videojuego[1]/videojuego[2]
            cantDiversion += fraccion
            solucion.add(videojuego[0])  # SE ME OLVIDÓ AÑADIR EL ELEMENTO QUE DIVIDIMOS!!!
            break

    print("{:.2f}".format(cantDiversion))
    if "Switch2" in solucion:
        print("SI")
    else:
        print("NO")


# Lectura de entrada
nVideojuegos, presupuestomax = map(int,input().strip().split())
videojuegos = []
for _ in range(nVideojuegos):
    nombre, valor, coste = input().strip().split()
    videojuegos.append((str(nombre), int(valor), int(coste)))
# print(videojuegos)
mochila(videojuegos, presupuestomax)

# Ejemplos de entrada
# 1
"""
5 150
Switch2 100 45
EldenRing 20 30
Intergalactic 15 40
Maincra 22 30
F12025 33 40
"""
# 2
"""
5 110
Switch2 100 65
EldenRing 200 30
Intergalactic 75 10
Maincra 220 30
F12025 330 40
"""

# Salida 1
"""
176.88
SI
"""

# Salida 2
"""
825.00
NO
"""