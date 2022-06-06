def displayInventory(inventario):
    inventario_texto = 'Inventario:\n'
    total_objetos = 0
    for k,v in inventario.items():
        inventario_texto += str(v) + ' ' + str(k) + '\n'
        total_objetos += int(v)
    inventario_texto += 'Número total de objetos: '+str(total_objetos)
    print(inventario_texto)
def addToInventory(lista,inventario):
    for v in lista:
        inventario.setdefault(v,0)
        inventario[v]+=1

inventario = {'dagas':12, 'pociones':4, 'pergaminos':2, 'mapas':6}
displayInventory(inventario)
addToInventory(['kunai','shuriken','katana','pergaminos'],inventario)
displayInventory(inventario)