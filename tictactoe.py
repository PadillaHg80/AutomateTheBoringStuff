tablero = {'sup_izq' : ' ', 'sup_m' : ' ', 'sup_der':' ',
           'centro_izq' : ' ', 'centro' : ' ', 'centro_der':' ',
           'inf_izq' : ' ', 'inf_m' : ' ', 'inf_der':' '}
def imprime_tablero(tablero):
    print(tablero['sup_izq']+'|'+tablero['sup_m']+'|'+tablero['sup_der'])
    print('-+-+-')
    print(tablero['centro_izq']+'|'+tablero['centro']+'|'+tablero['centro_der'])
    print('-+-+-')
    print(tablero['inf_izq']+'|'+tablero['inf_m']+'|'+tablero['inf_der'])
turno = 'X'
for i in range(9):
    imprime_tablero(tablero)
    print('Turno para '+turno+'. ¿En qué posición será la tirada?')
    posicion = input()
    tablero[posicion] = turno
    if turno == 'X': turno = 'O'
    else: turno = 'X'
imprime_tablero(tablero)