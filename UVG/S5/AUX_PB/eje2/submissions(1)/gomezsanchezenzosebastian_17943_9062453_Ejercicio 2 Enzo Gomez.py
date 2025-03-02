unidad = input("¿Temperatura en Fahrenheit o Celsius? (F/C): ")

if unidad == "F" or unidad == "C":
    temperatura = float(input("¿Cuál es la temperatura?: "))
    
    if unidad == "F":
        temperatura_celsius = (temperatura - 32) * 5 / 9
        print(f"La temperatura en Celsius es: {temperatura_celsius:.2f}°C")
    else:
        temperatura_celsius = temperatura
    
    if 0 <= temperatura_celsius <= 10:
        categoria = "Frío"
        vestimenta = "Chumpa, guantes, bufanda, pantalón adecuado"
    elif 11 <= temperatura_celsius <= 25:
        categoria = "Templado"
        vestimenta = "Ropa cómoda, sudadero, playera"
    elif 26 <= temperatura_celsius <= 40:
        categoria = "Cálido"
        vestimenta = "Pantaloneta, tenis, gorra, playera y bloqueador"
    else:
        categoria = "Calor extremo"
        vestimenta = " Traje de baño"
    
    print(f"Categoría: {categoria}")
    print(f"Sugerencia de vestimenta: {vestimenta}")
else:
    print("Entrada inválida. Intenta de nuevo.")
