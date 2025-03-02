#
#Universidad Del Valle de Guateamala
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Nombre: Jhordy López
#Carné: 251403
#

temperatura = str(input("Quiere ingresar temperatura Fahrenheit o Celsius? (F/C):"))
valort = float(input("Cual es la tempertura?:"))
if temperatura == "F" or temperatura =="f":
    valort = (valort - 32) * 5/9  
    print("la temperatura en Celsius es:", valort)
elif temperatura == "C" or temperatura =="c":
    valort = valort
    print("la temperatura en Celsius es:", valort)
else:
    print("error ingrese una escala correcta")
    exit()
    
if 0 > valort:
    print("Clima demasiado frio, no hay recomendaciones.")
elif 0 <= valort <= 10:
    print("Clima frio, se recomienda llevar chumpa, guantes, bufanda y pantalon adecuado.")
elif 11 <= valort <= 25:
    print("Clima templado, se recomienda llevar ropa comoda, sudadero y playera.")
elif 26 <= valort <= 40:
    print("Clima calido, se recomienda llevar pantaloneta, tenis, gorra, playera y bloqueador.")
else:
    print("Calor extremo, se recomienda ir a una piscina con traje de bano.")
