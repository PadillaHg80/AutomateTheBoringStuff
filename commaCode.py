def commaCode(lista):
    toString_lista = ''
    for i,x in enumerate(lista):
        if (i < len(lista)-1):
            toString_lista += str(x) + ', '
        else:
            toString_lista += 'and ' + str(x)
    return toString_lista
#spam = ['huevos', 'plátano', 'leche']
spam = [1, [2, 'huevos'],'leche']
print(commaCode(spam))
