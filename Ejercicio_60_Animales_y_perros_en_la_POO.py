""" 
Crea una clase llamada **`Animal`** que represente a un animal con los siguientes atributos:

- **`nombre`**: El nombre del animal.
- **`especie`**: La especie del animal.

La clase **`Animal`** debe tener los siguientes métodos:

1. **`__init__(self, nombre, especie)`:** Método constructor que inicializa los atributos **`nombre`** y **`especie`**.
2. **`__str__(self)`:** Método especial que devuelve una representación de cadena de la instancia de la clase. Debe devolver una cadena que incluya el nombre y la especie del animal.
3. **`sonido(self)`:** Método que imprime un mensaje que representa el sonido que hace el animal.

Crea una subclase de **`Animal`** llamada **`Perro`** que represente a un perro. La clase **`Perro`** debe tener los siguientes atributos de clase adicionales:

- **`total_perros`**: Un contador que lleva la cuenta de la cantidad total de perros creados.

La clase **`Perro`** debe tener los siguientes métodos adicionales:

1. **`__init__(self, nombre)`:** Método constructor que inicializa el atributo **`nombre`** y aumenta el contador **`total_perros`**.
2. **`__str__(self)`:** Método especial que sobrescribe el método **`__str__`** de la clase base **`Animal`** para incluir el nombre, la especie y una descripción del perro.
3. **`sonido(self)`:** Método que imprime un ladrido, representando el sonido de un perro.

Escribe un programa principal que:

- Cree varias instancias de la clase **`Perro`** con diferentes nombres.
- Muestre la representación de cadena de cada instancia de la clase **`Perro`**.
- Llame al método **`sonido()`** de cada instancia de la clase **`Perro`**.
- Muestre el valor del contador **`total_perros`** al finalizar.
"""