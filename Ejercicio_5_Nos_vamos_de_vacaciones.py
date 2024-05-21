# Ejercicio: Planificación de maletas para vacaciones

""" 
Instrucciones:

Ayuda al usuario a planificar sus maletas para las vacaciones.
Pídele que introduzca la información de los objetos que deben
incluirse en diferentes maletas. Al final, muestra toda la información
de manera ordenada.
 1. Pide al usuario que introduzca la información para cada maleta:
		- accesorios
		- ropa
		- tecnología
		- zapatos & zapatillas.

2. Cuando el usuario haya terminado de introducir la información, le va a devolver
los resultados en 4 listas diferentes, con toda la información en minúsculas,
y el título de cada lista en mayúsculas:
		· LISTA ACCESORIOS
		· LISTA ROPA
		· LISTA TECNOLOGÍA
		· LISTA ZAPATOS & ZAPATILLAS
"""

#Solución creativa sin normalizar métodos
# Ejercicio de Planificación de Maletas para Vacaciones

# Solicitar al usuario que introduzca la información de las maletas
maleta_ropa = input("Introduce los objetos para la maleta de ropa, ¡OJO! NO SE OLVIDE DE NADA: ")
maleta_accesorios = input("Introduce los objetos para la maleta de accesorios, ¡OJO! NO SE OLVIDE DE NADA: ")
maleta_calzado = input("Introduce los objetos para la maleta de calzado, ¡OJO! NO SE OLVIDE DE NADA: ")
maleta_tecnologia = input("Introduce los objetos para la maleta de tecnología, ¡OJO! NO SE OLVIDE DE NADA: ")
maleta_aseo = input("Introduce los objetos para la maleta de aseo, ¡OJO! NO SE OLVIDE DE NADA: ")

# Imprimir un mensaje de confirmación
print("\n¡Maletas planificadas con éxito!")

# Mostrar al usuario la información ordenada y en minúsculas
print("\nResumen de Maletas:".upper())
print(f"Maleta de ropa:".upper(), maleta_ropa.lower())
print(f"MALETA DE ACCESORIOS: {maleta_accesorios.lower()}")
print(f"MALETA DE CALZADO: {maleta_calzado.lower()}")
print(f"MALETA DE TECNOLOGÍA: {maleta_tecnologia.lower()}")
print(f"MALETA DE ASEO: {maleta_aseo.lower()}")

print("\n¡Muchas gracias por utilizar nuestro programas!")


#..............................................

#Solución en una sola línea

# Ejercicio de Planificación de Maletas para Vacaciones

print("\nBienvenidos al planificador de vacaciones: Vacaciones Estupendas\n")

#Solicitar al usuario el destino
destino= input("\nIntroduce el destino de su viaje:\n")

# Solicitar al usuario que introduzca la información de las maletas


maleta_ropa = input("\nIntroduce los objetos para la maleta de ropa, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_accesorios = input("\nIntroduce los objetos para la maleta de accesorios, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_calzado = input("\nIntroduce los objetos para la maleta de calzado, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_aseo = input("\nIntroduce los objetos para la maleta de aseo, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_tecnologia = input("\nIntroduce los objetos para la maleta de tecnología, ¡OJO! NO SE OLVIDE DE NADA:\n")




print(f"\n¡Perfecto! Este es el resumen del contenido de tus  maletas de lo que llevas a tu estupendo viaje a "+destino+"\n"+"\n"+"Resumen de maletas:".upper()+"\n"+"\n"+"maleta de ropa:".upper(),maleta_ropa.lower()+"\n"+"\n"+"maleta de accesorios:".upper(),maleta_accesorios.lower ()+"\n"+"\n"+"maleta de calzado:".upper() ,maleta_calzado.lower() +"\n"+"\n"+"maleta de calzado:".upper(), maleta_calzado.lower() +"\n"+"\n"+"maleta de aseo:".upper(),maleta_aseo.lower() +"\n"+"\n"+ "maleta de tecnología:".upper(), maleta_tecnologia.lower() +"\n"+"\n" + "¡Maletas planificadas con éxito!"+"\n"+"\n"+"¡Muchas gracias por confiar en nosotros!"+"\n"+"\n"+"El equipo Haz el bien y no Mires a quien, le desea un buen viaje")

#-------------------------------------------------------------------

#Solución en varias líneas

# Ejercicio de Planificación de Maletas para Vacaciones

print("\nBienvenidos al planificador de vacaciones: Vacaciones Estupendas\n")

#Solicitar al usuario el destino
destino= input("\nIntroduce el destino de su viaje:\n")

# Solicitar al usuario que introduzca la información de las maletas


maleta_ropa = input("\nIntroduce los objetos para la maleta de ropa, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_accesorios = input("\nIntroduce los objetos para la maleta de accesorios, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_calzado = input("\nIntroduce los objetos para la maleta de calzado, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_aseo = input("\nIntroduce los objetos para la maleta de aseo, ¡OJO! NO SE OLVIDE DE NADA:\n")
maleta_tecnologia = input("\nIntroduce los objetos para la maleta de tecnología, ¡OJO! NO SE OLVIDE DE NADA:\n")


# Imprimir un mensaje de confirmación
print("\n¡Maletas planificadas con éxito!")

# Mostrar al usuario la información ordenada y en minúsculas
print("\nResumen de Maletas:\n".upper())
print(f"Maleta de ropa:".upper(), maleta_ropa.lower())
print(f"MALETA DE ACCESORIOS: {maleta_accesorios.lower()}")
print(f"MALETA DE CALZADO: {maleta_calzado.lower()}")
print(f"MALETA DE ASEO: {maleta_aseo.lower()}")
print(f"MALETA DE TECNOLOGÍA: {maleta_tecnologia.lower()}")

print("\n¡Muchas gracias por utilizar nuestro programa! El equipo haz el bien y no mires a quien, le desea un buen viaje")