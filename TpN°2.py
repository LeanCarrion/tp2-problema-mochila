import os
from itertools import product


objetos = [
    (1,150,20),
    (2,325,40),
    (3,600,50),
    (4,805,36),
    (5,430,25),
    (6,1200,64),
    (7,770,54),
    (8,60,18),
    (9,930,46),
    (10,353,28)
]
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    input("\nPresione ENTER para continuar...")


def mostrar_objetos():
    print("\nOBJETOS DISPONIBLES")
    print("-" * 45)
    print("Obj\tVolumen\t\tValor")
    print("-" * 45)

    for obj in objetos:
        print(f"{obj[0]}\t{obj[1]}\t\t${obj[2]}")

    pausa()


def busqueda_exhaustiva():
    limpiar_pantalla()

    print("===================================")
    print("    BUSQUEDA EXHAUSTIVA")
    print("===================================")

    capacidad = int(input("Capacidad de la mochila (cm3): "))

    mejor_valor, mejor_combinacion = exhaustiva(capacidad, objetos)

    print(f"\nCapacidad elegida: {capacidad} cm3")
    print(f"Mejor combinación: {mejor_combinacion}")
    print(f"Mejor valor: ${mejor_valor}")

    pausa()

def exhaustiva(capacidad, objetos):
    mejor_valor = 0
    mejor_combinacion = []

    combinaciones = product([0, 1], repeat=len(objetos))

    for combinacion in combinaciones:

        volumen_total = 0
        valor_total = 0
        combinacion_actual = []

        for j in range(len(objetos)):

            if combinacion[j] == 1:
                volumen_total += objetos[j][1]
                valor_total += objetos[j][2]
                combinacion_actual.append(objetos[j][0])

        if volumen_total <= capacidad and valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_combinacion = combinacion_actual

    return mejor_valor, mejor_combinacion


def algoritmo_greedy():
    limpiar_pantalla()

    print("===================================")
    print("       ALGORITMO GREEDY")
    print("===================================")

    capacidad = int(input("Capacidad de la mochila (cm3): "))

    print("\nSeleccione el criterio:")
    print("1) Mejor Valor")
    print("2) Mejor Volumen")
    print("3) Mejor relación Valor/Volumen")

    opcion = input("\nOpción: ")

    # Validamos que la opción ingresada sea correcta (1, 2 o 3)
    if opcion in ["1", "2", "3"]:
        # Le pasamos la opción elegida a la función greedy
        combinacion, volumen, valor = greedy(capacidad, objetos, opcion)

        print("\n--- RESULTADO ---")
        print(f"Objetos seleccionados: {combinacion}")
        print(f"Volumen utilizado: {volumen} cm3")
        print(f"Valor total: ${valor}")
    else:
        print("\nOpción inválida.")

    pausa()

def greedy(capacidad, objetos, opcion):
    # Definimos el criterio de ordenamiento según la opción del menú
    if opcion == "1":
        # Opción 1: Mayor Valor primero (objeto[2] es el precio/valor)
        objetos_ordenados = sorted(objetos, key=lambda obj: obj[2], reverse=True)
    elif opcion == "2":
        # Opción 2: Menor Volumen primero (objeto[1] es el volumen)
        # Nota: En estrategia greedy de volumen, conviene priorizar los más chicos para que entren más.
        # Por eso aquí reverse=False (de menor a mayor volumen).
        objetos_ordenados = sorted(objetos, key=lambda obj: obj[1], reverse=False)
    else:
        # Opción 3: Mejor relación Valor/Volumen (objeto[2] / objeto[1])
        objetos_ordenados = sorted(objetos, key=lambda obj: obj[2] / obj[1], reverse=True)

    combinacion = []
    volumen = 0
    valor = 0

    for objeto in objetos_ordenados:
        numero = objeto[0]
        volumen_objeto = objeto[1]
        valor_objeto = objeto[2]

        if volumen + volumen_objeto <= capacidad:
            combinacion.append(numero)
            volumen += volumen_objeto
            valor += valor_objeto

    return combinacion, volumen, valor

def comparar():
    # Lista basada estrictamente en Pesos (grs.) y Valores ($)
    objetos2 = [
        (1, 1800, 72),  # (nroElemento, Peso, Valor)
        (2, 600, 36),
        (3, 1200, 60)
    ]
    limpiar_pantalla()

    print("===================================")
    print(" COMPARACIÓN DE ALGORITMOS")
    print("===================================")

    while True:
        opc = input("\nSeleccione el criterio para Greedy \n1: Mejor Valor, \n2: Mejor Peso, \n3: Mejor relación Valor/Peso\nOpción: ")
    
        # Verificamos si la opción ingresada está dentro de las válidas
        if opc in ["1", "2", "3"]:
            break  # Rompe el bucle while y continúa con el programa
        else:  # <-- Corregida la indentación (tenía un espacio de más)
            print("Opción inválida. Por favor, elija 1, 2 o 3.")

    print("\n>> Ejecutando ambos algoritmos para una capacidad de 3000 grs.")
    print(">> Comparando Grado de Optimización...")

    # Ejecución del Algoritmo Greedy con la opción elegida por el usuario
    combinacion, peso_greedy, valor = greedy(3000, objetos2, opc)

    # Definimos un texto dinámico para el título según la opción
    criterios = {"1": "Mejor Valor", "2": "Mejor Peso", "3": "Relación Valor/Peso"}
    print(f"\n--- RESULTADO GREEDY ({criterios[opc]}) ---")
    
    print(f"Objetos seleccionados: {combinacion}")
    print(f"Peso utilizado: {peso_greedy} grs.")
    print(f"Valor total: ${valor}")

    print("\n--- RESULTADO EXHAUSTIVA ---")
    mejor_valor, mejor_combinacion = exhaustiva(3000, objetos2)
    
    # Para la exhaustiva calculamos el peso usado sumando los objetos elegidos
    peso_exh = sum(obj[1] for obj in objetos2 if obj[0] in mejor_combinacion)
    
    print(f"Objetos seleccionados: {mejor_combinacion}")
    print(f"Peso utilizado: {peso_exh} grs.")
    print(f"Mejor valor obtenido: ${mejor_valor}")
    
    pausa()


def menu():

    while True:

        limpiar_pantalla()

        print("=" * 45)
        print("     TRABAJO PRÁCTICO N°2")
        print("      PROBLEMA DE LA MOCHILA")
        print("=" * 45)

        print("\n1) Mostrar objetos")
        print("2) Búsqueda Exhaustiva")
        print("3) Algoritmo Greedy")
        print("4) Comparar métodos")
        print("0) Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_objetos()

        elif opcion == "2":
            busqueda_exhaustiva()

        elif opcion == "3":
            algoritmo_greedy()

        elif opcion == "4":
            comparar()

        elif opcion == "0":
            print("\nHasta luego.")
            break

        else:
            print("\nOpción inválida.")
            pausa()


menu()