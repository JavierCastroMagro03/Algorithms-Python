# Calcular el mayor número de tentaciones a un concursante en un tiempo determinado.
# Característica que más valora el concursante que va a ser seducido.
# Valor de cada persona en cada una de las características.

nConcursantes = 1
cualidadmasValorada = 'kindness'  # Puede ser kindness intelligence o beauty
posiblesParejas = 4
parejas = [("Saul", 70, 100, 30, 5), ("Jara", 100, 60, 100, 50), ("Ivan", 20, 80, 100, 70), ("Rosa", 20, 100, 70, 100)]  # Nombre, belleza, inteligencia, amabilidad y tiemporequerido


def algoritmo(parejas_ordenadas):
    solucion = []
    beneficio = 0
    tiempoRestante = 100
    for pareja in parejas_ordenadas:
        if tiempoRestante > pareja[4]:
            solucion.append(pareja[0])
            beneficio += pareja[cualidadmasValorada]
            tiempoRestante -= pareja[4]
        else:
            if tiempoRestante > 0:
                fraccion = tiempoRestante / pareja[4]
                beneficio += pareja[cualidadmasValorada] * fraccion
                solucion.append(pareja[0])
                tiempoRestante = 0

    print(*solucion)
    print("{:.2f}".format(beneficio))


if cualidadmasValorada == 'kindness':
    cualidadmasValorada = 3
elif cualidadmasValorada == 'intelligence':
    cualidadmasValorada = 2
elif cualidadmasValorada == 'beauty':
    cualidadmasValorada = 1
else:
    print("Cualidad no válida")

parejas_ordenadas = sorted(parejas, key=lambda x: (x[cualidadmasValorada] / x[4]), reverse=True)
algoritmo(parejas_ordenadas)
