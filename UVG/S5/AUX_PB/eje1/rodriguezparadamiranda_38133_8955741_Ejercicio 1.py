#-------------------------------------------
#Universidad del Valle de Guatemala 
#057ccc Algoritmos y Programación Básica
#Sección 50
#Miranda Rodriguez
#carné 251418
#-------------------------------------------

#Solicitar datos al usuario
ancho_terreno = float(input("ingrese el ancho del terreno: "))
longitud_terreno = float(input("Ingrese la longitud del terreno: "))
costo_madera = float(input("Ingrese el costo de la madera: "))
distancia_postes = float(input("Ingrese distancia la máxima entre los postes: "))
#Calcular perímetro, costos y cantidad postes
perimetro_terreno = 2*(ancho_terreno+longitud_terreno)
costo_total = costo_madera*perimetro_terreno
cantidad_postes = perimetro_terreno/distancia_postes
#Mostrar resultados al usuario
print("Este es el perimetro del terreno:", perimetro_terreno)
print("Este es el costo por metro de la madera:", costo_total)
print("Esta es la cantidad de postes necesarios:", cantidad_postes)





