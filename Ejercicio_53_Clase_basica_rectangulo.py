""" 
Crea una clase llamada **`Rectangulo`** que represente un rectángulo. La clase debe tener los siguientes atributos:

- **`base`**: Representa la longitud de la base del rectángulo.
- **`altura`**: Representa la altura del rectángulo.

La clase **`Rectangulo`** debe tener los siguientes métodos de instancia:

1. **`__init__(self, base, altura)`**: Constructor que recibe la longitud de la base y la altura del rectángulo y los asigna a los atributos correspondientes.
2. **`area(self)`**: Método que calcula y devuelve el área del rectángulo (base * altura).
3. **`perimetro(self)`**: Método que calcula y devuelve el perímetro del rectángulo (2 * (base + altura)).
"""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Programa principal
rectangulo1 = Rectangulo(5, 3)

print("Información del rectángulo:")
print("Base:", rectangulo1.base)
print("Altura:", rectangulo1.altura)
print("Área:", rectangulo1.area())
print("Perímetro:", rectangulo1.perimetro())
