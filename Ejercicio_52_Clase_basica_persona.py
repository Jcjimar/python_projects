""" 
1. Crea una clase llamada **`Persona`** con los siguientes atributos:
    - **`nombre`**: El nombre de la persona.
    - **`edad`**: La edad de la persona.
2. La clase **`Persona`** debe tener los siguientes métodos:
    - **`__init__(self, nombre, edad)`**: Método constructor que inicializa los atributos **`nombre`** y **`edad`**.
    - **`presentarse(self)`**: Método que imprime un mensaje de presentación de la persona, mostrando su nombre y edad.
3. Desarrolla un programa principal que permita al usuario:
    - Crear instancias de la clase **`Persona`**.
    - Establecer los valores de los atributos **`nombre`** y **`edad`**.
    - Invocar el método **`presentarse()`** para cada instancia creada.
"""
class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre #Defino el nombre de la persona
        self.edad = edad #Defino la edad de la persona
    def presentarse(self):
       print(f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años.")
if __name__ == "__main__":
    nombre= str(input("Pon tu nombre:\t"))
    edad= int(input("Pon tu edad:\t"))

    persona = Persona(nombre,edad)
    persona.presentarse()