#-----------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2002 Algoritmos y Programación Básica
#Sección 50
#Nombre: Ely Sofía Sandoval
#Carné: 25723
#-----------------------------------------------------------------------------------------

longitud=float(input("Ingrese la longitud del terreno en metros: "))
ancho=float(input("Ingrese el ancho del terreno en metros: "))
perimetro=2*longitud+2*ancho
print("El perímetro del terreno es", perimetro, "metros")

preciomadera=float(input("Ingrese el precio por metro de madera: "))
preciototal=perimetro*preciomadera
print("El precio total del cerco es", preciototal, "quetzales")

distanciaposte=float(input("Ingresar distancia máxima en metros entre postes: "))
divisiona=longitud/distanciaposte
divisionb=ancho/distanciaposte

#Se coloca una condicional, dado a el total de postes no puede ser menor a 4, y para que esta condición se cumpla el valor mínimo de las divisiones debe ser 1
if divisiona>=1:
    a=float(2*divisiona)
else:
    b=0
if divisionb>=1:
    b=float(2*divisionb)
else:
    b=0

totalposte=int(a+b)
print("El número total de postes es:", totalposte)
