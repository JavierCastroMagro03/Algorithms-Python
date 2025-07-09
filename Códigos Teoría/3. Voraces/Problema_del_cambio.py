monedas = [1000, 500, 100, 50, 20, 10, 5, 2, 1]  # Los diferentes tipos de moneda que se tienen
ans = []  # Donde se guardan las monedas que voy a devolver
gasto = 93  # Tenemos que devolver este cambio
i = 0  # Iterador para avanzar en monedas
while i < len(monedas):  # Mientras que tenga monedas
    while gasto >= monedas[i]:  # Mientras que el gasto sea divisible entre una moneda en la posición i
        gasto -= monedas[i]  # A gasto le resto la moneda que estoy valorando
        ans.append(monedas[i])  # Agrego la moneda a mi respuesta
    i += 1  # Cuando termino con una moneda avanzo en mi array monedas a la siguiente

# Imprimimos la lista por consola
for moneda in ans:
    print(moneda, end=" ")
