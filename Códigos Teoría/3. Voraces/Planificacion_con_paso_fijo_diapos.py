tareas = [(50, 2, "T1"), (10, 1, "T2"), (15, 2, "T3"), (30, 1, "T4")]
solucion = ["-1"] * len(tareas)
tareas.sort(reverse=True)  # ordenar de mayor a menor

beneficio = 0

while len(tareas) > 0:
    tarea_act = tareas.pop(0)
    if solucion[tarea_act[1]] == "-1":
        solucion[tarea_act[1]] = tarea_act[2]
        beneficio += tarea_act[0]
print(beneficio)

t_act = 1
# Mientras no haya recorrido toda nuestra solución y la tarea actual sea distinta del -1, la podemos imprimir
# La vamos a imprimir separada por espacios y sumamos 1
while t_act < len(solucion) and solucion[t_act] != "-1":
    print(solucion[t_act], end=" ")
    t_act = t_act + 1
print()
