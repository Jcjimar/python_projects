""" 
Crea un programa que gestione una lista de tareas pendientes, un conjunto de elementos de una lista de compras y un diccionario de contactos. 

1. **Creación de las Colecciones de Datos:**
    - Inicia el programa creando las siguientes colecciones de datos:
        - Una lista llamada **`tareas_pendientes`** que contenga al menos 5 tareas pendientes.
        - Un conjunto llamado **`lista_compras`** que incluya los elementos de una lista de compras con al menos 5 ítems.
        - Un diccionario llamado **`agenda_contactos`** que contenga los nombres y números de teléfono de al menos 5 contactos.
2. **Operaciones con la Lista de Tareas Pendientes:**
    - Utiliza el método **`append()`** para agregar una nueva tarea a la lista de tareas pendientes.
    - Utiliza el método **`remove()`** para eliminar una tarea específica de la lista de tareas pendientes.
    - Utiliza el método **`sort()`** para ordenar las tareas pendientes alfabéticamente.
    - Utiliza el método **`clear()`** para vaciar la lista de tareas pendientes.
3. **Operaciones con el Conjunto de la Lista de Compras:**
    - Utiliza el método **`add()`** para agregar un nuevo ítem a la lista de compras.
    - Utiliza el método **`discard()`** para eliminar un ítem específico de la lista de compras.
    - Utiliza el método **`clear()`** para vaciar el conjunto de la lista de compras.
4. **Operaciones con el Diccionario de Contactos:**
    - Utiliza el método **`update()`** para agregar nuevos contactos al diccionario de contactos.
    - Utiliza el método **`sorted()`** para ordenar los contactos por nombre y mostrarlos en orden alfabético.
    - Utiliza el método **`pop()`** para eliminar un contacto específico del diccionario de contactos.
    - Utiliza el método **`clear()`** para vaciar el diccionario de contactos.
5. **Mostrar Resultados:**
    - Después de cada operación, muestra el estado actual de cada colección de datos.
6. **Finalizar el Programa:**
    - Proporciona una opción para que el usuario pueda salir del programa cuando lo desee.
"""
print("Bienevenidos a nuestro super programa de tareas pendientes, lista de compras y agenda de contactos.")

# 1· Creación de las bases de datos
tareas_pendientes =["estudiar python","cocinar","nadar","correr","leer","comprar","preparar entrevistas"]
lista_compras = {"pan","tomate", "cebolla","pasta", "legumbres","gel","pasta de dientes", "enjuague bucal"}
agenda_contactos = {
    "Carlos": "123456789",
    "Ana": "0987654321",
    "Juan": "1112223333",
    "Pablo": "555555555",
    "Javier": "999999999",
    "Fran":  "666666666",
}
print("Las tareas pendientes actualmente son:\n",tareas_pendientes,"en total en este listado de tareas pendientes,tenemos:\n",len(tareas_pendientes),"tareas pendientes por hacer.")
print("Actualmente tienes que comprar los siguientes productos;\n",lista_compras,"en total en esta lista de la compra tenemo", len(lista_compras), "productos pendientes que comprar")
print("Los contactos guardados actualmente son;\n",agenda_contactos, "por lo que actualmente en mi agenda de contactos tengo: ",len(agenda_contactos), "contactos")

# 2· Operaciones con la lista de tareas pendientes
tareas_pendientes.append("echar la siesta")
print("Mi lista tras añadir la tarea -echar la siesta- es ahora:\n",tareas_pendientes, "ahora tengo",len(tareas_pendientes),"tareas pendientes en mi lista de tareas pendientes")
tareas_pendientes.remove("nadar")
print("Mi nueva lista de tareas pendientes tras eliminar la tarea -estudiar python- es ahora:\n ",tareas_pendientes,"por lo que ahora tengo",len(tareas_pendientes),"tareas pendientes")
tareas_pendientes.sort()
print("Mi lista tras ordenar mis tareas, queda de la siguientes forma:\n",tareas_pendientes)
tareas_pendientes.clear()
print("Tareas pendientes tras vaciar la lista de tares pendientes es:\n",tareas_pendientes, "y el numero de tareas pendientes a realizar ahora es:",len(tareas_pendientes))

