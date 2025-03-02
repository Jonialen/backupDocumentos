#Universidad del Valle
#Algoritmos y Programación Básica
#Sección 50
#Kimberly Urrutia
#25704

#Solicitar datos al usuario
longitud = float(input("Ingrese la longitud del terreno en metros: "))
ancho= float(input("Ingrese el ancho del terreno en metros: "))
Costo_madera= float(input("Ingrese el costo por metro de madera: "))
Distancia_postes= float(input("Ingrese la distancia máxima entre postes: "))

#Calcular el perímetro del terreno
perímetro = (longitud * ancho)

#Calcular el costo total de la madera
costo_total = perímetro * Costo_madera

#Calcular la cantidad de postes necesarios
#Calcular la cantidad de postes por lado
postes_lado_longitud =(longitud / Distancia_postes)
postes_lado_ancho =(ancho / Distancia_postes)

#Calcular el total de postes
postes_total = 2*(postes_lado_longitud + postes_lado_ancho)

#Mostrar los resultados
print("Resultados:")
print("Longitud total de la cerca (perímetro):" ,perímetro, "metros")
print("Costo total de la madera: $",costo_total,)
print("Cantidad total de postes necesarios:" ,postes_total,)