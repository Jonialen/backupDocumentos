#Universidad Del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica
#Seccción 50
#Nombre: Melania Espinoza
#Carné: 25905

#input
Temperatura=float(input("Cual es la temperatura actual: "))
Unidad=str(input("¿La temperatura esta en grados Celsius (ingrese 1) o grados Fahrenheit (ingrese 2)? "))

#output
if Unidad == "2":
    resultado=(Temperatura - 32)*5/9
    print("La temperatura en Celsius es: ",resultado)
    if Temperatura>40:
        print("El clima se clasifica como calor extremo. Te sugiero ir a una piscina, con traje de baño.")
    elif Temperatura>25:
        print("El clima se clasifica como cálido. Te sugiero llevar pantaloneta, tenis, gorra, playera, bloqueador")
    elif Temperatura>10:
        print("El clima se clasifica como templado. Te sugiero llevar ropa cómoda, un sudadero, playera")
    else:
        print("El clima se clasifica como frío. Te sugiero llevar chumpa, guantes, bufanda, pantalón adecuado")
elif Unidad=="1":
    if Temperatura>40:
        print("El clima se clasifica como calor extremo. Te sugiero ir a una piscina, con traje de baño.")
    elif Temperatura>25:
        print("El clima se clasifica como cálido. Te sugiero llevar pantaloneta, tenis, gorra, playera, bloqueador")
    elif Temperatura>10:
        print("El clima se clasifica como templado. Te sugiero llevar ropa cómoda, un sudadero, playera")
    else:
        print("El clima se clasifica como frío. Te sugiero llevar chumpa, guantes, bufanda, pantalón adecuado")
else:
    print("Ingrese una opcion valida")
        
print("¡Que tengas lindo viaje!")


