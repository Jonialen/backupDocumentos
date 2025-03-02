#------------------------------------------------------------------------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Nombre: Sebastián Pivaral Rodríguez
#Carné: 25012
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Input
ancho = float(input("Ingresar ancho "))
longitud = float(input("Ingresar longitud "))
distancia_postes = float(input("Ingresar distancia entre postes "))
costo_madera = float(input("Ingresar costo por metro de madera "))

print("\n")

#Operaciones
Perímetro = 2*(ancho + longitud)
Costo_Total = Perímetro*costo_madera
Postes_ancho = int((ancho/distancia_postes)+1)
Postes_largo = int((longitud/distancia_postes)+1)
Número_Postes = Postes_ancho + Postes_largo

#Output
print("Perímetro: ", round(Perímetro,2), "metros")
print("Costo Total: ", round(Costo_Total,2), "quetzales")
print("Número de Postes: ", Número_Postes)