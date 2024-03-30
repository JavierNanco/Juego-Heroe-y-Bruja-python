import random # Permite generar numeros aleatorios.
import tkinter as tk
from tkinter import ttk
import networkx as nx # Permite trabajar con grafos de manera mas sencilla.
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def dado(caraAzul, caraRoja):
    
    # Define las caras del dado como tuplas de dos números.
    
    carasDado = [(1, 3), (1, 1), (0, 2), (1, 3), (1, 1), (2, 0)] + [(caraAzul, caraRoja)] # ORIGINAL (Bruja, Heroe) + Hándicap 
    #carasDado = [(0, 3), (0, 1), (0, 2), (0, 3), (0, 1), (0, 0)] + [(caraAzul, caraRoja)]# PRUEBA MOVIMIENTO HEROE
    #carasDado = [(1, 0), (1, 0), (0, 0), (1, 0), (1, 0), (2, 0)] + [(caraAzul, caraRoja)]# PRUEBA MOVIMIENTO BRUJA

    # Lanza el dado.
    
    resultado = random.choice(carasDado)

    # Obtiene el primer y segundo número de la cara.
    
    primerNumero = resultado[0] # Bruja
    segundoNumero = resultado[1] # Heroe
    
    # Retorna el valor de los dados.
    
    return primerNumero, segundoNumero

def grafo(rutas):
    
    # Crea un grafo vacio llamado "G".
    
    G = nx.Graph()

    # Agregar vertices al grafo.
    
    G.add_nodes_from(rutas.keys())

    # Agregar aristas al grafo.
    
    for nodo, vecinos in rutas.items():
        G.add_edges_from((nodo, vecino) for vecino in vecinos)

    # Retorna el grafo.
    
    return G 

def recorrer(rutas, G, posicionInicial, caraAzul, caraRoja, modificacion):
    
    # Indice es la ubicación ficticia de la bruja, se utiliza para visualizar a la bruja en un arreglo,
    # permite que identifiquemos cuando un camino no es posible producto de una mala suerte con los dados.
    # Cont Bruja y Cont Heroe son los contadores de victorias para cada uno.
    # deNuevo = 1 permite inicializar el bucle while cuando el heroe debe elegir entre 2 o mas caminos y no devolverse.
    # finPartida = 0 permite inicializar el bucle while, que hasta que no se cumpla la condicion no se gana la partida.
    
    indice = 0; contBruja = 0; contHeroe = 0; deNuevo = 1; finPartida = 0
    
    # bruja y heroe indican las posiciones de estos, se inicializan y se reinician con la misma posición.
    
    bruja = 1 ; heroe = posicionInicial
    
    # movimientoAnterior un arreglo que permite saber los posibles caminos anteriores del Heroe.
    # contador = 1 indica la posicion del arreglo de movimientoAnterior.
 
    movimientoAnterior = [0, 0, 0, 0]; contador = 1
    
    # posicionLlave indica 3 valores para las posiciones de las llaves, posteriormente se elige aleatoriamente donde se esconde.
    
    posicionLlave = [31, 40, 41]; llave = random.choice(posicionLlave)
    
    # Jugadas minimas para conseguir la victoria, se elige un valor sumamente alto y no 0 para que sea posible reemplazarlo.
    # jugadasAuxiliar permite contabiliza la cantidad de jugadas en una partida.
    
    jugadasMinimaBruja = 99999999; jugadasMinimaHeroe = 99999999; jugadasAuxiliar = 0;
    
    # Jugadas maximas para conseguir la victoria.
    
    jugadasMaximaBruja = 0; jugadasMaximaHeroe = 0
    
    # Inicia la partida, el for se recorre la cantidad de partidas que queramos (solo bajo las condiciones definidas en la función),
    # en este caso son 5000 partidas.   

    for numero in range(5000):
        
        # El while permite iterar hasta que se acabe una partida, cada iteracion correspone a una jugada
        
        while(finPartida != 1):          
            dadoBruja, dadoHeroe = dado(caraAzul, caraRoja) # Se indica los movimientos que permite el dado en la jugada.
            noGana = 1 # Indica 2 si ganó el heroe en la jugada, en caso de ser valor 1 permite a la bruja seguir jugando, se reestablece cada partida.
            
            caminoBruja = nx.shortest_path(G, source=bruja, target=llave) # Busca el camino mas corto entre la bruja y la llave.
            
