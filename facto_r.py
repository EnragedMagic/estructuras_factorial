from memory_profiler import profile
import time

@profile
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))

    inicio = time.time()
    resultado = factorial_recursivo(n)
    fin = time.time()

    print("Resultado:", resultado)
    print("Tiempo de ejecucion:", fin - inicio, "segundos")
