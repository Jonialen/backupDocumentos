#Universidad del Valle de Guatemala
#CC2005 Algoritmos y programación básica
#25081
#Lucía Juracán


#Datos del usuario
nombre = input("Ingrese su nombre ")
ancho = input("Ingrese el ancho del terreno ")
largo = input("Ingrese el largo del terreno ")
postes1 = input("Ingrese la cantidad de esquinas del terreno ")
postes2 = input("Ingrese la cantidad lados del terreno ")
costo = input("Ingrese el costo por metros ")

#Convertir entradas a enteros
ancho = int(ancho)
largo = int(largo)
postes1 = int(postes1)
postes2 = int(postes2)
costo = float(costo)

#Cálculos
Metros = 2 * (ancho + largo)
CostoTotal = costo * Metros
PostesTotales = postes1 + postes2

#Mostrar en pantalla
print("\nResultados:")
print("Los metros totales del terreno son: ",Metros)
print("El costo total es: ",CostoTotal)
print("La cantidad de postes es de : ",PostesTotales)
