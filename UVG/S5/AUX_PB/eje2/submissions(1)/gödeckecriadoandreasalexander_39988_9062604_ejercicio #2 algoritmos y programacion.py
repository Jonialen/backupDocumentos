#Programa: Clasificación de Temperatura y Recomendación de Vestimenta
#Autor: Andreas Godecke
#Curso: CC2005 - Algoritmos y Programación Básica
#Descripción: Este programa solicita una temperatura en Fahrenheit o Celsius, luego lo convierte si es necesario y nos da una recomendacion de vestimenta en base a la temperatura.


def convertir_a_celsius(f):
    return (f - 32) * 5/9

# Pedir unidad de temperatura
unidad = input("¿Quieres ingresar Fahrenheit o Celsius? (F/C): ").strip().upper()

# Pedir la temperatura
temp = float(input("¿Cuál es la temperatura?: "))

# Convertir si es necesario
if unidad == "F":
    temp = convertir_a_celsius(temp)

# Clasificar y recomendar vestimenta
if 0 <= temp <= 10:
    recomendacion = "Frío: Lleva chumpa, guantes, bufanda y pantalón adecuado."
elif 11 <= temp <= 25:
    recomendacion = "Templado: Lleva ropa cómoda, sudadero y playera."
elif 26 <= temp <= 40:
    recomendacion = "Cálido: Lleva pantaloneta, tenis, gorra, playera y bloqueador."
else:
    recomendacion = "Calor extremo: Ve a una piscina con traje de baño."

# Mostrar resultado
print(f"La temperatura en Celsius es: {temp:.2f} grados")
print(recomendacion)

