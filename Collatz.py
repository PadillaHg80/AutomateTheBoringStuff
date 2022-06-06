def collatz(number):
    if not (number % 2):
        return number // 2
    else:
        return 3*number + 1

print('Este programa aplica el algoritmo de Collatz a cualquier número, generando una secuencia que siempre concluye en 1'+
            '\nPor favor ingrese un número a continuación:')
while True:
    try:
        numero = int(input())
        break #Rompe el ciclo infinito una vez que se asegura de tener un valor numérico
    except ValueError:
        print('Valor incorrecto. Por favor ingrese un valor numérico')
valor_actual = numero #Empieza la secuencia
indice = 1
while (valor_actual > 1) :
    print('El valor actual en el paso ' + str(indice) + ' es: ' + str(valor_actual))
    valor_actual = collatz(valor_actual)
    indice = indice + 1
print('Tras ' + str(indice) + ' pasos, la secuencia llegó a 1')
