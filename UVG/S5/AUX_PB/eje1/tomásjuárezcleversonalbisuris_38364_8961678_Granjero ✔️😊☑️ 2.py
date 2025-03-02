"""
Desarrolo de un programa para calcular los requerimientos de una cerca para un
terreno rectangular.
Calcula el perímetro, costo de la madera y cantidad de postes necesarios.
Autor: Clever
Fecha: 2025-30-01
"""

import math

def main():
    # pedir los  datos al usuario
    longitud = float(input("Ingrese la longitud del terreno en metros: "))
    ancho = float(input("Ingrese el ancho del terreno en metros: "))
    costo_por_metro = float(input("Ingrese el costo por metro lineal de madera: "))
    distancia_postes = float(input("Ingrese la distancia máxima entre postes en metros: "))

    # Calcular perímetro y costo total de la madera
    perimetro = 2 * (longitud + ancho)
    costo_total = perimetro * costo_por_metro

    # Calcular cantidad de postes por lado
    postes_por_largo = math.ceil(longitud / distancia_postes) + 1
    postes_por_ancho = math.ceil(ancho / distancia_postes) + 1

    # Calcular total de postes restando las esquinas duplicadas
    total_postes = 2 * (postes_por_largo + postes_por_ancho) - 4

    # Mostrar resultados
    print("\nResultados:")
    print(f"Perímetro requerido: {perimetro:.2f} metros")
    print(f"Costo total de la madera: Q{costo_total:.2f}")
    print(f"Cantidad de postes necesarios: {total_postes}")

if __name__ == "__main__":
    main()