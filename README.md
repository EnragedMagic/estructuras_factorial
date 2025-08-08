# estructuras_factorial
Comparación de eficiencia de algoritmos hecho por Johan Steven Galeano Gonzalez G02



# Comparacion de Eficiencia: Factorial Recursivo vs Iterativo

Este proyecto tiene como objetivo comparar la eficiencia de dos enfoques distintos para calcular el factorial de un numero entero n: uno mediante recursividad y otro mediante iteracion, implementados en Python y C.

---

## Proposito de la tarea

Explorar y analizar el comportamiento de dos algoritmos diferentes para resolver el mismo problema (factorial), comparando su tiempo de ejecucion y uso de memoria. El resultado debe incluir representaciones graficas y una documentacion clara del proceso.

---

## Implementacion de funciones

Se implementaron dos funciones por lenguaje (Python y C):

- `facto_r(n)` → Implementacion recursiva
- `facto_i(n)` → Implementacion iterativa

Cada una calcula el factorial de un numero natural n. La funcion recursiva se llama a si misma, mientras que la iterativa utiliza un bucle for.

---

## Metodos para medir eficiencia

### En Python:
- Tiempo de ejecucion: con el modulo `time`
- Uso de memoria: con el modulo `memory_profiler`

### En C:
- Tiempo de ejecucion: con `clock()` de la biblioteca `time.h`
- Uso de memoria: con la herramienta `valgrind`

---

## Representacion grafica

Los resultados se representaron usando:

- Python: con la biblioteca `matplotlib`, se generaron graficas de lineas comparando:
  - Tiempo vs valor de n
  - Memoria vs valor de n

- C: los datos obtenidos se exportaron a un archivo `.csv` y luego se graficaron para facilitar la comparacion.