#-----------------------------HEROE-------------------------------------------------------------
            
            jugadasAuxiliar += 1 # Contabiliza una jugada.
            for numero1 in range(modificacion):
                contador = 1 # Reestablece contador.
                for num in range(dadoHeroe): # Estructura de repetición que permite generar la logica para avanzar la cantidad de casillas que indica el dado.
                    movimientoAnterior[contador] = heroe # Reestablece el guardado del movimiento anterior.
                    cantidadAristas = 0 # Indica la cantidad de aristas posibles para avanzar, aqui reestablece al valor inicial.       
                
                    for lista in rutas.values():
                        if heroe in lista: # Permite saber cuantos caminos posibles hay al avanzar una posición.
                            cantidadAristas+=1 # Cantidad de caminos posibles.
                        
                    if(cantidadAristas > 2): # Comprueba si existen mas de 2 caminos para avanzar.
                        while(deNuevo == 1):
                            aux1 = random.choice(rutas[heroe]) # Ruta[clave] obtiene sus valores.
                            if(aux1 != movimientoAnterior[contador-1]): # Comprueba si el siguiente camino a tomar es diferente del que se venia.
                                heroe = aux1 # Heroe avanza.
                                deNuevo+=1 # Termina el While.
                            
                    deNuevo = 1 # Reestablece el bucle While.
                
                    if(cantidadAristas <= 2): # MAX y MIN Comprueba el valor, si el vertice que esta a la derecha es mayor y diferente al cual ya vino.
                        aux2 = max(rutas[heroe]) # MAX (comprueba mayor valor del vertice).
                        if( aux2 != movimientoAnterior[contador-1] or aux2 == 38):
                            
                            heroe = aux2 # El heroe avanza a la casilla no anterior o a la casilla 38.
                        else:
                            heroe = min(rutas[heroe]) #MIN (comprueba menor valor del vertice).            
                    contador += 1 # Pasa al siguiente valor del indice del arreglo movimientoAnterior.

                if(heroe == llave and finPartida == 0): # Comprueba si el heroe cayó en la casilla de la llave.
                    '''
                        Siempre se comprueba la llave despues de FINALIZAR la jugada,
                        debemos comprobar si aun no ha finalizado la partida, esto se
                        debe a que si el heroe esta modificado para jugar mas veces por
                        turno y gano dentro de la misma jugada, no se considerara una
                        segunda victoria.
                    '''
                    if(jugadasAuxiliar < jugadasMinimaHeroe): # Compara si la jugada actual es menor a cualquiera de las 5000 iteraciones.
                        jugadasMinimaHeroe = jugadasAuxiliar  # Reemplaza la jugada menor.
                    if(jugadasAuxiliar > jugadasMaximaHeroe): # Compara si la jugada actual es mayor a cualquiera de las 5000 iteraciones.
                        jugadasMaximaHeroe = jugadasAuxiliar # Reemplaza la jugada mayor.
                    finPartida = 1 # Finaliza la partida.
                    noGana = 2 # No permite a la bruja seguir jugando. Gana siempre primero el heroe.
                    contHeroe += 1 # Añade una victoria al contador.
                
