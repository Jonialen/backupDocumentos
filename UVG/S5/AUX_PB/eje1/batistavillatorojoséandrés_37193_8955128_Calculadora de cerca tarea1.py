#---------------------------------------------------------------
#Universidad del Valle de Guatemala
#Algoritmos y programacion
#Seccion: 50
#Jose Batista
#Carne: 25269
#---------------------------------------------------------------
#solicitamos todos los datos necesarios para hacer los calculos
longitud_cerca = float(input("Ingrese la longitud de la cerca en metros: "))
ancho_cerca = float(input("Ingrese el ancho de la cerca en metros: "))
costo_metro = float(input("Ingrese el costo por metro de la cerca en quetzales: "))
distancia_entre_postes = float(input("Ingrese la distancia maxima posible entre postes en metros: ")) 
#hacemos las operaciones necesarias para obtener el perimetro, la cantidad de postes y el costo total
perimetro_cerca = 2 * longitud_cerca + 2 * ancho_cerca
cantidad_postes = longitud_cerca // distancia_entre_postes
costo_total = perimetro_cerca * costo_metro
#regresamos los datos que solicitaba quien use el programa
print("El costo total de la cerca es: Q", costo_total)
print ("La cantidad de postes necesarios es: ", cantidad_postes)
print ("el perimetro total de la cerca es: ", perimetro_cerca)