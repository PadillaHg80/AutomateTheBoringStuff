import time, sys #importa los módulos time, sys
identacion = 0 # cuánto identará el texto
incrementa_identación = True #si es verdadero, incrementa, si es falso, decrementa
try:
    while True :# Programa principal
        print(' '*identacion, end='')
        print('*********')
        time.sleep(0.1) #Hace una pausa por 1/10 de segundo
        if incrementa_identación:
            identacion = identacion + 1
            if identacion == 20:
            # Cambia de dirección
                incrementa_identación = False
        else:
            identacion = identacion - 1
            if identacion == 0:
            # Cambia de dirección
                incrementa_identación = True
except KeyboardInterrupt:
    sys.exit()
