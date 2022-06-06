import sys, pyperclip
if len(sys.argv) < 3:
    print('Uso: python MClip.py [frase] [numero de reporte] - copia la frase')
    sys.exit()
frase =sys.argv[1]
reporte = sys.argv[2]
TEXTO = {'fuga-de-agua': 'Evidencias recibidas, se generó el reporte {reporte}. Se analizarán y en cuanto contemos con un dictamen, se lo compartiremos. Por favor quede al pendiente del seguimiento. ',
        'si-hay-cst': 'Evidencias recibidas, se generó el reporte {reporte}. Estamos validando fecha de visita con nuestro técnico. Por favor quede al pendiente del seguimiento. ',
        'no-hay-cst': f'Evidencias recibidas, se generó el reporte {reporte}. Por favor quede al pendiente del seguimiento. '}
if frase in TEXTO:
    pyperclip.copy(TEXTO[frase])
    print(f'Se copió el texto de {frase} al portapapeles.')
else: 
    print(f'No hay texto para {frase}')