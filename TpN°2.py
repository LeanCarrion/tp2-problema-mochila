import os

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
    print("\n>> Aquí irá el algoritmo exhaustivo.")

    pausa()


def algoritmo_greedy():
    limpiar_pantalla()

    print("===================================")
    print("      ALGORITMO GREEDY")
    print("===================================")

    capacidad = int(input("Capacidad de la mochila (cm3): "))

    print("\nSeleccione el criterio:")

    print("1) Mayor valor")
    print("2) Menor volumen")
    print("3) Mejor relación Valor/Volumen")

    opcion = input("\nOpción: ")

    print(f"\nCapacidad: {capacidad} cm3")
    print(f"Criterio seleccionado: {opcion}")

    print("\n>> Aquí irá el algoritmo greedy.")

    pausa()


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


menu()