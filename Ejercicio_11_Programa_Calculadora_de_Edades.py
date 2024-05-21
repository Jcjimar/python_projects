""" 
Crea un programa en Python que solicite al usuario ingresar su año de nacimiento y el año actual. Utiliza esta información para calcular su edad actual y edad futura.

1. Solicita al usuario que introduzca su año de nacimiento.
2. Solicita al usuario que introduzca el año actual.

Luego, realiza los siguientes cálculos:

- Calcula la edad actual restando el año de nacimiento del año actual.
- Calcula la edad que tendría en 5 años sumando 5 a la edad actual.
- Calcula la edad que tendría en 10 años sumando 10 a la edad actual.

Finalmente, utiliza la función **`print()`** para mostrar un mensaje que incluya la información de la siguiente manera:

*¡Bienvenido a la Calculadora de Edades!*

*Introduce tu año de nacimiento: 1990
Introduce el año actual: 2023*

*Resultados:*

- *Tienes 33 años, ¡Aún te queda muchas cosas buenas por vivir!*
- *En 5 años tendrás 38 años.*
- *En 10 años tendrás 43 años.*
"""
#Calculadora de edades
print('Bienvenido a la calculadora de edades\n')

# Entrada de datos
anio_nacimiento=int(input('introduce tu año de nacimiento: \n'))
anio_actual=int(input('introduce el año actual:\n'))

#Cálculos

edad_actual=anio_actual-anio_nacimiento
edad_futura_5 =edad_actual+5
edad_futura_10=edad_actual+10

#Mostrar resultados
print('\n---------------------------------------------\n')
print('\nResultados:\n')
print(f'\n · Tienes {edad_actual} años en este momento.\n')
print(f'\n · En 5 años tendrás {edad_futura_5} años. \n')
print(f'\n · En 10 años tendrás {edad_futura_10} años. \n')