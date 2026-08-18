import os
from itertools import product
#

bestmejor_valor = 1.3
bestmejor_combinacion = []
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
    for obj in objetos:
        print(f"{obj[0]}\t{obj[1]}\t\t${obj[2]}")

    pausa()


def busqueda_exhaustiva():
    limpiar_pantalla()

    print("===================================")
    print("    BUSQUEDA EXHAUSTIVA")
    print("===================================")

    capacidad = int(input("Capacidad de la mochila (cm3): "))

    print(f"\nCapacidad elegida: {capacidad} cm3")
    """print("\n>> Aquí irá el algoritmo exhaustivo.")"""
    # Implementar el algoritmo de búsqueda exhaustiva aquí lean
    bestmejor_valor, bestmejor_combinacion = exhaustiva(capacidad, objetos)
    print(f"\nMejor combinación: {bestmejor_combinacion}")
    print(f"Mejor valor: ${bestmejor_valor}")
    pausa()


def algoritmo_greedy():
    limpiar_pantalla()

    print("===================================")
    print("      ALGORITMO GREEDY")
    print("===================================")

    capacidad = int(input("Capacidad de la mochila (cm3): "))

    print("\nSeleccione el criterio:")

    #print("1) Mayor valor")
    #print("2) Menor volumen")
    print("3) Mejor relación Valor/Volumen")

    opcion = input("\nOpción: ")

    print(f"\nCapacidad: {capacidad} cm3")
    print(f"Criterio seleccionado: {opcion}")

    if opcion == "3":
        combinacion, volumen, valor = greedy(capacidad, objetos)

        print("\n--- RESULTADO ---")
        print(f"Objetos seleccionados: {combinacion}")
        print(f"Volumen utilizado: {volumen} cm3")
        print(f"Valor total: ${valor}")
    else:
        print("\nOpción inválida.")
    pausa()

def greedy(capacidad, objetos):

    # Ordenamos los objetos según su relación valor/volumen
    objetos_ordenados = sorted(
        objetos,
        key=lambda x: x[2] / x[1],
        reverse=True
    )

    combinacion = []
    volumen = 0
    valor = 0

    for objeto in objetos_ordenados: 

        numero = objeto[0]
        volumen_objeto = objeto[1]
        valor_objeto = objeto[2]

        # Verificamos si el objeto entra en la mochila
        if volumen + volumen_objeto <= capacidad:

            combinacion.append(numero)
            volumen += volumen_objeto
            valor += valor_objeto

    return combinacion, volumen, valor

def comparar():
    limpiar_pantalla()

    print("===================================")
    print(" COMPARACIÓN DE ALGORITMOS")
    print("===================================")

    print("\n>> Aquí se ejecutarán ambos algoritmos")
    print(">> y se compararán los resultados.")

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


def exhaustiva(capacidad, objetos):
    n = len(objetos)

    mejor_valor = 0
    mejor_combinacion = []

    # Generamos todas las combinaciones posibles
    combinaciones = product([0, 1], repeat=n)

    for combinacion in combinaciones:
        volumen_total = 0
        valor_total = 0
        combinacion_actual = []

        # Recorremos los objetos
        for j in range(n):

            # Si el valor es 1, llevamos ese objeto
            if combinacion[j] == 1:
                volumen_total += objetos[j][1]
                valor_total += objetos[j][2]
                combinacion_actual.append(objetos[j][0])

        # Verificamos si entra y si mejora la solución
        if volumen_total <= capacidad and valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_combinacion = combinacion_actual

    return mejor_valor, mejor_combinacion

menu()