#algoritmos y programacion
#Gabriel Busto
#251286
#seccion 50

tipotemp = input("Vas a ingresar tu temperatura en Fahrenheit o Celsius (F o C)? ").upper()
temp = float(input("¿Cuál es su temperatura? "))

if tipotemp == "F" or tipotemp=="f":
    temp = (temp - 32) * 5 / 9
elif tipotemp == "C" or tipotemp=="c":
    temp=temp
else:
    print("Error, ingrese una opción válida")
if temp<0:
    ropa = "Opcion no valida"
elif 0 <= temp <= 10:
    ropa = "Llevar chumpa, guantes, bufanda, pantalón adecuado."
elif 11 <= temp <= 25:
    ropa = "Llevar ropa cómoda, un sudadero, playera."
elif 26 <= temp <= 40:
    ropa = "Llevar pantaloneta, tenis, gorra, playera, bloqueador."
else:
    ropa = "Ir a una piscina, con traje de baño."
    
print("La temperatura en Celsius es: " + str(round(temp,2)))
print("Te sugiero: " + ropa)
