def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "No se puede dividir entre 0."
    return a / b


def potencia(base, exponente):
    return base ** exponente


def modulo(dividendo, divisor):
    if divisor == 0:
        return "No se puede calcular el modulo con divisor cero."
    return dividendo % divisor
