def voraz(participantes, tamaniogrupos):
    grupo_jovenes = []
    grupo2 = []
    participantes_ordenados = sorted(participantes, key=lambda x: x[1])  # Participantes ordenados por edad de menor a mayor
    for participante in participantes_ordenados:
        if tamaniogrupos > 0:
            grupo_jovenes.append(participante[0])
            tamaniogrupos -= 1
        else:
            grupo2.append(participante[0])
    print(*grupo_jovenes)
    print(*grupo2)


# Entrada
nParticipantes, tamaniogrupos = map(int, input().split())
participantes = []
for _ in range(nParticipantes):
    nombreParticipante, edad = input().strip().split()
    participantes.append((str(nombreParticipante), int(edad)))
# print(participantes)
voraz(participantes, tamaniogrupos)

"""
5 2
JamesLineberger 55
JeanetteMaurey 73
ChristieDangelo 29
HeatherTrew 78
LeolaSwift 30
"""
