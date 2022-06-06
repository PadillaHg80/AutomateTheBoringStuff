tablero_gato = {'sup_izq' : ' ', 'sup' : ' ', 'sup_der' : ' ',
                'centro_izq' : ' ', 'centro' : ' ', 'centro_der' : ' ',
                'inf_izq' : ' ', 'inf' : ' ', 'inf_der' : ' ',

def printBoard(board):
    print(board['sup_izq'] + '|' + board['sup'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
