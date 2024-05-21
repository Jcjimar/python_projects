""" 
Crea una colección de datos inmutable, que me permita añadir los siguientes datos de usuario:
- Nombre y apellidos
- Edad
- Ciudad de nacimiento
- Ciudad de residencia
"""
tupla_andar_casa = ["nombre", "apellidos"], [0], ["ciudad residencia"], ["ciudad nacimiento"]

tupla_andar_casa[0][0] = str(input("Introduce un nombre:\n "))
tupla_andar_casa[0][1] = str(input("Introduce un apellido:\n "))
tupla_andar_casa[1][0] = int(input("Introduce una edad:\n "))
tupla_andar_casa[2][0] = str(input("Introduce una ciudad de residencia:\n "))
tupla_andar_casa[3][0] = str(input("Introduce una ciudad de nacimiento:\n "))

print(tupla_andar_casa)

