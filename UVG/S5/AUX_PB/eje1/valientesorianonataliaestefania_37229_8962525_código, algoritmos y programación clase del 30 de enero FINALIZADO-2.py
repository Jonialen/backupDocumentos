#
#Universidad del Valle de Guatemala
#CC2005 Algoritmos y Prrogramación Básica
#Sección 50
#Nombre Natalia Valiente
#Carné: 25767
#
#Resolver antes de acción
ancho= float(input("Ingrese el ancho del sitio de construcción:"))
largo= float(input("Ingrese el largo del sitio de construcción"))
costo= float(input("Ingrese el costo de la madera para construcción:"))
distancia = float(input("Ingrese distancia máxima entre postes:"))
poste_1= float(input("Ingrese la cantidad de esquinas en el sitio de construcción"))
poste_2= float(input("Ingrese la cantidad del lados en el sitio de construcción"))

#Convertir perímetro 
perimetro= (ancho+largo)*2
print (perimetro)
Postes=perimetro/distancia

#Convertir costo
costo= perimetro*costo

#Cálculos
perimetro=(ancho+largo)*2
costo= (poste_1+poste_2*distancia)
metros= 2*(ancho+largo)
Postes_necesarios_para_construcción= (poste_1+poste_2)

#Resultados finales
print("Resultado de datos:")
print("El total de metros en área de construcción:", metros)
print("La cantidad de postes en el área de construcción es de:",Postes_necesarios_para_construcción)
print("costo total:",costo)






