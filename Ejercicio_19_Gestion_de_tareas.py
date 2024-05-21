""" 
Crear un programa en Python que simule la gestión de las tareas pendientes. 

1. Utiliza una lista para almacenar las tareas y realiza las siguientes operaciones:
    1. Agregar tres tareas de forma simultánea al final de la lista.
    2. Mostrar todas las tareas actuales
    3. Verificar si una tarea específica, tarea_buscar, está presente en vuestra lista
    4. Eliminar la segunda tarea de la lista
    5. Mostrar el número de tareas después de eliminar la del punto d.
"""
#Programa gestión de tareas (listas)
""" ------------------------------- """
""" ------------------------------- """

#Bienvenida al programa 
""" ------------------- """

print("\n¡Bienvenido a tu programa de gestion de tareas pendientes!\n\n\n")

#Creamos la variable en donde guardaremos la lista de tareas pendientes // Inicializamos la lista de tareas=[].
""" ---------------------------------------------------------------------------------------------------------- """

lista_tareas_pendientes = []



# 1. Agregar tres tareas al final de la lista de forma simultánea
""" ------------------------------------------------------------- """
print("Agregar tres tareas:")
lista_tareas_pendientes.append(str(input("\nEscribe la tarea 1 pendiente por realizar:\n ")))
lista_tareas_pendientes.append(str(input("\nEscribe la tarea 2 pendiente por realizar:\n ")))
lista_tareas_pendientes.append(str(input("\nEscribe la tarea 3 pendiente por realizar:\n")))

# 2. Mostrar todas las tareas actuales
"""  ---------------------------------"""

print("\nTareas actuales:\n")
print("-", lista_tareas_pendientes[0])
print("-", lista_tareas_pendientes[1])
print("-", lista_tareas_pendientes[2])


# 3. Función buscar, buscar una tarea específica esta en nuestra lista
""" ------------------------------------------------------------------ """
tarea_buscar = input("\nIngrese una tarea a buscar:\n ")
contador_tarea = lista_tareas_pendientes.count(tarea_buscar)
print(f"\nLa tarea '{tarea_buscar}' está presente {contador_tarea} veces en la lista.")

"""Otra forma de resolverlo:
tarea_en _lista = tarea_buscar in lista_tareas_pendientes
print("La tarea que acabas de añadir esta en la lista:", tarea_en_lista)
"""

# 4. Eliminar la segunda tarea  de la lista
""" ------------------------------- """

print("Felicidades, acabas de realizar una de las tareas pendientes", {lista_tareas_pendientes[1]},"continua así y logra superar las siguientes y elminarla de tu lista de tareas pendientes")

lista_tareas_pendientes.remove(lista_tareas_pendientes[1])



# 5. Mostrar el numero de tareas pendientes después de eliminar la segunda
""" ---------------------------------------------------------------------- """
print("El número de tareas pendientes es:\n",len(lista_tareas_pendientes),"\n")

