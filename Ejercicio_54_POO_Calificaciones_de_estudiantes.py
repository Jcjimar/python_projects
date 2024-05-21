""" 
Crea un programa en Python que permita al usuario registrar la asistencia y calificaciones de un estudiante. Trabaja con métodos de instancia para resolver este ejercicio. 

1. Crea una clase llamada **`Estudiante`** con los siguientes atributos:
    - **`nombre`**: El nombre del estudiante.
    - **`asistencia`**: Un contador que registra la cantidad de días de asistencia.
    - **`calificaciones`**: Una lista que almacena las calificaciones del estudiante.
2. La clase **`Estudiante`** debe tener los siguientes métodos de instancia:
    - **`__init__(self, nombre)`**: Método constructor que inicializa el nombre del estudiante, la asistencia en cero y una lista vacía de calificaciones.
    - **`registrar_asistencia(self)`**: Método que incrementa el contador de asistencia en uno.
    - **`agregar_calificacion(self, calificacion)`**: Método que agrega una calificación a la lista de calificaciones del estudiante.
    - **`promedio_calificaciones(self)`**: Método que calcula y devuelve el promedio de las calificaciones del estudiante.
3. Solicita al usuario los siguientes datos del estudiante:
    - Nombre del estudiante.
    - Cantidad de días de asistencia.
    - Calificaciones del estudiante.
4. Utiliza la clase **`Estudiante`** para crear una instancia con los datos proporcionados por el usuario y realiza las siguientes acciones:
    - Registra la asistencia del estudiante.
    - Agrega las calificaciones del estudiante.
    - Calcula el promedio de calificaciones del estudiante.
5. Muestra los resultados por pantalla, incluyendo el nombre del estudiante, la cantidad de días de asistencia, y el promedio de calificaciones. 
"""

class Estudiante: #Creo la clase Estudiante
    def __init__(self, nombre):
        self.nombre = nombre #Defino el nombre del estudiante
        self.asistencia=0  #La asistencia del estudiante la comienzo en 0
        self.calificaciones= [] #Creo una lista de calificaciones del estudiante        
              
    def registrar_asistencia(self):        
        """Incrementa el contador de asistencia en uno."""
        self.asistencia += 1
           
    def agregar_calificacion(self, calificacion):
        
       
            self.calificaciones.append(calificacion)

    def promedio_calificaciones(self):
        """
        Calcula y devuelve el promedio de las calificaciones del estudiante.
        :return: El promedio de las calificaciones
        """
        if not self.calificaciones:
            return 0.0  # Si no hay calificaciones, el promedio es 0
        suma_calificaciones = sum(self.calificaciones)
        num_calificaciones = len(self.calificaciones)
        promedio = suma_calificaciones / num_calificaciones
        return promedio

print("*******************"*5)

nombre= str(input("Pon tu nombre:\t"))
estudiante= Estudiante(nombre)
cantidad_dias_asistencia =int(input("Ingrese los días de asistencia:\t"))
estudiante.asistencia=cantidad_dias_asistencia

 # Solicitar y agregar las calificaciones (puedes hacerlo en un bucle si hay más de una)
while True:
    calificacion = input("Ingresa una calificación (ó out para finalizar): ")
    if calificacion.lower() == 'out':
        break
    estudiante.agregar_calificacion(float(calificacion))

print("Resultados del Estudiantes:")
print(f"Nombre:\t{estudiante.nombre}")
print(f"Asistencia:\t{estudiante.asistencia}")
print(f"Promedio de calificaciones:\t{estudiante.promedio_calificaciones():.2f}")