#------------------------------------------------------------------------------------------------
#Universidad el Valle de Guatemala
#QQ2017 Algoritmos y Programación Básica
#Sección 50
#Nombre: Diana Villatoro
#Carné: 241471
#-------------------------------------------------------------------------------------------------

#Datos del granjero
largo = float(input("ingrese longitud terreno: ")) #largo
ancho = float(input("ingrese ancho terreno: ")) #ancho
distancia = float(input("ingrese distancia entre postes: ")) #distancia
precio = float(input("ingrese precio madera: ")) #precio


#Calcular perímetro
perimetro = 2*(largo + ancho)
print("el perimetro es: ", perimetro, "metros")
 
#Calcular la cantidad de madera necesaria
madera_necesaria = perimetro
print("la madera necesaria es: ",perimetro, "metros de madera")


#Calcular los costos totales de madera
costo = perimetro * precio
print("el costo total es: ", costo, "quetzales")

#Calcular los postes necesarios
Postes_largo = (largo / distancia) 
Postes_ancho = (ancho / distancia)


#Resultados
print("el total de postes es: ", 2*int(Postes_largo + Postes_ancho))
