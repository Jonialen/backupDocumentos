#--------------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Nombre: Daniela Alivat
#Carné: 251500
#--------------------------------------------------------------------------------------------
unidad = str(input("Ingrese la unidad de su temperatura (F/C): "))
temperatura = float(input("Ingrese temperatura: "))

# ¿Es Fahrenheit?
if unidad == "F":
    temperatura = (temperatura - 32) * 5 / 9
elif unidad != "C":
    print("Ingrese unidad válida")
    exit()
    
# Recomendación de vestimenta según el clima ingresado
if 0 <= temperatura <= 10:
    clima = "Hace frío"
    recomendacion = "Llevar chumpa, guantes, bufanda, pantalón adecuado."
elif 11 <= temperatura <= 25:
    clima = "Está templado"
    recomendacion = "Llevar ropa cómoda, un sudadero, playera."
elif 26 <= temperatura <= 40:
    clima = "Esta cálido"
    recomendacion = "Llevar pantaloneta, tenis, gorra, playera, bloqueador."
elif temperatura > 40:
    clima = "ALERTA DE CALOR EXTREMO"
    recomendacion = "Debes ir a la piscina y llevar traje de baño."
else:
    clima = "No valido"
    recomendacion = "intentar de nuevo"
    
# Mostrar resultados
print(f"temperatura en C: {temperatura:.2f}°C")
print(f"clima: {clima}")
print(f"recomendacion: {recomendacion}")
    