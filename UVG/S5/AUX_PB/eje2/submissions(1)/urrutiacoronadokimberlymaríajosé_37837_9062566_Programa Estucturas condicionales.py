#Universidad del Valle
#Algoritmos y Programación Básica
#Sección 50
#Kimberly Urrutia
#Carnét 25704
print("Bienvenido a tu closet personalizado.")
unidad = input("¿En qué unidad ingresará la temperatura? (C para Celsius, F para Fahrenheit): ")
if unidad == "F" or unidad =="f":
    temperatura = float(input("Ingrese la temperatura del destino en Fahrenheit: "))
    temperatura = (temperatura-32)*5/9
    print("Temperatura convertida a Celsius" +str(temperatura)+"°C")
elif unidad =="C" or unidad =="c":
    temperatura = float(input("Ingrese la temperatura del destino en Celsius: "))
else:
    print("Unidad no válida. Por favor, ingrese C o F únicamente, en mayúsculas.")


if temperatura <=10:
    print("Usted se encontrará con un clima frío, se recomienda usar chumpa, guantes, bufanda y un pantalón adecuado.")
elif 11 <= temperatura <=25:
    print("Usted se encontrará con un clima templado, se recomienda usar ropa cómoda, sudadero, y playera.")
elif 26 <= temperatura <=40:
    print("Usted se encontrará con un clima cálido, se recomienda usar pantaloneta, tenis, gorra, playera y bloqueador.")
elif 40<temperatura :
    print("Usted se encuentra con un clima de calor extremo, se recomienda usar traje de baño e ir a una piscina.")
else:
    print("Ingrese un número válido")
        