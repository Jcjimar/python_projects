""" 
Desarrolla un programa en Python que permita calcular el precio final de un producto después de aplicar un descuento. 

1. **Inicio del programa:**
    - Inicia el programa con un mensaje de bienvenida.
2. **Entrada de datos:**
    - Solicita al usuario ingresar el precio original del producto como un número decimal.
3. **Entrada de descuento:**
    - Pide al usuario que ingrese el porcentaje de descuento que desea aplicar al producto.
4. **Cálculo del precio con descuento:**
    - Calcula el precio final después de aplicar el descuento. Utiliza la fórmula: **`Precio Final = Precio Original - (Precio Original * Porcentaje de Descuento / 100)`**
5. **Mostrar resultados:**
    - Muestra el precio original, el porcentaje de descuento y el precio final después de aplicar el descuento.
    - Utiliza f-strings para formatear los resultados y mostrar el precio final con dos decimales.
 """
#Bienvenida al usuario 
print("Bienvenido a nuestro programa de descuentazos")

#Pido al usuario el precio original
precio_original=float(input('\nIngrese el precio original del producto: \n----------------------------------------\n'))
#Pido al usuario descuento a aplicar al precio original al producto, sin decimles ni caracteres especiales
porcentaje_descuento= int(input('\nIngrese el descuento a aplicar al precio original del producto, escríbalo sin decimales ni símbolo de porcentaje (%): \n----------------------------------------\n'))

print('Gracias por la información facilitada')

#Cálculo del precio aplicando el descuento
precio_final= precio_original-(precio_original*(porcentaje_descuento/100))


# Mostrar resultados


#Precio original

print(f"\nPrecio Original: {precio_original:.2f}€")


#Porcentaje de descuento

print(f"Porcentaje de Descuento: {porcentaje_descuento}%")

print('\n----------------------------------------\n')
#Precio final con descuento

print(f"Precio Final con Descuento: {precio_final:.2f}€\n")