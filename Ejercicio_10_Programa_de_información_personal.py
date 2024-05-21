""" 
Crea un programa en Python que solicite al usuario ingresar su información personal, incluyendo su nombre, edad y ciudad de residencia. Luego, utiliza la función **`print()`** para mostrar un mensaje personalizado utilizando diferentes métodos de formateo de cadenas.

1. Solicita al usuario que introduzca su nombre.
2. Solicita al usuario que introduzca su edad.
3. Solicita al usuario que introduzca su ciudad de residencia.

Luego, muestra un mensaje de saludo personalizado que incluya la información ingresada. Utiliza tanto la función **`.format()`** como las f-strings para formatear la salida de la siguiente manera:

- En el primer mensaje, utiliza **`.format()`** para incluir el nombre y la ciudad.
- En el segundo mensaje, utiliza una f-string para incluir la edad.

*Ejemplo de salida:* 

*¡Bienvenido al Programa de Información Personal!*

*Introduce tu nombre: Juan
Introduce tu edad: 30
Introduce tu ciudad de residencia: Ciudad Paraíso*

*¡Hola, Juan! Bienvenido a Ciudad Paraíso.
Esperamos que disfrutes tu estudio. Tienes 30 años de sabiduría.*
"""
# Programa de Información Personal
print("¡Bienvenido al Programa de Información Personal!\n")

# Entrada de datos
nombre = str(input("Introduce tu nombre: \n"))
edad = int(input("Introduce tu edad: \n"))
ciudad = str(input("Introduce tu ciudad de residencia: \n"))


# Mensaje personalizado usando .format()
mensaje_format = "¡Hola, {}! Bienvenido a {}.".format(nombre, ciudad)

# Mensaje personalizado usando f-string
mensaje_fstring = f"Esperamos que disfrutes tu estancia. Tienes {edad} años de sabiduría."

# Mostrar resultados
print('\n----------------------------------\n')
print(mensaje_format)
print('\n----------------------------------\n')
print(mensaje_fstring)
print('\n----------------------------------\n')
print('Deseseo que te haya gustado mi programa')
print('\n----------------------------------\n')