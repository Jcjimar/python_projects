""" 
1. Crea una tupla llamada **`compras_enero`** que contenga los precios de productos comprados durante el mes de enero.
2. Implementa la funcionalidad para calcular el total gastado en compras durante un mes.
3. Implementa la funcionalidad para encontrar el precio del producto más caro en una lista de precios.
4. Crea una tupla llamada **`compras_febrero`** con precios de productos comprados en febrero.
5. Utiliza el método **`count`** para contar cuántas veces se compró un producto específico en febrero.
6. Utiliza la función **`max`** para encontrar el precio más alto entre las dos tuplas.
7. Utiliza la función **`sum`** para calcular el gasto total en ambos meses.
8. Utiliza la función **`sorted`** para obtener una tupla ordenada de precios en ambos meses.
9. Imprime los resultados de las operaciones anteriores y verifica que las funcionalidades y métodos están trabajando correctamente.
"""
# 1. Creo la tupla de compras de enero
compras_enero = (19.75, 18.5, 32.25, 30.0, 31.99)

# 2. Calculo el total gastado en enero
total_enero = sum(compras_enero)

# 3. Encuentro el precio más alto en la lista de precios de enero
precio_max_enero = max(compras_enero)

# 4. Creo la tupla de compras de febrero
compras_febrero = (20.0, 29.99, 25.5, 22.0, 23.75, 33.0)

# 5. Cuenta cuántas veces se compró un producto específico en febrero
cantidad_producto_febrero = compras_febrero.count(20.0)

# 6. Encuentra el precio más alto entre las dos tuplas
precio_max_total = max(max(compras_enero), max(compras_febrero))

# 7. Calcula el gasto total en ambos meses
gasto_total = sum(compras_enero) + sum(compras_febrero)

# 8. Obtiene una tupla ordenada de precios en ambos meses
precios_ordenados = tuple(sorted(compras_enero + compras_febrero))

# 9. Imprime los resultados
print("1. Compras de Enero:", compras_enero)
print("2. Total gastado en Enero:", total_enero)
print("3. Precio más alto en Enero:", precio_max_enero)
print("4. Compras de Febrero:", compras_febrero)
print("5. Cantidad de veces que se compró el producto 18.0 en Febrero:", cantidad_producto_febrero)
print("6. Precio más alto entre ambos meses:", precio_max_total)
print("7. Gasto total en ambos meses: {:.3f}".format(gasto_total))
print("8. Precios ordenados en ambos meses:", precios_ordenados)