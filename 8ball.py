import random #importa el modulo random
#la lista a continuación escribe los mensajes,
mensajes = ['Con toda certeza',
            'Con seguridad',
            'Definitivamente sí',
            'La respuesta no es clara, intenta de nuevo',
            'Pregunta de nuevo más tarde',
            'Concéntrate y pregunta de nuevo',
            'Mi respuesta es no',
            'El desenlace no te gustará',
            'Es muy incierto']
print(mensajes[random.randint(0,len(mensajes)-1)])
