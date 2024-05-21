""" 
Crea un programa que simule un gestor de información de un diario. Para ello el programa deberá solicitar al usuario que introduzca la fecha con formato DÍA DE LA SEMAMA + día del mes (en número) + mes. Además en una nueva instrucción le pedirá al usuario que introduzca la hora y en una nueva instrucción le pedirá el texto de la entrada que desea almacenar. Al finalizar el programa mostrará al usuario toda la información con el siguiente formato: 

• fecha string en mayúscula 

• hora string

• texto de la entrada del diario en minúscula.
"""
#Crea un programa que simule un gestor de información de un diario

#Bienvenida al gestor de información del diario
print("\nBienvenid@ a tu diario\n")

#Pedimos al usuario que introduzca la fecha del registro
dia_de_la_semana= input("\nIntrouzca el día de la semana\n")
dia_mes=int(input("\nIndique el día actual de mes en formato número\n"))
mes=input("\nIntrouzca el mes en el que estamos\n")
hora=input("\nIntroduzca la hora con el siguiente formato '09:35' o '21:47'\n")
texto=input("\nEscriba el texto de su diario\n")

#Imprimimimos

print(f"\n"+dia_de_la_semana.upper( )+", "+str(dia_mes)+" de "+mes.upper(),"a   las "+ str(hora)+"\n-------------------------------\n"+texto.lower()+"\n"+"\n" +"¡Muchas gracias por confiar en nosotros!"+"\n"+"\n"+"El equipo Haz el bien y  no Mires a quien, desea que siga registrando su diario con nuestra aplicación")
