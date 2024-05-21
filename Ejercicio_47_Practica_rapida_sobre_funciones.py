""" 
Crear un programa que le solite al usuario su nombre y sus apellidos. A continuación el programa ejecutará una función saludar para saludar al usuario.
Solicitamos el año de nacimiento, y a continuación el programa ejecutará una función diciendo al usuario los años que tiene. 
"""


""" EJERCICIO 1 """

def calcular_edad():
    # Solicitar al usuario su año de nacimiento
    anio_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: \n"))
    anio_actual = int(input("Por favor, ingresa el año actual:\n"))
    # Calcular la edad restando el año de nacimiento al año actual
    edad = anio_actual - anio_nacimiento
    
    # Devolver la edad calculada
    return edad

# Llamar a la función para calcular la edad del usuario
edad_usuario = calcular_edad()

# Mostrar la edad calculada
print("Tienes", edad_usuario, "años de edad.")

""" EJERCICIO 2 """


def saludar(nombre):  # 'nombre' es un parámetro de la función
    print("¡Hola,", nombre, "!")

# Pedimos al usuario que introduzca su nombre
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Llamamos a la función 'saludar' y le pasamos el nombre del usuario como argumento
saludar(nombre_usuario)
