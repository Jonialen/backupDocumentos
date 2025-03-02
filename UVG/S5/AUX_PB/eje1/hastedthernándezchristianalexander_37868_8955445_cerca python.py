#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica 
#Sección 50
#Nombre: Christian Hastedt
#Carné: 25705
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Pedir datos al usuario
longitud = float(input("Ingrese la longitud del terreno"))
ancho = float(input("Ingrese el ancho del terreno"))
costo_metro = float(input("Ingrese el costo por metro lineal de su material"))
distancia_postes = float(input("Ingrese la distancia entre los postes de su cerca"))

#Calcular el perímetro
Perímetro = 2 * (longitud + ancho)

#Calcular el costo total
Costo_total = Perímetro * costo_metro

#Calcular la cantidad de postes
postes_longitud = int(longitud / distancia_postes) + 1
postes_ancho = int(ancho / distancia_postes) + 1
Cantidad_postes = (postes_longitud * 2) + (postes_ancho * 2) - 4

#Mostrar resultados
print("\nResultados: ")
print("El perímetro de la cerca es: ", Perímetro, "metros")
print("El costo total es: ", Costo_total, "dólares")
print("La cantidad de postes es: ", Cantidad_postes, "postes")