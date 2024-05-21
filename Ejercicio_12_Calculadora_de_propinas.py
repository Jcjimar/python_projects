""" 
Desarrolla un programa en Python que permita calcular la propina a dejar en un restaurante. El ejercicio se centrará en practicar operaciones aritméticas básicas, la entrada de datos desde el teclado, la conversión de datos mediante casting, y la presentación de resultados utilizando f-strings.

1. **Inicio del programa:**
    - Inicia el programa con un mensaje de bienvenida.
2. **Entrada de datos:**
    - Solicita al usuario que ingrese el monto total de la factura del restaurante como un número decimal.
3. **Entrada de porcentaje de propina:**
    - Pide al usuario que ingrese el porcentaje de propina que desea dejar.
4. **Cálculo de la propina:**
    - Calcula la propina a partir del monto total y el porcentaje ingresado. Utiliza la fórmula: **`Propina = Monto Total * (Porcentaje de Propina / 100)`**
5. **Mostrar resultados:**
    - Muestra el monto total de la factura, el porcentaje de propina y el monto total a pagar incluyendo la propina.
    - Utiliza f-strings para formatear los resultados y mostrar montos con dos decimales.
"""

# Inicio del programa
print("\n\n\n¡Bienvenido a la Calculadora de Propinas!\n \n \n")

# Entrada de datos. Pedimos que nos de el importe total del tiket para el posterior cálculo de la propina
monto_total = float(input("\nIngrese el importe total de la factura: \n"))

# Entrada de porcentaje de propina en formato decimal
porcentaje_propina = float(input("\nIngrese el porcentaje de propina que desea dejar: \n"))

# Cálculo de la propina
propina = monto_total * (porcentaje_propina / 100)

# Cálculo del monto total a pagar incluyendo la propina
total_a_pagar = monto_total + propina

# Mostrar resultados
print('\n------------------------------------\n')
print(f"\nTotal de la Factura: {monto_total:.2f}€\n")
print(f"Porcentaje de Propina: {porcentaje_propina}%\n")
print("----------------------------------------------\n")
print(f"Propina a Dejar: {propina:.2f}€\n \n")
print(f"Total a Pagar: {total_a_pagar:.2f}€\n\n\n")