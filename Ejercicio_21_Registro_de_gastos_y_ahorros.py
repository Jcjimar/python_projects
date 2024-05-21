""" 
Crea un programa en Python que simule el registro de gastos y ahorros. Utiliza variables para representar el saldo inicial, solicita al usuario ingresar gastos y ahorros, y utiliza operadores y el método **`append()`** para actualizar la información. Realiza las siguientes operaciones:

1. Pregunta al usuario por su saldo inicial utilizando **`input()`**.
2. Muestra un mensaje de bienvenida y el saldo inicial.
3. Pregunta al usuario por el importe de un gasto y lo resta del saldo.
4. Pregunta al usuario por el importe de un ahorro y lo suma al saldo.
5. Muestra el saldo actualizado y una lista con los gastos y ahorros registrados.
"""
# Registro de gastos y ahorros

# Pregunta al usuario por el saldo inicial
saldo_inicial = float(input("\n\nIngrese su saldo inicial:\n\n "))

# Inicializa listas para gastos y ahorros
gastos = []
ahorros = []

# Muestra un mensaje de bienvenida y el saldo inicial
print(f"\n\nBienvenido al Registro de Gastos y Ahorros. Saldo inicial: {saldo_inicial:.2f}€\n\n\n")

# Pide al usuario ingresar un gasto y lo resta del saldo
gasto = float(input("\n\nIngrese el importe del gasto: "))
saldo_inicial -= gasto
gastos.append(gasto)

# Pide al usuario ingresar un ahorro y lo suma al saldo
ahorro = float(input("Ingrese el importe del ahorro: "))
saldo_inicial += ahorro
ahorros.append(ahorro)

# Muestra el saldo actualizado y la lista de gastos y ahorros
print(f"\nSaldo actualizado: {saldo_inicial:.2f}€")
print("Lista de gastos registrados:", gastos)
print("Lista de ahorros registrados:", ahorros)