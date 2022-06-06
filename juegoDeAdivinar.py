# Involucra el modulo random en el programa
import random
import sys
numero_secreto = random.randint(1,20)
print('Estoy pensando en un número entre el 1 y el 20. ')
for intentos in range(1,7):
    print('Adivina cuál es.')
    intento = int(input())
    if (intento < numero_secreto):
        print('Estás yéndote muy abajo')
    elif (intento < numero_secreto):
        print('Estás yéndote muy arriba')
    else:
        print('¡Excelente trabajo, adivinaste el número secreto en ' + str(intentos) + ' intentos.')
        #Esto implica que acertaste
        sys.exit(0)
print('No. Estaba pensando en ' + str(numero_secreto) + '.')


