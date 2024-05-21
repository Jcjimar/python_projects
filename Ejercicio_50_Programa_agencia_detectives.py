""" 
Has sido contratado por una empresa de detectives para desarrollar un programa que les ayude a identificar si una serie de palabras en clave son utilizadas en un mensaje. 

1. Crea una función llamada **`buscar_palabras_clave(mensaje)`** que tome un mensaje como entrada y devuelva un mensaje indicando si se encontraron o no palabras clave en el mensaje.
2. Define una lista de palabras clave que se utilizarán para buscar en el mensaje.
3. La función **`buscar_palabras_clave`** debe tomar como argumento el mensaje a analizar.
4. Si alguna de las palabras clave está presente en el mensaje, la función debe devolver "Se han encontrado palabras clave en el mensaje".
5. Si ninguna de las palabras clave está presente, la función debe devolver "No se han encontrado palabras clave en el mensaje".
6. Resuelve este ejercicio dos veces: la primera aplicando el retorno condicional y la segunda aplicando el retorno temprano
"""
#-- Resultado aplicando el retorno temprano --

# Definir las palabras clave
palabras_clave = ["secreto", "confidencial", "urgente", "importante"]

# Definir la función buscar_palabras_clave
def buscar_palabras_clave(mensaje):
    for palabra in palabras_clave:
        if palabra in mensaje:
            return "Se han encontrado palabras clave en el mensaje"
    return "No se han encontrado palabras clave en el mensaje"

# Solicitar al usuario que ingrese las frases
mensaje1 = str(input("Ingresa una frase para evaluar:\n"))
mensaje2 = str(input("Ingresa una frase para evaluar:\n"))
mensaje3 = str(input("Ingresa una frase para evaluar:\n"))

print(buscar_palabras_clave("Mensaje 1:", mensaje1))  
print(buscar_palabras_clave("Mensaje 2:", mensaje2))  
print(buscar_palabras_clave("Mensaje 3:", mensaje3)) 
