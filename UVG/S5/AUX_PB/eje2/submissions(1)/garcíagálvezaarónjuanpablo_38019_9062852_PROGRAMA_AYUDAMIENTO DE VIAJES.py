#------------------------------------------
#Universidad del valle de Guatemala
#CC2005 ALgoritmos y programación Básica
#Sección 50
#Nombre: Aarón García
#Carné: 251185
#------------------------------------------

#Programa
viajes = input("¿Qué visitaras esta vez?: ")
temperatura = float(input("Coloca la temperatura del lugar: "))
Tem = input("¿Tú temperatura es en fahrenheit(1) o Celsius(2)?: ")

#Definir clima
if Tem == "1" :
    celsius = (temperatura - 32) * 5/9
    print(f"La temperatura en celsius es {celsius} °C")
elif Tem == "2" :
    celsius = temperatura
    print("La temperatura en fahrenheit es {(celsius * 9/5) + 32:c.2f} °F")
else:
    print("Opcion no valida")
#Conversion de clima
if    0 <= celsius <= 10:
    clima = "Hace frio"
    propuesta = "Podrias utilizar sudadera, gorro, guantes y pantalon."
elif 11 <= celsius <= 25:
    clima = "El clima estara templado"
    propuesta = "Chaqueta ligera, camiseta, jeans, zapatillas."
elif 26 <= celsius <= 40:
    clima = "El clima sera calido"
    propuesta = "Camiseta, shorts, sandalias, gorra."
elif celsius > 40:
    clima = "Calor extremo"
    propuesta = "Puedes ir a una psicina y usar traje de baño"
else:
    clima = "No es valida"
    propuesta = "Vuelva a intentarlo"
#Respuestas del programa
print(f"\nDestino: {viajes}")
print(f"Temperatura en celsius: {celsius: .2f} °C")
print(f"Clima: {clima}")
print(f"propuesta: {propuesta}")