# Nombre, HabPentester, Habcrayontester, Habpenciltester, Salario
#reclutas = [("YeimsBond", 70, 40, 40, 60), ("MataJari", 100, 90, 100, 30), ("SteveRogers", 40, 90, 150, 70), ("NatashaRomanof", 10, 10, 7, 50)]
#nEquipos = 3  # Número de equipos
#equipos = [(0, 150), (1, 250), (2, 200)]  # Perfil buscado, Presupuesto

def resolver(reclutas, equipos):
    while len(equipos) > 0:  # Mientras haya equipos restantes
        especialidad, presupuesto = equipos.pop(0)  # Saco y leo la especialidad buscada y el presupuesto del primer equipo
        habilidad_total = 0  # Variable para acumular la habilidad total de ese equipo para la especialidad concreta
        solucion = []  # Lista para mostrar los nombres de las personas que forman el equipo
        reclutas_ordenados = sorted(reclutas, key=lambda x: (x[especialidad + 1]/x[4]), reverse=True)  # Ordenamos los reclutas de mayor a menor según la especialidad que requiera el equipo que estamos valorando
        for recluta_act in reclutas_ordenados:  # Recorremos cada recluta de la lista ordenada
            if presupuesto >= recluta_act[4]:  # Si el presupuesto es mayor que el salario del recluta que estoy valorando
                solucion.append(recluta_act[0])  # Añado su nombre a la solución
                habilidad_total += recluta_act[especialidad + 1]  # Acumulo a la habilidad total del equipo la habilidad de ese recluta
                presupuesto -= recluta_act[4]  # Resto al presupuesto el salario del recluta actual
            else:  # En caso contrario (no puedo contratar al recluta al completo)
                if presupuesto > 0:  # Comprobamos que el presupuesto no sea 0
                    fraccion = presupuesto / recluta_act[4]  # Fracciono su salario en función del presupuesto restante
                    habilidad_total += recluta_act[especialidad + 1] * fraccion  # Calculo la habilidad que me podrá aportar
                    solucion.append(recluta_act[0])  # Añado su nombre a la solución
                    presupuesto = 0  # Presupuesto agotado
        print("{:.2f}".format(habilidad_total))  # Imprimimos la habilidad total del equipo con dos decimales
        print(*solucion)  # Imprimimos los nombres uno seguido del otro y sin comillas(*)


# Para leer entrada genérica
if __name__ == '__main__':
    # Entrada
    reclutas = []
    equipos = []
    nReclutas = int(input().strip())
    for _ in range(nReclutas):
        nombre, habpen, habcryon, habpencil, salario = input().strip().split()
        reclutas.append((nombre, int(habpen), int(habcryon), int(habpencil), int(salario)))
    nEquipos = int(input().strip())
    for _ in range(nEquipos):
        equipo = map(int, input().strip().split())
        equipos.append(equipo)
        # especialidad, presupuesto = input().strip().split()
        # equipos.append(int(especialidad),int(presupuesto))
    resolver(reclutas, equipos)
