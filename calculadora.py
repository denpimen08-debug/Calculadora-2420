import operaciones


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("-- Operaciones basicas --")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("-- Operaciones avanzadas --")
    print("5. Potencia")
    print("6. Modulo")
    print("7. Raiz cuadrada")
    print("8. Porcentaje")
    print("9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")
    print("12. Redondeo")
    print("0. Salir")


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no valida. Ingrese un numero.")


def main():
    print("Bienvenido a la calculadora.")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            print("Hasta luego.")
            break

        if opcion not in [str(numero) for numero in range(1, 13)]:
            print("Opcion no valida.")
            continue

        a = leer_numero("Primer numero: ")
        b = leer_numero("Segundo numero: ")

        try:
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
            elif opcion == "12":
                print("Resultado:", operaciones.redondear(a, b))
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
