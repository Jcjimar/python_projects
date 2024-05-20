""" 
Crea 3 variables, una de tipo número que represente tu  edad, otra de tipo string que represente tu nombre y otra  de tipo decimal que represente tu peso.
Imprime estas variables utilizando la función print() 
"""
nombre = "Jose Carlos"
edad=35
peso= 70.5
altura= 1.72

imc= peso / (altura**2)

print("Mi nombre es " + nombre + " tengo " + str(edad)+    " años "+" mi peso es de  "+ str(peso)+" kg "+ " y mi altura es "  +str(altura)+" mts "+ " y mi indice de masa        muscular es " + str(imc))
