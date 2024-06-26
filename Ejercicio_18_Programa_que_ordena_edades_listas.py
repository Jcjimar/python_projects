""" 
Crea un programa que le solicite al usuario que piense en 4 familiares cercanos, y que introduzca las edades de sus 4 familiares en 4 entradas por teclado diferentes que se almacenarán en una lista. Posteriormente devolveremos la información de salida con el siguiente formato:

Ejemplo de salida:
*Las edades que has introducido son las siguientes: [Mostrar contenido de la lista]
Este es el resultado de las edades organizadas ascendentemente: [lista_edades_ascendente_sort, lista_edades_ascendente_sorted]
Este es el resultado de las edades organizadas descendentemente:
[lista_edades_descendente_sort, lista_edades_descendente_sorted]*

1. Inicializar las siguientes variables y asignar un valor de entrada por teclado: edad1, edad2, edad3 y edad4
2. Ordenar las edades de forma ascendente y descendente utilizando el método **`sort()`**. y también el método **`sorted()`**.
3. Mostrar el resultado por salida utilizando el método **`print()`**.
"""
#Mensaje de bienvenida
print("Bienvenido al sistema ordenador de las edades de sus familiares.")

#Creamos una variable vacía con formato lista 
lista_edades = []

#Pedimos al usuario que ingrese las edades de sus familiares
edad1 = int(input("Introduzca la edad de su primer familiar: "))
edad2 = int(input("Introduzca la edad de su segundo familiar: "))
edad3 = int(input("Introduzca la edad de su tercer familiar: "))
edad4 = int(input("Introduzca la edad de su cuarto familiar: "))

#Agregamos las edades introducidas por el usuario a la variable lista que anteriormente creamos
lista_edades.extend([edad1, edad2, edad3, edad4])

# Orden ascendente con sort()
lista_edades.sort()
print("Éste es el resultado de las edades ordenadas ascendentemente:", lista_edades)

# Orden ascendente con sorted()
lista_edades_ascendente_sorted = sorted(lista_edades)
print("Éste es el resultado de las edades ordenadas ascendentemente:", lista_edades_ascendente_sorted)

# Orden descendente con sort()
lista_edades.sort(reverse=True)
print("Éste es el resultado de las edades ordenadas descendentemente:", lista_edades)

# Orden descendente con sorted()
lista_edades_descendente_sorted = sorted(lista_edades, reverse=True)
print("Éste es el resultado de las edades ordenadas descendentemente:", lista_edades_descendente_sorted)
