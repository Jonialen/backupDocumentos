#Algoritmos y programacion
#Gabriel Busto
#Carnet: 251286
#Seccion:50
L= float(input("Ingrese la longitud del terreno " ))
A = float(input("Ingrese el ancho del terreno " ))
Costo = float(input("Ingrese el costo por metro " ))
D = float(input("Ingrese la distancia entre postes "))

p = (2 * (L + A))
print("Perimetro: ", p)

Costo_total = p * Costo
print("El costo total es: ", Costo_total)

Po = (p/D)
print("La cantidad de postes son: ", int(Po) )
