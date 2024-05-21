""" 
1. Crea un diccionario llamado **`agenda_telefonica`** que contenga los nombres de algunas personas como claves y sus números de teléfono como valores.
2. Imprime el diccionario completo para verificar su contenido.
3. Accede al número de teléfono de una persona específica en la agenda telefónica e imprímelo.
4. Añade una nueva entrada a la agenda telefónica para una persona adicional junto con su número de teléfono.
5. Modifica el número de teléfono de una persona existente en la agenda telefónica.
6. Imprime el diccionario actualizado para verificar los cambios realizados.
"""
# 1. Crea el diccionario de la agenda telefónica
agenda_telefonica = {
    "Carlos": "123456789",
    "Dani": "987654321",
    "Paula": "555555555"
}

# 2. Imprime el diccionario completo
print("2. Agenda Telefónica:", agenda_telefonica)

# 3. Accede al número de teléfono de una persona específica y imprímelo
print("3. Número de teléfono de Dani:", agenda_telefonica["Dani"])

# 4. Añade una nueva entrada a la agenda telefónica
agenda_telefonica["Manolo"] = "111111111"

# 5. Modifica el número de teléfono de una persona existente
agenda_telefonica["Paula"] = "999999999"

# 6. Imprime el diccionario actualizado
print("6. Agenda Telefónica Actualizada:", agenda_telefonica)