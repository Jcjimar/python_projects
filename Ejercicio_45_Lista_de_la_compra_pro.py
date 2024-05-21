""" 
Vamos a crear un programa que permita gestionar una lista de la compra. El programa solicitará al usuario que introduzca los elementos que desea comprar y los agregará a una lista. Cuando el usuario escriba "fin", el programa mostrará la lista de la compra y terminará.

Instrucciones:

1. Inicia el programa con un mensaje de bienvenida.
2. Crea una lista vacía llamada **`lista_compra`**.
3. Utiliza un bucle **`while`** para solicitar al usuario que introduzca un elemento que desea comprar.
4. Dentro del bucle, agrega cada elemento introducido por el usuario a la lista **`lista_compra`**.
5. Si el usuario escribe "fin", sal del bucle.
6. Después de salir del bucle, muestra un mensaje de despedida y la lista de la compra.
7. BONUS TRACK: ¿Qué pasaría si yo quisiera almacenar los elementos de mi lista y además la cantidad de cada elemento que necesito comprar? Modifica el ejercicio para ampliar la solución dando respuesta a esta cuestión.
"""
# Mensaje de bienvenida
print("Bienvenido a la lista de la compra.")

# Lista para almacenar los elementos de la compra
lista_compra = []

# Bucle para solicitar los elementos de la compra
while True:
    elemento = input("Introduce un elemento que deseas comprar (o escribe 'fin' para terminar): ")
    if elemento.lower() == 'fin':
        break  # Salir del bucle si el usuario escribe 'fin'
    else:
        lista_compra.append(elemento)  # Agregar el elemento a la lista de la compra

# Mensaje de despedida y lista de la compra
print("\nLista de la compra:")
for item in lista_compra:
    print("-", item)

print("\nGracias por usar la lista de la compra. ¡Que tengas un buen día!")
