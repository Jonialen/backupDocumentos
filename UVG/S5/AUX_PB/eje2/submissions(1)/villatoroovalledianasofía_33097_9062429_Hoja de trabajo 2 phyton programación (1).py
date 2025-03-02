#----------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Nombre: Diana Villatoro
#Carné: 241471
#----------------------------------------------------------------------------------

#Ingresar la temperatura
temperatura = float(input("Ingrese temperatura: "))
escala = str(input("Ingrese la escala (celsius/fahrenheit): "))

#Convertir a Celsius si la temperatura está en Fahrenheit
if escala == "fahrenheit":
    temperatura = (temperatura - 32) * 5 / 9
elif escala == "celsius":
    temperatura = temperatura
else:
    print("Ingrese una escala válida")

#Definir clima y propuesta
if 0 <= temperatura <= 10:
    clima = "hace frío"
    propuesta = "podrías usar chumpa, guantes, bufanda y pantalón adecuado"
elif 11 <= temperatura <= 25:
    clima = "el clima es templado"
    propuesta = "podrías usar ropa comoda, sudadero y playera"
elif 26 <= temperatura <= 40:
    clima = "el clima es cálido"
    propuesta = "podrías usar pantaloneta, tenis, gorra y bloqueador solar"
elif temperatura > 40:
    clima = "hace calor extremo"
    propuesta = "podrías ir a la piscina y usar traje de baño"
else:
    clima = "opción no válida"
    propuesta ="intente de nuevo"
    

#resultados
print(f"temperatura en celsius: {temperatura:.1f}°C")
print(f"clima: {clima}")
print(f"propuesta: {propuesta}")