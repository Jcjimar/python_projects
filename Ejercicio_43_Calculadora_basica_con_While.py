""" 
Desarrolla un programa en Python que simule una calculadora básica. El programa solicitará al usuario que ingrese dos números y luego le permitirá realizar operaciones matemáticas básicas seleccionando un operador. El programa continuará ejecutándose hasta que el usuario decida salir.

1. El programa iniciará un bucle **`while`** para permitir la ejecución continua del programa.
2. Dentro del bucle, el programa solicitará al usuario que ingrese dos números y almacenará estos valores en variables.
3. Luego, el programa solicitará al usuario que seleccione un operador matemático entre suma (+), resta (-), multiplicación (*) o división (/).
4. Dependiendo del operador seleccionado, el programa realizará la operación correspondiente con los dos números ingresados.
5. El resultado de la operación se mostrará al usuario.
6. Después de mostrar el resultado, el programa preguntará al usuario si desea continuar o salir del programa.
7. Si el usuario elige continuar, el programa volverá al paso 2.
8. Si el usuario elige salir, el programa imprimirá un mensaje de despedida y finalizará la ejecución.
"""
# Inicialización del bucle while
while True:
    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Solicitar al usuario que seleccione un operador matemático
    operador = input("Seleccione un operador matemático (+, -, *, /): ")
    
    # Realizar la operación correspondiente según el operador seleccionado
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        # Manejar el caso de división por cero
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = num1 / num2
            # Mostrar el resultado de la operación al usuario
            print("El resultado es:", resultado)
    else:
        print("Operador inválido.")
    
    # Preguntar al usuario si desea continuar o salir del programa
    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        print("¡Hasta luego!")
        break  # Salir del bucle while y finalizar la ejecución del programa
