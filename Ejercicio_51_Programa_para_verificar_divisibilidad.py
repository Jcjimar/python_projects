""" 
Imagina que estás desarrollando un programa para verificar si un número es divisible por una serie de divisores dados. Para esto, debes crear una función llamada **`verificar_divisibilidad(numero, divisores)`** que tome un número y una lista de divisores como entrada y devuelva un mensaje indicando si el número es divisible por alguno de los divisores.

**Requisitos:**

- La función **`verificar_divisibilidad`** debe tomar como argumentos el número a verificar y una lista de divisores.
- Si el número es divisible por alguno de los divisores dados, la función debe devolver "El número es divisible por al menos uno de los divisores".
- Si el número no es divisible por ninguno de los divisores dados, la función debe devolver "El número no es divisible por ninguno de los divisores".
"""
#EJEMPLO SOLUCIÓN UTILIZANDO RETURN PARA VERIFICAR DIVISIBILIDAD

def verificar_divisibilidad(numero, divisores):
    resultados = []
    for divisor in divisores:
        if numero % divisor == 0:
            resultados.append(numero)
    if len(resultados) >= 1:
        return "Se han encontrado números divisibles" 
    else:
        return "No se han encontrado números divisibles"

numero = int(input("Introduce el numero a evaluar:\n"))
divisor1 = int(input("Introduce el primer divisor:\n"))
divisor2 = int(input("Introduce el segundo divisor:\n"))
divisores = [divisor1, divisor2]
resultado = verificar_divisibilidad(numero, divisores)
print(resultado)


#EJEMPLO NO UTILIZANDO RETURN PARA VERIFICAR DIVISIBILIDAD

def verificar_divisibilidad(numero, divisores):
    resultados = []
    for divisor in divisores:
        if numero % divisor == 0:
            resultados.append(numero)
    if len(resultados) >= 1:
        print("Se han encontrado números divisibles") 
    else:
        print("No se han encontrado números divisibles")

numero = int(input("Introduce el numero a evaluar:\n"))
divisor1 = int(input("Introduce el primer divisor:\n"))
divisor2 = int(input("Introduce el segundo divisor:\n"))
divisores = [divisor1, divisor2]
verificar_divisibilidad(numero, divisores)
