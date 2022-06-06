#TRADUCE TEXTO EN ESPAÑOL A PIG LATIN.
# LAS REGLAS DEL PIG LATIN SON:
# 1. SI UNA PALABRA EMPIEZA CON UNA VOCAL O CON Y, SE LE AGREGA LA PALABRA 'YAY' ENFRENTE DE LA PALABRA
# 2. SI UNA PALABRA EMPIEZA CON UNA CONSONANTE, SE RECORRE TODA LA SÍLABA AL FINAL 
print('Ingresa el texto que quieres sea traducido a pig latin:')
mensaje = 'Quiero instalar el calentador INSTANTANEO 1939Iusa616651 pero necesito niples, mangueras y como cubrirlo del viento y de la lluvia'
VOCALES = ('a','e','i','o','u','y')
piglatin = []
for palabra in mensaje.split():
    prefijo_no_letras = ''
    while len(palabra) > 0 and not palabra[0].isalpha():
        # En este ciclo, se recorre la palabra para la derecha para ignorar todos los
        # caracteres que no sean letras
        prefijo_no_letras += palabra[0]
        palabra = palabra[1:]
    if len(palabra) == 0: # La palabra solo fueron simbolos especiales o números
        piglatin.append(prefijo_no_letras)
        continue #la palabra no se modifica
    sufijo_no_letras = ''
    while not palabra[-1].isalpha():
        sufijo_no_letras += palabra[-1]
        palabra = palabra[:-1]
    # recordamos si la palabra empezaba con mayúscula, o era todo mayúscula:
    era_mayuscula = palabra.isupper()
    empezaba_con_mayuscula = palabra.istitle()
    palabra = palabra.lower()

    consonantes_prefijo = ''
    while len(palabra)>0 and not palabra[0] in VOCALES:
        consonantes_prefijo += palabra[0]
        palabra = palabra[1:]
    if consonantes_prefijo != '':
        palabra += consonantes_prefijo + 'ay'
    else:
        palabra += 'yay'
    if era_mayuscula:
        palabra = palabra.upper()
    if empezaba_con_mayuscula:
        palabra = palabra.title()
    piglatin.append(prefijo_no_letras + palabra + sufijo_no_letras)
print(' '.join(piglatin))
        
