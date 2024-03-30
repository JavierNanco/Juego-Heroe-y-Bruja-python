# Juego-Heroe-y-Bruja-python

'''
LA TORRE ENCANTADA

Autor:  Constanza Olivos
        Javier Nanco

Profesor: Michael Cristi.

Programa enfocado en solucionar el trabajo número 3 del ramo de grafos 2-2023.
Basado en soluciones enfocadas en la rubrica entregada en Canvas.
Fecha de entrega 25/11/2023 a las 9:00
Interpretado en python 3.11.0 y con el entorno de desarrollo Visual Studio Code.
CONSTA DE APROXIMADAMENTE 30 SEGUNDOS EN ENTREGAR TODA LA INFORMACIÓN.

Contexto: 
    Una malvada bruja ha llegado al pantano y ha encerrado a la princesa. Nuestro héroe será el 
    encargado de rescatarla y para ello tendrá que hacer una serie de cálculos matemáticos y 
    estadísticos apoyados de la computación, los algoritmos y lo aprendido en la unidad de grafos.

Objetivo del juego: 
Para nuestro héroe es recorrer el mapa buscando la llave hasta encontrarla. Debe encontrarla antes 
de que la bruja llegue a robarla. La bruja tiene la ventaja de que sabe donde se encuentra la llave, 
pero tiene la desventaja del dado. 

Inicio del juego:
Al comenzar la partida, nuestro héroe se ubicará en la posición inicial 1 y la bruja en la casilla con la 
estrella azul. 
La bruja escogerá al azar 1 de las 3 casillas con el icono de la llave para esconderla, de modo tal que 
nuestro héroe sabe que 1 de esos 3 lugares tiene la llave. La llave permanecerá en esta casilla hasta 
que el héroe o la bruja lleguen a ella. 

Dinámica del juego: 
Para cada turno del juego se lanzará el dado. Nuestro héroe tiene la ventaja de ser el primero en 
moverse en cada turno y luego hará lo propio la bruja. Ambos se moverán la cantidad indicada por 
el dado. El dado se lanza una vez y según esos números, ambos se mueven para luego lanzar 
nuevamente el dado.

Resultados 
Los resultados que se solicitan son los siguientes: 
1. Número de casos de éxito del héroe, desde las distintas casillas. (3)
2. Número de casos de éxito de la bruja, desde las distintas casillas. 
3. Como cambian los resultados anteriores si los números del dado rojos aumentan en 1 en 
cada cara y se mantienen los mismos números azules. 
4. Como cambian los resultados anteriores si los números del dado azules aumentan en 1 en 
cada cara y se mantienen los mismos números rojos. 
5. Número de lanzamientos o turnos máximo y mínimo para el que nuestro héroe encontró la 
llave. 
6. Número de lanzamientos o turnos máximo y mínimo para el que la bruja llegó a la llave. 

Propuesta:
Proponer una y solo una modificación al juego de forma tal que el héroe tenga una probabilidad de 
ganar mayor al 50% en el juego. Implementar dicha propuesta en el programa arrojando los datos 
necesarios para comprobar que se cumple con lo solicitado. 

'''
