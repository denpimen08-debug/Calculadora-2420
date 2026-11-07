# Calculadora-2420

## Descripción

Calculadora de línea de comandos desarrollada en Python para la Práctica 2 de la asignatura SIS2420B. El proyecto parte de las operaciones básicas (suma, resta, multiplicación y división) y se ampliará incorporando nuevas operaciones, validaciones y mejoras. Cada nueva funcionalidad se gestiona mediante un Issue en GitHub, registrando el avance con Git y documentando el proyecto con Markdown.

## Tabla de operaciones y estados

| N.º | Operación | Descripción | Estado |
|-----|-----------|-------------|--------|
| - | Suma | Suma dos números | Completada |
| - | Resta | Resta dos números | Completada |
| - | Multiplicación | Multiplica dos números | Completada |
| - | División | Divide dos números y controla el divisor cero | Completada |
| 1 | Potencia | Calcula una base elevada a un exponente | Pendiente |
| 2 | Módulo | Obtiene el residuo de una división | Pendiente |
| 3 | Raíz cuadrada | Calcula la raíz cuadrada de un número no negativo | Pendiente |
| 4 | Porcentaje | Calcula un porcentaje de una cantidad | Pendiente |
| 5 | Valor absoluto | Obtiene el valor absoluto de un número | Pendiente |
| 6 | Factorial | Calcula el factorial de un entero no negativo | Pendiente |
| 7 | Promedio | Calcula el promedio de varios números | Pendiente |
| 8 | Redondeo | Redondea un número a la cantidad de decimales indicada | Pendiente |
| 9 | Validación de entradas | Controla entradas no numéricas | Pendiente |
| 10 | División por cero | Evita divisiones y módulos con divisor cero | Pendiente |
| 11 | Mejorar el menú | Organiza las operaciones en un menú claro | Pendiente |
| 12 | Repetir operaciones | Permite realizar varias operaciones sin reiniciar | Pendiente |
| 13 | Historial de operaciones | Almacena y muestra las operaciones realizadas | Pendiente |
| 14 | Limpiar historial | Permite borrar el historial de operaciones | Pendiente |
| 15 | Mejorar documentación | README con ejemplos de uso y presentación mejorada | Pendiente |

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

### Ejemplo de uso

```text
===== CALCULADORA =====
1. Suma
2. Resta
3. Multiplicación
4. División
Seleccione una opción: 1
Primer número: 8
Segundo número: 5
Resultado: 13.0
```

## Uso de GitHub Issues

Cada funcionalidad pendiente está registrada como un Issue en el repositorio, con título, descripción, lista de tareas (checklist), criterios de aceptación y asignada al estudiante. Cuando la funcionalidad esté implementada y probada, el Issue correspondiente se cierra.

## Uso de Git

```bash
git status
git add .
git commit -m "feat: agregar operación de potencia"
git push
```

## Autor

Denzel Daniel Pimentel Ramil (denpimen08-debug)
