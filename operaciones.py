import math


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


def raiz_cuadrada(numero):
    if numero < 0:
        return "No se puede calcular la raiz cuadrada de un numero negativo."
    return numero ** 0.5


def porcentaje(cantidad, porciento):
    return cantidad * porciento / 100


def valor_absoluto(numero):
    return abs(numero)


def factorial(numero):
    if numero < 0 or int(numero) != numero:
        return "El factorial solo se calcula para enteros no negativos."
    return math.factorial(int(numero))


def promedio(numeros):
    if not numeros:
        return "Se necesita al menos un numero para calcular el promedio."
    return sum(numeros) / len(numeros)


def redondear(numero, decimales):
    if decimales < 0 or int(decimales) != decimales:
        return "La cantidad de decimales debe ser un entero no negativo."
    return round(numero, int(decimales))
