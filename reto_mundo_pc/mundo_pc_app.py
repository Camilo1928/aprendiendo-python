from reto_mundo_pc.computadora import Computadora
from reto_mundo_pc.monitor import Monitor
from reto_mundo_pc.orden import Orden
from reto_mundo_pc.raton import Raton
from reto_mundo_pc.teclado import Teclado

print('*** Mundo PC ***')

# COMPUTADORA 1
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


# COMPUTADORA 2
teclado2 = Teclado('Gamer', 'bluetooth')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', teclado2, raton2, monitor2)

# CREAR LA lISTA DE COMPUTADORAS
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
# print(orden1)


teclado3 = Teclado('Dell', 'Bluetooth')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Dell', 27)
computadora3 = Computadora('Dell', teclado3, raton3, monitor3)
orden1.agregar_computadora(computadora3)
print(orden1)