#Juego de la vida
import random #para generar numeros aleatorios
import time #para hacer pequeñas pausas
import copy #contiene funciones para hacer copias totales a objetos
ANCHO = 6
ALTURA = 6
celdas_siguientes = []
for x in range(ANCHO):
    columna = [] #Crea una nueva columna
    for y in range(ALTURA):
        if random.randint(0,1) == 0:
            columna.append('#') #Añade una celda viva
        else:
            columna.append(' ')
    celdas_siguientes.append(columna) #celdas_siguientes es una lista de columnas
while True: #Programa principal
    print('\n\n\n\n\n') #Se separa cada generación de celdas con un espacio vacío
    celdas_actuales = copy.deepcopy(celdas_siguientes)
    # este bloque imprime las celdas actuales
    for y in range(ALTURA):
        for x in range(ANCHO):
            print(celdas_actuales[x][y], end = '') #Imprime el # o el espacio
        print() #Imprime una nueva línea al final de cada fila

    #calcular el siguiente estado de las celdas
    for x in range(ANCHO):
        for y in range(ALTURA):
            # Obtener las coordenadas vecinas:
            # %ANCHO se asegura que la coordenada izquierda esté siempre entre 0 y ANCHO
            coord_izq = (x-1) % ANCHO
            coord_der = (x+1) % ANCHO
            coord_sup = (y-1) % ALTURA
            coord_inf = (y+1) % ALTURA
            # Cuenta el número de vecinos vivos:
            num_vecinos = 0
            if celdas_actuales[coord_izq][coord_sup] == '#':
                num_vecinos += 1 #En la esq. superior izquierda hay un vecino vivo
            if celdas_actuales[x][coord_sup] == '#':
                num_vecinos += 1 #En la parte superior hay un vecino vivo
            if celdas_actuales[coord_der][coord_sup] == '#':
                num_vecinos += 1 #En la esq. superior derecha hay un vecino vivo
            if celdas_actuales[coord_izq][y] == '#':
                num_vecinos += 1 #En la izquierda hay un vecino vivo
            if celdas_actuales[coord_der][y] == '#':
                num_vecinos += 1 #En la derecha hay un vecino vivo
            if celdas_actuales[coord_izq][coord_inf] == '#':
                num_vecinos += 1 #En la esq. inferior izquierda hay un vecino vivo
            if celdas_actuales[x][coord_inf] == '#':
                num_vecinos += 1 #En la parte inferior hay un vecino vivo
            if celdas_actuales[coord_der][coord_inf] == '#':
                num_vecinos += 1 #En la esq. inferior derecha hay un vecino vivo
            # Se aplican las reglas del juego de la vida:
            if celdas_actuales[x][y] == '#' and (num_vecinos == 2 or num_vecinos == 3):
                # si tiene dos o tres vecinos queda vivo:
                celdas_siguientes[x][y] = '#'
            elif celdas_actuales[x][y] == ' ' and num_vecinos == 3:
                celdas_siguientes[x][y] = '#' #celdas muertas con tres vecinos nacen
            else:
                celdas_siguientes[x][y] = ' ' #si no es ninguno de los casos anteriores, se mueren o quedan muertos
    time.sleep(1)
