#-------------------------------------------
#Universidad del Valle de Guatemala 
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Miranda Rodriguez Parada
#Carné 251418
#13 de febrero de 2025
#-------------------------------------------

#Soliciar tipo de escala al usuario
escala = input("¿Desea ingresar Fahrenheit o Celsius (F/C)?: ")
#Solicitar al usuario la temperatura en números
tempt = float(input("Ingrese la temperatura del lugar a donde se dirige:"))
if escala == "F" or escala=="f":
    print("Escala en Fahrenheit (F)")
    tempt=(tempt-32)*5/9
else:
    print("Escala en Celsius (C)")


if 0 <= tempt and tempt <= 10:
    print("La temperatura es fría.") 
    print("Se le sugiere llevar al viaje: chumpa, guantes, bufanda, pantalon adecuado, manga larga y botas.")
elif 11 <= tempt and tempt<= 25:
    print("La temperatura es templada.")
    print("Se le sugiere llevar al viaje: ropa cómoda, un sudadero y playera.")
elif 26 <= tempt and tempt<= 40:
    print("La temperatura es cálida.")
    print("Se le sugiere llevar al viaje: pantaloneta o falda, tenis o un zapato descubierto, gorra, playera, bloqueador, lentes de sol.")
elif tempt>40:
    print("La temperatura es de calor extremo.")
    print("Se le sugiere: ir a una piscina en traje de baño y llevar bloqueador solar.")
else:
    print("La temperatura es inválida.")

