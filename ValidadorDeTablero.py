
def suma_valores_dict(diccionario):
    suma = 0
    for v in diccionario.values(): suma += int(v)
    return suma

'''
El tablero debe ser un diccionario, las llaves deben de ser coordenadas del tablero el tipo xn, 
donde x \in {a,b,c,d,e,f,g} y n \in{1,2,3,4,5,6,7,8}.

Las piezas del tablero deben ser a lo más 16, y son los valores del diccionario.

La función regresa VERDADERO o FALSO dependiendo si el tablero es válido, o no.
'''
def validaTablero(tablero):
    if tablero is None or not(type(tablero) is dict): return False
    coordenadas = tablero.keys()
    valores = tablero.values()
    #valida que los valores correspondan a piezas
    valores_blancas =  {'rey': 0,'reina': 0,'peon': 0,'alfil': 0,'torre': 0,'caballo': 0}
    valores_negras =  {'rey': 0,'reina': 0,'peon': 0,'alfil': 0,'torre': 0,'caballo': 0}
    #a continuación, validamos si las piezas son correctas:
    try:
        for v in valores:
            color = v[0]
            pieza = v[1:]
            if color == 'b':             
                valores_blancas[pieza] +=1
            elif color == 'n':
                valores_negras[pieza] += 1
            else:
                return False #Se encontró algo que no era ni 'n' ni 'b', entonces no es un tablero válido
    except Exception: #Se encontró una pieza que no está definida
        return False
    if(suma_valores_dict(valores_blancas) > 16 or suma_valores_dict(valores_negras) > 16): return False
    # son 16 piezas, que están definidas. Entonces las piezas son correctas. 

    #a cotinuación, validamos si las coordenadas son correctas
    
    filas = ['a','b','c','d','e','f','g','h']
    columnas = ['1','2','3','4','5','6','7','8']
    try:
        for k in coordenadas:
            if len(k) != 2 or not (k[0] in filas and k[1] in columnas) :
                return False
    except IndexError:
        return False
    #las coordenadas fueron revisadas una a una, y todas fueron definidas
    return True

''' tablero1 = {'e6': 'nrey', 'h7':'bcaballo'}
print(validaTablero(tablero1)) '''

''' tablero = None
print(validaTablero(tablero)) '''

''' tablero = ['e6','rey','lol']
print(validaTablero(tablero)) '''

''' tablero = {'b1':'bspock','a2':{'a1':'npeon'}}
print(validaTablero(tablero)) '''