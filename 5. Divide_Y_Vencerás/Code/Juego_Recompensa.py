def busquedabinaria(recompensas, recompensaSeleccionada, i, j):
    if i > j:
        return -1
    else:
        k = (i + j) // 2
        if recompensas[k][0] == recompensaSeleccionada:
            return k
        elif recompensas[k][0] < recompensaSeleccionada:
            return busquedabinaria(recompensas, recompensaSeleccionada, k + 1, j)
        else:
            return busquedabinaria(recompensas, recompensaSeleccionada, i, k - 1)


# Lectura de entrada
if __name__ == '__main__':
    nCajasRecompensa = int(input().strip())
    # print(nCajasRecompensa)
    recompensas = []
    for _ in range(nCajasRecompensa):
        identificador, nombre = input().strip().split()
        recompensas.append((int(identificador), str(nombre)))
    # print(recompensas)
    nParticipantes = int(input().strip())
    # print(nParticipantes)
    ini = 0  # i
    fin = len(recompensas) - 1  # j
    solucion = []
    poselegidas = set()
    mensaje = "No hay recompensa"
    for _ in range(nParticipantes):
        recompensaSeleccionada = int(input().strip())
        pos = busquedabinaria(recompensas, recompensaSeleccionada, ini, fin)
        if pos == -1:
            solucion.append(mensaje)
        elif pos not in poselegidas:  # Si ese premio no ha sido elegido aún
            solucion.append(recompensas[pos][1])
            poselegidas.add(pos)
        else:  # Si ya ha sido elegido
            i = 1
            while True:
                # Miro uno derecha uno izq si no dos derecha dos izquierda...
                RDcha = pos + i
                RIzda = pos - i
                if RDcha < len(recompensas) and RDcha not in poselegidas:  # Si el de la derecha no ha sido elegido lo añado
                    solucion.append(recompensas[RDcha][1])
                    poselegidas.add(RDcha)
                    break
                elif RIzda > 0 and RIzda not in poselegidas:  # Si el de la izquierda no ha sido elegido lo añado
                    solucion.append(recompensas[RIzda][1])
                    poselegidas.add(RIzda)
                    break
                elif RDcha and RIzda in poselegidas:  # Si derecha e izda ya han sido elegidos incremento i
                    i += 1
                else:  # Si todos han sido elegidos no hay recompensa
                    solucion.append(mensaje)
    for s in solucion:
        print(s)
        # print(recompensaSeleccionada)

'''
5
36 curious-skeleton
66 crunchy-scaffold
109 acyclic-market
272 strong-buffer
433 flashed-distance
3
65
433
109
'''


'''
10
372 oscillating-pitch
439 windy-moss
440 radial-transform
498 afraid-vendor
562 blended-content
577 instant-jay
686 salty-combustion
773 distinct-lake
909 volumetric-double
919 threadbare-character
6
577
562
909
440
773
562
'''

'''
instant-jay
blended-content
volumetric-double
radial-transform
distinct-lake
afraid-vendor
'''