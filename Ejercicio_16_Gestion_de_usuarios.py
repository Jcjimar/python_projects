#Operadores de pertenencia & identidad
""" 
Crea un programa en Python que simule la gestión de usuarios en un sistema. Utiliza variables para representar información sobre dos usuarios diferentes. Luego, utiliza operadores de pertenencia (**`in`**, **`not in`**) y de identidad (**`is`**, **`is not`**) para realizar las siguientes acciones:

1. Verifica si un usuario llamado **`usuario_actual`** está registrado en el sistema.
2. Comprueba si ambos usuarios comparten la misma dirección de correo electrónico.
3. Identifica si los objetos que representan a los usuarios son diferentes.

Muestra los resultados utilizando la función **`print()`**.

*Condiciones iniciales*

*# Información del Usuario 1*

*usuario1_nombre = "Alice"
usuario1_correo = "[alice@email.com](mailto:alice@email.com)"*

*# Información del Usuario 2*

*usuario2_nombre = "Bob"
usuario2_correo = "[bob@email.com](mailto:bob@email.com)"*

*# Usuario Actual a Verificar*

*usuario_actual = "Alice"*

*Ejemplo de salida*

*# Verificación de Usuarios:*

*Usuario 'Alice' está registrado: True*

*Comprobación de Correo Electrónico:
Ambos usuarios comparten el mismo correo electrónico: False*

*Identificación de Objetos:
Los objetos que representan a los usuarios son diferentes: True*
"""
#Información del usuario 1

usuario1_nombre= "Jose"
usuario1_correo="jose@email.com"

#Información del usuario 2

usuario2_nombre = "Carlos"
usuario2_correo="carlos@email.com"

#Usuario actual a verificar
usuario_actual_predefinido= 'Jose'
usuario_actual= "Jose" in usuario1_nombre
usuario_actual_1= "José" in usuario2_nombre

# Datos de los usuarios
print('El primer usuario se llama {} y su email es {} '.format(usuario1_nombre,usuario1_correo))
print('\n-------------------------------------------------------------\n')
print('El segundo usuario se llama {} y su email es {} '.format(usuario2_nombre,usuario2_correo))
print('\n-------------------------------------------------------------\n\n\n')


#Verificación de usuarios:
print("Usuario Jose esta registrado\n",usuario_actual)

print('Usuario José está registrado\n',usuario_actual_1)

# --------------------------------------------------------------------------

print('Otra posible solución:\n')
usuario_actual_registrado = usuario_actual_predefinido in (usuario1_nombre, usuario2_nombre)
print("Usuario '{}' está registrado: {}\n".format(usuario_actual_predefinido, usuario_actual_registrado))
# Otra forma de resolverlo: print("El resultado es", usuario_actual in (usuario1_nombre, usuario2_nombre))

print('\n-------------------------------------------------------------\n')
print('\n-------------------------------------------------------------\n')

#Verificación de correos electronicos
""" ¿Ambos usuarios comparten el mismo correo electrónico? """
print('Ambos usuarios comparten el mismo correo eléctronico\n',usuario1_correo is usuario2_correo)

# -----------------------------------------------------------------------------------

print('Otra posible solución:\n')
mismo_correo = usuario1_correo is usuario2_correo
print("\nAmbos usuarios comparten el mismo correo electrónico:", mismo_correo)

print('\n-------------------------------------------------------------\n')
print('\n-------------------------------------------------------------\n')

#Otra forma de resolverlo es 
#objetos_diferentes = usuario1_nombre is not usuario2_nombre
#print("\nLos objetos que representan a los usuarios son diferentes:", objetos_diferentes)