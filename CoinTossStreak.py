import random #importa el modulo random para numeros aleatorios
#crea una lista con simulaciones de lanzar una moneda
def crea_simulacion_lanzamientos(numero_de_tiros):
    #total de lanzamientos de moneda
    lista_lanzamientos = []
    for i in range(numero_de_tiros):
        if random.randint(0,1) == 0:
            lista_lanzamientos.append('H')
        else:
            lista_lanzamientos.append('T')
    return lista_lanzamientos

def cuenta_rachas(lista, longitud_racha):
    if longitud_racha > len(lista):
        return 0 #no puede haber rachas más grandes del tamaño de la lista
    contador_de_rachas = 0 #cuenta cuantas rachas han encontrado al momento
    k = 0
    while k < len(lista): #k recorre toda la lista:
        j = 1 #indice 1
        while k+j <= len(lista): # j va a aumentar cuando
            if k+j == len(lista) or lista[k+j] != lista[k+j-1]: #si el elemento anterior difiere del actual, se rompe la racha
                if j >= longitud_racha: #la racha lograda supera el tamaño de racha solicitado
                    contador_de_rachas += 1
                break #deja de desplazar j porque ya no hay racha
            j += 1
        k = k + j
    return contador_de_rachas

numero_de_tiros_general = 100
numero_de_rachas = 0
for numero_de_experimento in range(10000):
    lista = crea_simulacion_lanzamientos(numero_de_tiros_general)
    cuenta = cuenta_rachas(lista,6)
    if cuenta > 0:
        numero_de_rachas += 1
print("Probabilidad de racha: %s%%"%(numero_de_rachas/100))
