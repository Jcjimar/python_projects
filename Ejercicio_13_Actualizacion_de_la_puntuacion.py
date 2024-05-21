""" 
Crea un programa en Python que simule la actualización de la puntuación de un juego. Inicializa una variable llamada **`puntuacion`** con un valor inicial de 100. Luego, utiliza **operadores de asignación** para realizar las siguientes acciones:

1. Incrementa la puntuación en 10 unidades: Ha adquirido una vida extra
2. Reduce la puntuación en 5 unidades: Ha sido alcanzado por un enemigo
3. Multiplica la puntuación por 2: Ha recibido un bonus extra
4. Divide la puntuación por 4: Ha repartido el botín entre el equipo
5. Calcula el módulo de la puntuación entre 3: Ha perdido la parte del botín no repartida de forma equitativa entre los miembros del equipo.

Muestra la puntuación después de cada operación utilizando la función **`print()`**.

*Ejemplo de salida:*

*Puntuación Inicial: 100
Puntuación después de incrementar: 110
Puntuación después de reducir: 105
Puntuación después de multiplicar por 2: 210
Puntuación después de dividir por 4: 52.5
Puntuación después de calcular el módulo: 1.5*
"""

# Actualización de Puntuación
#Inicializar la puntuación
puntuacion=100
print (f'Puntuación inicial:{puntuacion} puntos')

#Has adquirido una vida extra y se incrementa la puntuación en 10 unidades
puntuacion+=10
print(f'Has alcanzado una vida extra, y tu puntuación final después despues del incremeneto es ahora {puntuacion} puntos.')

#Ha sido alcanzdado por un enemigo y se reduce la puntuación en 5 unidades
puntuacion-=5
print(f'Te ha alcanzado un enemigo,tu puntuación queda ahora {puntuacion} puntos')

#Has recibido un bonus extra y la puntación se duplica

puntuacion*=2
print(f'Felicidades, has obtenido un bonus extra, y te hemos duplicdo los puntos y ahora tienes :{puntuacion} puntos')

#Reparte el botín entre el equipo. Dividir la puntuación entre 4

puntuacion/=4
print(f"Tu equipo te ha entregado este dinero: {puntuacion} puntos, despues de repartir el botin")

#Calcular el módulo de la puntuación entre 3
puntuacion%=3
print(f"Y tú pierdes esta parte del botín: {puntuacion} puntos de la parte del  botín no repartida de forma equitativa entre los miembros del equipo ")