def mochila(pmax, souvenirs):
    souvenirs_ordenados = sorted(souvenirs, key=lambda x: (x[0] / x[1]), reverse=True)
    valortotal = 0
    for souvenir_act in souvenirs_ordenados:
        if pmax >= souvenir_act[1]:
            pmax -= souvenir_act[1]
            valortotal += souvenir_act[0]

        elif souvenir_act[1] > pmax:
            fraccion = pmax * souvenir_act[0] / souvenir_act[1]
            valortotal += fraccion
            break
    print("{:.2f}".format(valortotal))


# Entrada
pmax, nSouvenirs = map(int, input().split())
souvenirs = []
for _ in range(nSouvenirs):
    valor, peso = input().strip().split()
    souvenirs.append((int(valor), int(peso)))
    # Alternativa a las dos líneas anteriores:
    # valor, peso = map(int, input().strip().split())
    # souvenirs.append((valor, peso))

# print(souvenirs)
mochila(pmax, souvenirs)

'''
50 3
60 10
100 20
120 30
'''
