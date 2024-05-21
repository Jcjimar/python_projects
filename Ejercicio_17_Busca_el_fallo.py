""" 
Localiza los errores en cada una de estas instrucciones de Python. Una vez que hayas localizado el error, documéntalo con un comentario en la misma línea de código.
"""
""" #BLOQUE NÚMERO 1

1numero = 5          # El naming de las variables no admite comenzar con un número
.decimal = 5.2      # El naming de las variables no admite comenzar con un caracter especial a excepcion del "_"
cadena-caracteres ="Hola"    # El naming de la variable no admite guion medio,solo gruión bajo "_". Además para separar dos palabras en el naming de una variable, utilizamos el "snake_case". Además los opereadores de asignacion deben contener un espacio inmediatamentes antes e inmediatamentes después del operador.
bool = True     # El naming de la varibale no puede contener un keyword (palabra reservada) de python.  En python no se pueden utilizar las palabras reservadas  para incializar variables, funciones y cualquier otro elemento.
variableUno = 'valor'  #El naming de la vatiable no debería contener mayúsculas. El recurso del camelCase esta reservado para el naming de clases, las variables y las funciones utilizamos el "snake_case"
cadena(1:2) # En este caso nos quiere mostrar una sección de la cadera. Usa los parentesis normales en vez de los corchetes. Además no hemos definido la variable cadena, por tanto nos lanzará un error de sintaxis.  Un SyntaxError

entrada = input[] # Después del input van paréntesis, no corchetes . 
Entrada = ent(input()) # Para convertir  a entero el input usamos el comando "int" no el comando "ent". El naming de las variables no recomiendan utilizar mayusculas.

# Sin \n
nombre = input("Por favor, introduce tu nombre:") #falta str delante del input. En python es fundamental determninar el tipo de dato que le solicitemos a un usuario a través del método input()
print("Hola,", nombre "¡Bienvenido!")   #Faltaría una coma despues de la variable nombre. En Python no podemos representar en salida datos que no estén concatenados correctamente o sin haber realizado las conversiones pertinentes.         


# Con \n
nombre = input\n("Por favor, introduce tu nombre:\n") # Aquí el error se encuentra en la "\n" del principio que debería estar dentro del paréntesis del input y después de las momillas del mensaje. Tambien falta el str delante del input. Es obligatorio definir el tipo de dato de entrada. 
print("n\Hola,", nombre, "\n¡Bienvenido!") # El recurso para generar un salto de linea dentro de un string es \n, no es n\. Dentro del print 

print("Introduce tu nombre") #Temnos una instruccion correcta.
tu-nombre = input()  #El naming de las variables no debe contener el guión medio. 
print("Hola", tunombre. tuapellido)  #El problema lo tenemos en "tunombre" porque la variable no se ha definido antes. 
tuapellido = str(input("Introduce tu apellido\n"))

#BLOQUE NÚMERO 1. Solucion más completa

1numero = 5   # El naming de las variables no admite comenzar con un número
.decimal = 5.2  # El naming de las variables no adminite caracteres especiales, a excepción del _
cadena-caracteres ="Hola" # El naming de las variables no admite -, solo _. Además para separar dos palabras en el naming de una variable, utilizamos el "snake_case". Además los operadores de asignación deben incluir un espacio inmediatamente antes e inmediatamente después del símbolo del operador
bool = True  # bool es una palabra reservada, y en Python no se permite utilizar las palabras reservadas para inicializar variables, funciones o cualquier otro elemento.
variableUno = 'valor' #El recurso del CamelCase en Python está reservado para realizar naming de CLASES, las variables y las funciones utilizan "snake_case"
cadena(1:2) # Para acceder al index de una cadena o un elemento utilizo los corchetes, no los paréntesis cadena[1:2]. Además no hemos definido la variable cadena, por lo tanto nos lanzara un error de sintaxis SyntaxError

entrada = input[] # Los métodos en Python utilizan () paréntesis, no corchetes []
Entrada = ent(input()) # El método que me permite formatear el tipo de dato a un entero es int() no ent(). El naming de las variables no recomienza utilizar mayúsculas. 

# Sin \n
nombre = input("Por favor, introduce tu nombre:") #Es fundamental en Python determinar el tipo de dato que le solicitamos a un usuario a través del método input(). La solución sería nombre = str(input("Por favor, introduce tu nombre:"))
print("Hola", nombre "¡Bienvenido!") # En Python no podemos representar en salida datos que no estén concatenados correctamente o sin haber realizado las conversiones pertinentes. La solución sería print("Hola,", nombre, "¡Bienvenido!")


# Con \n
nombre = input\n("Por favor, introduce tu nombre:\n") # Los saltos de línea de un string que generamos con el recurso \n deben ir siempre dentro del propio string, en el punto exacto donde yo quiera generar el salto de línea. Además, debemos especificar el tipo de dato de entrada. La solución sería: nombre = str(input("\nPor favor, introduce tu nombre:\n"))
print("n\Hola," {nombre} "\n¡Bienvenido!") # El recurso para generar un salto de línea dentro de un string es \n, no n\. La solución sería: print(f"\nHola, {nombre} \n¡Bienvenido!")

print("Introduce tu nombre") # Por fin una instrucción correcta :)
tu-nombre = input() #  El naming de las variables no admite -, solo _. Además debemos formatear la entrada de datos directamente en el método input()
#A nivel de estructura, la forma correcta de resolver las dos instrucciones anteriores:
#tu_nombre = str(input("Introduce tu nombre"))

print("Hola", tunombre. tuapellido) # Para concatenar variables utilizamos el operador ",", no el "."; La variable tunombre no está inicializada, por lo tanto nos lanzará un error. Para utilizar una variable en cualquier operación, necesito inicializarla y asignarle un valor ANTES.
tuapellido = str(input("Introduce tu apellido\n")) #Debería haberse inicializado antes de la instrucción anterior que utiliza esta variable en una operación de salida, y además, según las reglas de estilo del PEP8, para separar dos palabras en una variable debo utilizar el recurso del "snake_case".

# BLOQUE NÚMERO 2
Programa de Información Personal  # Para introducir un comentario o aclaración,  SIEMPRE es obligatorio comenzar la línea el simbolo "#" o """ """ si fuera un comentario o aclaración en bloque.

print( "¡Bienvenido al Programa de Información Personal!\n" )

# Mensaje personalizado usando .format()
mensaje_format = "¡Hola, {}, ! Bienvenido a {}."(format[nombre, ciudad]);  #Ciudad no es una variable declarada previamente o a posteriori

# Entrada de datos
nombre =input (Introduce tu nombre: ) #Faltan las la comillas "" dentro del print antes y después del mensaje.
edad =input ("Introduce tu edad: ")
ciudad =input ("Introduce tu ciudad de residencia: ') #El tipo de comillado debe ser el mismo al principio y al final y no de dos tipos omo en este caso.

# Mensaje personalizado usando f-string
mensaje_fstring = F"Esperamos que disfrutes tu estadía. Tienes {edad:x.2h} años de sabiduría." #  La "f" de fstring nunca va en letra mayúscula. Además.  no es ".2h" sino ".2f"

# Mostrar resultados
print(mensaje_format x 2) # El naming de la variable es mensaje_fstring
print(mensaje_fxtring) #El naming de la variable es mensaje_fstring


# BLOQUE NÚMERO 2
Programa de Información Personal # Falta la almohadilla para que este texto se convierta en un comentario y no sea interpretado por el intérprete
print( "¡Bienvenido al Programa de Información Personal!\n" ) #No debemos dejar espacio inmediatamente antes o después del paréntesis de apertura, o antes del paréntesis de cierre, detrás de este parétesis de cierre de print directamente incluímos un salto de línea, ya que en Python debemos incluir una instrucción por línea 

# Mensaje personalizado usando .format()
mensaje_format = "¡Hola, {}, ! Bienvenido a {}."(format[nombre, ciudad]); # Nos sobran los paréntesis inmediatamente antes y después del método .format(). Además, para incluir los argumentos de este método utilizamos paréntesis(), no corchetes[]. El método .format() incluye un punto entre el string y el nombre del método. En Python NUNCA se cierra una instrucción con ";". Además, las variables nombre y ciudad no están aún inicializadas, por lo que nos va a generar un error de SyntaxError. La solución a esta instrucción sería: mensaje_format = "¡Hola, {}, ! Bienvenido a {}.".format(nombre, ciudad). --> Incluyéndolo detrás de las 3 variables que inicializamos a continuación.

# Entrada de datos
nombre =input (Introduce tu nombre: ) # Los operadores deben incluir un espacio inmediatamente antes e inmediatamente después. El método input no incluye nunca espacio entre el nombre del método y los parénteris que nos indican que estamos ante un método de Python que admite argumentos. Faltan las comillas antes y después del string de - Introduce tu nombre -. Además debemos incluir SIEMPRE el tipo de dato de entrada.
edad =input ("Introduce tu edad: ") # Los operadores deben incluir un espacio inmediatamente antes e inmediatamente después. El método input no incluye nunca espacio entre el nombre del método y los parénteris que nos indican que estamos ante un método de Python que admite argumentos. Además debemos incluir SIEMPRE el tipo de dato de entrada.
ciudad =input ("Introduce tu ciudad de residencia: ') # Los operadores deben incluir un espacio inmediatamente antes e inmediatamente después. El método input no incluye nunca espacio entre el nombre del método y los parénteris que nos indican que estamos ante un método de Python que admite argumentos. En Python podemos utilizar indistintamente las comillas dobles o simples, pero no podemos mezclarlas en ningún caso - Introduce tu nombre -. Además debemos incluir SIEMPRE el tipo de dato de entrada.

# Mensaje personalizado usando f-string
mensaje_fstring = F"Esperamos que disfrutes tu estadía. Tienes {edad:x.2h} años de sabiduría." # El método f-string utiliza la f en minúscula inmediatamente antes del string para indicar al intérprete que estamois ante un f-string. Además, dentro del marcador de edad por lógica, nos sobra la conversión de formato :x.2h, ya que la edad no es un número flotante. Pero si lo fuera la sintaxis sería {edad:.2f}. La solución sería: mensaje_fstring = f"Esperamos que disfrutes tu estadía. Tienes {edad} años de sabiduría."

# Mostrar resultados
print(mensaje_format x 2) # El operador de multiplicación es "*" no "x". Además mensaje_format es un tipo de dato str y 2 es un tipo de dato int, y en Python no es posible operar con tipos de datos diferentes sin realizar previamente una conversión.
print(mensaje_fxtring) # La variable mensaje_fxtring no esta inicializada previamente en el programa, por lo tanto me arrojará un SyntaxError """