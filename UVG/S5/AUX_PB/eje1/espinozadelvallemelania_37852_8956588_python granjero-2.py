"""
Universidad Del Valle de Guatemala
CC2005 Algoritmos y Programación Básica
Seccción 50
Nombre: Melania Espinoza
Carné: 25905
"""

#Colocar datos que ya se saben
#Input
print ("Ingresar información necesaria")
longitud = int (input("Ingrese longitud:"))
ancho = int (input("Ingrese ancho:"))
costo = int(input ("Ingrese costo de madera:"))
distancia =int(input("Ingrese distancia entre postes:"))

perimetro = float (2*longitud + 2*ancho)
total_madera = float (perimetro * costo)
postes = int (perimetro / distancia)

print ("\n")

#Output
print ("Longitud de terreno: ", longitud, "metros")
print ("Ancho del terreno: ", ancho, "metros")
print ("Costo de madera: ", costo, "quetzales")
print ("Distancia entre postes: ", distancia, "metros")
metros= float (longitud)
metros = float (ancho)
quetzales = float (costo)
metros = float (distancia)

print  ("\n")

#Cálculemos la longitud total de la cerca:
print ("Perimetro del terreno: ", perimetro, "metros")

#calcular el costo total de madera necesaria para la cerca:
print ("costo total de madera es:", total_madera, "quetzales")

#Cálculemos la cantidad de postes necesarios
print ("la cantidad de postes es:", postes, "postes")






