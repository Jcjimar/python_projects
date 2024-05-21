""" Escribe un programa en Python que solicite al usuario ingresar un número entero positivo. Luego, utiliza un bucle **`for`** y el parámetro **`end`** en la función **`print()`** para imprimir un patrón de asteriscos con forma de pirámide, como se muestra en el ejemplo a continuación:

Si el usuario introduce el número 5 la salida debería ser: 
    *
   ***
  *****
 *******
*********

1. Solicita al usuario ingresar un número entero positivo que representará la altura de la pirámide.
2. Utiliza un bucle **`for`** para iterar sobre cada fila de la pirámide.
3. En cada iteración del bucle, imprime una cadena de asteriscos con un número creciente de asteriscos, seguido de un espacio en blanco, y especifica el parámetro **`end`** de la función **`print()`** para que no haya salto de línea después de imprimir cada fila.

Recuerda validar la entrada del usuario para garantizar que sea un número entero positivo.
#BONUS TRACK: El usuario debe introducir cuantas filas y columnas quiere en su cuadrado vacío--> + 1 MIN en el proyecto final
*****
*   *
*   *
*   *
*****
"""
# Imprimir una pirámide
print("\nReto Semana Santa")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1), end=' ')
    print()

#_____________________________________

altura = int(input("De cuanto quieres que sea la altura: "))
anchura = int(input("De cuanto quieres que sea la anchura: "))
for i in range(altura): #0, 1, 2, 3, 4, 5, 6
    for j in range(anchura): #0, 1, 2, 3, 4, 5
        if i == 0 or i == altura -1 or j == 0 or j == anchura-1:
            print ("*",end="")
        else:
            print (" ", end="")
    print()


""" Por cada valor que encuentres en los valores 0 - 5, ejecuta el siguiente código:
    --> Primera columna - Iteración j == 0: True
    --> Segunda columna - Iteración j == 1: False
    --> Tercera columna - Iteración j == 2: False
    --> Cuarta columna - Iteración j == 3: False
    --> Quinta columna - Iteración j == 4: False
    --> Sexta columna - Iteración j == 4: True
 """

#______________________________________________


#PIRÁMIDE

altura = int(input("Pon numeros: "))

for i in range(1, altura + 1): # empiezo con la primera posicion hasta la posicion que escribe altura
    for j in range(altura - i):
        print(" ", end="") # cada vez que imprimo pues elimino  el espacio de la ultima columna.
    for k in range(i): # 0, 1, 2,...
        print("*", end=" ") # y aqui pues se crea # 
    print()

"""
BUCLE 1: 1, 2, 3, 4, 5
Primera iteración: i == 1 
    · Imprime 5 espacios en blanco (j)
    · Imprime una estrella (k)
    · Imprime un salto de línea
Segunda iteración: i == 2
    · Imprime 5 espacios en blanco (j)
    · Imprime dos estrelas (k)
    · Imprime un salto de línea
Tercera iteración: i == 2
    · Imprime 5 espacios en blanco (j)
    · Imprime dos estrelas (k)
    · Imprime un salto de línea
Cuarta iteración: i == 2
    · Imprime 5 espacios en blanco (j)
    · Imprime dos estrelas (k)
    · Imprime un salto de línea
"""
     