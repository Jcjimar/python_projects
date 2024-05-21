""" 
Desarrolla un programa en Python que ayude a un autónomo a calcular los impuestos que deberá pagar en un trimestre. 

1. **Inicio del Programa:**
    - Inicia el programa con un mensaje de bienvenida para el autónomo.
2. **Entrada de Datos:**
    - Solicita al autónomo ingresar los siguientes datos:
        - Ingresos totales del trimestre como un número decimal.
        - Gastos deducibles del trimestre como un número decimal.
        - Otros gastos no deducibles del trimestre como un número decimal.
3. **Cálculo de la Base Imponible:**
    - Calcula la base imponible restando los gastos deducibles y otros gastos no deducibles a los ingresos totales.
4. **Cálculo del Impuesto a Pagar:**
    - Calcula el impuesto a pagar como el 10% de la base imponible.
5. **Mostrar Resultados:**
    - Muestra los siguientes resultados:
        - Ingresos totales.
        - Gastos deducibles.
        - Otros gastos no deducibles.
        - Base imponible.
        - Impuesto a pagar.
6. **Consideraciones Adicionales:**
    - Utiliza f-strings para formatear los resultados y mostrar montos con dos decimales.
    - No es necesario utilizar la estructura de control **`if`** en este ejercicio.
"""
# Mensaje de bienvenida de la calculadora de impuestos para autónomos
print('\n\n\n¡Bienenido a la caluladora de impuestos para autonomos!\n\n\n')

#Entrada de datos
Ingresos_totales= float(input('Ingresos totales del trimestre como un número decimal de dos decimales: \n \n'))
gastos_deducibles= float(input('Gastos deducibles del trimestre como un número decimal: \n \n'))
gastos_no_deducible= float(input('Gastos deducibles del trimestre como un número decimal: \n \n'))

# Cálculo de la Base Imponible

base_imponible= Ingresos_totales - (gastos_deducibles + gastos_no_deducible )  

# Cálculo impuesto a pagar

impuesto_a_pagar_por_el_contribuyente= base_imponible * 0.1

# Mostrar resultados
print('\n--------------------------\n RESULTADOS:\n-------------------------------\n\n\n')

print(f'Los Ingresos totales del trimestre son: {Ingresos_totales:.2f}€\n\n')
print(f'Los gastos deducibles del trimestre son:{gastos_deducibles:.2f}€\n\n')
print(f'Los gastos no deducibles del trimestre son:{gastos_no_deducible:.2f}€\n\n')
print(f"La base imponible es: {base_imponible:.2f}€\n\n")
print(f'El impuesto a pagar por el contribuyente es:{impuesto_a_pagar_por_el_contribuyente:.2f}€\n\n\n')