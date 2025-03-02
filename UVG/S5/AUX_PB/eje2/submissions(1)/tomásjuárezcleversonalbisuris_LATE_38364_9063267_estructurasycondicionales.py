""""Instrucciones específicas:
Imagina que has decidido hacer un emocionante viaje alrededor del mundo. Pasarás por varios países, 
cada uno con su propio clima y cultura. Para aprovechar al máximo tus visitas, 
es fundamental planificar qué llevar en tu maleta y cómo vestirte para cada lugar que visitar. 
¡El clima será tu guía!. Tu misión es preparar tu ropa en función de la temperatura de cada lugar que vayas a conocer.
 Como sabemos que los climas pueden variar mucho de un lugar a otro,
   crearemos un sistema que te ayudará a determinar qué tipo de vestimenta debes llevar según la temperatura de cada destino.

Recuerda que en algunos paises te darán la temperatura en Fahrenheit por lo que
hay que hacer la conversión para que sea mucho más sencillo para ti verlo en grados celsius. El cálculo de la conversión es lo siguiente:
Fahrenheit Celsius: (°F - 32) x 5/9 =°C
Celsius a Fahrenheit: (°C x 9/5) + 32 =°F

La clasificación de tu vestimenta estará dado de la siguiente manera.

Si la temperatura está entre 0°C y 10°C, se clasifica como "Frío", debes sugerir llevar chumpa, guantes, bufanda, pantalon adecuado.
Si está entre 11°C y 25°C, se clasifica como "Templado", debes sugerir llevar ropa cómoda, un sudadero, playera.
Si está entre 26°C y 40°C, se clasifica como "Cálido", debes sugerir llevar pantaloneta, tenis, gorra, playera, bloqueador.
Si supera los 40°C, se clasifica como "Calor extremo", sugiere ir a una piscina, con traje de baño.


Ejemplo:
¿Quieres ingresar Fahrenheit o Celsius? (F/C): F
¿Cuál es la temperatura?: 77

*********************************************

La temperatura en Celcius es: 25 grados

Te sugiero llevar ropa cómoda, un sudadero, playera.

Instrucciones Parte 1: Análisis y Diseño
(20 pts) Análisis:
(05 pts) ¿Qué acciones debe poder hacer su programa? Enumérelas.
(05 pts) ¿Con qué va a trabajar (datos)? ¿Qué información debe pedir al usuario? Especifique qué variables va a utilizar e incluya el tipo de datos.
(05 pts) ¿Qué condiciones o restricciones debe tomar en cuenta? ¿Qué cálculos debe hacer? Incluya cualquier explicación de cómo diseñará su solución.
(05 pts) ¿Cómo va a ingresar el usuario sus acciones?
(40 pts) Diseño:
(40 pts) ¿Cuáles son los pasos para realizar el programa? El diagrama de flujo.
Fecha de entrega
Fecha límite para la entrega: 13 de febrero 8:30AM
********************************************************************************************************************************************************************"""

def convertir_fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def clasificar_temperatura(temperatura):
    if 0 <= temperatura <= 10:
        return "Frío", "Te sugiero llevar chumpa, guantes, bufanda, pantalón adecuado."
    elif 11 <= temperatura <= 25:
        return "Templado", "Te sugiero llevar ropa cómoda, un sudadero, playera."
    elif 26 <= temperatura <= 40:
        return "Cálido", "Te sugiero llevar pantaloneta, tenis, gorra, playera, bloqueador."
    elif temperatura > 40:
        return "Calor extremo", "Te sugiero ir a una piscina, con traje de baño."
    else:
        return None, "Temperatura no válida."

def main():
    unidad = input("¿Quieres ingresar Fahrenheit o Celsius? (F/C): ").upper()
    if unidad not in ['F', 'C']:
        print("Unidad no válida. Por favor ingresa 'F' o 'C'.")
        return
    
    try:
        temperatura = float(input("¿Cuál es la temperatura?: "))
    except ValueError:
        print("Por favor ingresa un número válido para la temperatura.")
        return
    
    if unidad == 'F':
        temperatura_celsius = convertir_fahrenheit_a_celsius(temperatura)
    else:
        temperatura_celsius = temperatura
    
    clasificacion, sugerencia = clasificar_temperatura(temperatura_celsius)
    
    if clasificacion:
        print(f"La temperatura en Celsius es: {temperatura_celsius:.2f} grados.")
        print(sugerencia)
    else:
        print("No se pudo clasificar la temperatura.")

if __name__ == "__main__":
    main()