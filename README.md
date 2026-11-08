# Calculadora-2420

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Práctica](https://img.shields.io/badge/SIS2420B-Pr%C3%A1ctica%202-orange)
![Estado](https://img.shields.io/badge/estado-completado-brightgreen)

## Descripción

Calculadora de línea de comandos desarrollada en Python para la Práctica 2 de la asignatura SIS2420B. El proyecto parte de las operaciones básicas (suma, resta, multiplicación y división) e incorpora operaciones avanzadas, validaciones, mejoras en el menú e historial de operaciones. Cada funcionalidad se gestiona mediante un Issue en GitHub, registrando el avance con Git y documentando el proyecto con Markdown.

## Características

- Operaciones básicas: suma, resta, multiplicación y división.
- Operaciones avanzadas: potencia, módulo, raíz cuadrada, porcentaje, valor absoluto, factorial, promedio y redondeo.
- Validación de entradas no numéricas con reintento.
- Control de división y módulo con divisor cero.
- Menú organizado que se repite hasta que el usuario elige salir.
- Historial de operaciones con opción para verlo y limpiarlo.

## Tabla de operaciones y estados

| N.º | Operación | Descripción | Estado |
|-----|-----------|-------------|--------|
| - | Suma | Suma dos números | Completada |
| - | Resta | Resta dos números | Completada |
| - | Multiplicación | Multiplica dos números | Completada |
| - | División | Divide dos números y controla el divisor cero | Completada |
| 1 | Potencia | Calcula una base elevada a un exponente | Completada |
| 2 | Módulo | Obtiene el residuo de una división | Completada |
| 3 | Raíz cuadrada | Calcula la raíz cuadrada de un número no negativo | Completada |
| 4 | Porcentaje | Calcula un porcentaje de una cantidad | Completada |
| 5 | Valor absoluto | Obtiene el valor absoluto de un número | Completada |
| 6 | Factorial | Calcula el factorial de un entero no negativo | Completada |
| 7 | Promedio | Calcula el promedio de varios números | Completada |
| 8 | Redondeo | Redondea un número a la cantidad de decimales indicada | Completada |
| 9 | Validación de entradas | Controla entradas no numéricas | Completada |
| 10 | División por cero | Evita divisiones y módulos con divisor cero | Completada |
| 11 | Mejorar el menú | Organiza las operaciones en un menú claro | Completada |
| 12 | Repetir operaciones | Permite realizar varias operaciones sin reiniciar | Completada |
| 13 | Historial de operaciones | Almacena y muestra las operaciones realizadas | Completada |
| 14 | Limpiar historial | Permite borrar el historial de operaciones | Completada |
| 15 | Mejorar documentación | README con ejemplos de uso y presentación mejorada | Completada |

## Tecnologías

- Python 3
- Git
- GitHub
- Markdown

## Estructura del proyecto

```text
calculadora/
├── README.md
├── calculadora.py
└── operaciones.py
```

## Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/denpimen08-debug/Calculadora-2420.git
cd Calculadora-2420
```

2. Ejecutar el programa:

```bash
python calculadora.py
```

## Ejemplos de uso

Al iniciar, el programa muestra el menú principal:

```text
===== CALCULADORA =====
-- Operaciones basicas --
1. Suma
2. Resta
3. Multiplicacion
4. Division
-- Operaciones avanzadas --
5. Potencia
6. Modulo
7. Raiz cuadrada
8. Porcentaje
9. Valor absoluto
10. Factorial
11. Promedio
12. Redondeo
13. Ver historial
14. Limpiar historial
0. Salir
```

### Operación básica (suma)

```text
Seleccione una opcion: 1
Primer numero: 8
Segundo numero: 5
Resultado: 13.0
```

### Operación avanzada (potencia)

```text
Seleccione una opcion: 5
Primer numero: 2
Segundo numero: 10
Resultado: 1024.0
```

### Raíz cuadrada

```text
Seleccione una opcion: 7
Primer numero: 81
Segundo numero: 0
Resultado: 9.0
```

### Ver historial

```text
Seleccione una opcion: 13

--- Historial de operaciones ---
1. 8.0 + 5.0 = 13.0
2. 2.0 ^ 10.0 = 1024.0
3. raiz(81.0) = 9.0
```

### Limpiar historial

```text
Seleccione una opcion: 14
Historial limpiado.
```

### Salir

```text
Seleccione una opcion: 0
Hasta luego.
```

## Validaciones

- Las entradas no numéricas se rechazan y se solicita el valor nuevamente.
- La división y el módulo con divisor cero muestran un mensaje de error sin cerrar el programa.
- Una opción de menú inválida regresa al menú principal.

## Uso de GitHub Issues

Cada funcionalidad está registrada como un Issue en el repositorio, con título, descripción, lista de tareas (checklist), criterios de aceptación y asignada al estudiante. Cuando la funcionalidad está implementada y probada, el Issue correspondiente se cierra.

## Uso de Git

```bash
git status
git add .
git commit -m "feat: agregar operación de potencia"
git push
```

## Autor

Denzel Daniel Pimentel Ramil (denpimen08-debug)
