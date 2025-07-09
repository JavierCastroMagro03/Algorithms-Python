# Como el problema del cambio
# Dada una cantidad
# Un conjunto de valores de monedas
# Devolver el mínimo número de monedas y la cantidad de cada una de las monedas seleccionadas (siempre que haya 1 o más de una)
# A veces recibirán menor cantidad de dinero del que cambian por diferencia en divisa

# Ejemplo
# cambio = 70  # Cantidad de dinero terrícola a cambiar
# monedas = [1, 5, 2, 100, 10, 20, 50, 500, 1000]  # No tienen por qué estar ordenadas

def metodo(cambio, monedas):
    monedas.sort(reverse=True)  # Ordenamos las monedas de mayor a menor
    cantidadtotalmonedas = 0  # Inicializo la variable que almacenará el total de monedas devueltas
    solucion = []  # Inicializo la lista en la que almacenaré la solución

    for moneda in monedas:  # Recorremos las monedas de diferentes valores
        cantidadmoneda = 0  # Inicializamos el contador para la cantidad de monedas de ese valor
        while cambio >= moneda:  # Mientras el cambio sea mayor que el valor de la moneda que estoy evaluando en ese momento
            cambio -= moneda  # Actualizamos cambio restándole la moneda devuelta
            cantidadmoneda += 1  # Aumentamos en 1 la cantidad de esa moneda
            cantidadtotalmonedas += 1  # Aumentamos en 1 la cantidad total de monedas
        if cantidadmoneda > 0:  # Si de la moneda evaluada tengo al menos una
            solucion.append(str(moneda) + ": " + str(cantidadmoneda))  # La añado a la solución
    print(cantidadtotalmonedas)  # Muestro la cantidad total de monedas devueltas
    for i in solucion:  # Recorro la solución
        print(i)  # Voy imprimiendo cada solución con un salto de línea


# Entrada genérica
if __name__ == '__main__':
    cambio = int(input())  # Leemos el cambio a devolver
    monedas = list(map(int, input().strip().split()))  # Creamos la lista con los distintos valores de monedas
    metodo(cambio, monedas)  # Llamada a la función
