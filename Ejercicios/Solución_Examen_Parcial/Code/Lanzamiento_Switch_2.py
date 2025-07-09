def voraz(cola, ttotal, tiempoacumulado, solucion):
    cola_ordenada = sorted(cola, key = lambda x: x[1])  # Ordenamos la cola por el tiempo que va a tardar cada persona de menor a mayor
    # print(cola_ordenada)
    for persona in cola_ordenada:  # while cola_ordenada:
        # nombre, tiempo = cola_ordenada.pop(0) EL POP ME INCREMENTA LA COMPLEJIDAD DE MI ALGORITMO
        tiempo = persona[1]  # Por cada persona obtengo su tiempo
        solucion.append(persona[0])  # Añado su nombre a la solución
        tiempoacumulado += tiempo  # Tiempo acumulado es el tiempoacumulado que ya tenía más el tiempo que tarda la persona. Se irá acumulando por cada persona nueva que me llegue
        ttotal += tiempoacumulado  # ESTABA CALCULANDO MAL EL TIEMPO TOTAL.
    return solucion, ttotal


# Lectura entrada
# INICIALIZAR LAS VARIABLES DENTRO DEL FOR NCOLAS PARA QUE SE REINICIEN POR CADA COLA QUE RECIBA
nColas = int(input().strip())  # Número de colas
for _ in range(nColas):
    ttotal = 0  # Variable que me almacenará el tiempo total invertido por todas las personas de la cola
    tiempoacumulado = 0  # Variable para ir almacenando el tiempo acumulado de espera que se irá actualizando por cada persona nueva de la cola
    solucion = []
    cola = []
    nPersonas = int(input().strip())  # Personas que hay en la cola
    for _ in range(nPersonas):  # Por cada persona
        nombre, tprueba = input().strip().split()  # Me guardo su nombre y su tiempo
        cola.append((str(nombre), int(tprueba)))  # La añado a la cola
    # print(cola)
    solucion, ttotal = voraz(cola, ttotal, tiempoacumulado, solucion)  # TABULADO PARA LLAMAR A LA FUNCIÓN POR CADA UNA DE LAS COLAS QUE RECIBA
    # Imprimir por consola por cada cola recibida:
    print()
    print(*solucion)
    print(ttotal)

# Ejemplo de entrada
"""
1
3
Silvia 3
Noelia 2
Sol 5
"""

# 2 + (2+3) + (2+3+5) = 17

# Salida esperada
"""
Noelia Silvia Sol
17
"""
