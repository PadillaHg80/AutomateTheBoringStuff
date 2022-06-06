# En este programa, se tiene de entrada una lista de listas con strings, 
# y lo muestra en una tabla bien organizada con cada columna justificada a la derecha.
# Supondremos que cada lista tiene la misma cantidad de entradas.
def encuentra_string_mas_larga(tabla): 
    # bubble sort
    max = 0
    for l in tabla: #recorremos cada renglón
        for k in l: #recorremos cada entrada, que es una string
            if len(k) > max:
                max = len(k)
    return max
def principal(tabla):
    just = encuentra_string_mas_larga(tabla)
    tabla_como_texto = ''
    for l in tabla: #recorremos cada renglón
        for k in l: #recorremos cada entrada, que es una string
            tabla_como_texto += k.rjust(just) + ' '
        if(tabla.index(l)+1 == len(tabla)): continue
        tabla_como_texto+= '\n'
    print(tabla_como_texto)
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
principal(tableData)