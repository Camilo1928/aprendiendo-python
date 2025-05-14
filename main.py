from reto_mundo_pc.raton import Raton
from reto_mundo_pc.teclado import Teclado
from reto_mundo_pc.monitor import Monitor
from computadora import Computadora

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 27)
    Computadora1 = Computadora('HP', monitor1, teclado1, raton1,)
    print(Computadora1)