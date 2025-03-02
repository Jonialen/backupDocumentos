import math

longitud = float(input("Ingrese la longitud del terreno (en metros): "))
ancho = float(input("Ingrese el ancho del terreno (en metros): "))
costo_metro = float(input("Ingrese el costo por metro lineal de madera: "))
distancia_postes = float(input("Ingrese la distancia máxima entre postes (en metros): "))

#calcular el perimetro del terreno

perimetro = 2*(longitud + ancho)

#Costo total de la madera

costo_total = perimetro * costo_metro

#Cantidad de postes

cantidad_postes = int(perimetro / distancia_postes)

print("El perimetro es ",perimetro)
print("El costo total es",costo_total)
print("La cantidad de postes es",cantidad_postes)