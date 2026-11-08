import operaciones


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Raíz cuadrada")
    print("8. Porcentaje")
    print("9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")


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
    elif opcion == "5":
        print("Resultado:", operaciones.potencia(a, b))
    elif opcion == "6":
        print("Resultado:", operaciones.modulo(a, b))
    elif opcion == "7":
        print("Resultado:", operaciones.raiz_cuadrada(a))
    elif opcion == "8":
        print("Resultado:", operaciones.porcentaje(a, b))
    elif opcion == "9":
        print("Resultado:", operaciones.valor_absoluto(a))
    elif opcion == "10":
        print("Resultado:", operaciones.factorial(a))
    elif opcion == "11":
        print("Resultado:", operaciones.promedio([a, b]))
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
