from memory_profiler import profile
import time

@profile
def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un numero: "))


inicio = time.time()
resultado = factorial_iterativo(numero)
fin = time.time()

print("Resultado:", resultado)
print(f"Tiempo de ejecucion: {fin - inicio:.15f} segundos")
