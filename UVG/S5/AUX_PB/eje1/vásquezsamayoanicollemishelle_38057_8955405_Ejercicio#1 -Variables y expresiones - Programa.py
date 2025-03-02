#Universidad Del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Nombre: Nicolle Vásquez
#Carné: 251181

#Datos obtenidos del usuario
Longitud = float(input("Por favor ingrese la longitud de su terreno: "))
Ancho = float(input("Por favor ingrese el ancho de su terreno: "))
CostoMadera = float(input("Por favor ingrese el costo de la madera: "))
CantidadPostes = float(input("Por favor ingrese la cantidad requerida entre los postes: "))

#Perímetro del terreno
Perimetro = (2 * Longitud + 2 * Ancho)

#Longitud total de la cerca
LongitudCerca = Perimetro

#Costo total de la madera
CostoTotalMadera = LongitudCerca * CostoMadera

#Numero total de postes
NumLadosPostes = int(Longitud - CantidadPostes)/CantidadPostes
NumPostesTotales = int(4 + 2 * NumLadosPostes)

#Salida al ejecutar
print("La longitud tota de la cerca es metros", LongitudCerca)
print("El costo total de la madera es quetzales", CostoTotalMadera)
print("La cantidad de postes necesarios para el terreno es", NumPostesTotales)