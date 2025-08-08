Análisis de Resultados – Python
En esta seccion se presentan los resultados obtenidos al comparar las implementaciones recursiva e iterativa del calculo de factorial en Python, evaluando su tiempo de ejecucion, uso de memoria y limitaciones.

1. Funcion recursiva (factorial_recursivo)
Límite alcanzado: La funcion recursiva logra calcular factoriales hasta el numero 247. A partir de 248, Python lanza un error de recursiun maxima excedida.
Esto ocurre porque Python impone por defecto un limite de profundidad de recursion para prevenir desbordamientos de pila (stack overflow).
En el caso del factorial, cada llamada recursiva genera un nuevo nivel en la pila, y a medida que n aumenta, el numero de llamadas anidadas crece linealmente, alcanzando el límite antes de finalizar el calculo.

Tiempo de ejecucion para 247!: 23.7412 segundos.

Uso de memoria: aproximadamente 26.9 MiB constantes durante la ejecucion.



2. Función iterativa (factorial_iterativo)
Límite alcanzado: No presenta la limitacion de profundidad de recursion, ya que no realiza llamadas anidadas. Puede calcular factoriales extremadamente grandes mientras haya memoria suficiente.

Tiempo de ejecucion para 248!: 0.0305 segundos.

Uso de memoria: aproximadamente 25.7 MiB, ligeramente inferior a la versión recursiva.

3. Comparacion general
Velocidad: La implementacion iterativa es considerablemente mas rápida que la recursiva, especialmente para valores grandes de n.

Memoria: Ambas implementaciones usan una cantidad de memoria similar, aunque la recursiva incurre en un pequeño overhead debido al almacenamiento en la pila de ejecución.

Limitaciones: La recursiva esta limitada por la configuracion de profundidad maxima de recursión en Python, mientras que la iterativa no presenta este problema.
