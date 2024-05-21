""" 
Crea 3 diccionarios, utilizando las 3 versiones para crear diccionarios que hemos visto en clase (sintaxis básica, y las dos versiones del método de constructor dict() ). Rellena los datos de cada dicc

1. El primer diccionario incluirá los datos básicos del usuario: Nombre, apellidos, fecha de nacimiento, ciudad de nacimiento, nombre del padre y nombre de la madre.
2. El segundo diccionario incluirá: Nº de DNI, fecha de expedición y fecha de caducidad
3. El tercer diccionario: Nacionalidad y domicilio.

A continuación realizaremos las siguientes operaciones:

1. Mostraremos los datos antiguos del diccionario.
2. El programa le pedirá al usuario que actualice los datos uno a uno utilizando la función **`input()`**
3. Por último le mostraremos al usuario los datos actualizados de los 3 diccionarios.
"""
#Creamos los 3 diccionarios
dni1={
    "Nombre":"José Carlos",
    "Apellidos":"Jiménez Arroyo",
    "Fecha de Nacimiento":"16/9/1988",
    "Ciudad de nacimiento": "Vélez-Málaga",
    "Nombre del padre": "José Carlos",
    "Nombre de la madre": "Maria del Carmen"
}
dni2= {
    "Número de DNI": "450789654t",
    "fecha de expedición": "3/8/2022",
    "fecha de caducidad":  "3/8/2032",
}
dni3={
    "Nacionalidad":"Español",
    "Domicilio": "Calle Falsa 123",
}
# Mostramos los diccionarios

print(dni1)
print(dni2)
print(dni3)

# Pedir al usuario que actualice los datos uno a uno utilizando la función input()

dni1["Nombre"] = str(input("Ingrese su nombre:\n")).title()
dni1["Apellidos"] = str(input("Ingrese sus apellidos: \n")).title()
dni1["Fecha de Nacimiento"] = str(input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa:\n "))
dni1["Ciudad de nacimiento"] = str(input("Ingrese su ciudad de nacimiento:\n")).title()
dni1["Nombre del padre"] = str(input("Ingrese el nombre de su padre:\n")).title()
dni1["Nombre de la madre"] = str(input("Ingrese el nombre de la madre:\n")).title()

dni2["Número de DNI" ] = str(input("Ingrese el número de su DNI:\n"))
dni2["fecha de expedición"] = str(input("Ingrese su fecha de expedicion de su DNI en formato dd/mm/aaaa:\n"))
dni2["fecha de caducidad" ] = str(input("Ingrese su fecha de caducidad de su DNI en formato dd/mm/aaaa:\n"))

dni3["Nacionalidad"] = str(input("Ingrese su nacionalidad:\n"))
dni3["Domicilio" ] = str(input("Ingrese su domicilio:\n")).title()

# Volvemos a mostrar los diccionarios

print(dni1)
print(dni2)
print(dni3)

