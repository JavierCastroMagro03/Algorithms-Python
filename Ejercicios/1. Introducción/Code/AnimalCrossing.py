# Puntuación = suma de las dos mejores capturas
# Pez: id y puntuación
# Puntuación total e id de los dos mejores peces
# lista (2, 88), (6, 86)
def salida(lista):
    listaordenada = sorted(lista, key=lambda x: x[1], reverse=True)
    puntuacion = listaordenada[0][1] + listaordenada[1][1]
    print(str(listaordenada[0][0]), str(listaordenada[1][0]), str(puntuacion))


capturas = int(input())
list = []

for _ in range(capturas):
    i, s = input().split()
    nuevo_elemento = (int(i), int(s))
    list.append(nuevo_elemento)

salida(list)
