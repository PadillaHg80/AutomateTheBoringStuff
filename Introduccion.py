# Como manipular strings:
# nombre = 'Gerardo'
# edad = 24
# print(f'Mi nombre es {nombre}. El año siguiente tendré {edad+1}.')

# Métodos
# nombre.upper()
# nombre.lower()

def imprime_tickets(compras,ancho_izq, ancho_der):
    print('MIXI STORE'.center(ancho_izq+ancho_der,'-'))
    for k,v in compras.items():
        print(k.ljust(ancho_izq,'.')+str(v).rjust(ancho_der))


compras = {'tomate':30,'habas':20,'cebolla':20,'arenas':24*11.6}
imprime_tickets(compras,20,10)