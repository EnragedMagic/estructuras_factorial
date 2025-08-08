#include <stdio.h>
#include <time.h>

unsigned long long factorial_recursivo(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial_recursivo(n - 1);
}

int main() {
    int numero;
    printf("Ingrese un numero: ");
    scanf("%d", &numero);

    clock_t inicio = clock();  // Medir tiempo de inicio

    unsigned long long resultado = factorial_recursivo(numero);

    clock_t fin = clock();     // Medir tiempo de fin
    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("Resultado: %llu\n", resultado);
    printf("Tiempo de ejecucion: %.15f segundos\n", tiempo);

    return 0;
}

