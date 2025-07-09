objetos = [(10/20, 10, 20, "agua"), (20/30, 20, 30, "comida"), (30/66, 30, 66, "switch"), (40/40, 40, 40, "libro"), (50/60, 50, 60, "cartera")] # (Peso/beneficio, peso, beneficio, "objeto")
objetos.sort() # Queremos ordenarlos de menor a mayor
# print(objetos)
limite = 100  # Capacidad de mi mochila
coste_total_mochila = 0  # Peso que voy acumulando
beneficio_total_mochila = 0  # Valor que voy acumulando en la mochila
mochila = [] # Donde guardamos lo objetos (el nombre de cada objeto que vamos a ir añadiendo)
i = 0  # Inicialización iterador

while i < len(objetos) and coste_total_mochila < limite:  # Mientras haya objetos disponibles y mi peso actual sea menor que el que puedo llevar
    obj_actual = objetos[i]  # El objeto que estoy valorando ahora. Por ejemplo, el primero sería: (10/20, 10, 20)
    coste_actual = obj_actual[1]  # Lee el coste(peso del objeto actual) en nuestros objetos, el peso lo guardamos en la posición 1
    beneficio_actual = obj_actual[2]  # Leemos el beneficio del objeto actual que está acumulado en la posición 2
    mochila.append(obj_actual[3])  # Añadimos a la Lista mochila el objeto (el nombre) posición 3
    if coste_total_mochila + coste_actual <= limite:  # Compruebo si con mi coste total (el actual más lo que ya tenía) supera o no el límite
        coste_total_mochila += coste_actual  # Acumulamos el coste actual con el coste total
        beneficio_total_mochila += beneficio_actual  # Acumulamos el beneficio total
    else:
        proporcion = (limite - coste_total_mochila) / coste_actual
        beneficio_total_mochila += proporcion * beneficio_actual
        coste_total_mochila = limite
    i += 1  # Incrementamos iterador
print(beneficio_total_mochila)  # Imprimimos el beneficio total acumulado
mochila.sort()  # Ordenamos los objetos por orden lexicográfico
print(*mochila)  # Imprimimos la mochila. El * hace que solo me salga: agua cartera comida switch
# Sin el * me devuelve ['agua', 'cartera', 'comida', 'switch']
