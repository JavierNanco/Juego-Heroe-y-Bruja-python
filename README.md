# La Torre Encantada

**Autores:**  
- Constanza Olivos  
- Javier Nanco  
**Profesor:** Michael Cristi  
**Fecha de entrega:** 25/11/2023  
**Interpretado en:** Python 3.11.0  
**Entorno de desarrollo:** Visual Studio Code  

## Descripción

Este programa fue creado para resolver el trabajo número 3 del ramo de Grafos (2-2023). El juego simula una carrera entre un héroe y una bruja para encontrar una llave oculta en el mapa. El héroe debe moverse estratégicamente para encontrar la llave antes que la bruja, quien tiene ventaja al conocer la ubicación de la llave, pero está limitada por el azar del dado.

## Contexto del Juego

La malvada bruja ha llegado al pantano y ha encerrado a la princesa. Nuestro héroe tiene la misión de rescatarla, pero antes debe encontrar la llave que abre la torre donde está prisionera. Tanto el héroe como la bruja se mueven por el mapa según el resultado de un dado, lo que hace que el juego dependa tanto de la estrategia como de la suerte.

### Objetivo
El héroe debe encontrar la llave antes de que lo haga la bruja. La bruja sabe dónde está la llave, pero se enfrenta a la limitación del dado, mientras que el héroe se mueve primero en cada turno.

## Dinámica del Juego

1. **Inicio**: 
   - El héroe comienza en la posición inicial (casilla 1), mientras que la bruja empieza en una casilla marcada con una estrella azul.
   - La bruja esconde la llave en una de las tres casillas designadas al azar.

2. **Turnos**: 
   - Se lanza un dado en cada turno para determinar cuántas casillas avanzan tanto el héroe como la bruja.
   - El héroe se mueve primero y luego la bruja, siguiendo el mismo número de casillas que indica el dado.

3. **Fin del Juego**: 
   - El juego termina cuando el héroe o la bruja encuentran la llave. El héroe gana si llega primero, mientras que la bruja gana si lo hace antes.

## Resultados Solicitados

El programa debe proporcionar los siguientes resultados tras la simulación de 5000 partidas:

1. Número de veces que el héroe encuentra la llave desde distintas posiciones iniciales.
2. Número de veces que la bruja encuentra la llave desde las mismas posiciones.
3. Cómo cambian estos resultados si las caras del dado rojo aumentan en 1.
4. Cómo cambian estos resultados si las caras del dado azul aumentan en 1.
5. Número mínimo y máximo de turnos en los que el héroe encuentra la llave.
6. Número mínimo y máximo de turnos en los que la bruja encuentra la llave.

## Propuesta de Mejora

Se propone realizar una modificación en el juego para que el héroe tenga una probabilidad mayor al 50% de ganar. Esta modificación se implementa en el programa, y se generan los datos necesarios para demostrar que efectivamente mejora las probabilidades de éxito del héroe.

## Funcionalidades

1. **Simulación del juego**:  
   - El programa simula 5000 partidas y proporciona las estadísticas sobre el éxito del héroe y la bruja.
   
2. **Gráficos y tablas**:  
   - Se generan gráficos de barras que comparan el número de victorias del héroe y la bruja en diferentes configuraciones de dados.
   - También se crean tablas que muestran los movimientos mínimos y máximos necesarios para que el héroe o la bruja encuentren la llave.

## Cómo ejecutar el programa

1. Instala Python 3.11.0 y las bibliotecas requeridas:
   ```bash
   pip install networkx matplotlib tkinter
   ```

2. Ejecuta el script:
   ```bash
   python juego_heroe_bruja.py
   ```

3. Se abrirá una interfaz gráfica donde podrás visualizar los resultados y la comparación de las estrategias.

Este programa combina teoría de grafos, simulaciones y visualizaciones para proporcionar un análisis detallado del juego y posibles mejoras en las estrategias del héroe.
