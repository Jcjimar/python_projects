""" 
Crea una clase llamada **`Persona`** que represente a una persona con los siguientes atributos:

- **`nombre`**: El nombre de la persona.
- **`edad`**: La edad de la persona.

La clase **`Persona`** debe tener los siguientes métodos:

1. **`__init__(self, nombre, edad)`:** Método constructor que inicializa los atributos **`nombre`** y **`edad`**.
2. **`__str__(self)`:** Método especial que devuelve una representación de cadena de la instancia de la clase. Debe devolver una cadena que incluya el nombre y la edad de la persona.

Además, crea una clase llamada **`Estudiante`** que herede de la clase **`Persona`** y tenga un atributo adicional:

- **`grado`**: El grado del estudiante.

La clase **`Estudiante`** debe tener un método adicional:

1. **`__str__(self)`:** Método especial que sobrescribe el método **`__str__`** de la clase base **`Persona`** para incluir el nombre, la edad y el grado del estudiante.

Escribe un programa principal que:

- Cree una instancia de la clase **`Persona`** con un nombre y una edad.
- Muestre la representación de cadena de la instancia de la clase **`Persona`**.
- Cree una instancia de la clase **`Estudiante`** con un nombre, una edad y un grado.
- Muestre la representación de cadena de la instancia de la clase **`Estudiante`**.
 """