# 3· Operaciones con el Conjunto de la Lista de Compras

lista_compras.add( "manzana" )
print("\nLos productos que ahora debo de comprar son:\n",lista_compras,"por lo que ahora deberé de comprar", len(lista_compras), "producto.")
lista_compras.discard("tomate")
print("\nLos productos que ahora debo comprar son:\n",lista_compras,"por lo que ahora debo comprar", len(lista_compras), "productos.")
lista_compras.clear()
print("La cantidad de productos que hay que comprar tras vacias la lista de la compra es:", len(lista_compras)),"productos."

# 4· Operaciones con el Diccionario de Contactos:
agenda_contactos.update(luis=22222222222,monica = 333333333333,paloma = 777777777)
print("Mi agenda de contactos queda así tras incluirle los nuevos contactos:\n", agenda_contactos, "\n y el número total de contactos en mi agenda es ahora:",len(agenda_contactos),"contactos tengo ahora en mi agenda.")
print("Mis contactos ordenados alfabéticamente quedan de la siguiente manera:\n",sorted(agenda_contactos))
contacto_eliminado = agenda_contactos.pop("Ana")
print("El contacto eliminado es:\n",contacto_eliminado,"\n y mi agenda de contactos queda así sin Ana:\n",agenda_contactos)

agenda_contactos.clear()
print("La cantidad de contactos que quedan en mi agenda es tras vaciarla:", len(agenda_contactos), "contactos quedan en mi agenda.")

print("Recuerde que es muy facil salir de nuestro programa con solo pulsar la tecla escape de su teclado.")



""" 
OTRA POSIBLE SOLUCIÓN

# Creación de las colecciones de datos
tareas_pendientes = ['Hacer la compra', 'Estudiar para el examen', 'Llamar al médico', 'Enviar correo electrónico', 'Preparar la cena']
lista_compras = {'Manzanas', 'Leche', 'Pan', 'Huevos', 'Arroz'}
agenda_contactos = {'Juan': '123456789', 'María': '987654321', 'Carlos': '456789123', 'Ana': '321654987', 'Luisa': '654321987'}

# Operaciones con la lista de tareas pendientes
tareas_pendientes.append('Sacar al perro')
print("Tareas pendientes después de agregar una nueva tarea:", tareas_pendientes)
tareas_pendientes.remove('Llamar al médico')
print("Tareas pendientes después de eliminar una tarea:", tareas_pendientes)
tareas_pendientes.sort()
print("Tareas pendientes ordenadas alfabéticamente:", tareas_pendientes)
tareas_pendientes.clear()
print("Tareas pendientes después de vaciar la lista:", tareas_pendientes)

# Operaciones con el conjunto de la lista de compras
lista_compras.add('Cerveza')
print("Lista de compras después de agregar un ítem:", lista_compras)
lista_compras.discard('Leche')
print("Lista de compras después de eliminar un ítem:", lista_compras)
lista_compras.clear()
print("Lista de compras después de vaciar el conjunto:", lista_compras)

# Operaciones con el diccionario de contactos
nuevos_contactos = {'Pedro': '654987321', 'Elena': '789456123'}
agenda_contactos.update(nuevos_contactos)
print("Agenda de contactos después de agregar nuevos contactos:", agenda_contactos)

# Ordenar los contactos por nombre y mostrarlos en orden alfabético
contactos_ordenados = sorted(agenda_contactos.items())
print("Contactos ordenados alfabéticamente:", contactos_ordenados)

# Eliminar un contacto específico del diccionario de contactos
agenda_contactos.pop('María')
print("Agenda de contactos después de eliminar un contacto:", agenda_contactos)

# Vaciar el diccionario de contactos
agenda_contactos.clear()
print("Agenda de contactos después de vaciar el diccionario:", agenda_contactos)
"""