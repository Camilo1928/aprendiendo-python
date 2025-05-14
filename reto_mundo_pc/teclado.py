from reto_mundo_pc.dispocitivos_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contador_teclado = 0 
    
    def __init__(self, teclado):
        self.teclado = teclado

    def __str__(self, teclado):
        return f'''Teclado
        teclado: {self.teclado}'''