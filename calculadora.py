import operaciones


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")


def main():
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", operaciones.suma(a, b))
    elif opcion == "2":
        print("Resultado:", operaciones.resta(a, b))
    elif opcion == "3":
        print("Resultado:", operaciones.multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", operaciones.division(a, b))
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
