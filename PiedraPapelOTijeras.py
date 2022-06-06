import random #importa el módulo random
import sys #importa el módulo sys
victorias = 0
derrotas = 0
empates = 0
print('Este es el juego de piedra, papel o tijeras.')
while (True):
    print( 'Escoge tu tirada: (pi)edra,(pa)pel o (t)ijeras (o (h)uir)\nMarcador actual:\nVictorias: '+str(victorias)+
        '\nDerrotas: '+str(derrotas)+'\nEmpates: '+str(empates))
    movida = input()
    if movida == 'h': sys.exit('bye')
    elif ( movida == 'pi' or movida == 'pa' or movida == 't'):
        # En este bloque se calcula la jugada del oponente, con la variable @jugada_oponente.
        aleatorio = random.randint(1,3)
        if(aleatorio == 1): jugada_oponente = 'pi'
        elif(aleatorio == 2): jugada_oponente = 'pa'
        else: jugada_oponente = 't'
        # En este bloque, se calcula el resultado del juego
        if(jugada_oponente == movida): print('Empate'); empates = empates + 1
        elif((jugada_oponente == 'pi' and movida== 'pa')
                or (jugada_oponente == 'pa' and movida== 't')
                or (jugada_oponente == 't' and movida== 'pi')) : print('Victoria!'); victorias = victorias + 1
        elif((jugada_oponente == 'pa' and movida== 'pi')
                or (jugada_oponente == 't' and movida== 'pa')
                or (jugada_oponente == 'pi' and movida== 't')) : print('Derrota!'); derrotas = derrotas + 1
    else: print('Movida inválida. Por favor escoja una movida válida')
