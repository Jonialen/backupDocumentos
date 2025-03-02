Temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de temperatura (°C o °F): ")

if unidad == "°C":
    temperatura_f = (Temperatura * 9/5) + 32
    print(f"{Temperatura} grados Celsius son {temperatura_f:.2f} grados Fahrenheit")
elif unidad == "°F":
    temperatura_c = (Temperatura - 32) * 5/9
    print(f"{Temperatura} grados Fahrenheit son {temperatura_c:.2f} grados Celsius")
else:
    print("Unidad de temperatura no válida. Ingrese '°C' o '°F'.")


def sugerencia_prenda(Temperatura, unidad):
    if 0 <= Temperatura <= 10:    
        return "Frío. Sugiero llevar chumpa, guantes, bufanda y pantalón adecuado."
    elif 11 <= Temperatura <= 25:
        return "Templado. Sugiero llevar ropa cómoda, un sudadero y playera."
    elif 26 <= Temperatura <= 40:
        return "Cálido. Sugiero llevar pantaloneta, tenis, gorra, playera y bloqueador."
    elif Temperatura > 40:
        return "Calor extremo. Sugiero ir a una piscina con traje de baño."
    else:
        return "Temperatura no válida."

print(sugerencia_prenda(Temperatura, unidad))