#--------------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#QQ2017 Algoritmos y Programación Básica
#Sección 50
#Nombre: Daniela Alivat
#Carné: 251500
#--------------------------------------------------------------------------------------------
#Datos de terreno
longitud = float(input("Ingrese longitud:"))
ancho = float(input("Ingrese ancho: "))
costo_madera = float(input("Ingrese costo de madera por metro: "))
distancia_postes = float(input("Ingrese distancia máxima entre postes: "))

#datos
print("\n")
print("Información:")

#Calcular el perímetro
perimetro = 2*(longitud+ancho)
print("Perímetro: ", perimetro, "m")

#Calcular la madera necesaria
print("La madera necesaria es: ", perimetro, "m")

#Calcular costo total de madera
costo_total_de_madera = perimetro*costo_madera
print("Costo total de madera: ", costo_total_de_madera, "pesos")

#Cantidad de postes
postes_largos = (longitud/distancia_postes)-1
postes_cortos = (ancho/distancia_postes)-1
total = 4+2*(postes_largos+postes_cortos)
print("Cantidad de postes: ", total)
