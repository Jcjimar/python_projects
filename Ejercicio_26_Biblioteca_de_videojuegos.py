""" 
Vamos a crear un programa en Python que simule la gestión de una biblioteca de videojuegos. Para ello, vamos a utilizar conjuntos para representar diferentes categorías de videojuegos y realizar operaciones sobre ellos.

1. Define los siguientes conjuntos para representar diferentes categorías de videojuegos:
    - **`aventura`**: Contiene videojuegos de aventura.
    - **`accion`**: Contiene videojuegos de acción.
    - **`estrategia`**: Contiene videojuegos de estrategia.
    - **`deportes`**: Contiene videojuegos de deportes.
2. Utiliza la función **`input()`** para permitir al usuario agregar videojuegos a cada categoría. Pídele al usuario que ingrese los nombres de los videojuegos separados por comas.
3. Convierte las cadenas ingresadas por el usuario en conjuntos utilizando el método **`split()`** y luego agregalos a los conjuntos correspondientes utilizando el método **`update()`**.
4. Muestra al usuario un resumen de las categorías de videojuegos y la cantidad de videojuegos en cada una utilizando la función **`print()`** y la función **`len()`** .
5. Utiliza operadores de conjuntos para realizar algunas operaciones como:
    - Mostrar los videojuegos que están presentes en la categoría de acción y aventura.
    - Mostrar los videojuegos que están presentes en la categoría de estrategia pero no en la de deportes.
    - Mostrar todos los videojuegos únicos presentes en todas las categorías.

Instrucciones adicionales:

- **Asegúrate de manejar correctamente la entrada del usuario (separadores, uso de mayúsculas y minúsculas) y realizar las conversiones necesarias de datos utilizando casting de datos.**
- Recuerda usar la función **`split()`** para dividir la entrada del usuario en elementos separados y el método **`update()`** para agregar elementos a los conjuntos.
"""
# 1· Define los siguientes conjuntos para representar diferentes categorías de videojuegos: 
"""
- **`aventura`**: Contiene videojuegos de aventura.
- **`accion`**: Contiene videojuegos de acción.
- **`estrategia`**: Contiene videojuegos de estrategia.
- **`deportes`**: Contiene videojuegos de deportes. 
"""
aventura = set()
accion = set()
estrategia = set()
deportes = set()

# 2· Utiliza la función input() para permitir al usuario agregar videojuegos a cada categoría. Pídele al usuario que ingrese los nombres de los videojuegos separados por comas.

print("Bienvenido a la gestión de la biblioteca de videojuegos.")
print("Ingresa los videojuegos para cada categoría separados por comas.")

# Pedir al usuario que ingrese los videojuegos para cada categoría

juegos_aventura = str(input("\nIngrese sus juegos de aventuras, separado por comas\n\nVideojuegos de aventura:")).lower()
juegos_accion = str(input("\nIngrese sus juegos de acción, separado por comas\n\nVideojuegos de acción:")).lower()
juegos_estrategia = str(input("\nIngrese sus juegos de estrategia, separado por comas\n\nVideojuegos de estrategia:")).lower()
juegos_deportes = str(input("\nIngrese sus juegos de estrategia, separado por comas\n\nVideojuegos de deportes:")).lower()

# 3· Convierte las cadenas ingresadas por el usuario en conjuntos utilizando el método split() y luego agregalos a los conjuntos correspondientes utilizando el método update().

# Actualizar conjuntos con los videojuegos ingresados por el usuario

aventura.update(juegos_aventura.split(","))
accion.update(juegos_accion.split(","))
estrategia.update(juegos_estrategia.split(","))
deportes.update(juegos_deportes.split(","))

# 4· Muestra al usuario un resumen de las categorías de videojuegos y la cantidad de videojuegos en cada una utilizando la función print() y la función len() .

print("\ Resumen de juegos por categoria y cantiga de videojuegos por categoria:\n")

print ("\nAventura: ", aventura, " y la cantidad de video juegos en esta categoria es:",len(aventura),"\n")
print ("\nAccion: ", accion," y la cantidad de video juegos en esta categoria es:", len(accion),"\n")
print("\nEstrategia:",estrategia," y la cantidad de video juegos en esta categoria es:", len(estrategia),"\n")
print("\nDeportes:", deportes, " y la cantidad de video juegos en esta categoria es:", len(deportes),"\n")

# 5· Utiliza operadores de conjuntos para realizar algunas operaciones como:
# · Mostrar los videojuegos que están presentes en la categoría de acción y aventura.
print(f"\nLos juegos de acción y aventura:{accion.intersection(aventura)} \n")

# · Mostrar los videojuegos que están presentes en la categoría de estrategia pero no en la de deportes.
diferencia=estrategia.difference(deportes)
print(f"\nJuegos que se encuentran  solo en Estrategia y no en deportes son:{estrategia.difference(deportes)}\n")

# · Mostrar todos los videojuegos únicos presentes en todas las categorías.

print("Todos los videojuegos únicos en todas las categorías:", aventura.union(accion, estrategia, deportes))