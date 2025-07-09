# El líder es el mayor. Si dos coinciden, el líder es el que se apuntó primero
# luego tenemos al resto
# al contra el numero de miembros, al líder no se le cuenta

# Función
def salida(lista):
    listaordenada = sorted(lista, key=lambda x: x[1], reverse = True)
    lidernombre = listaordenada[0][0]
    tamaño = len(lista) - 1
    if tamaño < 2:
        print("Bienvenido equipo de " + str(lidernombre) + " compuesto por " + str(tamaño) + " persona")
    else:
        print("Bienvenido equipo de " + str(lidernombre) + " compuesto por " + str(tamaño) + " personas")

# Entrada
lista = []
nIntegrantes = input().strip()
for _ in range(int(nIntegrantes)):
    nombre, edad = input().strip().split()
    insertar = nombre, int(edad)
    lista.append(insertar)
salida(lista)
