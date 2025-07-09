def busquedabinaria(checkpoints, elem, i, j):
    if i > j:
        return i
    else:
        k = (i + j) // 2
        if checkpoints[k] == elem:
            return k
        elif checkpoints[k] < elem:
            return busquedabinaria(checkpoints, elem, k + 1, j)
        else:
            return busquedabinaria(checkpoints, elem, i, k - 1)


# Entrada
Gm = list(map(int, input().strip().split()))
Gf = list(map(int, input().strip().split()))

elemM, elemF = map(int, input().strip().split())
ini = 0  # i
fin = len(Gm) - 1  # j
solucion = []

posM = busquedabinaria(Gm, elemM, ini, fin)
#print(posM)
if elemM < Gm[0]:  # Si mi elemento es menor que el primero de mis checkpoint no llego a ninguno
    solucion.append(0)
elif posM >= len(Gm):  # Si
    solucion.append(len(Gm))
elif elemM == Gm[posM]:
    solucion.append((posM + 1))
else:
    solucion.append(posM)

posF = busquedabinaria(Gf, elemF, ini, fin)
#print(posF)
if elemF < Gf[0]:
    solucion.append(0)
elif posF >= len(Gf):
    solucion.append(len(Gf))
elif elemF == Gf[posF]:
    solucion.append((posF + 1))
else:
    solucion.append(posF)

print(*solucion)

if solucion[0] > solucion[1]:
    print("MCQUEEN")
elif solucion[0] == solucion[1]:
    print("EMPATE")
else:
    print("FRANCESCO")


# Para hacer pruebas
'''
50 75 115 213 278 294
30 120 190 222 287 443
115 120
'''