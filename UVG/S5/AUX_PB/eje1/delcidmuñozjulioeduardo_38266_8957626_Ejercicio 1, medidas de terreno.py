#...................................................................
# Universidad del Valle de Guatemala
# CC2005 Algoritmos Y Programación Básica
# Sección 50
# Nombre: Julio Eduardo del Cid Muñoz
# Carné: 251496
#--------------------------------------------------------------------

print("Buen dia querido cliente :), le ayudaremos a calcular el costo y tamaño de su cercado, disfrute del programa.")
import time
time.sleep(3)
print("\n")

print("Por favor no ingresar letras, solo valores numericos.")
Ancho= float(input("ingrese el ancho de su terreno en metros:"))
Longitud= float(input("ingrese la longitud o largo de su terreno en metros:"))
Coste_m_madera= float(input("ingrese en quetzales costo de metro lineal de madera:"))
Distancia_max_postes= float(input("ingrese la distancia maxima entre los postes:"))
Perimetro=((Ancho*2)+(Longitud*2)) #Variable para simplificar operaaciones

print("\n")
print("La longitudad total del terreno es:", Perimetro, "metros")
print("Costo total de la madera necesaria: Q", Coste_m_madera*Perimetro)
print("Cantidad de postes requerida:",int( Perimetro/Distancia_max_postes), "postes")
print("Tenga un muy buen dia ")