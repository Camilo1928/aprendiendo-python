from reto_mundo_pc.monitor import Monitor
from reto_mundo_pc.raton import Raton
from reto_mundo_pc.teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self,nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return  f'''{self.nombre}: {self.id_computadora}, 
        Monitor: {self.monitor},
        Teclado: {self.teclado},
        Raton: {self.raton}'''



if __name__ == '__main__':
  pass

