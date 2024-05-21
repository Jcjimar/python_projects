""" 
Crea un programa en Python que permita al usuario jugar un juego interactivo de suma. El programa debe seguir las siguientes reglas:

1. Solicita al usuario que introduzca un número que servirá como límite para la suma.
2. Utiliza un bucle **`while`** para permitir al usuario introducir números y sumarlos.
3. Muestra la suma parcial después de cada entrada del usuario.
4. Cuando la suma alcance o supere el límite introducido por el usuario, muestra un mensaje indicando que el límite ha sido alcanzado.
5. Agradece al usuario por jugar a nuestro juego y deséale un buen día 😊.
"""

#Solicita al usuario que introduzca un límite para la suma
limite = int(input("Introduzca un límite para la suma: "))

# Inicializa la variable suma parcial
suma = 0

# Utiliza un bucle while para permitir al usuario introducir números
while True:
    # Solicita al usuario que introduzca un número
    numero = int(input("Introduzca un número: "))

    # Sume el número a la suma parcial
    suma += numero

    # Muestre la suma parcial
    print(f"Suma parcial: {suma}")

    # Si la suma alcanza o supera el límite, muestre un mensaje
    if suma >= limite:
        print(f"¡Has alcanzado el límite de {limite}!")
        break

# Agradece al usuario por jugar a nuestro juego
print("Gracias por jugar a nuestro juego interactivo de suma 😊.")


""" 
OTRA SOLUCIÓN ALTERNATIVA 

def juego_suma_hasta_limite():
    print("¡Bienvenido al juego de Suma hasta cierto límite!")
    print("Elige un límite y trata de sumar números hasta alcanzarlo.")

    limite = int(input("Introduce el límite deseado: "))
    suma_actual = 0

    while suma_actual < limite:
        numero = int(input("Introduce un número para sumar: "))
        suma_actual += numero

        if suma_actual < limite:
            print(f"Suma actual: {suma_actual}")
        else:
            print(f"¡Felicidades! Has alcanzado o superado el límite de {limite}.")
    print("¡Gracias por jugar!")

# Ejecutar el juego
juego_suma_hasta_limite()
"""