#-----------------------------BRUJA--------------------------------------------------------------
           
            if(noGana == 1):    
            
                cantidadAristasBruja = 0 # Inicializa y reestablece la cantidad de caminos posibles que puede optar la bruja.
                for listaAuxiliar in rutas.values():
                    if caminoBruja[indice] in listaAuxiliar:
                        cantidadAristasBruja += 1 # Cantidad de caminos posibles.
                                
                cantidadVerticesBruja = len(caminoBruja) - 1 # Se contabiliza el largo de camino de la bruja.

                if((dadoBruja == 2) and (caminoBruja[indice] == caminoBruja[cantidadVerticesBruja - 1])): # caminoBruja[] es el vertice.
                    '''
                    Es muy posible que cuando quede una casilla para llegar a la llave en el dado aparezca un 2,
                    la bruja en este caso debe pasarse de ese camino, tomar otro o exclusivamente en la casilla 41
                    le tocara devolverse. Es por eso que cada vez que el dado obtenga el valor de 2 y se esté una
                    posición anterior a la llave, se inicializara un bucle while y se buscara un camino aleatorio donde
                    no se devuelva la bruja o el camino posible sea igual a 38 (esto ya que en la casilla 41 existe
                    una excepción y se permite a la bruja devolverse, en ese caso el unico camino por el cual puede
                    hacerlo es por el vertice que designamos como 38).
                    
                    Ya cumplidas estas condiciones la bruja tomara un nuevo camino, se designara nuevamente la opción
                    de camino mas corto, se reiniciara el indice y se saldrá del bucle while.
                    '''
                    indice = indice + 1
                    numA = 0 # Permite entrar al bucle while.
                    while(numA != 1):
                        nuevoCamino = random.choice(rutas[caminoBruja[indice]]) # Ahora desde este vertice se elige aleatoriamente.
                        if(caminoBruja[indice - 1] != nuevoCamino or nuevoCamino == 38): 
                            bruja = nuevoCamino # Avanza la bruja.
                            caminoBruja = nx.shortest_path(G, source = bruja, target = llave) # Se designa un nuevo camino mas corto.
                            indice = 0 # Reinicia indice.
                            numA = 1 # Sale del bucle while.
                else: # En caso de no cumplir con las condiciones significa que la bruja puede avanzar sin complicaciones.
                    indice = indice + dadoBruja # Se suma el valor del indice mas el del dado.     
                
                if(caminoBruja[indice] == llave): # Se comprueba si la bruja logró la victoria.
                    if(jugadasAuxiliar < jugadasMinimaBruja): # Compara si la jugada actual es menor a cualqueira de las 5000 iteraciones.
                        jugadasMinimaBruja = jugadasAuxiliar # Reemplaza la jugada menor.
                    if(jugadasAuxiliar > jugadasMaximaBruja): # Compara si la jugada actual es mayor a cualqueira de las 5000 iteraciones.
                        jugadasMaximaBruja = jugadasAuxiliar # Reemplaza la jugada mayor.
                    finPartida = 1 # Finaliza esta partida. 
                    contBruja += 1 # Añade una victoria a la bruja.
                    
        # Reestablece los valores iniciales, reestablece la partida

        heroe = posicionInicial; bruja = 1; indice = 0; jugadasAuxiliar = 0
        finPartida = 0

    # Retorna la suma de los resultados de todas las partidas.
        
    return contBruja, contHeroe, jugadasMinimaBruja, jugadasMaximaBruja, jugadasMinimaHeroe, jugadasMaximaHeroe

#-----------------------------Interfaz--------------------------------------------------------------

#-----------------------------Grafico de Barras-----------------------------------------------------

