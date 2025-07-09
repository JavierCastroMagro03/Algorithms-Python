monedas = [11, 5, 1]  # Monedas disponibles
ans = []  # Lista para almacenar la solución
gasto = 20  # Lo que tengo que devolver

i = 0  # Iterrador
while i < len(monedas):  # Recorro las 3 monedas
    while gasto >= monedas[i]:  # Mientras el gasto sea mayor o igual que la moneda que estoy evaluando
        gasto -= monedas[i]  # Restamos al gasto la moneda que estoy evaluando
        ans.append(monedas[i])  # agregamos la moneda a la solución
    i += 1  # Incrementamos iterados para pasar a evaluar la siguiente moneda

# Recorremos e imprimimos la solución
for moneda in ans:
    print(moneda, end=" ")
