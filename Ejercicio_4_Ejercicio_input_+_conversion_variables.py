""" 
Crear un programa que le solicite al usuario sus datos para renovarse el DNI. Una vez que el usuario ha introducido los datos, el programa se los mostrará a modo de resumen
"""
nombre_completo= input("\nIngrese su nombre:\n")
primer_apellido=input("\nIngrese su primer apellido:\n")
segundo_apellido=input("\nIngrese su segundo apellido:\n")
numero_DNI_con_letra=  str(input("\nIngrese su número de DNI con Letra:\n"))
print(f"Hola, {nombre_completo} {primer_apellido} {segundo_apellido} con DNI número {numero_DNI_con_letra}, verifique que sus datos están correctos antes de continuar con el proceso de renovación de su DNI ")
print(f"Hola, \n{nombre_completo}\n{primer_apellido}\n{segundo_apellido}\ncon DNI número\n{numero_DNI_con_letra}\nverifique que sus datos están correctos antes de continuar con el proceso de renovación de su DNI ")