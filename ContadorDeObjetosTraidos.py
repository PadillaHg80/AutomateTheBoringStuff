Invitados = {'Abby': {'manzanas': 5, 'peras':2},
             'Nely': {'sandias': 1, 'manzanas': 2},
             'Jenny': {'peras': 3, 'duraznos': 3}}
def contar_objetos(invitados,objeto):
    cuenta_total = 0 
    for k,v in invitados.items():
        cuenta_total = cuenta_total + v.get(objeto,0)
    return cuenta_total
print('Numero de cosas que trajeron:')
print(' - Manzanas '+str(contar_objetos(Invitados, 'manzanas')))
print(' - Peras    '+str(contar_objetos(Invitados, 'peras')))
print(' - Sandias  '+str(contar_objetos(Invitados, 'sandias')))
print(' - Duraznos '+str(contar_objetos(Invitados, 'duraznos')))