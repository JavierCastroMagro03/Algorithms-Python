# Streamers con lista de actividades y el momento en el que pueden hacerlas
# Las actividades, aunque coincidan en horario, no se pueden solapar. No se pueden hacer dos cosas a la vez.
# Hacer un programa que organice el horario para que pueda hacer el máximo de actividades en un día (la mayoría de veces no se realizarán todas)

# Lista de actividades: Nombre, tiempo de inicio, tiempo de finalización
# Actividades = [("Vacunarse", 20, 30), ("BaniarAlPez", 35, 40), ("Entrenar", 31, 60), ("PonerTweets", 10, 15), ("LlamadaConIbai", 80, 100)]


def algoritmo(actividades):
    actividades_ordenadas = sorted(actividades, key=lambda x: x[2])  # Ordenamos las actividades por tiempo de finalización de menor a mayor
    solucion = 0  # Variable que acumula el número de tareas que puede realizar ese día
    hora_fin_anterior = 0  # Variable que almacena la hora de finalización de cada tarea

    for actividad in actividades_ordenadas:  # Mientras tenga actividades por realizar
        if actividad[1] >= hora_fin_anterior:  # Si mi actividad actual empieza más tarde de cuando terminó la anterior
            solucion += 1  # La realizo
            hora_fin_anterior = actividad[2]  # Me guardo la hora de finalización de la tarea actual
    print(solucion)  # Imprimimos el número de tareas que puede realizar ese día


if __name__ == '__main__':
    # Entrada
    actividades = []  # Lista para guardar las actividades
    nActividades = int(input().strip())  # Variable que almacena el número de actividades que quiere realizar
    for _ in range(nActividades):  # Por cada actividad
        nombre, tinicio, tfin = input().strip().split()  # Leemos su nombre, tiempo de inicio y tiempo de finalización
        actividades.append((nombre, int(tinicio), int(tfin)))  # Agregamos las actividades a la lista
    algoritmo(actividades)  # Llamada a la función