def interfazGrafica(contBruja1, contHeroe1, contBruja2, contHeroe2, contBruja3, contHeroe3):
    
    datosHeroe = [contHeroe1, contHeroe2, contHeroe3] # Ingresan los datos generados por la funcion recorrer
    datosBruja = [contBruja1, contBruja2, contBruja3]
    
    '''
    Nota: No se incluyo la funcion recorrer en la funcion de interfaz para minimizar las lineas de codigo.
    Si bien reduce significativamente la cantidad de tiempo al iniciar el programa, suele ser mas incomodo
    y requiere mas tiempo para cambiar entrecada grafico. De esta manera se logra que no se requiera tanto tiempo
    despues de que se inicie la interfaz grafica.
    '''
    
    
    categorias = ['Heroe(Casilla 6)', 'Heroe(Casilla 7)', 'Heroe(Casilla 8)']
    
    # Crear figura y ejes
    figura = Figure(figsize=(6, 4), dpi=100)
    ejes = figura.add_subplot()

    # Crear barras rojas
    ejes.bar([1, 3, 5], datosHeroe, color='turquoise', width=0.8, label='Héroe')

    # Crear barras azules
    ejes.bar([2, 4, 6], datosBruja, color='purple', width=0.8, label='Bruja')

    # Configuraciones adicionales
    ejes.set_title('Gráfico de Barras')
    ejes.set_xlabel('Posición inicial(Heroe, Bruja = 1)')
    ejes.set_ylabel('Cantidad de victorias')
    
    ejes.set_xticks([1.5, 3.5, 5.5])
    ejes.set_xticklabels(categorias)
    
    ejes.legend()

    # Mostrar el gráfico en el lienzo de tkinter
    canvas = FigureCanvasTkAgg(figura, master=window)
    canvasWidget = canvas.get_tk_widget()
    canvasWidget.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    
    

#-----------------------------Tablas----------------------------------------------------------------

def crear_tabla(root=None, datos1=[()]):

    # Crear un lienzo
    canvas = tk.Canvas(root)
    canvas.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

    # Crear un Treeview con cinco columnas
    tree = ttk.Treeview(canvas, columns=("ID", "Bruja Min", "Bruja Max", "Héroe Min", "Héroe Max"), show="headings")

    # Definir encabezados
    tree.heading("ID", text="Posición inicial")
    tree.heading("Bruja Min", text="Mov. Mínimos")
    tree.heading("Bruja Max", text="Mov. Máximos")
    tree.heading("Héroe Min", text="Mov. Mínimos")
    tree.heading("Héroe Max", text="Mov. Máximos")

    # Ajustar columnas
    tree.column("ID", width=100)
    tree.column("Bruja Min", width=100)
    tree.column("Bruja Max", width=100)
    tree.column("Héroe Min", width=100)
    tree.column("Héroe Max", width=100)


    # Insertar datos de ejemplo
    tree.insert("", "end", values=("", " Bruja", " Bruja", " Héroe", "   Héroe"))
    for dato in datos1:
        tree.insert("", "end", values=dato)



    # Agregar Treeview al lienzo
    tree.grid(row=0, column=0, padx=10, pady=10)

    if root is not None:
        root.mainloop()



#------------------Main------------------------------------------------------------------------------------------

# Para la creación del grafo se identifica Vertice Indicado: [Vertice Adyacente, Vertice Adyacente].

rutas = {   1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8],
            8: [14, 19, 20], 9: [10, 14], 10: [9, 15, 11], 11: [10, 12, 16], 12: [11, 13],
            13: [12, 18, 25], 14: [8, 9, 21], 15: [10, 21], 16: [21, 11], 17: [11, 22, 24], 
            18: [13, 26], 19: [8, 27], 20: [8, 23, 28, 29], 21: [14, 15, 16, 23], 22: [17, 29], 
            23: [20, 21], 24: [17, 25], 25: [13, 24, 31], 26: [18, 31], 27: [19, 28, 33],
            28: [20, 27], 29: [20, 22, 30, 33], 30: [29, 35, 36], 31: [25, 26, 36],  32: [33, 37],
            33: [27, 29, 32],34: [38, 35], 35: [30, 34, 40], 36: [30, 31, 40], 37: [32, 38],
            38: [34, 37, 39, 41], 39: [38, 42], 40: [35, 36, 42], 41: [38], 42: [39, 40]
        }

# Se utiliza las rutas para crear el grafo gracias a la función "grafo".

G = grafo(rutas)

