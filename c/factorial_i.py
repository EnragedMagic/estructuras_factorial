#include <stdio.h>
#include <time.h>


unsigned long long factorial_iterativo(int n) {
    unsigned long long resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

int main() {
    int numero;
    printf("Ingrese un numero: ");
    scanf("%d", &numero);

    clock_t inicio = clock();  // Medir tiempo de inicio

    unsigned long long resultado = factorial_iterativo(numero);

    clock_t fin = clock();     // Medir tiempo de fin
    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("Resultado: %llu\n", resultado);
    printf("Tiempo de ejecucion: %.15f segundos\n", tiempo);

    return 0;
}

