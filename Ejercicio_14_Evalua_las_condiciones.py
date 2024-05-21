""" 
Crea un programa en Python que simule la evaluación de condiciones utilizando **operadores lógicos + operadores de comparación**. Utiliza variables para representar las siguientes situaciones:

1. Un estudiante ha aprobado si su puntuación es mayor o igual a 60.
2. Un usuario tiene acceso si es un administrador o tiene una suscripción premium.
3. Un número es positivo si es mayor que 0 y menor que 100.
4. Un equipo gana si ha anotado más de 3 goles y no ha recibido ningún gol en contra.

Utiliza operadores lógicos (**`and`**, **`or`**, **`not`**) para evaluar estas condiciones y muestra el resultado de cada situación utilizando la función **`print()`**.

*Ejemplo de salida:*

*Puntuación del estudiante: 75
El estudiante ha aprobado: True*

*Usuario es administrador: True
Usuario tiene suscripción premium: False
El usuario tiene acceso: True*

*Número a evaluar: 45
El número es positivo: True*

*Goles a favor: 4
Goles en contra: 0
El equipo ha ganado: True*
"""

#Situación 1: Estudiante aprueba si su puntiación es mayor o igual a 60
puntuacion_estudiante = int(input("Ingrese tu puntuación"))
aprobado = puntuacion_estudiante >= 60
print(f"Puntuación del estudiante: {puntuacion_estudiante}\nEl estudiante ha aprobado: {aprobado}\n")    

#Situación 2: Un usuario tiene acceso si es un administrador o tiene una suscripción premium.
es_administrador = True
tiene_suscripcion_premium = False
acceso_usuario = es_administrador or tiene_suscripcion_premium
print(f"Usuario es administrador: {es_administrador}\nUsuario tiene suscripción premium: {tiene_suscripcion_premium}\nEl usuario tiene acceso: {acceso_usuario}\n")

# Situación 3: Un número es positivo si es mayor que 0 y menor que 100.
numero_evaluar = 45
es_positivo = 0 < numero_evaluar < 100
print(f"Número a evaluar: {numero_evaluar}\nEl número es positivo: {es_positivo}\n")

#Situación 4: Evaluación de victoria del equipo. Un equipo gana si ha anotado más de 3 goles y no ha recibido ningún gol en contra. 
goles_a_favor = 4
goles_en_contra = 0
equipo_gana = goles_a_favor > 3 and goles_en_contra == 0
print(f"Goles a favor: {goles_a_favor}\nGoles en contra: {goles_en_contra}\nEl equipo ha ganado: {equipo_gana}\n")


#Solución con if y else

# Situación 1: Estudiante aprueba si su puntuación es mayor o igual a 60
puntuacion=int(input("Ingrese la puntuación del estudiante: ") )
if puntuacion >= 60:
    print ("El estudiante aprobó")
else :
    print ("El estudiante reprobó") 
        

#Situación 2: Un usuario tiene acceso si es un administrador o tiene una suscripción premium.
usuario=input("Ingrese si es administrador(A) o usuario Premium(P)")
if (usuario=='A') or (usuario=='P'):
    print ("Acceso permitido")  
else :
    print ("Acceso denegado")   

# Situación 3: Un número es positivo si es mayor que 0 y menor que 100.
    numero = int(input("Ingrese el número: "))
    if (numero > 0) and (numero < 100):
        print ("Número positivo")
    else:       
        print ("Número negativo o fuera de rango")  
#Situación 4: Un equipo gana si ha anotado más de 3 goles y no ha recibido ningún gol en contra. 
goles_anotados=int(input("Cuántos goles anotaron?: "))
goles_recibidos=int(input("Cuántos goles recibieron?: "))
if (goles_anotados>3)and(goles_recibidos==0):
     print ("Equipo ganador")
else:
    print ("No hay ganador todavía")