# Resultados principales, 5000 iteraciones para los dados originales y 3 posiciones del heroe 6,7,8 se imprime las victorias (bruja, Heroe).
# La funcion recorrer inicializa con los parametros:
# (Ruta, Grafo, Posicion Inicial Del Heroe, "Hándicap" Cara Roja, "Hándicap" Cara Azul, Cantidad de veces que juega el heroe por turno).

window = tk.Tk()
window.configure(bg='white')
window.title('Información de Montecarlo')

contBruja1, contHeroe1, jugadasMinimaBruja1, jugadasMaximaBruja1, jugadasMinimaHeroe1, jugadasMaximaHeroe1 = recorrer(rutas, G, 6, 0, 0, 1)
contBruja2, contHeroe2, jugadasMinimaBruja2, jugadasMaximaBruja2, jugadasMinimaHeroe2, jugadasMaximaHeroe2 = recorrer(rutas, G, 7, 0, 0, 1)
contBruja3, contHeroe3, jugadasMinimaBruja3, jugadasMaximaBruja3, jugadasMinimaHeroe3, jugadasMaximaHeroe3 = recorrer(rutas, G, 8, 0, 0, 1)
#datos1=[(6, jugadasMinimaBruja1, jugadasMaximaBruja1, jugadasMinimaHeroe1, jugadasMaximaHeroe1), (7, jugadasMinimaBruja2, jugadasMaximaBruja2, jugadasMinimaHeroe2, jugadasMaximaHeroe2),  (8, jugadasMinimaBruja3, jugadasMaximaBruja3, jugadasMinimaHeroe3, jugadasMaximaHeroe3)]

contBruja4, contHeroe4, jugadasMinimaBruja4, jugadasMaximaBruja4, jugadasMinimaHeroe4, jugadasMaximaHeroe4 = recorrer(rutas, G, 6, 0, 1, 1)
contBruja5, contHeroe5, jugadasMinimaBruja5, jugadasMaximaBruja5, jugadasMinimaHeroe5, jugadasMaximaHeroe5 = recorrer(rutas, G, 7, 0, 1, 1)
contBruja6, contHeroe6, jugadasMinimaBruja6, jugadasMaximaBruja6, jugadasMinimaHeroe6, jugadasMaximaHeroe6 = recorrer(rutas, G, 8, 0, 1, 1)
#datos1=[(6, jugadasMinimaBruja4, jugadasMaximaBruja4, jugadasMinimaHeroe4, jugadasMaximaHeroe4), (7, jugadasMinimaBruja5, jugadasMaximaBruja5, jugadasMinimaHeroe5, jugadasMaximaHeroe5),  (8, jugadasMinimaBruja6, jugadasMaximaBruja6, jugadasMinimaHeroe6, jugadasMaximaHeroe6)]

contBruja7, contHeroe7, jugadasMinimaBruja7, jugadasMaximaBruja7, jugadasMinimaHeroe7, jugadasMaximaHeroe7 = recorrer(rutas, G, 6, 1, 0, 1)
contBruja8, contHeroe8, jugadasMinimaBruja8, jugadasMaximaBruja8, jugadasMinimaHeroe8, jugadasMaximaHeroe8 = recorrer(rutas, G, 7, 1, 0, 1)
contBruja9, contHeroe9, jugadasMinimaBruja9, jugadasMaximaBruja9, jugadasMinimaHeroe9, jugadasMaximaHeroe9 = recorrer(rutas, G, 8, 1, 0, 1)
#datos3=[(6, jugadasMinimaBruja7, jugadasMaximaBruja7, jugadasMinimaHeroe7, jugadasMaximaHeroe7), (7, jugadasMinimaBruja8, jugadasMaximaBruja8, jugadasMinimaHeroe8, jugadasMaximaHeroe8),  (8, jugadasMinimaBruja9, jugadasMaximaBruja9, jugadasMinimaHeroe9, jugadasMaximaHeroe9)]

