#metodo para contar incidencias de letras en una misma oración
import pprint# es para imprimir mas bonitos los diccionarios
frase = '''
        He cursed inwardly. "That wasn't for you to hear." Sal began to shrink away from him like linus had raised a hand to him. "No," Linus said quickly. "That's not- what I meant was, I should have been more ware of what I said. I should have been more careful with my words."
        '''
def contador_de_letras(frase):
    caracteres = {}
    for caracter in frase:
        caracteres.setdefault(caracter,0)
        caracteres[caracter] += 1
    return caracteres
pprint.pprint(contador_de_letras(frase))
