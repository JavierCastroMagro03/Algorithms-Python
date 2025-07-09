# input lee la entrada como si fuese una cadena de texto. Lo interpreta de manera literal (depende del
# sistema operativo será o 1\n (linux) o 1\r\n (windows). Por lo que el profe, después de cada input nos recomienda
# poner un . strip(). Para eliminar lo valores de formateo que no vemos). Para usar el dato C como un entero, tendremos
# que convertirlo al tipo de dato que nos interese.

C = int(input().strip())

for _ in range(C): # Lista completa desde el 0 hasta C-1. El _ es para cuando la variable de control del bucle no la
# vas a utilizar dentro del bucle
    print("¡Hola mundo!")

