import zombiedice
class mi_zombie:
    def __init__(self,name):
        self.name = name
    def turn(self,estado_del_juego):
        # estado_del_juego es un diccionario con el estado actual del juego
        resultados_tiro = zombiedice.roll
        # roll regresa un diccionario con cantidad de 'cerebros', 'shotgun' y 'pasos';
        # con cuantos resultados salieron de tirar los dados
        # la llave 'rolls' es un lista con tuples (color,ícono) con el resultado del tiro exacto.
        # Ejemplo de un resultado de roll():
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]} 
        brains = 0
        while resultados_tiro is not None:
            brains += resultados_tiro['brains']

            if brains < 2:
                resultados_tiro = zombiedice.roll() # roll again
            else:
                break
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2
Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1
Shotgun', minShotguns=1),
    mi_zombi(name='My Zombie Bot'),
    # Add any other zombie players here.
)