from memory_profiler import profile

@profile
def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


numero = int(input("Ingrese un número: "))
print("Resultado:", factorial_iterativo(numero))

