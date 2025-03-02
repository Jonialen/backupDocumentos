ancho = float(input("Ingrese el ancho de su terreno: "))
largo = float(input("Ingrese el largo de su terreno: "))
costom = float(input("Ingrese el costo de madera por metro: "))
distanciap = float(input("Ingrese la distancia que debe existir entre sus postes en metros: "))

print("\n")

longitudc = (ancho + ancho + largo + largo)
costototalm = (costom * longitudc)
totalp = (int(longitudc // distanciap))

print("La longitud total de su cerca debe ser de: ", longitudc, "m")
print("El costo total de la madera que va a utilizar es de: ", costototalm, "Q")
print("El total de postes que necesita es de: ", totalp, " postes")


