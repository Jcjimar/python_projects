""" 
Vamos a trabajar con una tupla que representa las temperaturas diarias de una ciudad durante una semana. La tupla se llama **`temperaturas`** y contiene valores en grados Celsius. Realiza las siguientes tareas:

1. Crea una tupla llamada **`temperaturas`** con al menos 7 valores de temperaturas diarias.
2. Imprime la longitud de la tupla.
3. Utiliza el método **`count`** para determinar cuántas veces aparece la temperatura 25 en la tupla.
4. Encuentra el índice de la primera aparición de la temperatura 18 utilizando el método **`index`**.
5. Crea una nueva tupla llamada **`temperaturas_ordenadas`** que contenga las temperaturas ordenadas de manera ascendente de la tupla **`temperaturas`**.
6. Concatena la tupla original con la nueva tupla **`temperaturas_ordenadas`**.
7. Repite la tupla original tres veces y almacénala en una nueva tupla llamada **`temperaturas_repetidas`**.
8. Imprime todas las tuplas resultantes y observa los cambios.

**Nota:** Asegúrate de utilizar los métodos y operadores adecuados para realizar estas operaciones.
"""

# Crear una tupla de temperaturas diarias
temperaturas = (22, 24, 26, 25, 23, 18, 20)

# Imprimir la longitud de la tupla
print("Longitud de la tupla:", len(temperaturas))

# Contar cuántas veces aparece la temperatura 25
apariciones_25 = temperaturas.count(25)
print("Número de apariciones de la temperatura 25:", apariciones_25)

# Encontrar el índice de la primera aparición de la temperatura 18
indice_18 = temperaturas.index(18)
print("Índice de la primera aparición de la temperatura 18:", indice_18)

# Crear una nueva tupla con temperaturas ordenadas
temperaturas_ordenadas = tuple(sorted(temperaturas))
print("Temperaturas ordenadas:", temperaturas_ordenadas)

# Concatenar la tupla original con la nueva tupla ordenada
temperaturas_concatenadas = temperaturas + temperaturas_ordenadas
print("Tupla original concatenada con temperaturas ordenadas:", temperaturas_concatenadas)

# Repetir la tupla original tres veces
temperaturas_repetidas = temperaturas * 3
print("Tupla original repetida tres veces:", temperaturas_repetidas)
