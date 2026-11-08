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
    print("13. Ver historial")
    print("0. Salir")


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no valida. Ingrese un numero.")


def ver_historial(historial):
    if not historial:
        print("El historial esta vacio.")
        return
    print("\n--- Historial de operaciones ---")
    for indice, operacion in enumerate(historial, start=1):
        print(f"{indice}. {operacion}")


def main():
    historial = []
    print("Bienvenido a la calculadora.")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            print("Hasta luego.")
            break

        if opcion == "13":
            ver_historial(historial)
            continue

        if opcion not in [str(numero) for numero in range(1, 13)]:
            print("Opcion no valida.")
            continue

        a = leer_numero("Primer numero: ")
        b = leer_numero("Segundo numero: ")

        try:
            if opcion == "1":
                resultado = operaciones.suma(a, b)
                descripcion = f"{a} + {b}"
            elif opcion == "2":
                resultado = operaciones.resta(a, b)
                descripcion = f"{a} - {b}"
            elif opcion == "3":
                resultado = operaciones.multiplicacion(a, b)
                descripcion = f"{a} * {b}"
            elif opcion == "4":
                resultado = operaciones.division(a, b)
                descripcion = f"{a} / {b}"
            elif opcion == "5":
                resultado = operaciones.potencia(a, b)
                descripcion = f"{a} ^ {b}"
            elif opcion == "6":
                resultado = operaciones.modulo(a, b)
                descripcion = f"{a} % {b}"
            elif opcion == "7":
                resultado = operaciones.raiz_cuadrada(a)
                descripcion = f"raiz({a})"
            elif opcion == "8":
                resultado = operaciones.porcentaje(a, b)
                descripcion = f"{b}% de {a}"
            elif opcion == "9":
                resultado = operaciones.valor_absoluto(a)
                descripcion = f"|{a}|"
            elif opcion == "10":
                resultado = operaciones.factorial(a)
                descripcion = f"{a}!"
            elif opcion == "11":
                resultado = operaciones.promedio([a, b])
                descripcion = f"promedio({a}, {b})"
            elif opcion == "12":
                resultado = operaciones.redondear(a, b)
                descripcion = f"redondear({a}, {b})"
            print("Resultado:", resultado)
            historial.append(f"{descripcion} = {resultado}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
