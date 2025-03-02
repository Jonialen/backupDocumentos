#------------------------------------------
#Universidad del valle de Guatemala
#CC2005 ALgoritmos y programación Básica
#Sección 50
#Nombre: Aarón García
#Carné: 251185
#------------------------------------------

#Programa
def calcular_cerca():
    perimetro = float(input("Ingrese el perímetro del terreno en metros: "))
    opciones_madera = {
        1: {"tipo": "Pino", "precio_metro": 15, "distancia_postes": 2.5},
        2: {"tipo": "Roble", "precio_metro": 25, "distancia_postes": 3},
        3: {"tipo": "Cedro", "precio_metro": 35, "distancia_postes": 3.5}
    }
    print("Opciones de madera:")
    for key, value in opciones_madera.items():
        print(f"{key}. {value['tipo']} - Precio por metro: ${value['precio_metro']} - Distancia entre postes: {value['distancia_postes']}m")
    eleccion = int(input("Seleccione el tipo de madera (1, 2 o 3): "))
    
    madera = opciones_madera.get(eleccion, opciones_madera[1])
    
    cantidad_postes = round(perimetro / madera["distancia_postes"])
    
    costo_total_madera = perimetro * madera["precio_metro"]
    
    print("\nPresupuesto:")
    print(f"Longitud total de la cerca: {perimetro} metros")
    print(f"Madera seleccionada: {madera['tipo']}")
    print(f"Cantidad de postes necesarios: {cantidad_postes}")
    print(f"Costo total de la madera: ${costo_total_madera:.2f}")

calcular_cerca()