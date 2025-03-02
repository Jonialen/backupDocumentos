# Crear las siguientes funciones e ingresar los datos para cada función.
longitud = float(input("Ingrese la longitud:"))
ancho = float(input("Ingrese la ancho:"))
costo_madera_x_m = int(input("Ingrese el costo de la madera por metro:"))
distancia_pos_t = float(input("Ingrese la distancia entre postes:"))


# Calcular el perímetro del terreno sumando las longitud y el ancho
perimetro = 2 * (longitud + ancho)

# Calcular el costo total de la madera multiplicando el perímetro por el costo de la madera por metro
costo_total = float(perimetro) * float(costo_madera_x_m)

# Calcular la cantidad total de postes necesarios
num_postes_longitud = int(longitud) / int(distancia_pos_t) + 1
num_postes_ancho = int(ancho) / int(distancia_pos_t) + 1
num_postes_total = 2 * (num_postes_longitud + num_postes_ancho)

# Mostrar en pantalla los resultados
print("Longitud de la cerca:", perimetro, "metros")
print("Costo total de la madera:", costo_total, "Quetzales")
print("Cantidad de postes necesarios:", num_postes_total)    