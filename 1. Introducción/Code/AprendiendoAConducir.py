def logica(S):
    if S == "Arranca":
        print("Mete primera y pisa acelerador")
    if S == "Cambia de marcha":
        print("Pisa embrague a fondo")
    if S == "Para":
        print("Pisa freno y embrague")
    if S == "Aparca":
        print("Imposible")
    if S == "Rotonda":
        print("POR EL CARRIL DERECHO")
    if S == "Gira":
        print("El intermitente, por favor")


N = int(input().strip())

for _ in range(N):
    S = str(input().strip())
    logica(S)
