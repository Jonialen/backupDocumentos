#Universidad del Valle de Guatemala
#CC2005 Algoritmos y programacion basica
#2512295
#Estrella Cobos
#Solicitar los siguientes datos al usuario
longitud = float(input("Ingrese la longitud del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))
costo = float(input("Ingrese el costo por metro lineal de madera: "))
distancia= float(input("Ingrese ingrese la distancia maxima entre los postes: "))

#Calculos
#Longitud total de la cerca (perimetro del rectangulo)
perimetro = (2 * longitud + 2 * ancho)

longitud = perimetro

#Costo de madera por metro lineal
costo = (perimetro * costo)

#Cantidad total de postes
cantidad = int((longitud - distancia)/distancia)
total = (4 + 2 * distancia)


#Imprimir resultados
print("La longitud total de la cerca es: ", longitud)
print("El costo total de madera que necesitas es: ", costo)
print("La cantidad de postes requeridos es: ", distancia)