contBruja10, contHeroe10, jugadasMinimaBruja10, jugadasMaximaBruja10, jugadasMinimaHeroe10, jugadasMaximaHeroe10 = recorrer(rutas, G, 6, 0, 0, 5)
contBruja11, contHeroe11, jugadasMinimaBruja11, jugadasMaximaBruja11, jugadasMinimaHeroe11, jugadasMaximaHeroe11 = recorrer(rutas, G, 7, 0, 0, 5)
contBruja12, contHeroe12, jugadasMinimaBruja12, jugadasMaximaBruja12, jugadasMinimaHeroe12, jugadasMaximaHeroe12 = recorrer(rutas, G, 8, 0, 0, 5)
#datos4=[(6, jugadasMinimaBruja10, jugadasMaximaBruja10, jugadasMinimaHeroe10, jugadasMaximaHeroe10), (7, jugadasMinimaBruja11, jugadasMaximaBruja11, jugadasMinimaHeroe11, jugadasMaximaHeroe11),  (8, jugadasMinimaBruja12, jugadasMaximaBruja12, jugadasMinimaHeroe12, jugadasMaximaHeroe12)]

button1 = ttk.Button(window, text='Original', command=lambda: (interfazGrafica(contBruja1, contHeroe1, contBruja2, contHeroe2, contBruja3, contHeroe3), crear_tabla(window, datos1=[(6, jugadasMinimaBruja1, jugadasMaximaBruja1, jugadasMinimaHeroe1, jugadasMaximaHeroe1), (7, jugadasMinimaBruja2, jugadasMaximaBruja2, jugadasMinimaHeroe2, jugadasMaximaHeroe2),  (8, jugadasMinimaBruja3, jugadasMaximaBruja3, jugadasMinimaHeroe3, jugadasMaximaHeroe3)])))
button1.grid(row=0, column=0, padx=25, pady=5)

button2 = ttk.Button(window, text='Dado Rojo', command=lambda: (interfazGrafica(contBruja4, contHeroe4, contBruja5, contHeroe5, contBruja6, contHeroe6), crear_tabla(window, datos1=[(6, jugadasMinimaBruja4, jugadasMaximaBruja4, jugadasMinimaHeroe4, jugadasMaximaHeroe4), (7, jugadasMinimaBruja5, jugadasMaximaBruja5, jugadasMinimaHeroe5, jugadasMaximaHeroe5),  (8, jugadasMinimaBruja6, jugadasMaximaBruja6, jugadasMinimaHeroe6, jugadasMaximaHeroe6)])))
button2.grid(row=0, column=1, padx=25, pady=5)

button3 = ttk.Button(window, text='Dado Azul', command=lambda: (interfazGrafica(contBruja7, contHeroe7, contBruja8, contHeroe8, contBruja9, contHeroe9), crear_tabla(window, datos1=[(6, jugadasMinimaBruja7, jugadasMaximaBruja7, jugadasMinimaHeroe7, jugadasMaximaHeroe7), (7, jugadasMinimaBruja8, jugadasMaximaBruja8, jugadasMinimaHeroe8, jugadasMaximaHeroe8),  (8, jugadasMinimaBruja9, jugadasMaximaBruja9, jugadasMinimaHeroe9, jugadasMaximaHeroe9)])))
button3.grid(row=0, column=2, padx=25, pady=5)

button4 = ttk.Button(window, text='Hándicap', command=lambda: (interfazGrafica(contBruja10, contHeroe10, contBruja11, contHeroe11, contBruja12, contHeroe12), crear_tabla(window, datos1=[(6, jugadasMinimaBruja10, jugadasMaximaBruja10, jugadasMinimaHeroe10, jugadasMaximaHeroe10), (7, jugadasMinimaBruja11, jugadasMaximaBruja11, jugadasMinimaHeroe11, jugadasMaximaHeroe11),  (8, jugadasMinimaBruja12, jugadasMaximaBruja12, jugadasMinimaHeroe12, jugadasMaximaHeroe12)])))
button4.grid(row=0, column=3, padx=25, pady=5)


# Iniciar el bucle principal de Tkinter
window.mainloop()
  
#---
