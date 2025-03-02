#---------------------------------------------------------------------------------------------------------------------------
#Universidad Del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Nombre: María Isabel Liquidano
#Carné: 251158
#----------------------------------------------------------------------------------------------------------------------------

#Calcular el perímetro de el terreno

longitud = float(input("Ingrese la longitud del terreno"))
ancho = float(input("Ingrese el ancho del terreno"))

perímetro = 2*(ancho + longitud)

print("El perímetro del terreno es: ", perímetro, "metros")

#Calcular el costo total

costo = float(input("Ingrese el costo por metro"))

Costo_total = perímetro * costo

print("El costo total es: ", Costo_total, "dólares")

#Calcular la cantidad de postes

distancia_entre_postes = float(input("Ingrese la distancia entre postes"))

cantidad_de_postes = int((perímetro / distancia_entre_postes))

print("La cantidad de postes es: ",cantidad_de_postes)


                 