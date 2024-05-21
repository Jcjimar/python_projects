""" 
1. **Inicialización del inventario:**
    - Crea una lista llamada **`inventario`** que contendrá tuplas representando los productos en stock. Cada tupla contendrá el nombre del producto, su precio y la cantidad disponible en la tienda.
    - Agrega al menos 5 productos al inventario.
2. **Operaciones del inventario:**
    - Agrega un nuevo producto al inventario especificando su nombre, precio y cantidad.
    - Actualiza la cantidad disponible de un producto existente en el inventario.
    - Elimina un producto del inventario.
    - Busca un producto en el inventario y muestra su información si está disponible.
3. **Operaciones adicionales:**
    - Ordena el inventario alfabéticamente por nombre de producto.
    - Cuenta cuántos productos tienes en el inventario.
    - Encuentra la posición de un producto específico en el inventario.
4. **Mostrar resultados:**
    - Después de cada operación, muestra el inventario actualizado con todos los productos y su información.
    - Al final, muestra el inventario completo una última vez antes de finalizar el programa.
    - Puedes dar formato de salida a la muestra de inventario para que simule una tabla utilizando caracteres especiales.
"""
inventario = []
television = ("television1",150,12)
computadora = ("computadora1",300,8)
smartphone = ("smartphone1",70,4)
smartwatch = ("smartwatch1",20,1)
lavadora =  ("lavadora1",60,10)
frigorifico =  ("frigorifico1",90,10)
inventario.extend([television,computadora,smartphone,smartwatch,lavadora, frigorifico])
print("\nMi inventario es el siguiente:\n",inventario,"\nEl número de productos diferentes en nuestro catalogo es:\n",len(inventario),"productos hay en nuestro catálogo.")

# Agregar un nuevo producto a mi inventario
impresora = ("impresora1",50,7)
inventario.append(impresora)
print("\nMi inventario  actual tras agregar un nuevo producto es: ",inventario)

# Actualiza la cantidad disponible de un producto existente en el inventario.
inventario.remove(television)
list_television = list(television)
list_television[2] = 20
television = tuple(list_television)
inventario.append(television)
print("\nEl inventario actualizado con la nueva cantidad de televisores es:", inventario)

# Elimine un producto del inventario
inventario.remove(lavadora)
print("\nMi inventario una vez eliminada la lavadora es:", inventario)

# Busca un producto en el inventario y muestra su información si está disponible.
inventario.index(smartphone)
print("La información de la smartphone es:", inventario[inventario.index(smartphone)])

# Ordena el inventario alfabéticamente por nombre de producto.
inventario.sort()
print("Mi inventario ordenado alfabeticamente es:", inventario)

# Cuenta cuántos productos tienes en el inventario.
print("El numero toral de productos del inventario es:",len(inventario),"productos.\n")

# Encuentra la posición de un producto específico en el inventario.
inventario.index(television)
print("La television es la posición",inventario.index(television)," en el inventario\n")

#Inventario completo  con los precios unitarios y cantidades
print("Inventario completo:", inventario,"\n")


""" 
OTRA POSIBLE SOLUCIÓN:

#SOLUCIÓN CON CONDICIONALES
# 1. Inicialización del inventario
inventario = [
    ("Camiseta", 15.99, 20),
    ("Pantalón", 29.99, 15),
    ("Zapatos", 49.99, 10),
    ("Bufanda", 9.99, 30),
    ("Gorra", 5.99, 25)
]

# 2. Operaciones del inventario
# Agregar un nuevo producto
print("Agregar un nuevo producto al inventario:")
nombre = str(input("Nombre del producto: ").title())
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad disponible: "))
nuevo_producto = (nombre, precio, cantidad)
inventario.append(nuevo_producto)

# Mostrar el inventario actualizado
print("\nInventario actualizado:")
print(f"| {'Nombre':<10} | {'Precio':>9} | {'Cantidad':>10} |")
print("|------------|-----------|------------|")
for producto in inventario:
    print(f"| {producto[0]:<10} | {producto[1]:>8.2f}€ | {producto[2]:>10} |")

INCISO PARA EXPLICAR LA ÚLTIMA INSTRUCCIÓN
El formato de ancho fijo en Python se refiere a la técnica de formatear cadenas de texto para que tengan una longitud específica, independientemente de la longitud del contenido real. Esto se logra utilizando caracteres de relleno, como espacios en blanco, para ajustar la cadena al ancho deseado.

Su sintaxis se crea a partir de la combinación de especificadores de formato y modificadores. Por ejemplo:

<: Indica alineación a la izquierda.
>: Indica alineación a la derecha.
^: Indica alineación central.
10: Indica el ancho deseado de la cadena, en este caso, 10 caracteres.

Algunos ejemplos:
· nombre:<10
· Precio:>9.2f
· Cantidad:^10


# Eliminar un producto del inventario
print("\nEliminar un producto del inventario:")
producto_eliminar = str(input("Nombre del producto a eliminar: ")).title()
inventario_copia = inventario.copy()
for producto in inventario_copia:  # Iterar sobre una copia superficial de la lista para evitar problemas al eliminar elementos
    if producto[0] == producto_eliminar:
        inventario.remove(producto)
        break
else:
    print(f"El producto '{producto_eliminar}' no está en el inventario.")

# Mostrar el inventario actualizado
print("\nInventario actualizado:")
print(f"| {'Nombre':<10} | {'Precio':>9} | {'Cantidad':>10} |")
print("|------------|-----------|------------|")
for producto in inventario:
    print(f"| {producto[0]:<10} | {producto[1]:>8.2f}€ | {producto[2]:>10} |")


# Buscar un producto en el inventario
print("\nBuscar un producto en el inventario:")
producto_buscar = str(input("Nombre del producto a buscar: ")).title()
for producto in inventario:
    if producto[0] == producto_buscar:
        print(f"Información del producto {producto[0]}: Precio: {producto[1]}€, Cantidad: {producto[2]}")
        break
else:
    print(f"El producto '{producto_buscar}' no está en el inventario.")

# Mostrar el inventario actualizado
print("\nInventario actualizado:")
print(f"| {'Nombre':<10} | {'Precio':>9} | {'Cantidad':>10} |")
print("|------------|-----------|------------|")
for producto in inventario:
    print(f"| {producto[0]:<10} | {producto[1]:>8.2f}€ | {producto[2]:>10} |")


# 3. Operaciones adicionales
# Ordenar el inventario alfabéticamente por nombre de producto
print("El inventario ordenado es:", sorted(inventario))

# Contar cuántos productos hay en el inventario
num_productos = len(inventario)
print("\nNúmero total de productos en el inventario:", num_productos)

# Encontrar la posición de un producto específico en el inventario
posicion_producto = inventario.index(("Camiseta", 15.99, 20))
print("Posición del producto 'Camiseta' en el inventario:", posicion_producto)
"""