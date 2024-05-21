""" 
Implementa un bucle while que permita al usuario crear instancias de la clase libro, aportando el nombre de la instancia y los valores correspondientes a cada uno de los atributos que forman la propia instancia, hasta que el usuario decida salir del programa para agregar libros a la biblioteca. Antes de salir del programa tenemos que mostrar al usuario la cantidad de libros en biblioteca actualizada.
· Creamos una estructura de control del bucle While que se corresponda con un bucle infinito.
· Solicitamos al usuario la entrada de los datos de la nueva instancia que queremos crear: 
    · Título
    · Autor
    · Páginas
· Creamos un nuevo objeto de la clase libro con los valores de sus atributos introducidos por el usuario.
· Le pregguntamos al usuario si quiere crear un nuevo objeto o si quiere salir del programa.
· Antes de salir del programa y despedirnos, imprimimos por pantalla la cantidad actualizada de los libros de mi biblioteca.
"""
# CONTINUAMOS CON EL EJEMPLO BIBLIOTECA

class Libro:
    #Este atributo de clase hace referencia a todas las instancias que se creen de esta misma clase. Este valor es común para todas las instancias. 
    cantidad_libros_en_biblioteca = 0
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        #Cada vez que cree una instancia de la clase Linro, quiero que la cantidad de libros en biblioteca se incremente en 1
        Libro.cantidad_libros_en_biblioteca += 1
    #Formateamos la salida del objeto para que en vez de mostrarnos la clase a la que pertenece y su ubicación en la memoria, nos muestre la salida con el formato que necesitamos, más legible y fácilmente comprensible.
    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor}"
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de paginas: {self.paginas}\n")

#Creamos dos objetos de la clase Libro      
libro_uno = Libro("El Alquimista", "Paulo Coehlo", 149)
libro_dos = Libro("Juan Salvador Gaviota", "Nader El Yacoubi", 239)

#Modifico el valor de un atributo en una instancia específica
libro_uno.titulo = "Nuevo valor para el título del libro 1"

#Mostrar la información de las instancias que he creado
print("Información libro 1:\n")
libro_uno.mostrar_info()

print("Información libro 2:\n")
libro_dos.mostrar_info()

#Mostrar la cantidad actual de libros en mi biblioteca
print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca}")

#Creo un nuevo objeto de la clase Libro
libro_tres = Libro("Python essentials", "Guido Van Rossum", 698)

#Mostrar la cantidad actual de libros en mi biblioteca
print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca}")

#Creamos una lista 'biblioteca' que almacene los objetos de la clase Libro
biblioteca = [libro_uno, libro_dos, libro_tres]
#Iteramos sobre cada uno de los elementos de la lista 'biblioteca', imprimiéndolos en pantalla. 
for libro in biblioteca:
    print(libro)

""" 
EJERCICIO RÁPIDO 1: Implementa un bucle while que permita al usuario crear instancias de la clase libro, aportando el nombre de la instancia y los valores correspondientes a cada uno de los atributos que forman la propia instancia, hasta que el usuario decida salir del programa para agregar libros a la biblioteca. Antes de salir del programa tenemos que mostrar al usuario la cantidad de libros en biblioteca actualizada.
· Creamos una estructura de control del bucle While que se corresponda con un bucle infinito.
· Solicitamos al usuario la entrada de los datos de la nueva instancia que queremos crear: 
    · Título
    · Autor
    · Páginas
· Creamos un nuevo objeto de la clase libro con los valores de sus atributos introducidos por el usuario.
· Le pregguntamos al usuario si quiere crear un nuevo objeto o si quiere salir del programa.
· Antes de salir del programa y despedirnos, imprimimos por pantalla la cantidad actualizada de los libros de mi biblioteca.
"""

#SOLUCIÓN CARLOS:
# Lista para almacenar los libros
biblioteca = []
while True:
    print("\n--- Agregar un nuevo libro a la biblioteca ---")
    titulo = str(input("Ingrese el título del libro (o escriba 'salir' para finalizar): "))
    
    if titulo.lower() == "salir":
        break  # Salir del bucle si el usuario ingresa "salir"
    
    autor = str(input("Ingrese el autor del libro: "))
    paginas = int(input("Ingrese el número de paginas del libro: "))
    
    # Crear una instancia de la clase Libro
    nuevo_libro = Libro(titulo, autor, paginas)
    
    # Agregar el libro a la biblioteca
    biblioteca.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado a la biblioteca.")

#Mostar la cantidad actual de libros en mi biblioteca  
print(f"La cantidad de libros en la biblioteca es: {Libro.cantidad_libros_en_biblioteca}")
print("Muchas gracias por usar el programa de gestión de biblioteca, hasta la próxima")
